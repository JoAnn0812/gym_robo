from gym.envs.registration import register

from gym_robo.tasks import LobotArmFixedGoal, LobotArmRandomGoal, HyQTask1, HyQTask2, HyQTask3
from gym_robo.robots import LobotArmSim, HyQSim

register(
    id='LobotArmContinuous-v0',  # Continuous action space
    entry_point='gym_robo.envs:LobotArmEnv',
    kwargs={'task_cls': LobotArmRandomGoal,
            'robot_cls': LobotArmSim,
            'robot_kwargs': {
                'use_gui': True
            }
            }
)
register(
    id='LobotArmContinuous-v1',  # Continuous run environment, does not stop upon reaching goal
    entry_point='gym_robo.envs:LobotArmEnv',
    kwargs={'task_cls': LobotArmRandomGoal,
            'robot_cls': LobotArmSim,
            'robot_kwargs': {
                'use_gui': False
            },
            'task_kwargs': {
                'max_time_step': 500,
                'accepted_dist_to_bounds': 0.002,
                'accepted_error': 0.002,
                'reach_target_bonus_reward': 20.0,
                'reach_bounds_penalty': 20.0,
                'contact_penalty': 20.0,
                'episodes_per_goal': 1,
                'goal_buffer_size': 50,
                'goal_from_buffer_prob': 0.98,
                'num_adjacent_goals': 0,
                'random_goal_seed': 10,
                'is_validation': False,
                'normalise_reward': False,
                'continuous_run': True
            }
            }
)
register(
    id='LobotArmContinuous-v2',  # With reward decay, exponential reward
    entry_point='gym_robo.envs:LobotArmEnv',
    kwargs={'task_cls': LobotArmRandomGoal,
            'robot_cls': LobotArmSim,
            'robot_kwargs': {
                'use_gui': False
            },
            'task_kwargs': {
                'max_time_step': 500,
                'accepted_dist_to_bounds': 0.002,
                'accepted_error': 0.001,
                'reach_target_bonus_reward': 20.0,
                'reach_bounds_penalty': 10.0,
                'contact_penalty': 10.0,
                'episodes_per_goal': 1,
                'goal_buffer_size': 50,
                'goal_from_buffer_prob': 1.0,
                'num_adjacent_goals': 0,
                'random_goal_seed': 10,
                'is_validation': False,
                'normalise_reward': False,
                'continuous_run': False,
                'reward_noise_mu': 0.0,
                'reward_noise_sigma': 0.5,
                'reward_noise_decay': 0.31073,
                'exp_rew_scaling': 5.0
            }
            }
)
register(
    id='LobotArmContinuousRel-v0', # Continuous, relative action space
    entry_point='gym_robo.envs:LobotArmEnv',
    kwargs={'task_cls': LobotArmRandomGoal,
            'robot_cls': LobotArmSim,
            'robot_kwargs': {
                'use_gui': True,
                'control_mode': "Relative"
            }
            }
)


register(
    id='LobotArmContinuousValidation-v0',
    entry_point='gym_robo.envs:LobotArmEnv',
    kwargs={'task_cls': LobotArmRandomGoal,
            'robot_cls': LobotArmSim,
            'robot_kwargs': {
                'use_gui': False
            },
            'task_kwargs': {
                'accepted_dist_to_bounds': 0.001,
                'accepted_error': 0.001,
                'reach_target_bonus_reward': 0.0,
                'reach_bounds_penalty': 0.0,
                'contact_penalty': 0.0,
                'episodes_per_goal': 1,
                'goal_from_buffer_prob': 0.0,
                'num_adjacent_goals': 0,
                'random_goal_seed': 10,
                'is_validation': True
            }
            }
)
register(
    id='LobotArmContinuousValidation-v1',
    entry_point='gym_robo.envs:LobotArmEnv',
    kwargs={'task_cls': LobotArmRandomGoal,
            'robot_cls': LobotArmSim,
            'robot_kwargs': {
                'use_gui': False
            },
            'task_kwargs': {
                'accepted_dist_to_bounds': 0.002,
                'accepted_error': 0.001,
                'reach_target_bonus_reward': 0.0,
                'reach_bounds_penalty': 0.0,
                'contact_penalty': 0.0,
                'episodes_per_goal': 1,
                'goal_from_buffer_prob': 0.0,
                'num_adjacent_goals': 0,
                'random_goal_seed': 10,
                'is_validation': True
            }
            }
)
register(
    id='LobotArmContinuousValidation-v2',
    entry_point='gym_robo.envs:LobotArmEnv',
    kwargs={'task_cls': LobotArmRandomGoal,
            'robot_cls': LobotArmSim,
            'robot_kwargs': {
                'use_gui': False
            },
            'task_kwargs': {
                'accepted_dist_to_bounds': 0.003,
                'accepted_error': 0.001,
                'reach_target_bonus_reward': 0.0,
                'reach_bounds_penalty': 0.0,
                'contact_penalty': 0.0,
                'episodes_per_goal': 1,
                'goal_from_buffer_prob': 0.0,
                'num_adjacent_goals': 0,
                'random_goal_seed': 10,
                'is_validation': True
            }
            }
)



register(
    id='HyQ-v0',  # Continuous action space
    entry_point='gym_robo.envs:HyQEnv',
    kwargs={'task_cls': HyQTask1,
            'robot_cls': HyQSim,
            'robot_kwargs': {
                'use_gui': True,
                'rtf': 0.0,
                'control_mode': "Absolute"
            },
            'task_kwargs': {
                'max_time_step': 1000,
                'accepted_dist_to_bounds': 0.002,
                'accepted_error': 0.05,
                'reach_target_bonus_reward': 0.0,
                'reach_bounds_penalty': 0.0,
                'fall_penalty': 10.0,
                'norm_rew_scaling': 100,
                'exp_rew_scaling': 7.0,
                'is_validation': False
            }
            }
)

register(
    id='HyQ-v1',  # Continuous action space
    entry_point='gym_robo.envs:HyQEnv',
    kwargs={'task_cls': HyQTask2,
            'robot_cls': HyQSim,
            'robot_kwargs': {
                'use_gui': True,
                'rtf': 6.0
            },
            'task_kwargs': {
                'max_time_step': 1000,
                'accepted_dist_to_bounds': 0.002,
                'accepted_error': 0.001,
                'reach_target_bonus_reward': 0.0,
                'reach_bounds_penalty': 20.0,
                'fall_penalty': 10.0,
                'norm_rew_scaling': None,
                'exp_rew_scaling': None,
                'cycle_len': 100,
                'is_validation': False
            }
            }
)

register(
    id='HyQ-v2',  # Continuous action space
    entry_point='gym_robo.envs:HyQEnv',
    kwargs={'task_cls': HyQTask3,
            'robot_cls': HyQSim,
            'robot_kwargs': {
                'use_gui': True,
                'rtf': 0.0,
                'control_mode': "Absolute"
            },
            'task_kwargs': {
                'max_time_step': 1000,
                'accepted_dist_to_bounds': 0.002,
                'accepted_error': 0.001,
                'reach_target_bonus_reward': 0.0,
                'reach_bounds_penalty': 0.0,
                'fall_penalty': 10.0,
                'norm_rew_scaling': None,
                'exp_rew_scaling': None,
                'is_validation': False
            }
            }
)