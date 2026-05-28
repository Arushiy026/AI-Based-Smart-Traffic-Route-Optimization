# AI-Powered Smart Traffic Route Optimization System

A complete full-stack real-time traffic-aware routing system demonstrating dynamic graph algorithms, a machine learning engine for traffic prediction, and simulation capabilities (ripple effects, road blocks) against realistic mapping layouts (with Delhi coordinates used as the demo mock).

## Architecture
- **DAA Engine**: Dijkstra & A* pathfinding using dynamically predicted weights.
- **ML Engine**: Scikit-Learn `RandomForestRegressor` estimating traffic density based on historical volume and time of day.
- **Simulation**: Live edge removals (simulated road blocks) and BFS-based ripple propagation of traffic jams.
- **Backend**: Python FastAPI.
- **Frontend**: Vite + React + Leaflet + TailwindCSS.
- **Database (Docker)**: PostgreSQL + Redis caching orchestration.

## Prerequisites
- Node.js & npm (for frontend)
- Python 3.10+ (for backend)
- Docker Desktop (for Postgres/Redis orchestration)

## Quick Start (Local Setup)

### 1. Database (Docker Compose)
From the `docker/` directory, spin up the database and cache using:
```bash
cd docker
docker-compose up -d
```

### 2. Backend API Setup
Initialize the backend python environment, train the ML model, and start the FastAPI server:
```bash
# Create and activate virtual environment
python -m venv venv

# Windows activate:
.\venv\Scripts\activate
# Mac/Linux activate:
# source venv/bin/activate

# Install dependencies
pip install fastapi uvicorn sqlalchemy psycopg2-binary redis scikit-learn pandas numpy NetworkX pytest

# Generate mock data and Train ML model initially
python ml/train_model.py
python backend/api/data_generator.py

# Start the API server
python backend/api/main.py
```
*API will run on `http://localhost:8000`. Test via `http://localhost:8000/docs`.*

### 3. Frontend Setup
Open a new terminal window to serve the React interface:
```bash
cd frontend
npm install
npm run dev
```
*Interface will map `http://localhost:5173` to the backend endpoints.*

## Features Exposed
- **Find Route**: Calculate Dijkstra/A* optimal paths emphasizing Normal VS Emergency modes.
- **Compare Algos**: Fetch comparative time complexities and weights.
- **Simulation Controls**: 
  - *Ripple Congestion*: Adds artificial predicted traffic metrics to edges nearby a congested node.
  - *Edge Blockade*: Dynamically removes edges from the adjacency list rendering roads impassable.
