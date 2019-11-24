import random

import gym
from gym import spaces
from gym.utils import seeding
from gym.envs.toy_text import discrete
import numpy as np


class CasinoEnv(discrete.DiscreteEnv):
    """Simple roulette environment
    The roulette wheel has 37 spots. If the bet is 0 and a 0 comes up,
    you win a reward of 35. If the parity of your bet matches the parity
    of the spin, you win 1. Otherwise you receive a reward of -1.
    The long run reward for playing 0 should be -1/37 for any state
    The last action (38) stops the rollout for a return of 0 (walking away)
    """
    def __init__(self, spots=37):
        self.n = spots + 1
        self.action_space = spaces.Discrete(self.n)
        print(self.action_space)
        self.observation_space = spaces.Discrete(1)
        self.seed()
        self.env = self
        desc = []
        for i in range(spots):
            desc.append(random.random() * 0.00000001)
        self.desc = np.array(desc)

        nA = self.n
        nS = 1

        self.P = {s : {a : [] for a in range(nA)} for s in range(nS)}

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, action):
        assert self.action_space.contains(action)
        if action == self.n - 1:
            # observation, reward, done, info
            return 0, 0, True, {}

        # N.B. np.random.randint draws from [A, B) while random.randint draws from [A,B]
        val = self.np_random.randint(0, self.n - 1)
        if val == action == 0:
            reward = self.n - 5.0
        elif val != 0 and action != 0 and val % 2 == action % 2:
            reward = 1.0
        else:
            reward = -1.0
        return 0, reward, False, {}

    def reset(self):
        return 0

    # def desc(self):
    #     return ""
