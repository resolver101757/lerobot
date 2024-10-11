from lerobot.common.robot_devices.motors.dynamixel import DynamixelMotorsBus
from lerobot.common.robot_devices.motors.dynamixel import TorqueMode
import time

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

# connect the leader arm
leader_arm.connect()
# print the position of the leader arm
print(leader_arm.read("Present_Position"))

# connect the follower arm
follower_arm.connect()
# print the position of the follower arm
print(follower_arm.read("Present_Position"))

#enable torque (control mode)
#follower_arm.write("Torque_Enable", TorqueMode.ENABLED.value)

# make the follower arm follow the leader arm - add 30 to the leader arm position
#follower_arm.write("Goal_Position", follower_arm.read("Present_Position") + 30)
#follower_arm.write("Goal_Position", leader_arm.read("Present_Position"))

# read the position of the arms and make the follower arm follow the leader arm 
# the idea is to comment each one out and see the results when trouble shooting 
#fpos = follower_arm.read("Present_Position")
#lpos = leader_arm.read("Present_Position")
#fpos[0] = lpos[0]
#fpos[1] = lpos[1]
#fpos[2] = lpos[2]
#fpos[3] = lpos[3]
#fpos[4] = lpos[4]
#fpos[5] = lpos[5]

# write the position to the follower arm
#follower_arm.write("Goal_Position", fpos)
#time.sleep(3)

# disable the torque of the follower arm
#follower_arm.write("Torque_Enable", TorqueMode.DISABLED.value)
#time.sleep(3)

# disconnect the leader arm
leader_arm.disconnect()
# disconnect the follower arm
follower_arm.disconnect()