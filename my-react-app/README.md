# My React App

This project is a simple React application designed to run on a local machine within a cluster. It consists of two main sections: SQL DB Query and Analyze a Moller Run.

## Project Structure

```
my-react-app
├── public
│   └── index.html
├── src
│   ├── components
│   │   ├── AnalyzeMollerRun.jsx
│   │   └── SQLDBQuery.jsx
│   ├── App.jsx
│   ├── index.js
│   └── styles
│       └── App.css
├── package.json
└── README.md
```

## Features

1. **SQL DB Query Section**
   - Input field for Moller Run Number.
   - A button labeled "Fetch" to retrieve data.
   - Eight textboxes to display numbers related to the Moller Run Number.

2. **Analyze a Moller Run Section**
   - Input field for an integer.
   - A button labeled "Analyze" to execute a Python script.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd my-react-app
   ```

2. Install dependencies:
   ```
   npm install
   ```

3. Start the application:
   ```
   npm start
   ```

4. Open your browser and navigate to `http://localhost:3000` to view the application.

## Usage

- Enter a Moller Run Number in the SQL DB Query section and click "Fetch" to display related data.
- Enter an integer in the Analyze a Moller Run section and click "Analyze" to run the associated Python script.

## License

This project is licensed under the MIT License.