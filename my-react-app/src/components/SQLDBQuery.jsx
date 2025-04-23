import React, { useState } from 'react';

const fieldLabels = [
    'rundet_day',
    'rundet_anpow',
    'rundet_type',
    'rundet_pcrex_group',
    'rundet_qpedset',
    'rundet_deadtimetau',
    'rundet_comment',
    'experiment'
];

function SQLDBQuery() {
    const [runNumber, setRunNumber] = useState('');
    const [fields, setFields] = useState(Array(8).fill(''));
    const [status, setStatus] = useState('');

    // Only allow integer input for run number
    const handleRunNumberChange = (e) => {
        const value = e.target.value;
        if (value === '' || /^[0-9]+$/.test(value)) {
            setRunNumber(value);
        }
    };

    const handleFetch = async () => {
        setStatus('');
        setFields(Array(8).fill(''));
        if (!runNumber) {
            setStatus('Please enter a valid run number.');
            return;
        }
        try {
            const response = await fetch('http://localhost:8000/api/get_run_details/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ id_rundet: runNumber }),
            });
            const data = await response.json();
            if (response.ok) {
                setFields(fieldLabels.map(label => data[label] ?? ''));
            } else {
                setStatus(data.error || 'Error fetching data.');
            }
        } catch (error) {
            setStatus('Network error.');
        }
    };

    return (
        <div className="sql-db-query">
            <label>
                Moller Run Number:&nbsp;
                <input
                    type="text"
                    value={runNumber}
                    onChange={handleRunNumberChange}
                    placeholder="Enter run number"
                    inputMode="numeric"
                    pattern="[0-9]*"
                />
            </label>
            <button onClick={handleFetch}>Fetch</button>
            <div style={{ display: 'flex', marginTop: '1em', gap: '1em' }}>
                {fieldLabels.map((label, idx) => (
                    <div key={label} style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
                        <label style={{ fontSize: '0.9em' }}>{label}</label>
                        <input
                            type="text"
                            value={fields[idx]}
                            readOnly
                            style={{ width: 120 }}
                        />
                    </div>
                ))}
            </div>
            {status && <div style={{ color: 'red', marginTop: '1em' }}>{status}</div>}
        </div>
    );
}

export default SQLDBQuery;