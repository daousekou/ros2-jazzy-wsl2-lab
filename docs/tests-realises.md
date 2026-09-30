# Tests realises

Cette page sert de trace technique pour valider le laboratoire ROS 2.

## Tests prevus

| Test | Commande | Resultat attendu |
| --- | --- | --- |
| Version Ubuntu | `lsb_release -a` | Ubuntu 24.04 LTS |
| ROS 2 actif | `ros2 --help` | Affiche l'aide ROS 2 |
| Build workspace | `colcon build` | Build termine sans erreur |
| Package visible | `ros2 pkg list \| grep loq_ros2_demo` | Package liste |
| Talker | `ros2 run loq_ros2_demo simple_talker` | Publication de messages |
| Listener | `ros2 run loq_ros2_demo simple_listener` | Reception des messages |
| Topic | `ros2 topic echo /demo_message` | Messages visibles |
| URDF | `check_urdf urdf/simple_robot.urdf` | Modele parse correctement |

## Notes

Les tests dependent d'une installation locale ROS 2 Jazzy fonctionnelle. Aucun resultat local personnel n'est publie dans ce depot.
