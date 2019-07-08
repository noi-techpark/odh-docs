
.. geobank #10

.. _development:

How to set up your local Development Environment?
=================================================

This tutorial will guide you in the setup of the local infrastructure
to be able to deploy, on top of the |ODH|, a new Data Collector Object
starting from a simple :strong:`HelloWorld` template we provide.

This tutorial is divided into three parts:

#. Software installation
#. Services configuration
#. Troubleshooting

.. warning:: This tutorial is still work in progress and is largely incomplete!

	     
Software Installation
---------------------

The following installation directions have been verified on a VM with
installed either :strong:`Debian 9` or :strong:`Ubuntu 18.04.01 LTS`.
The applications installed on it are the :strong:`Suggested` version.

.. note:: All the commands and configuration items (including their
   location in the filesystem) refer to this distribution and should be
   identical or quite similar on all other debian-based distributions
   as well.

   On other Linux distribution some the name of the single packages
   might vary.

You need to install the following software:

============ ========= =========== =======================================
 Software     Minimum   Suggested   Notes
============ ========= =========== =======================================
PostgreSQL     9.6       10.5
postgis ext.   2.2        2.4
Java           JRE7      JRE8       Most of the packages require
                                    Java 8 to be built.
git            2.17      2.17
xmlstarlet     1.6.1     1.6.1    
Apache Maven   3.3.9     3.5.2      Optional. If you don't use it, do
                                    not install it.

tomcat8        8.0       8.5        You Optional can either use the
                                    tomcat server provided by |odh| or
				    install another application server.
============ ========= =========== =======================================

.. note:: In case you opt to not use Maven or Tomcat, remember to
   edit the script in order to not attempt to configure them!

On a typical debian-based Linux distribution, installing the software
is achieved by opening a shell/terminal, then issuing the following
command, provided you have the rights to install software:

.. code-block:: bash
	  
   odh@odh:~$ sudo apt-get install git openjdk-8-jdk postgresql postgis maven tomcat8 xmlstarlet 

This command ensures that all dependencies are installed as well. If
you have none of these package already installed, you might need to
download up to ~125Mb of packages.

Services configuration
----------------------

The services will be configured automatically, since we developed a
script that does most of the job for you. However, a few preliminary
steps are required:

#. Make sure tomcat8 and postgres are running. If the do not or if you
   are unsure, refer to :ref:`entry 1 <ts-1>` in section
   :ref:`setup-troubleshooting`.
#. Verify that tomcat and postgres are listening on the right port
   (:strong:`8080` and :strong:`5432` respectively). See :ref:`entry 2
   <ts-2>` in section :ref:`setup-troubleshooting` for more information.
#. Make sure there is a database role configured with a password and a
   few access permission.
#. Set two environment variables.
#. Edit the script to suit your workstation.
#. Launch the script.

.. warning:: The script :strong:`might silently fail` on some
   machine, for example on Ubuntu 18.04, because it ships with
   Java 11. In this case, please install also java 8 and make it the
   default java version.
   
  
.. _setup-troubleshooting:

Troubleshooting
---------------

.. _ts-1:

1. :strong:`How do I check if a service is running?`
   
You can check that a service like tomcat or postgres is running from
the CLI, by issuing the following command and see an output similar to
the one show here, where the :green:`active (running)` string can be
read.

.. code-block:: bash

   odh@odh:~$ service tomcat8 status
     tomcat8.service - LSB: Start Tomcat.
      Loaded: loaded (/etc/init.d/tomcat8; bad; vendor preset: enabled)
      Active: active (running) since Wed 2018-06-13 16:36:28 CEST; 14min ago
        Docs: man:systemd-sysv-generator(8)
      CGroup: /system.slice/tomcat8.service
              └─13828 /usr/lib/jvm/java-8-openjdk-amd64/bin/java -Djava.util.logging.config.file=/var/lib/tomcat8/conf/lo

   Jun 13 16:36:23 odh systemd[1]: Starting LSB: Start Tomcat....
   Jun 13 16:36:23 odh tomcat8[13802]:  * Starting Tomcat servlet engine tomcat8
   Jun 13 16:36:28 odh tomcat8[13802]:    ...done.
   Jun 13 16:36:28 odh systemd[1]: Started LSB: Start Tomcat..

If you do not use systemd, the command will have a differnt output:

.. code-block:: bash

   odh@odh:~$ service tomcat8 status
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
   
   odh@odh:~$ sudo service tomcat8 start
   [sudo] password for odh: 

You can check again if tomcat is running with the command
:command:`service tomcat8 status`.

.. _ts-2:

2. :strong:`How do I check the port on which a service is listening?`

You can use the :command:`netstat` command line utility, like this:
   
.. code-block:: bash
   
  root@odh:~$ netstat -plnt4
  Active Internet connections (only servers)
  Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
  tcp        0      0 0.0.0.0:5432              0.0.0.0:*               LISTEN      2427/postgresql        
  tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      2719/sshd           
  tcp        0      0 127.0.0.1:8080            0.0.0.0:*               LISTEN      2863/tomcat8
  
Make sure that at least ports 8080 and 5432 are present (tomcat and
postgres respectively) in the :strong:`Local Address`.

It is suggested to run this command as superuser, because otherwise
not all information is present.
