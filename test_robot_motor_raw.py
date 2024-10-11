# not verified this code yet 
# read through but trusting the code


from lerobot.common.robot_devices.motors.dynamixel import DynamixelMotorsBus, TorqueMode
import time
import numpy as np

# set the ports for the leader and follower arms
leader_port = "COM6"
follower_port = "COM5"

# initialise the leader arm
leader_arm = DynamixelMotorsBus(
    port=leader_port,
    motors={
        # name: (index, model)
        "shoulder_pan": (1, "xl330-m077"),
        "shoulder_lift": (2, "xl330-m077"),
        "elbow_flex": (3, "xl330-m077"),
        "wrist_flex": (4, "xl330-m077"),
        "wrist_roll": (5, "xl330-m077"),
        "gripper": (6, "xl330-m077"),
    },
)

# initialise the follower arm
follower_arm = DynamixelMotorsBus(
    port=follower_port,
    motors={
        # name: (index, model)
        "shoulder_pan": (1, "xl430-w250"),
        "shoulder_lift": (2, "xl430-w250"),
        "elbow_flex": (3, "xl330-m288"),
        "wrist_flex": (4, "xl330-m288"),
        "wrist_roll": (5, "xl330-m288"),
        "gripper": (6, "xl330-m288"),
    },
)

def read_raw_position(arm):
    motor_ids = [motor[0] for motor in arm.motors.values()]
    motor_models = [motor[1] for motor in arm.motors.values()]
    raw_values = arm._read_with_motor_ids(motor_models, motor_ids, "Present_Position")
    # Convert to unsigned 32-bit int, then to signed 32-bit int
    raw_values = np.array(raw_values, dtype=np.uint32).view(np.int32)
    return raw_values

# connect the leader arm
leader_arm.connect()
# print the calibrated and raw positions of the leader arm
print("Leader arm calibrated position:", leader_arm.read("Present_Position"))
print("Leader arm raw position:", read_raw_position(leader_arm))

# connect the follower arm
follower_arm.connect()
# print the calibrated and raw positions of the follower arm
print("Follower arm calibrated position:", follower_arm.read("Present_Position"))
print("Follower arm raw position:", read_raw_position(follower_arm))


# disconnect the leader arm
leader_arm.disconnect()
# disconnect the follower arm
follower_arm.disconnect()