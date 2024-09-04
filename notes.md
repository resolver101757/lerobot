# notes for koch robot arm

# run teleoperate without cameras

`python lerobot/scripts/control_robot.py teleoperate --robot-path lerobot/configs/robot/koch.yaml --robot-overrides '~cameras'` 

On powershell command prompt, the line 

`python lerobot/common/robot_devices/cameras/opencv.py \
    --images-dir outputs/images_from_opencv_cameras`

Needs changing to : 

`python lerobot/common/robot_devices/cameras/opencv.py --images-dir outputs/images_from_opencv_cameras`

The pixel pro camera on windows works without any extra libraries.  Just detects as 2nd index. Looks like you can select the zoom on the phone too which is pretty neat. 

# run teleoperate with cameras

python lerobot/scripts/control_robot.py teleoperate --robot-path lerobot/configs/robot/koch.yaml --robot-overrides '~cameras'

`python lerobot/scripts/control_robot.py teleoperate --robot-path lerobot/configs/robot/koch.yaml`

Hugging face api

`huggingface-cli login --token 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 --add-to-git-credential`

# Run a test record to test data 

`python lerobot/scripts/control_robot.py record --robot-path lerobot/configs/robot/koch.yaml --fps 30 --root data --repo-id ${HF_USER}/koch_test --tags tutorial --warmup-time-s 5 --episode-time-s 30 --reset-time-s 30 --num-episodes 2`

# run test without cameras 
`python lerobot/scripts/control_robot.py teleoperate --robot-path lerobot/configs/robot/koch.yaml --robot-overrides '~cameras'` 

# Test the dynamixel motors

list serail ports to see if they are available `python -m serial.tools.list_ports`

Test connection to the motors on follower arm `python lerobot/common/robot_devices/motors/dynamixel.py --port COM5`  

Test connection to the motors on leader arm `python lerobot/common/robot_devices/motors/dynamixel.py --port COM6`


# Run the calibration test script 

calibratess and runs the robot (will error if no cameras are connected)`python lerobot/scripts/control_robot.py calibrate`

