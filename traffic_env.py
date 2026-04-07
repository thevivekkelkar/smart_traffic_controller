"""
traffic_env.py
--------------
Core RL Environment for AI Smart Traffic Signal Control System.
A single 4-way intersection with North, South, East, West lanes.
"""

import random


class TrafficEnvironment:
    """
    4-way traffic intersection environment.

    State  : [cars_north, cars_south, cars_east, cars_west]
    Actions: 0=North green, 1=South green, 2=East green, 3=West green
    Reward : negative of total cars waiting (lower congestion = higher reward)
    """

    LANES = ["North", "South", "East", "West"]

    def __init__(self, arrival_rate=2, green_flow=3, max_cars=30, max_steps=50):
        self.arrival_rate = arrival_rate
        self.green_flow   = green_flow
        self.max_cars     = max_cars
        self.max_steps    = max_steps

        self.queue    = [0, 0, 0, 0]
        self.timestep = 0

    def reset(self):
        """Reset environment. Returns initial state."""
        self.queue    = [random.randint(0, 5) for _ in range(4)]
        self.timestep = 0
        return list(self.queue)

    def step(self, action):
        """
        Take one step in the environment.

        Parameters
        ----------
        action : int  0=North, 1=South, 2=East, 3=West

        Returns
        -------
        next_state : list
        reward     : float
        done       : bool
        """
        # 1. Cars depart from green lane
        departed = min(self.queue[action], self.green_flow)
        self.queue[action] -= departed

        # 2. New cars arrive
        for i in range(4):
            arrivals = max(0, min(3, int(random.gauss(self.arrival_rate, 0.5))))
            self.queue[i] = min(self.queue[i] + arrivals, self.max_cars)

        # 3. Reward
        reward = -sum(self.queue) - max(self.queue)

        # 4. Time update
        self.timestep += 1
        done = self.timestep >= self.max_steps

        return list(self.queue), reward, done

    def state(self):
        """Return current state (required for OpenEnv)"""
        return list(self.queue)