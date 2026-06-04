# LLM Pipeline Builder

A visual node-based pipeline builder for creating and executing LLM (Large Language Model) workflows.

## Features

- **Drag-and-Drop Interface**: Visually design pipelines by dragging nodes from the toolbar
- **Node Types**: Input, Output, LLM, and Text nodes with customizable properties
- **Visual Connections**: Connect nodes with animated edges to define data flow
- **Pipeline Validation**: Validates pipeline structure before execution
- **RESTful API**: Backend API for parsing and executing pipelines

## Project Structure

```
├── frontend/                 # React application
│   ├── public/              # Static files
│   ├── src/
│   │   ├── nodes/          # Node components (input, output, llm, text)
│   │   ├── App.js          # Main app component
│   │   ├── toolbar.js      # Toolbar with draggable nodes
│   │   ├── ui.js           # ReactFlow canvas
│   │   ├── submit.js       # Submit button
│   │   ├── store.js        # Zustand state management
│   │   └── index.js        # React entry point
│   └── package.json
├── backend/                 # Python/FastAPI application
│   ├── main.py             # API endpoints and pipeline logic
│   └── requirements.txt     # Python dependencies
└── README.md
```

## Installation & Setup

### Prerequisites
- Node.js (v16+)
- npm (v8+)
- Python (v3.8+)
- pip

### Backend Setup

1. Navigate to the backend directory:
```powershell
cd backend
```

2. Create a virtual environment (optional but recommended):
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

3. Install dependencies:
```powershell
pip install -r requirements.txt
```

4. Run the server:
```powershell
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:
```powershell
cd frontend
```

2. Install dependencies:
```powershell
npm install
```

3. Start the development server:
```powershell
npm start
```

The app will open at `http://localhost:3000`

## Running the Project

1. **Start the backend server** (in a terminal):
```powershell
cd backend
python -m uvicorn main:app --reload
```

2. **Start the frontend** (in a separate terminal):
```powershell
cd frontend
npm start
```

3. **Use the application**:
   - Drag nodes from the toolbar onto the canvas
   - Connect nodes by dragging from one handle to another
   - Configure node properties (names, types, prompts)
   - Click "Submit Pipeline" to execute the pipeline

## API Endpoints

### GET `/`
Health check endpoint.
- **Response**: `{"status": "Pipeline API is running", "version": "1.0"}`

### POST `/pipelines/parse`
Parses and validates a pipeline configuration.
- **Request Body**:
```json
{
  "nodes": [...],
  "edges": [...],
  "timestamp": "ISO-8601 timestamp"
}
```
- **Response**: Pipeline configuration with execution order and validation results

### POST `/pipelines/execute`
Executes a pipeline and returns results.
- **Request Body**: Same as `/pipelines/parse`
- **Response**: Execution results

## Node Types

### Input Node
- **Purpose**: Define pipeline inputs
- **Properties**: 
  - Name: Input variable name
  - Type: Text or File

### Output Node
- **Purpose**: Collect pipeline outputs
- **Properties**:
  - Name: Output variable name
  - Type: Text or Image

### LLM Node
- **Purpose**: Process data with a language model
- **Properties**:
  - System Prompt: System instructions for the LLM
  - User Prompt: User input/prompt

### Text Node
- **Purpose**: Text transformation and templating
- **Properties**:
  - Text: Template text with variable interpolation (e.g., `{{input}}`)

## Pipeline Validation

The backend validates pipelines for:
- At least one Input node
- At least one Output node
- Valid edge connections (no references to non-existent nodes)
- No circular dependencies

## Development

### Frontend Technologies
- React 18
- ReactFlow (for node-based UI)
- Zustand (for state management)
- Create React App

### Backend Technologies
- FastAPI (modern Python web framework)
- Pydantic (data validation)
- CORS middleware (for frontend communication)

## Future Enhancements

- [ ] Database integration for saving/loading pipelines
- [ ] Actual LLM integration (OpenAI, Hugging Face, etc.)
- [ ] Pipeline execution with real data processing
- [ ] User authentication and pipeline sharing
- [ ] Visual debugging and logging
- [ ] Pipeline versioning and history
- [ ] Custom node creation interface

## Troubleshooting

### CORS Errors
If you get CORS errors, ensure the backend is running on `http://localhost:8000` and the frontend on `http://localhost:3000`.

### Port Already in Use
- Frontend: Port 3000 is in use - change with `npm start -- --port 3001`
- Backend: Port 8000 is in use - change with `uvicorn main:app --port 8001`

### Dependencies Issues
- Frontend: Delete `node_modules` and `package-lock.json`, then run `npm install`
- Backend: Delete `venv` and recreate virtual environment, then reinstall dependencies

## License

MIT
