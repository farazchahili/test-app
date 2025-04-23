import React from 'react';
import SQLDBQuery from './components/SQLDBQuery';
import AnalyzeMollerRun from './components/AnalyzeMollerRun';
import './styles/App.css';

function App() {
    return (
        <div className="App">
            <h1>My React App</h1>
            <section>
                <h2>SQL DB Query</h2>
                <SQLDBQuery />
            </section>
            <section>
                <h2>Analyze a Moller Run</h2>
                <AnalyzeMollerRun />
            </section>
        </div>
    );
}

export default App;