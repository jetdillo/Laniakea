# laniakea

Roles: Mostly aspirational and under construction. Things mostly work, except when they don't. 

If you are looking for a quick way to make yourself an SD-card for a ROS-based Raspberry Pi robot, you want to be in the Playbooks tree, not here. 

What-does-what:

- common - Mostly ROS-specific environment variables and platform-common tasks. No plays planned at this time.
- ubiquity - role-based version of the make_sd and newbiquity playbooks
- sd - Role for generating an Ubuntu SD card for a Raspberry Pi 2/3 and then installing ROS on it.
- ubuntu - Role for installing ROS on an existing Ubuntu host. The user is expected to flavor-to-taste env. vars in defaults
- jetson - Role for flashing the Grinch distro and kernel onto a Jetson TK1 board, also including playbooks for installing & testing a Zed camera from Stereolabs. 


