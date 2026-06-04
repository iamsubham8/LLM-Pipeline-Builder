from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
import json

app = FastAPI()

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data models
class NodeData(BaseModel):
    id: str
    type: str
    position: Dict[str, float]
    data: Dict[str, Any]

class EdgeData(BaseModel):
    source: str
    target: str
    sourceHandle: Optional[str] = None
    targetHandle: Optional[str] = None

class PipelineRequest(BaseModel):
    nodes: List[NodeData]
    edges: List[EdgeData]
    timestamp: str

@app.get('/')
def read_root():
    return {'status': 'Pipeline API is running', 'version': '1.0'}

@app.post('/pipelines/parse')
def parse_pipeline(pipeline: PipelineRequest):
    """
    Parses and validates a pipeline configuration.
    """
    try:
        # Basic counts
        num_nodes = len(pipeline.nodes)
        num_edges = len(pipeline.edges)

        # Validate edges reference valid nodes (ignore if no nodes)
        node_ids = {node.id for node in pipeline.nodes}
        for edge in pipeline.edges:
            if node_ids and (edge.source not in node_ids or edge.target not in node_ids):
                raise HTTPException(status_code=400, detail=f"Invalid edge: {edge.source} -> {edge.target}")

        # Determine if DAG
        try:
            _ = build_execution_order(pipeline.nodes, pipeline.edges)
            is_dag = True
        except Exception:
            is_dag = False

        return {
            'num_nodes': num_nodes,
            'num_edges': num_edges,
            'is_dag': is_dag,
        }
    
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error parsing pipeline: {str(e)}")

def build_execution_order(nodes: List[NodeData], edges: List[EdgeData]) -> List[str]:
    """
    Builds the execution order of nodes using topological sort.
    """
    # Create adjacency list
    from collections import defaultdict, deque
    
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    node_ids = {node.id for node in nodes}
    
    # Initialize in_degree
    for node in nodes:
        if node.id not in in_degree:
            in_degree[node.id] = 0
    
    # Build graph
    for edge in edges:
        graph[edge.source].append(edge.target)
        in_degree[edge.target] += 1
    
    # Topological sort using Kahn's algorithm
    queue = deque([node_id for node_id in node_ids if in_degree[node_id] == 0])
    execution_order = []
    
    while queue:
        node_id = queue.popleft()
        execution_order.append(node_id)
        
        for neighbor in graph[node_id]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Check for cycles
    if len(execution_order) != len(node_ids):
        raise ValueError("Pipeline contains a cycle")
    
    return execution_order

@app.post('/pipelines/execute')
def execute_pipeline(pipeline: PipelineRequest):
    """
    Executes a pipeline and returns results.
    """
    try:
        # Parse the pipeline first
        parse_result = parse_pipeline(pipeline)
        
        # Here you would implement actual pipeline execution logic
        # For now, return a success message
        result = {
            'status': 'executed',
            'pipeline_id': pipeline.timestamp,
            'parse_info': parse_result,
            'result': 'Pipeline execution completed successfully',
        }
        
        return result
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error executing pipeline: {str(e)}")
