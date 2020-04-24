## Project's goal

In this project, **the goal is to train an agent to navigate a virtual world and collect as many yellow bananas as possible while avoiding blue bananas**

![In Project 1, train an agent to navigate a large world.](images/navigation.gif)

## Environment details

The environment is based on [Unity ML-agents](https://github.com/Unity-Technologies/ml-agents)

Note: The project environment provided by Udacity is similar to, but not identical to the Banana Collector environment on the Unity ML-Agents GitHub page.

> The Unity Machine Learning Agents Toolkit (ML-Agents) is an open-source Unity plugin that enables games and simulations to serve as environments for training intelligent agents. Agents can be trained using reinforcement learning, imitation learning, neuroevolution, or other machine learning methods through a simple-to-use Python API. 

A reward of +1 is provided for collecting a yellow banana, and a reward of -1 is provided for collecting a blue banana. Thus, the goal of the agent is to collect as many yellow bananas as possible while avoiding blue bananas.

The state space has 37 dimensions and contains the agent's velocity, along with ray-based perception of objects around the agent's forward direction. 

Given this information, the agent has to learn how to best select actions. Four discrete actions are available, corresponding to:

- 0 - move forward.
- 1 - move backward.
- 2 - turn left.
- 3 - turn right.

The task is episodic, and **in order to solve the environment, the agent must get an average score of +13 over 100 consecutive episodes.**

## Agent Implementation

### Rainbow DQN 

This project implements a *Value Based* method called [Rainbow DQN](https://deepmind.com/research/publications/rainbow-combining-improvements-deep-reinforcement-learning). 

Rainbow is a DQN based off-policy deep reinforcement learning algorithm with several improvements. Currently, it is the state-of-the-art algorithm on ATARI games:
![RainbowStatus](https://miro.medium.com/max/1400/1*8b_wJNn0tC_7t6T7ID_OUQ.png)
In fact, Rainbow combines seven algorithms together:
(1) DQN (Deep Q-Network)
(2) DDQN (Double Deep Q-Network)
(3) N-Step Q-Learning
(4) Prioritized Experience Replay
(5) Dueling Q-Network
(6) Distributional RL
(7) Noisy Network

The code structure for reinforcement learning is pretty clear:
(1) Env module: encapsulates all kinds of games with Gym, so we can easily to have interactions between the Agent and the Env.
(2) Agent module: Key module, implements the training process.
(3) Network module: define all kinds of network architectures for Q-network
(4) Replay Buffer module: store transitions
(5) Roll out module: do interactions between the Agent and the Env.


> The deep reinforcement learning community has made several independent improvements to the DQN algorithm. However, it is unclear which of these extensions are complementary and can be fruitfully combined. This paper examines six extensions to the DQN algorithm and empirically studies their combination. Our experiments show that the combination provides state-of-the-art performance on the Atari 2600 benchmark, both in terms of data efficiency and final performance. We also provide results from a detailed ablation study that shows the contribution of each component to overall performance. 

Model is able to keep 15 score in 100 episodes , which beats 13 average score.
[!results_overtrain](results.png)
[!score](score.png)