from fabric.api import *

env.hosts=['ubuntu.local']
env.user="ubuntu"
env.passwords={"ubuntu@ubuntu.local":"ubuntu"}

def anonymous():
    run("uname -a")

def keypush():
    with lcd("~/.ssh")
    if local("test -f id_rsa").failed:
       print "No local ssh key. Please run ssh-keygen then run this again...")
       sys.exit(1)
    else:
       run("mkdir -p /home/ubuntu/.ssh")
       run("sudo scp /etc/ssh_host_rsa_key /home/ubuntu/.ssh/known_hosts")
       put("~/.ssh/id_rsa.pub","/home/ubuntu/.ssh/authorized_keys")

def ansible_prep(): 
    local("sudo apt-get -y install software-properties-common && apt-add-repository -y ppa:ansible/ansible && apt-get update && apt-get -y install ansible")
    local("sudo apt-get -y install openssh-server")
    local("sudo apt-get -y install git") 
    local("sudo apt-get -y install curl") 
    local("sudo apt-get -y install initscripts") 

