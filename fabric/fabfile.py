from fabric.api import *

env.hosts=['ubuntu.local']
env.user="ubuntu"
env.passwords={"ubuntu@ubuntu.local":"ubuntu"}

def anonymous():
    run("uname -a")

def keypush():
   run("mkdir -p /home/ubuntu/.ssh")
   put("/etc/ssh/ssh_host_ecdsa_key.pub", "/home/ubuntu/.ssh/known_hosts",mode=0600,use_sudo=True)
   put("~/.ssh/id_rsa.pub","/home/ubuntu/.ssh/authorized_keys",mode=0600,use_sudo=True)
   run("ssh-keygen -b 2048 -t rsa -N '' ")
   run("cat ~/.ssh/id_rsa.pub >>/home/ubuntu/.ssh/authorized_keys")

def ansible_prep(): 
    local("sudo apt-get -y install software-properties-common && apt-add-repository -y ppa:ansible/ansible && apt-get update && apt-get -y install ansible")
    local("sudo apt-get -y install openssh-server")
    local("sudo apt-get -y install git") 
    local("sudo apt-get -y install curl") 
    local("sudo apt-get -y install initscripts") 

