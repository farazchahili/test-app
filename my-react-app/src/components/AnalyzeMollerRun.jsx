import React, { useState } from 'react';

const AnalyzeMollerRun = () => {
    const [inputValue, setInputValue] = useState('');
    const [status, setStatus] = useState('');

    const handleAnalyze = async () => {
        setStatus('');
        if (!inputValue || isNaN(inputValue)) {
            setStatus('Please enter a valid integer.');
            return;
        }
        try {
            const response = await fetch('http://localhost:8000/api/analyze_run/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ run_number: parseInt(inputValue, 10) }),
            });
            const data = await response.json();
            if (response.ok) {
                setStatus('Analysis started successfully.');
            } else {
                setStatus(data.error || 'Error starting analysis.');
            }
        } catch (error) {
            setStatus('Network error.');
        }
    };

    return (
        <div>
            <input 
                type="number" 
                value={inputValue} 
                onChange={(e) => setInputValue(e.target.value)} 
                placeholder="Enter an integer" 
            />
            <button onClick={handleAnalyze}>Analyze</button>
            {status && <div>{status}</div>}
        </div>
    );
};

export default AnalyzeMollerRun;