from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import subprocess
from .fetch_moller_run_details import fetch_moller_run_details

def home(request):
    return HttpResponse("Welcome to the Django app!")

def about(request):
    return render(request, 'app/about.html')

@csrf_exempt
def analyze_run_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        run_number = data.get('run_number')
        if not isinstance(run_number, int):
            return JsonResponse({'error': 'run_number must be an integer'}, status=400)
        try:
            subprocess.run(
                ['python3', 'analyze_run.py', str(run_number)],
                cwd='.',  # or the directory where analyze_run.py is located
                check=True
            )
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def get_run_details(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        run_id = data.get('id_rundet')
        if not run_id or not str(run_id).isdigit():
            return JsonResponse({'error': 'Invalid id_rundet'}, status=400)
        result = fetch_moller_run_details(run_id)
        if result:
            return JsonResponse(result)
        else:
            return JsonResponse({'error': 'No details found'}, status=404)
    return JsonResponse({'error': 'Invalid request'}, status=400)