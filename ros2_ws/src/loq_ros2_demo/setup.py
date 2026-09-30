from setuptools import find_packages, setup

package_name = "loq_ros2_demo"

setup(
    name=package_name,
    version="0.1.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Example Maintainer",
    maintainer_email="example@example.com",
    description="Minimal ROS 2 Jazzy demo package for WSL2 learning.",
    license="TODO",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "simple_talker = loq_ros2_demo.simple_talker:main",
            "simple_listener = loq_ros2_demo.simple_listener:main",
        ],
    },
)
