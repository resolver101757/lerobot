import time
from lerobot.scripts.control_robot import busy_wait
from lerobot.common.robot_devices.robots.koch import KochRobot

robot = KochRobot(
    leader_arms={"main": leader_arm},
    follower_arms={"main": follower_arm},
    calibration_path=".cache/calibration/koch.pkl",
)


robot.connect()

record_time_s = 30
fps = 60

states = []
actions = []
for _ in range(record_time_s * fps):
    start_time = time.perf_counter()
    observation, action = robot.teleop_step(record_data=True)

    states.append(observation["observation.state"])
    actions.append(action["action"])

    dt_s = time.perf_counter() - start_time
    busy_wait(1 / fps - dt_s)

# Note that observation and action are available in RAM, but
# you could potentially store them on disk with pickle/hdf5 or
# our optimized format `LeRobotDataset`. More on this next.