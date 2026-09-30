# Commandes reproductibles

## Verifier WSL2 cote Windows

```powershell
wsl --status
wsl --list --verbose
```

## Verifier Ubuntu

```bash
lsb_release -a
uname -a
```

Version attendue pour ROS 2 Jazzy :

```text
Ubuntu 24.04 LTS
```

## Installer les outils utiles

```bash
sudo apt update
sudo apt install -y git curl gnupg lsb-release build-essential python3-pip
sudo apt install -y python3-colcon-common-extensions python3-rosdep
```

## Initialiser rosdep

```bash
sudo rosdep init
rosdep update
```

Si `rosdep` est deja initialise, continuer avec `rosdep update`.

## Compiler le workspace

```bash
cd ros2_ws
source /opt/ros/jazzy/setup.bash
rosdep install --from-paths src --ignore-src -r -y
colcon build
source install/setup.bash
```

## Lancer le test talker/listener

Terminal 1 :

```bash
source /opt/ros/jazzy/setup.bash
cd ros2_ws
source install/setup.bash
ros2 run loq_ros2_demo simple_talker
```

Terminal 2 :

```bash
source /opt/ros/jazzy/setup.bash
cd ros2_ws
source install/setup.bash
ros2 run loq_ros2_demo simple_listener
```

## Inspecter ROS 2

```bash
ros2 node list
ros2 topic list
ros2 topic info /demo_message
ros2 topic echo /demo_message
```
