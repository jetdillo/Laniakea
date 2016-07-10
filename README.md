# laniakea

Laniakea AKA "Turtle Beach", where turtles and robots are hatched.

The Revolution will be automated. 

This started out as a collection of Ansible and Fabric scripts & playbooks for building the 
Ubiquity ROS image described at the [Ubiquity Robots Download and Install Guide](https://github.com/UbiquityRobotics/ubiquity_main/blob/master/Doc_Downloading_and_Installing_the_Ubiquity_Ubuntu_ROS_Kernel_Image.md). Spurred on by help and testing from [Ubiquity Robots](http://ubiquityrobotics) and the [Homebrew Robotics Club](http://hbrobotics.org), it has since grown into a project that aims to provide a automated way to install [ROS](http://www.ros.org) and ROS-related packages for Linux-based robots. 

As fine as the [OSRF ROS](http://www.ros.org/install/) and [Ubiquity Robots](http://ubiquityrobotics) documentation is, I got tired of having to go back over it time and again when building my own ROS-based robots, I figure others probably have too. 

The problem is that all real companies get this, spend tons of time on their own provisioning, repeat a lot of the same steps, flavor to taste w/ their own internal packages and then it all disappears inside that organization because now it contains their own internal special sauce.  So the next team that has to bring up a bunch of robots has to go look at the directions, write their own provisioning scripts...you see where this is going. The robot revolution is not going to happen, or at least not happen that quickly, if we can't at least have the robots help build themselves. 

Pull requests, feature enhancements, etc. are welcome. 

Laniakea is compatible w/ Ansible 1.x, I've not started looking at 2.x yet. 

Relevant websites for those that aren't familiar with either Fabric or Ansible:

Ansible: 
https://www.ansible.com/

Fabric:
http://www.fabfile.org/

If you are new to Ansible and are using it for the first time to try to bring up ROS, please don't try to install by pulling Ansible from their Github repo. That is almost guaranteed to end in sadness, esp. if you don't have a whole lot of experience w/ building large systems under Linux. 
 
Instead, use the Fabric script under the Fabric directory of this repo or rip out the apt-get lines from fabfile.py and run those from your shell. 

In any case, you should be using the current Ubuntu-provided Ansible packages, which will install Ansible 1.x, which is what Laniakea wants. I've not started looking at Ansible 2.x yet.  

Roles are proceeding apace and under active development & testing. 
* As of late June 2016, the `sd`, `ubuntu` and `rpi` roles have seen the most work.  
   * The `rpi3.yml` generates a satisfactory 16.04 image suitable for installing ROS Kinetic, but the distro as provided leaves a few things to be desired,
     openssh-server is not installed by default, there is no Python of any flavor installed. I can't recommend this unless you REALLY need an image for a Pi 3 because it's far from seamless. After getting up up and running you'd apply the 'ubuntu' role to install Kinetic on there. 

   * The Jetson role is mostly for flashing the "Grinch kernel" and related FS onto a TK1 board because NVidia has their own installer which they make you sign up and login for. 

The existing playbooks under the main top-level "playbooks" tree will be left as is for those who just want to play along at home and don't want/need a whole huge role-based build system. 

## Playbooks

Static, self-contained playbooks are found under laniakea/playbooks and do the following things:

* make_sd.yml
   * Makes a ready-to-run SD card using the Ubiquity image from [Ubiquity Robots](http://ubiquityrobotics). This will get you an Ubuntu 14.04 "Trusty" server image running ROS Indigo Igloo suitable for use on a Raspberry Pi 2. 
   * Run with the command-line: ``ansible-playbook -K make_sd.yml``
* newbiquity.yml
   *  Ansible provisioning playbook to finish up package installs and config tweaks on the image generated by ``make_sd.yml`` for the Ubiquity image.
   * Run with the command-line: ``ansible-playbook -K -k newbiquity.yml -u ubuntu --extra-vars "robothost=ubuntu.local"``
      * N.B. This is run w/ -K -k because the newly-flashed image will not have any public ssh keys installed on it yet and needs a user password. The public key ~/.ssh/id_rsa.pub is copied over as part of this playbook. 

* bv80.yml
   * Ansible provisioning playbook to add packages & configs for the SVROS BV80 BotVac, run after ``make_sd.yml`` and ``newbiquity.yml``
   * Run with the command-line: ``ansible-playbook -K bv80.yml -u ubuntu --extra-vars "robothost=ubuntu.local rosdistro=indigo"``

* setup_ros.yml 
   * A basic provisioning playbook to install a specified version of ROS onto a host.  You should only need to use this on a system/series of systems that don't have ROS already installed(like, say, a chaser/maintenance laptop or an SBC that already has Linux installed on it.) This is basically an Ansible-ization of the instructions found on [The OSRF Ubuntu install page](http://wiki.ros.org/indigo/Installation/Ubuntu). 


## Roles

Platform-based "Roles" live under `ansible/roles` and cover the following tasks below. 
These work best for experienced Ansible users

* common
   * Common variables and tasks, mostly apt-gets to install necessary packages live here

* sd  _under development_
   * Role for flashing Ubuntu and/or ROS onto SD-card

* ubiquity **WORKS**
   * Role for flashing the [Ubiquity Robots](http://ubiquityrobotics) image onto an SD card.

* ubuntu **WORKS**
   * Role for installing ROS and configuring a catkin workspace on an Ubuntu Linux system on the same LAN segment as the system you're running Ansible from. 

## Top-level 

`.yml` files at the top of the `ansible` tree bring in specific vars_files to the more generic roles. For example, the `rpi3.yml` playbook uses the `sd` role with variable set for making an SD card to run Ubuntu 16.04 on a Raspberry Pi 3. 

How to run:

You will need to have Ansible installed already on the computer you run these playbooks from.
cd <YOUR LOCAL GIT REPO>/laniakea/ansible/playbooks

## Make a ROS Indigo SD card running the Ubiquity Robotics 14.04 image

**NB: SD cards can be wonky and vary in quality from vendor to vendor or even batch to batch from the same vendor. If you are having problems getting the dd or other partition/imaging tasks to run, try another card before submitting a bug. I've run into this myself when testing the `sd` role **

To run make_sd.yml to flash an SD card with the Ubiquity Robotics image for Raspberry Pi do this:

`ansible-playbook -K make_sd.yml`  

...and follow the prompts

After make_sd.yml completes, run:
`ansible-playbook -k -K -u ubuntu --extra-vars "robothost=ubiquity" newbiquity.yml` 

...to finish installing some ubiquity-specific packages

## Install ros-<distro>-ros-base on an existing Ubuntu host:

* Add the following lines to your /etc/ansible/hosts file:
[newbot]
123.45.67.89 <---replace with the real IP of the target host

* Run `ansible-playbook -K -u ubuntu --extra-vars "robothost=newbot rosdistro=<distro>" ubuntu.yml`
  * Give the sudo password of the *remote* system when prompted. 
  * Wait 10-30 minutes depending on your Internet connectivity
  * Follow this up with whatever you need to do next, such as `ansible-playbook -K -u ubuntu --extra-vars "robothost=newbot" turtlebot.yml` if you're trying to build a Turtlebot for example...

The extra "-k" tells Ansible that you need to use regular password auth along with the sudo password for this playbook run. This is because fresh out of the box, this install doesn't have any ssh public keys stored in /home/ubuntu/.ssh/authorized_keys 

From here you branch off into other appropriate playbooks for installing the BV80 BotVac packages, for example.

These should mostly work, although the make_sd.yml has received the brunt of hacking and testing. Please send pull requests, comments, bug reports, etc. 
