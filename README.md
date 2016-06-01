# laniakea

Laniakea AKA "Turtle Beach", where turtles and robots are hatched.

The Revolution will be automated. 

This is a collection of Ansible and Fabric scripts & playbooks for building the 
Ubiquity ROS image described at the [Ubiquity Robots Download and Install Guide](https://github.com/UbiquityRobotics/ubiquity_main/blob/master/Doc_Downloading_and_Installing_the_Ubiquity_Ubuntu_ROS_Kernel_Image.md) and installing [ROS](http://www.ros.org) on existing Ubuntu systems.

Laniakea is compatible w/ Ansible 1.x, I've not started looking at 2.x yet. 

The robot revolution is not going to happen, or at least not happen that quickly, if we can't at least have the robots help build themselves. 
As fine as the [OSRF ROS](http://www.ros.org/install/) and [Ubiquity Robots](http://ubiquityrobotics) documentation is, I got tired of having to go back over it time and again when building my own ROS-based robots, I figure others probably have too. 

The problem is that all real companies get this, spend tons of time on their own provisioning, repeat a lot of the same steps, flavor to taste w/ their own internal packages and then it all disappears inside that organization. So the next team that has to bring up a bunch of robots has to go look at the directions, write their own provisioning scripts...you see where this is going. 

Relevant websites for those that aren't familiar with either Fabric or Ansible:

Ansible: 
https://www.ansible.com/
Fabric:
http://www.fabfile.org/

If you are new to Ansible and are using it for the first time to try to bring up ROS, please don't try to install by pulling Ansible from their Github repo. 

That is almost guaranteed to end in sadness, esp. if you don't have a whole lot of experience w/ building large systems under Linux. 
 
Use the Fabric script under the Fabric directory of this repo or rip out the apt-get lines from fabfile.py and run those from your shell. 

In any case, you should be using the current Ubuntu-provided Ansible packages. 

Here's what does what so far:

* make_sd.yml
   * Makes a ready-to-run SD card using the Ubiquity image from [Ubiquity Robots](http://ubiquityrobotics). This will get you an Ubuntu 14.04 "Trusty" server image running ROS Indigo Igloo
* newbiquity.yml
   * Post-boot Ansible provisioning playbook to finish up package installs and config tweaks on the image generated by ``make_sd.yml``
* bv80.yml
   * Post-boot Ansible provisioning playbook to add packages & configs for the SVROS BV80 BotVac

* setup_ros.yml 
   * A basic provisioning playbook to install a specified version of ROS onto a host. You will need to tweak the hosts: line to the system/inventory entry you want to deploy to. The ``make_sd.yml`` playbook generates images w/ ROS Indigo Igloo already installed on it. You should only need to use this on a system/series of systems that don't have ROS already installed(like, say, a chaser/maintenance laptop). 

How to run:

You will need to have Ansible installed already on the computer you run these playbooks from.
cd <YOUR LOCAL GIT REPO>/laniakea/ansible/playbooks

To run make_sd.yml to flash an SD card with the Ubiquity Robotics image for Raspberry Pi do this:

`ansible-playbook -K make_sd.yml`  

...and follow the prompts

After make_sd.yml completes, run:
`ansible-playbook -k -K -u ubuntu --extra-vars "robothost=ubiquity" newbiquity.yml` 

The extra "-k" tells Ansible that you need to use regular password auth along with the sudo password for this playbook run. This is because fresh out of the box, this install doesn't have any ssh public keys stored in /home/ubuntu/.ssh/authorized_keys 

From here you branch off into other appropriate playbooks for installing the BV80 BotVac packages, for example.

These should mostly work, although the make_sd.yml has received the brunt of hacking and testing. Please send pull requests, comments, bug reports, etc. 


