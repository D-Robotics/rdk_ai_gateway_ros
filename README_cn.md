# RDK AI Gateway ROS

## 节点介绍

本仓库让开发者在RDK系列开发板上使用火山引擎大模型网关。

支持的模型如下：
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

需用户准备以下：

1. 地瓜机器人社区账号和密码。地瓜机器人社区官网：https://developer.d-robotics.cc/
2. RDK系列开发板一台。用户需自行将RDK开发板连网。

## 节点使用

本项目分为申请节点和使用节点，申请节点只需执行一次。后续每次使用时，只需开启使用节点（即一个ROS服务）并向服务发送请求即可。

### 环境准备

安装ros依赖：
```
sudo apt update
sudo apt install python3-colcon-ros
```

激活ros环境（注：每次新开一个terminal（终端），都建议重新激活一下环境，即执行以下代码）
对于RDK OS V3.0版本，执行：`source /opt/tros/humble/setup.bash`
对于RDK OS V2.1版本，执行：`source /opt/tros/setup.bash`

在RDK开发板上新建一个工作空间目录，并构建src子目录：

```
mkdir -p colcon_ws/src
cd colcon_ws/src
```

使用git clone命令，将本项目克隆至src目录下。

```
git clone https://github.com/D-Robotics/rdk_ai_gateway_ros.git
```

进入项目，安装pip依赖
```
cd rdk_ai_gateway_ros
pip3 install -r requirements.txt
cd ..
```

回到工作空间目录，构建项目

```
cd ..
colcon build
```


激活项目环境（注：在完成环境构建后，每次新开一个terminal（终端），都建议重新激活一下环境，即执行以下代码）
对于RDK OS V3.0版本，执行：`source ./install/setup.sh`
对于RDK OS V2.1版本，执行：`source ./install/setup.bash`


### 申请节点

申请节点的意义在于，使用社区账号和RDK开发板申请api key。

```
ros2 run rdk_ai_gateway apply
```

输入Y，回车，同意许可协议。
输入用户名、密码。

如社区用户名、密码正确，则会在`/root/.ros/rdk_ai_gateway`目录下生成`auth.bin`文件。

### 使用节点

在`auth.bin`文件生成后，开发者可在`colcon_ws/src/rdk_ai_gateway_ros/rdk_ai_gateway/config/param.yaml`中配置当前.bin文件的路径。

随后，启动ROS server节点，输入刚配置的.yaml文件的路径：

```
ros2 run rdk_ai_gateway service --ros-args --params-file /root/colcon_ws/src/rdk_ai_gateway_ros/rdk_ai_gateway/config/param.yaml
```

后续，开发者可以通过以下两种方式，以client调用服务。

1. 命令行：`ros2 service call /text_to_text rdk_ai_gateway_msg/srv/TextToText "{input: '第一次去北京去哪玩', model: 'qwen-7b'}"`
2. 本项目已将client打包成节点，便于用户后续撰写自己节点时用于参考。继续在`colcon_ws/src/rdk_ai_gateway_ros/rdk_ai_gateway/config/param.yaml`中配置当前prompt，即input_str，和model。运行：`ros2 run rdk_ai_gateway client --ros-args --params-file /root/colcon_ws/src/rdk_ai_gateway_ros/rdk_ai_gateway/config/param.yaml`

model参数可做如下配置：
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