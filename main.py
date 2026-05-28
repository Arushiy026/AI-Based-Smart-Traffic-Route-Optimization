import json
import random
import os

# Real world coordinates around Connaught Place, New Delhi
NODES = [
    {"id": "rajiv_chowk", "lat": 28.6328, "lng": 77.2197, "name": "Rajiv Chowk"},
    {"id": "jantar_mantar", "lat": 28.6271, "lng": 77.2166, "name": "Jantar Mantar"},
    {"id": "barakhamba", "lat": 28.6315, "lng": 77.2255, "name": "Barakhamba Road"},
    {"id": "india_gate", "lat": 28.6129, "lng": 77.2295, "name": "India Gate"},
    {"id": "mandi_house", "lat": 28.6262, "lng": 77.2341, "name": "Mandi House"},
    {"id": "supreme_court", "lat": 28.6230, "lng": 77.2396, "name": "Supreme Court"},
    {"id": "ito", "lat": 28.6300, "lng": 77.2404, "name": "ITO"},
    {"id": "paharganj", "lat": 28.6425, "lng": 77.2131, "name": "Paharganj"},
    {"id": "new_delhi_rs", "lat": 28.6421, "lng": 77.2211, "name": "New Delhi Railway Station"},
    {"id": "khan_market", "lat": 28.6010, "lng": 77.2274, "name": "Khan Market"}
]

# Provide realistic distances (in km) and an initial traffic value (0 to 10)
EDGES = [
    {"source": "rajiv_chowk", "target": "jantar_mantar", "distance": 1.2, "traffic": 5},
    {"source": "jantar_mantar", "target": "rajiv_chowk", "distance": 1.2, "traffic": 4},
    {"source": "rajiv_chowk", "target": "barakhamba", "distance": 0.8, "traffic": 6},
    {"source": "barakhamba", "target": "rajiv_chowk", "distance": 0.8, "traffic": 5},
    {"source": "barakhamba", "target": "mandi_house", "distance": 1.5, "traffic": 3},
    {"source": "mandi_house", "target": "barakhamba", "distance": 1.5, "traffic": 4},
    {"source": "rajiv_chowk", "target": "new_delhi_rs", "distance": 1.5, "traffic": 8},
    {"source": "new_delhi_rs", "target": "paharganj", "distance": 0.9, "traffic": 7},
    {"source": "paharganj", "target": "jantar_mantar", "distance": 2.2, "traffic": 6},
    {"source": "mandi_house", "target": "ito", "distance": 1.1, "traffic": 9},
    {"source": "ito", "target": "supreme_court", "distance": 1.2, "traffic": 5},
    {"source": "supreme_court", "target": "mandi_house", "distance": 1.0, "traffic": 3},
    {"source": "mandi_house", "target": "india_gate", "distance": 2.0, "traffic": 7},
    {"source": "india_gate", "target": "khan_market", "distance": 2.0, "traffic": 4},
    {"source": "jantar_mantar", "target": "india_gate", "distance": 2.5, "traffic": 8}
    # Double directed edges are approximated, but graph engine handles undirected cleanly with distinct targets.
]

def generate_mock_data():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    data_dir = os.path.join(base_dir, 'data')
    os.makedirs(data_dir, exist_ok=True)
    
    with open(os.path.join(data_dir, 'nodes.json'), 'w') as f:
        json.dump(NODES, f, indent=4)
        
    with open(os.path.join(data_dir, 'edges.json'), 'w') as f:
        json.dump(EDGES, f, indent=4)
        
    print(f"Mock data generated in {data_dir}")

def get_graph_data():
    return {"nodes": NODES, "edges": EDGES}

if __name__ == "__main__":
    generate_mock_data()
