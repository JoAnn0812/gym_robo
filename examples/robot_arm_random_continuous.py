#!/usr/bin/env python3
import gym
import numpy
import time
from gym_robo.envs import LobotArmEnv
from gym.spaces import Box
from typing import Type


def main(args=None):
    env: LobotArmEnv = gym.make('LobotArmContinuousRel-v0')
    env.reset()
    action_space: Type[Box] = env.action_space
    done = False
    for _ in range(10):
        print("-------------Starting----------------")
        count = 0
        while not done:
            # action = numpy.array([1.00, -1.01, 1.01])
            action = action_space.sample()
            action_do_nothing = numpy.array([0.0, -0.1, 0.1])
            if count % 50 == 0:
                action = action_space.sample()
            count += 1
            observation, reward, done, info = env.step(action)
            # Type hints
            observation: numpy.ndarray
            reward: float
            done: bool
            info: dict
            if done:
                arm_state = info['arm_state']
                print(arm_state)
        # time.sleep(1.0)
        env.reset()
        done = False
        print("-------------Reset finished---------------")


if __name__ == '__main__':
    main()
