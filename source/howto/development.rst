
.. geobank #10

.. _development:

How to setup your local Development Environment
===============================================

This tutorial will guide you in the setup of the local infrastructure
to be able to deploy, on top of the Big Data Platform, a new Data
Collector Object starting from a simple :strong:`HelloWorld` template
we provide.

This tutorial is divided into three parts:

#. Software installation
#. Services configuration
#. Coding 

.. warning:: This tutorial is still work in progress and is largely incomplete!

	     
Software Installation
---------------------

In this tutorial we are using a virtual machine with installed
:strong:`Ubuntu 16.04 LTS`. This VM has IP Address
:envvar:`192.168.1.82`.

.. note:: All the commands and configuration items (including their
   location in the filesystem) refer to this distribution and should be
   identical or quite similar on all other debian-based distributions
   as well.

   On other Linux distribution some the name of the single packages
   and directory structure might vary.

You need to install the following software:

* PostgreSQL 9.3 or higher with postgis 2.2 extension.
* JRE7 or higher (JRE8 suggested).
* git version control system.
* xmlstarlet to edit the XML configuration file - you will need to do
  it manually otherwise.
* Apache Maven\ :sup:`#`.
* An application server (tomcat8 suggested)\ :sup:`#`.
  
  :sup:`#`\ These components are optional. You can skip Apache
  Maven installation if you do not use it and use the online
  application server provided by |odh| instead of deploying it
  locally.

On a typical debian-base Linux distribution, this is achieved by
opening a shell/terminal, then issuing the following command, provided
you have the rights to install software:

.. code-block:: bash
	  
   odh@bdp:~$ sudo apt-get install git openjdk-8-jdk postgresql postgis maven tomcat8 xmlstarlet 

This command ensures that all dependencies are installed as well. If
you have none of these package already installed, you might need to
download ~125Mb of packages.

Services configuration
----------------------

.. _setup-troubleshooting:

Troubleshooting
---------------

You can check that tomcat is running either from the CLI or using a
web browser. From the CLI you should issue the command ans see an
output similar to the one show, where at the :green:`active
(running)` string can be read.

.. code-block:: bash

   odh@bdp:~$ service tomcat8 status
   ● tomcat8.service - LSB: Start Tomcat.
      Loaded: loaded (/etc/init.d/tomcat8; bad; vendor preset: enabled)
      Active: active (running) since Wed 2018-06-13 16:36:28 CEST; 14min ago
        Docs: man:systemd-sysv-generator(8)
      CGroup: /system.slice/tomcat8.service
              └─13828 /usr/lib/jvm/java-8-openjdk-amd64/bin/java -Djava.util.logging.config.file=/var/lib/tomcat8/conf/lo

   Jun 13 16:36:23 bdp systemd[1]: Starting LSB: Start Tomcat....
   Jun 13 16:36:23 bdp tomcat8[13802]:  * Starting Tomcat servlet engine tomcat8
   Jun 13 16:36:28 bdp tomcat8[13802]:    ...done.
   Jun 13 16:36:28 bdp systemd[1]: Started LSB: Start Tomcat..

If you do not use systemd, the command will have a differnt output:

.. code-block:: bash

   odh@bdp:~$ service tomcat8 status
   [ ok ] Tomcat servlet engine is running with pid 11357.

From a browser you should connect to http://localhost:8080/ (replace
:envvar:`localhost` this the URL or IP where your application server
is located) and see the following page:

.. figure:: /images/tomcatOK.png
   :width: 80%

   The tomcat8 default landing page.

If tomcat is not running, start it using the following command, then
entering your password.

.. code-block:: bash
   
   odh@bdp:~$ sudo service tomcat8 start
   [sudo] password for odh: 

You can check again if tomcat is running with the command
:command:`service tomcat8 status`.
   
