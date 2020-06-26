from gym.envs.registration import register

register(
    id='foo-v0',
    entry_point='gym_foo.envs:FooEnv',
)
register(
    id='car-extrahard-v0',
    entry_point='gym_car.envs:FooExtraHardEnv',
)
