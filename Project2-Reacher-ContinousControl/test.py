from unityagents import UnityEnvironment
import numpy as np

import torch

from ddpg_agent import Agent
from collections import deque

import matplotlib.pyplot as plt

import time
env = UnityEnvironment(file_name='Reacher.x86_64')
brain_name = env.brain_names[0]
brain = env.brains[brain_name]
env_info = env.reset(train_mode=False)[brain_name]

num_agents = len(env_info.agents)
action_size = brain.vector_action_space_size
states = env_info.vector_observations
state_size = states.shape[1]
import torch

from ddpg_agent import Agent
from collections import deque

import matplotlib.pyplot as plt

import time

agent = Agent(state_size=state_size, action_size=action_size, random_seed=10)
agent.actor_local.load_state_dict(torch.load('actor.pth', map_location=torch.device('cuda')))
agent.critic_local.load_state_dict(torch.load('critic.pth', map_location=torch.device('cuda')))

# env_info = env.reset(train_mode=False)[brain_name]     # reset the environment    
states = env_info.vector_observations[0]                  # get the current state (for each agent)
score, t = 0, 0
max_rewards = -999

while True:
    t += 1
    actions = agent.act(states)
    env_info = env.step(actions)[brain_name]
    next_states = env_info.vector_observations[0]         # get next state (for each agent)
    rewards = env_info.rewards[0]                         # get reward (for each agent)
    dones = env_info.local_done                        # see if episode finished
    score += rewards
    if max_rewards < rewards:
        max_rewards = rewards
    print('\rRewards {:.2f} (max {:.2f})\tScore {:.2f} '.format(rewards, max_rewards, score), end='')
    states = next_states                               # roll over states to next time step
    if score >= 30:
        print('\rEnvironment is solved in {} steps with {:.2f} score.'.format(t, score))
        break
        
    if np.any(dones):                                  # exit loop if episode finished
        break
        
print('Total score (averaged over agents) this episode: {:.2f}'.format(score))