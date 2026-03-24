import numpy as np
from typing import List, Tuple

class Swarm:
    def __init__(self, num_agents: int, task_list: List[Tuple[int, int]]):
        self.num_agents = num_agents
        self.task_list = task_list
        self.agent_positions = np.random.uniform(0, 100, (num_agents, 2))
        self.task_assignments = [-1] * len(task_list)

    def assign_tasks(self):
        unassigned_tasks = [i for i in range(len(self.task_list)) if self.task_assignments[i] == -1]
        unassigned_agents = [i for i in range(self.num_agents) if self.task_assignments.count(i) < 1]

        while unassigned_tasks and unassigned_agents:
            min_distance = float('inf')
            best_agent = None
            best_task = None

            for task_idx in unassigned_tasks:
                task = self.task_list[task_idx]
                for agent_idx in unassigned_agents:
                    agent_pos = self.agent_positions[agent_idx]
                    distance = np.sqrt((agent_pos[0] - task[0])**2 + (agent_pos[1] - task[1])**2)
                    if distance < min_distance:
                        min_distance = distance
                        best_agent = agent_idx
                        best_task = task_idx

            self.task_assignments[best_task] = best_agent
            unassigned_tasks.remove(best_task)
            unassigned_agents.remove(best_agent)

    def move_agents(self):
        for agent_idx in range(self.num_agents):
            task_idx = self.task_assignments[agent_idx]
            if task_idx != -1:
                task = self.task_list[task_idx]
                agent_pos = self.agent_positions[agent_idx]
                direction = np.array([task[0] - agent_pos[0], task[1] - agent_pos[1]])
                direction /= np.linalg.norm(direction)
                self.agent_positions[agent_idx] += direction * 0.1

    def run(self):
        self.assign_tasks()
        self.move_agents()
        print(self.task_assignments)
        print(self.agent_positions)

if __name__ == '__main__':
    task_list = [(10, 20), (30, 40), (50, 60), (70, 80)]
    swarm = Swarm(5, task_list)
    swarm.run()