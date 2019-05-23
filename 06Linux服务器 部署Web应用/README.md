# Project - Linux Server Configuration #

## Introduction ##

This documentation will guide you to take a baseline installation of a Linux distribution on a virtual machine and prepare it to host your web applications, to include installing updates, securing it from a number of attack vectors and installing/configuring web and database servers.

This instanced Web applications named film item catalog allows users to login into the system and add films to the database. Logged-in users may modify and delete the items they have created. Only authenticated users are allowed to make any changes to the database.

## Server Address ##

- **Server IP Address:** 128.199.170.23
- **SSH server access port:** 2200
- **SSH login username:** grader
- **Application URL:** 
	- [http://lubocsu.me](http://lubocsu.me)
	- [http://128.199.170.23](http://128.199.170.23)

## Configuration ##

__1 Create server instance__ 

- Server provider :[DigitalOcean](https://cloud.digitalocean.com)
- Server instance :[droplet](https://www.digitalocean.com/products/droplets/)
- Server system : Ubuntu 18.04 x64 (OS only without application)
- Server instance plan : /1 GB Memory/25 GB Disk/SGP1 
- SSH and telnet client : [PuTTy](https://www.putty.org/)
- key pair generator : PuTTYgen
	- 1 Open PuTTYgen
	- 2 Click `Generate`(The type of key pair is RSA)
	- 3 Click `Save public key`and name it *droplet_public* to save.
	- 4 Click `Save private key`and name it *droplet_private* to save.
	- 5 Paste the conten of *droplet_public* to the Server instance console `Add Your SSH Keys`.

__2 Connect to server via SSH by PuTTY as root user__

- 1 Open PuTTY
- 2 `Session` Setting Option 
	- **Host name(or IP address):**  128.199.170.23
	- **Port:** 22
	- **Connection type:** SSH
	- **Auto-login username:** root
- 3 Choose *droplet_private* as `Auth` private key 
- 4 Click `open`

__3 Update and upgrade packages__

- 1 Update the package indexes:
`sudo apt-get update`
- 2 Upgrade the installed packages:
`sudo apt-get upgrade` 

__4 Keep terminal alive with server__

- 1 Open the ssh_config file:`sudo vi /etc/ssh/ssh_config`
- 2 Modify the ssh_config file as below and save:
```
Host *
ServerAliveInterval 100
```
- 3 Open the sshd_config file:`/etc/ssh/sshd_config`
- 4 Modify the sshd_config file as below and save:
```
ClientAliveInterval 60
TCPKeepAlive yes
ClientAliveCountMax 10000
```
- 5 Restart the SSH server:
```
sudo service ssh restart
``` 

__5 Add user grader with sudo privilege__

- 1 Add user *grader *:
`sudo adduser grader`
**Note**: Above, user `grader` password is, `grader`. 
- 2 Add the user to the sudo admin group:
`sudo usermod -aG sudo grader`

__6 Add SSH Access to the user grader__

```
su - grader
mkdir .ssh
chmod 700 .ssh
exit
sudo cp .ssh/authorized_keys /home/grader/.ssh/
sudo chown grader:grader /home/grader/.ssh/authorized_keys
sudo chmod 644 /home/grader/.ssh/authorized_keys
```

__7 Chang the SSH Port from 22 to 2200__

- 1 Open the sshd_config file:`sudo vi /etc/ssh/sshd_config`
- 2 Modify the `#Port:22`to `Port:2200` and save.
- 3 Restart the SSH server: `sudo service ssh restart`

__8 Set Up the Firewall__

- 1 Allow incoming connection for SSH on port 2200:`sudo ufw allow 2200/tcp`
- 2 Allow incoming connections for HTTP on port 80:` sudo ufw allow 80/www`
- 3 Allow incoming connection for NTP on port 123:`sudo ufw allow 123/udp`
- 4 To enable the firewall: `sudo ufw enable`
- 5 To check the status of the firewall:`sudo ufw status`
- 6 Active above setting:`sudo service ssh restart`

__9 Disable root login and password authentication__

- 1 Open the sshd_config file:`sudo vi /etc/ssh/sshd_config
- 2 Modify the `PermitRootLogin yes` to `PermitRootLogin no`.
- 3 Modify the `PasswordAuthentication yes` to `PasswordAuthentication no`and save .
- 4 Restart the SSH server: `sudo service ssh restart`

__10 Change timezone to UTC__

- 1 Open the timezone selection dialog:`sudo dpkg-reconfigure tzdata`
- 2 Chose 'None of the above', then 'UTC'.

__11 Connect to server via SSH by PuTTY as root user__

- 1 logout of the SSH instance:`exit`
- 2 Open PuTTY
- 3 `Session` Setting Option 
	- **Host name(or IP address):**  128.199.170.23
	- **Port:** 2200
	- **Connection type:** SSH
	- **Auto-login username:** grader
- 4 Choose *droplet_private* as `Auth` private key 
- 5 Click `open`

__12 Install apache2 and python mod-wsgi module__

- 1 Install Apache web server:`sudo apt install apache2`
- 2 Install mod_wsgi:`sudo apt install libapache2-mod-wsgi-py3`
- 3 Enable mod_wsgi:`sudo mod wsgi`
- 4 Restart the SSH server: `sudo service ssh restart`

__13 Install pip3 and git__

- 1 Install pip installer:`sudo apt install python3-pip`
- 2 Install git:`sudo apt-get install git`

__14 Install and configure PostgreSQL__

- 1 Create list file：`sudo vi /etc/apt/sources.list.d/pgdg.list`
- 2 Write the content `deb http://apt.postgresql.org/pub/repos/apt/ bionic-pgdg main` to the file.
- 3 Import signing key and update the package lists:`wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -`
- 4 Install PostgreSQL:`sudo apt-get install postgresql-10`
- 5 Log in as user postgres:`sudo su - postgres`
- 6 Open the psql shell:`psql`
- 7 Create database catalog owned by user catalog with password:
```create user catalog with password 'password';
   create database catalog with owner catalog;
```
- 8 Exit the psql shell:`\q`
- 9 Exit the postgres user:`exit`

__15 Download the web application and Install the packages__

- 1 Change the current working directory:`cd /var/www/`
- 2 Create a directory:`sudo mkdir CatalogApp`
- 3 Change the owner of the directory:`sudo chown -R grader:grader CatalogApp` 
- 4 Change the current working directory:`cd CatalogApp`
- 5 git clone the application:`sudo git clone https://github.com/lubocsu/CatalogApp CatalogApp` 
- 6 Change the current working directory:`cd CatalogApp`
- 7 Install the dependency packages:
```sudo pip3 install -r requirements.txt
   sudo pip3 install --upgrade Flask SQLAlchemy httplib2 oauth2client requests psycopg2 psycopg2-binary
```

__16 Make web .git inaccessible__
- 1 Change the current working directory:`cd ..`
- 2 Create the configuration file:`sudo vi .htaccess`
- 3 Write and save the content below:`RedirectMatch 404 /\.git`

__17 Configure mod-wsgi module__

- 1 Chang the current working directory:`cd ..`
- 2 Create the configuration file:`sudo vi catalogapp.conf`
- 3 Write and save the content below:

``` 
	#!/usr/bin/python3
	import sys
	import logging
	logging.basicConfig(stream=sys.stderr)
	sys.path.insert(0, "/var/www/CatalogApp/")
	from CatalogApp import app as application

```

__18 Configure Apache for virtual host__

- 1 Chang the current working directory:`cd ~`
- 2 Create the configuration file:`sudo vi /etc/apache2/sites-available/CatalogApp.conf`
- 3 Write and save the content below:
	
```
	<VirtualHost *:80>
		ServerName 128.199.170.23
		ServerAlias lubocsu.me
		ServerAdmin lubocsu@gmail.com
		WSGIScriptAlias / /var/www/CatalogApp/catalogapp.wsgi
    		<Directory /var/www/CatalogApp/CatalogApp/>
    			Require all granted
   			</Directory>
		Alias /static /var/www/CatalogApp/CatalogApp/static
		<Directory /var/www/CatalogApp/CatalogApp/static/>
    		Require all granted
		</Directory>
		ErrorLog ${APACHE_LOG_DIR}/error.log
		LogLevel warn
		CustomLog ${APACHE_LOG_DIR}/access.log combined
   	</VirtualHost>
 
```
- 4 Enable the virtual host:`sudo a2ensite CatalogApp`
- 5 Restart the SSH server: `sudo service ssh restart`

__19 Modify the web application content__

- 1 Rename the `app.py` to `__init__.py`
- 2 Change the path of loading json as below in `__init__.py`:
    r`/var/www/Catalog/Catalog/**.json`
- 3 Chang the format of import module which locate in the same directory of __init__.py as below:
   `from .database_setup import User, Category, Item`
- 4 Add the line below to the first line of all the `**.py` files:
   `#!/usr/bin/env python3`
- 5 Change the format of load database in all the  `**.py` files as below: 
    `engine = create_engine('postgresql://catalog:password@localhost/catalog')`
- 6 Put the line `app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'` out of `if __name__ == "__main__":`scope.

__20 Debug the application__

- 1 Show the latest 20 of debugging records:`sudo trail -20 /var/log/apache2/error.log`
- 2 run `sudo service ssh restart` after modification.

## Necessary Steps ##  

### Google credentials file
* Go to `https://console.developers.google.com/` to add a Web APP named 'Favourite Film APP'and activate Google OAuth Authorization.
* Add `http://lubocsu.me` `http://128.199.170.23` as Authorized JavaScript origins and Website URL.
* Add `http://lubocsu.me/gconnect` `http://lubocsu.me`  `http://lubocsu.me/` as Authorized redirect URIs.
* After saving, download JSON and rename the file to ```client_secrets.json``` and replace the file with the same name in the project directory.

### Facebook credentials file
* Go to `https://developers.facebook.com/apps`to add a Web APP named 'Favourite Film APP'and activate Facebook OAuth Authorization.
* Add `http://lubocsu.me` `http://128.199.170.23` as Authorized JavaScript origins and  Website URL.
* Add `http://lubocsu.me`  `http://lubocsu.me/` `http://lubocsu.me/fbconnect` as Authorized redirect URIs.
* Add your Client_id and Client_secret in the ```fb_client_secrets.json``` file and replace the file with the same name in the project directory.
 
## References

[1] <https://www.digitalocean.com/community/tutorials/how-to-use-ssh-to-connect-to-a-remote-server-in-ubuntu>

[2] <https://blog.webhostpython.com/how-to-prevent-an-ssh-timeout-in-putty/>

[3] <https://askubuntu.com/questions/254750/how-to-make-putty-ssh-connection-never-to-timeout-when-user-is-idle>

[4] <https://www.digitalocean.com/community/tutorials/how-to-create-a-sudo-user-on-ubuntu-quickstart>

[5]<https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04>

[6]<https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu-16-04>

[7]<https://www.digitalocean.com/docs/droplets/how-to/connect-with-ssh/putty/>

[8]<https://stackoverflow.com/questions/44914961/install-mod-wsgi-on-ubuntu-with-python-3-6-apache-2-4-and-django-1-11>

[9]<https://askubuntu.com/questions/889535/how-to-install-pip-for-python-3-6-on-ubuntu-16-10>

[10]<https://www.rosehosting.com/blog/how-to-install-python-3-6-on-ubuntu-16-04/>

[11]<http://docs.jinkan.org/docs/flask/deploying/mod_wsgi.html>

[12]<https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-apache-and-mod_wsgi-on-ubuntu-16-04>

[13]<https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps>

[14]<https://www.jianshu.com/p/dd6d08bc0ddd>

[15]<https://www.digitalocean.com/community/tutorials/how-to-structure-large-flask-applications>