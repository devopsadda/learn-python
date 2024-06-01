#!/bin/python3.11

#uderstanding the fabric module functionality
def hello():
 print("Hello, You are welcome to automation")

#executing the command on the local machine
from fabric.api import local
def uptime():
 local('uptime')

#executing the command on the remote machine
from fabric.api import env, run
env.user = 'cloud_user'
env.hosts = ['cloud_user@3.0.16.37','cloud_user@54.254.229.81']

def echo():
 run("echo -n 'Hello, you are tuned for automation'")

def deploy_lamp():
 run("yum install httpd mariadb-server php php-mysql -y")

def uptime_remote():
 run('uptime')

def disk_space():
 run('df -kh')

def kernel_version():
 run('uname -a')

hello()
uptime()
echo()
uptime_remote()
