# LLM Pipeline Builder

A full-stack visual workflow builder that enables users to create, validate, and manage LLM pipelines through an intuitive drag-and-drop interface.

## Features

### Part 1: Node Abstraction

* Created a reusable BaseNode abstraction to eliminate duplicated node logic.
* Standardized node rendering, styling, handles, and configuration.
* Added five custom nodes to demonstrate extensibility and rapid node creation.

### Part 2: Modern UI & Styling

* Designed a cohesive and responsive user interface.
* Applied consistent styling across the canvas, toolbar, nodes, and controls.
* Improved usability and visual hierarchy for pipeline creation.

### Part 3: Dynamic Text Node

* Text nodes automatically resize based on content length.
* Supports variable detection using double curly braces syntax (e.g. `{{input}}`).
* Dynamically generates input handles for detected variables.
* Enhances workflow visibility and data dependency mapping.

### Part 4: Backend Integration

* Connected the frontend to a FastAPI backend.
* Submit button sends pipeline nodes and edges to the backend.
* Backend validates pipeline structure and computes:

  * Number of nodes
  * Number of edges
  * DAG (Directed Acyclic Graph) status
* Frontend displays validation results through a user-friendly alert.

## Tech Stack

### Frontend

* React
* React Flow
* Zustand

### Backend

* FastAPI
* Pydantic
* Python

## Validation Logic

The backend uses Kahn's Topological Sort algorithm to:

* Validate node and edge relationships
* Detect cycles
* Determine whether the pipeline forms a valid DAG

## API Response

```json
{
  "num_nodes": 8,
  "num_edges": 10,
  "is_dag": true
}
```

This project demonstrates full-stack development, graph processing, reusable component architecture, and workflow orchestration concepts for AI-powered applications.
