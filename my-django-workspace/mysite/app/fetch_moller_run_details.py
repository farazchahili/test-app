import os
import sys
import mysql.connector

def fetch_moller_run_details(run_number):
    host = os.environ.get("MOLANA_DB_HOST", "localhost")
    user = os.environ.get("MOLANA_DB_USER", "root")
    password = os.environ.get("MOLANA_DB_PASS", "")
    database = os.environ.get("MOLANA_DB_NAME", "")

    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT rundet_day, rundet_anpow, rundet_type, rundet_pcrex_group,
               rundet_qpedset, rundet_deadtimetau, rundet_comment, experiment
        FROM moller_run_details
        WHERE moller_run_number = %s
        LIMIT 1
    """
    cursor.execute(query, (run_number,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python fetch_moller_run_details.py <run_number>")
        sys.exit(1)
    run_number = sys.argv[1]
    details = fetch_moller_run_details(run_number)
    if details:
        print(details)
    else:
        print("No details found for run number:", run_number)