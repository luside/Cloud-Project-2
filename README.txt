# Cloud-Project-2

Boto
======================================================================
Before we start, we need to ensure ubuntu has installed python:
$ sudo apt-get update
$ sudo apt-get install python-boto
To launch instances with ansible, first you need to know the id of image that you want to establish the instance on.
By executing this block of code:
image = ec2_conn.get_all_images() for img in images:
print(‘id’, img.id, ‘name’, img.name)
You will get a list of all available images on nectar, and for this project, we use the latest version of ubuntu 16.04, whose image id is ami-c163b887.
After we selected suitable image id, we can start to launch instances. For this group assignment, we are assigned with 4 instances, so the maximum amount of instance would be set to 4. The code for launching instances is listed below:
ec2_conn.run_instances(‘ami-c163b887’, min_count=1, max_count=4, key_name, key=<your key>, instance_type=<up to you to choose>, security_group=[<select what you need, separate by ‘,’>], placement=’melbourne-np’)
The next thing is to create volume and attach it to a instance, you can simply use the default setting in botoSetup.py


Ansible playbook
======================================================================
In this assignment, ansible is responsible for setting up the environment for crawling tweets, filtering and storing them into CouchDb.
To use ansible, first you need to install ansible on your own machine, if you have installed homebrew before, you can use this command:
$ brew install ansible
Before we use the ansible playbook, we need to create a host file containing the information of virtual machines whom we will connect to, and they should be divided into different groups according to your need. The following is an example:
[instance]
<name-you-would-like-to-call-it, like ‘instance-01’> ansible_ssh_host=<your-instance- address> ansible_connection=ssh ansible_ssh_private_key_file=<path-of-your-private-key>
3 ansible playbook are included in the project. The setup.yml can ensure all the packages are installed and then start crawling program. The config.yml is responsible for installing CouchDb on specific instance, configuring the bind address so that other instances can save processed tweets into it and changing the default database and view directories to the extra volume. Last, monitor.yml can be ran with a fixed interval to check the status of crawling programs running on instances. If all the programs work well ,then everything is fine, but when the amount of tweets that we crawled has exceeded the limitation of Twitter, the program will exit, monitor.yml can restart the failed program
To run setup.yml, you can use following command:
8
$ ansible-playbook setup.yml --ask-sudo-pass --ask-become-pass
The config.yml do not need to be run because it will be invoked in setup.yml automatically. To run monitor.yml, if you would like to check the process every hour, this command might be helpful:
$ while true; do ansible-playbook monitor.yml; sleep 3600; done


CouchDB
======================================================================
Before installing the CouchDB, we need to update the system
$ sudo apt-get update
install software that allows you to manage the source repositories
$ sudo apt-get install software-properties-common -y
Add the PPA to help us fetch the latest CouchDB version from the appropriate repository:
$ sudo add-apt-repository ppa:couchdb/stable -y
update the system to get latest package information
$sudo apt-get update
Install CouchDB
$sudo apt-get install couchdb -y
Create a new database with the curl -X PUT command:
$curl -X PUT localhost:5984/new_database
Bind to 0.0.0.0 so that other ip address besides localhost can access the database 
$sudo curl -X PUT http://localhost:5984/_config/httpd/bind_address -d '"0.0.0.0"'


Web
======================================================================
The web application is running on your own computer. If you’re running a Unix-like System, just follow the steps below. Otherwise, you need to find the corresponding operations of your system.
Before starting, you need to install Python 3 and some packages used in this application. If you have these things on your computer, you can skip these steps.
Install Python 3
$ sudo apt-get install python3
Install pip to get python packages
$ sudo apt-get install python3-pip
Install CouchDb package for Python
$ pip install couchdb
Install Flask package for Python
$ pip install Flask
Install geoJSON package for Python
$ pip install geojson
Now, you can run the web application.
Firstly, run the web server
$ python flask_server.py
It will create a url and every time the front-end access the url, it will query the latest tweets from CouchDb and then return the result to front-end.
It should be noticed that if the port (1337 as default) is being used by another application, you need to change the port value in the main function of flask_server.py (line 70), and then change the port of corresponding var url (‘http://localhost:1337/’ as default) in realtime_mp.js (line 6). That’s where the front-end request the latest tweets.
Then, before opening the web, you need to apply for a mapbox accesstoken and add it in realtime_map.js (line 2).
Now, you can open the index.html with Chrome browser directly to see the results.