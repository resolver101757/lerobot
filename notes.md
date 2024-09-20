# notes for koch robot arm

# run teleoperate without cameras

`python lerobot/scripts/control_robot.py teleoperate --robot-path lerobot/configs/robot/koch.yaml --robot-overrides '~cameras'` 

On powershell command prompt, the line

`python lerobot/common/robot_devices/cameras/opencv.py \
    --images-dir outputs/images_from_opencv_cameras`

Needs changing to : 

`python lerobot/common/robot_devices/cameras/opencv.py --images-dir outputs/images_from_opencv_cameras`

The pixel pro camera on windows works without any extra libraries.  Just detects as 2nd index. Looks like you can select the zoom on the phone too which is pretty neat.

# Run teleoperate with cameras

- orignal

`python lerobot/scripts/control_robot.py teleoperate --robot-path lerobot/configs/robot/koch.yaml`

- realsense and phone

`python lerobot/scripts/control_robot.py teleoperate --robot-path lerobot/configs/robot/koch_realsense_phone.yaml`

- just realsense

`python lerobot/scripts/control_robot.py teleoperate --robot-path lerobot/configs/robot/koch_realsense.yaml`

# Set the Huggingface token 

`huggingface-cli login --token $env:HUGGINGFACE_TOKEN --add-to-git-credential`

# Run a test record to test data 

- original 

    `python lerobot/scripts/control_robot.py record --robot-path lerobot/configs/robot/koch_original.yaml --fps 30 --root data --repo-id $env:HF_USER/koch_test --tags tutorial --warmup-time-s 5 --episode-time-s 30 --reset-time-s 30 --num-episodes 2`

- realsense and phone 

    `python lerobot/scripts/control_robot.py record --robot-path lerobot/configs/robot/koch_realsense_phone.yaml --fps 30 --root data --repo-id $env:HF_USER/koch_test --tags tutorial --warmup-time-s 5 --episode-time-s 30 --reset-time-s 30 --num-episodes 2`

- just realsense

    python lerobot/scripts/control_robot.py record `
        --robot-path lerobot/configs/robot/koch_realsense.yaml `
        --fps 30 `
        --root data `
        --repo-id $env:HF_USER/koch_test `
        --tags tutorial `
        --warmup-time-s 5 `
        --episode-time-s 30 `
        --reset-time-s 30 `
        --num-episodes 2

# Run test without cameras 

- origianl

`python lerobot/scripts/control_robot.py teleoperate --robot-path lerobot/configs/robot/koch_original.yaml --robot-overrides '~cameras'`

- realsense and phone  

`python lerobot/scripts/control_robot.py teleoperate --robot-path lerobot/configs/robot/    koch_realsense_phone.yaml --robot-overrides '~cameras'`

- just realsense

`python lerobot/scripts/control_robot.py teleoperate --robot-path lerobot/configs/robot/koch_realsense.yaml --robot-overrides '~cameras'`


# Test for the dynamixel motors

list serail ports to see if they are available `python -m serial.tools.list_ports`

Test connection to the motors on follower arm `python lerobot/common/robot_devices/motors/dynamixel.py --port COM5`  

Test connection to the motors on leader arm `python lerobot/common/robot_devices/motors/dynamixel.py --port COM6`

# Run the calibration test script 

calibratess and runs the robot (will error if no cameras are connected)`python lerobot/scripts/control_robot.py calibrate`

# List realsense cameras

import pyrealsense2 as rs

Create a context object
context = rs.context()

Get a list of all connected devices
devices = context.query_devices()

Iterate through the devices and print their info
for i, device in enumerate(devices):
    print(f"Device {i}:")
    print(f"  Name: {device.get_info(rs.camera_info.name)}")
    print(f"  Serial Number: {device.get_info(rs.camera_info.serial_number)}")
    print(f"  Product ID: {device.get_info(rs.camera_info.product_id)}")
    print()


# Potential tasks to complete

- use one of hugos small cups to move 
- pick up a ball from the table and place in a sloped shoot and pickup once it rolls to the bottom.
- Aliexpress, Richard sending it through
- 