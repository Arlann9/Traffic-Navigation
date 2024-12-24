# test_performance.py
from traffic_navigation import find_optimal_route

def test_navigation_system():
    # Simulated traffic data
    traffic_data = [{'source': (40.748817, -73.985428), 'destination': (40.712776, -74.005974), 'traffic_time': 15},
                    {'source': (40.712776, -74.005974), 'destination': (40.758896, -73.985130), 'traffic_time': 10}]
    start = (40.748817, -73.985428)
    destination = (40.712776, -74.005974)
    
    optimal_route = find_optimal_route(start, destination, traffic_data)
    print(f"Optimal Route: {optimal_route}")
    assert optimal_route is not None

if __name__ == "__main__":
    test_navigation_system()
