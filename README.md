# ROS 2 Jazzy sous WSL2

Projet de laboratoire pour installer, tester et documenter un environnement ROS 2 Jazzy dans Ubuntu sous WSL2.

Ce depot est volontairement generique. Il ne contient aucun secret, aucun chemin local personnel, aucun identifiant et aucune information liee a une entreprise.

## Objectifs

- Installer ROS 2 Jazzy dans Ubuntu sous WSL2.
- Creer un workspace ROS 2 avec `colcon`.
- Compiler et lancer un premier package Python.
- Verifier la communication ROS 2 avec `talker` et `listener`.
- Creer un premier noeud ROS 2 Python.
- Verifier le noeud avec `ros2 node list` et `ros2 node info`.
- Ajouter une base de travail pour TF2 et URDF.
- Documenter les commandes et les tests realises.

## Architecture

```text
.
|-- README.md
|-- docs/
|   |-- commandes.md
|   |-- securite.md
|   `-- tests-realises.md
|-- ros2_ws/
|   `-- src/
|       `-- loq_ros2_demo/
|           |-- package.xml
|           |-- resource/
|           |   `-- loq_ros2_demo
|           |-- setup.cfg
|           |-- setup.py
|           `-- loq_ros2_demo/
|               |-- __init__.py
|               |-- simple_listener.py
|               `-- simple_talker.py
`-- urdf/
    `-- simple_robot.urdf
```

## Prerequis

- Windows 11 avec WSL2 active.
- Ubuntu 24.04 dans WSL2.
- Connexion Internet pendant l'installation.
- Droits administrateur Windows uniquement pour l'installation de WSL2 si necessaire.

ROS 2 Jazzy est prevu pour Ubuntu 24.04. Les commandes peuvent evoluer avec le temps : il faut toujours verifier la documentation officielle ROS 2 avant une nouvelle installation.

Documentation officielle : <https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html>

## Installation de base

Dans Ubuntu WSL2 :

```bash
sudo apt update
sudo apt install -y software-properties-common curl lsb-release
sudo add-apt-repository universe
sudo apt update
```

Ajouter le depot ROS 2 officiel :

```bash
export ROS_APT_SOURCE_VERSION=$(curl -s https://api.github.com/repos/ros-infrastructure/ros-apt-source/releases/latest | grep -F "tag_name" | awk -F\" '{print $4}')

curl -L -o /tmp/ros2-apt-source.deb \
  "https://github.com/ros-infrastructure/ros-apt-source/releases/download/${ROS_APT_SOURCE_VERSION}/ros2-apt-source_${ROS_APT_SOURCE_VERSION}.$(. /etc/os-release && echo ${UBUNTU_CODENAME:-${VERSION_CODENAME}})_all.deb"

sudo dpkg -i /tmp/ros2-apt-source.deb

sudo apt update
sudo apt install -y ros-jazzy-desktop ros-dev-tools python3-colcon-common-extensions
```

Activer ROS 2 dans le terminal :

```bash
source /opt/ros/jazzy/setup.bash
```

Option pratique :

```bash
echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc
```

## Utilisation du workspace

Depuis la racine du depot :

```bash
cd ros2_ws
source /opt/ros/jazzy/setup.bash
colcon build
source install/setup.bash
```

Terminal 1 :

```bash
ros2 run loq_ros2_demo simple_talker
```

Terminal 2 :

```bash
ros2 run loq_ros2_demo simple_listener
```

## Tests rapides

Tester les noeuds de demonstration ROS 2 :

```bash
ros2 run demo_nodes_cpp talker
ros2 run demo_nodes_py listener
```

Verifier les topics :

```bash
ros2 topic list
ros2 topic echo /demo_message
```

Verifier les packages :

```bash
ros2 pkg list | grep loq_ros2_demo
```

Lancer le package de demonstration du depot :

```bash
ros2 run loq_ros2_demo simple_talker
ros2 run loq_ros2_demo simple_listener
```

Verifier les noeuds actifs :

```bash
ros2 node list
ros2 node info /simple_talker
```

## Concepts couverts

### Publisher, topic et subscriber

Le premier test ROS 2 illustre le principe :

```text
Node publisher -> Topic -> Node subscriber
```

Ce schema est la base de nombreux systemes robotiques. Par exemple, un capteur peut publier des mesures pendant qu'un autre noeud les utilise pour la localisation, le SLAM ou la navigation.

### Workspace ROS 2

Un workspace ROS 2 contient generalement :

```text
ros2_ws/
|-- build/
|-- install/
|-- log/
`-- src/
```

Le dossier `src` contient le code source. Les dossiers `build`, `install` et `log` sont generes par `colcon` et ne sont pas suivis dans Git.

### Premier noeud Python

Un noeud ROS 2 Python repose sur `rclpy` et herite de la classe `Node`. Le fichier doit ensuite etre declare dans `setup.py` pour pouvoir etre lance avec `ros2 run`.

Exemple de commande de build ciblee :

```bash
colcon build --packages-select loq_ros2_demo
source install/setup.bash
```

### Erreur courante

Une erreur Python comme `IndentationError` indique souvent un probleme d'alignement dans le code. Apres correction, il faut reconstruire le package puis recharger l'environnement du workspace.

## URDF

Le fichier `urdf/simple_robot.urdf` contient un robot minimal pour comprendre la structure `base_link`, `joint` et `link`.

Pour verifier le fichier :

```bash
sudo apt install -y liburdfdom-tools
check_urdf urdf/simple_robot.urdf
```

## Securite

Ce depot ne doit pas contenir :

- tokens ou cles API ;
- mots de passe ;
- adresses e-mail personnelles ;
- chemins locaux personnels ;
- adresses IP privees ou hostnames internes ;
- informations internes d'entreprise ;
- fichiers `.env`, certificats, cles SSH ou configurations avec credentials.

Voir [docs/securite.md](docs/securite.md).

## Licence

Ce projet est fourni comme support d'apprentissage. Ajouter une licence explicite avant reutilisation publique dans un contexte professionnel.
