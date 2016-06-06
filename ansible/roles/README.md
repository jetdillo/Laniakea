# laniakea

Roles: Mostly aspirational and under construction. Don't expect any of this to work just yet, but feel free to jump in if you want to help. 
Placed here mostly as a placeholder for when I forget what I was doing here last. 
 The plan here is to break out the playbooks into roles so that each build can be abstracted out a bit more. 

You should, for example, just be able to ask for the software stack for a Ubiquity or Turtlebot-like robot to be built and not have to worry about which playbook you run in what order. This will also allow for abstraction for tests. 

This is really only for users looking to use/help build a larger, publically-available automated build-and-deploy system for ROS robots. 

If you are looking for a quick way to make yourself an SD-card for a ROS-based Raspberry Pi robot, you want to be in the Playbooks tree, not here. 

What-does-what:

- common - Mostly ROS-specific environment variables and platform-common tasks. No plays planned at this time.
- ubiquity - role-based version of the make_sd and newbiquity playbooks
- sd - Role for generating an Ubuntu SD card for a Raspberry Pi 2/3 and then installing ROS on it.
- ubuntu - Role for installing ROS on an existing Ubuntu host. The user is expected to flavor-to-taste env. vars in defaults
- jetson - Role for flashing the Grinch distro and kernel onto a Jetson TK1 board

