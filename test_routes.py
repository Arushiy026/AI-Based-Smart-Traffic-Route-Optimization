import sys
import os

base_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_dir)

try:
    from backend.services.simulation_engine import SimulationEngine
    from backend.api.data_generator import NODES

    def main():
        print("Initializing Engine...")
        engine = SimulationEngine()
        
        # Pick two real nodes from the generator
        source = NODES[0]['id']
        target = NODES[-1]['id']
        
        print(f"Finding routes from {source} to {target}...")
        routes, time_est = engine.find_route(source, target, mode="normal", preference="balanced")
        
        print(f"Found routes count: {len(routes)}")
        for i, r in enumerate(routes):
            print(f"--- Route {i+1} ---")
            print(f"Path Length: {len(r['path'])}")
            print(f"Distance: {r['distance']} km")
            print(f"Time: {r['estimated_time']} mins")
            print(f"Traffic Cost: {r['traffic_cost']}")
            print(f"Score: {r['score']}")
            print(f"Explanation: {r['explanation']}")

    if __name__ == "__main__":
        main()
except Exception as e:
    import traceback
    traceback.print_exc()
