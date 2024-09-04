# RDK AI Gateway ROS

## Node introduction

This repository allows developers to use the Volcengine Large Model Gateway on RDK series development boards.

Supported models are as follows:
```
doubao-pro-4k
doubao-pro-32k
doubao-pro-128k
doubao-lite-4k
doubao-lite-32k
doubao-lite-128k
qwen-VL-8k
qwen-7B
```

Users need to prepare the following:

1. D-Robotics Community Account and Password. D-Robotics Community Official Website: https://developer.d-robotics.cc/
2. One RDK series development board. Users need to connect the RDK development board to the network by themselves.

## Node use

This project is divided into application nodes and usage nodes. The application node only needs to be executed once. For each subsequent use, only the usage node (i.e. a ROS service) needs to be enabled and a request needs to be sent to the service.

### Environmental preparation

Install ros dependencies:
```
sudo apt update
sudo apt install python3-colcon-ros
```

Activate the ROS environment (Note: It is recommended to reactivate the environment every time a new terminal (end point) is opened, that is, execute the following code).
For RDK OS V3.0 version, execute: `source /opt/tros/humble/setup.bash`
For RDK OS V2.1, execute: `source /opt/tros/setup.bash`

Create a new workspace directory on the RDK development board and build the src subdirectory.

```
mkdir -p colcon_ws/src
cd colcon_ws/src
```

Use the git clone command to clone this project to the src directory.

```
git clone https://github.com/D-Robotics/rdk_ai_gateway_ros.git
```

Enter the project and install the pip dependencies
```
cd rdk_ai_gateway_ros
pip3 install -r requirements.txt
cd ..
```

Return to the workspace directory and build the project

```
cd ..
colcon build
```


Activate the project environment (Note: After completing the environment construction, it is recommended to reactivate the environment every time a new terminal (end point) is opened, that is, execute the following code).
For RDK OS V3.0 version, execute: `source./install/setup.sh`
For RDK OS V2.1, execute: `source./install/setup.bash`


### Apply node

The significance of applying for nodes is to apply for API keys using community accounts and RDK development boards.

```
ros2 run rdk_ai_gateway apply
```

Enter Y, press Enter, and agree to the Licensing Agreement.
Enter username and password.

If the community username and password are correct, the `auth.bin` file will be generated in the `/root/.ros/rdk_ai_gateway` directory.

### Use node

After the `auth.bin` file is generated, developers can configure the path of the current .bin file in `colcon_ws/src/rdk_ai_gateway_ros/rdk_ai_gateway/config/param.yaml`.

Afterwards, start the ROS server node and enter the path of the newly configured .yaml file.

```
ros2 run rdk_ai_gateway service --ros-args --params-file /root/colcon_ws/src/rdk_ai_gateway_ros/rdk_ai_gateway/config/param.yaml
```

Later, developers can call the service as a client in the following two ways.

3. Command line: `ros2 service call /text_to_text rdk_ai_gateway_msg/srv/TextToText "{input: 'Where to play in Beijing for the first time', model: 'qwen-7b'}"`
4. This project has packaged the client into a node for reference when users write their own nodes later. Continue to configure the current prompt, i.e. input_str, and model in `colcon_ws/src/rdk_ai_gateway_ros/rdk_ai_gateway/config/param.yaml`. Run: `ros2 run rdk_ai_gateway client --ros-args --params-file /root/colcon_ws/src/rdk_ai_gateway_ros/rdk_ai_gateway/config/param.yaml`

The model parameters can be configured as follows:
```
doubao-pro-4k
doubao-pro-32k
doubao-pro-128k
doubao-lite-4k
doubao-lite-32k
doubao-lite-128k
qwen-VL-8k
qwen-7B
```