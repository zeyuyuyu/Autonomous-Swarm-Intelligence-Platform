import numpy as np
from typing import List, Tuple

class Drone:
    def __init__(self, id: int, position: Tuple[float, float, float], velocity: Tuple[float, float, float]):
        self.id = id
        self.position = position
        self.velocity = velocity
        self.neighbors = []
        self.consensus_position = position
        self.consensus_velocity = velocity

    def update_neighbors(self, drones: List['Drone']) -> None:
        self.neighbors = [d for d in drones if np.linalg.norm(np.array(self.position) - np.array(d.position)) <= 10]

    def update_consensus(self) -> None:
        if self.neighbors:
            self.consensus_position = np.mean([d.position for d in self.neighbors], axis=0)
            self.consensus_velocity = np.mean([d.velocity for d in self.neighbors], axis=0)
        else:
            self.consensus_position = self.position
            self.consensus_velocity = self.velocity

    def update_state(self) -> None:
        self.position = self.consensus_position
        self.velocity = self.consensus_velocity

class SwarmController:
    def __init__(self, drones: List[Drone]):
        self.drones = drones

    def run_consensus(self) -> None:
        for drone in self.drones:
            drone.update_neighbors(self.drones)
            drone.update_consensus()
            drone.update_state()

if __name__ == '__main__':
    # Example usage
    drones = [
        Drone(0, (0, 0, 0), (1, 0, 0)),
        Drone(1, (5, 0, 0), (0, 1, 0)),
        Drone(2, (0, 5, 0), (0, 0, 1)),
        Drone(3, (0, 0, 5), (-1, 0, 0))
    ]
    swarm_controller = SwarmController(drones)
    swarm_controller.run_consensus()
    for drone in drones:
        print(f'Drone {drone.id}: position={drone.position}, velocity={drone.velocity}')