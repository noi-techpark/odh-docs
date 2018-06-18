
.. geobank #10

.. _development:

How to set up a BDP locally
===========================

This tutorial will guide you in the setup of the local infrastructure
to be able to deploy a new Data Collector Object starting from a
simple :strong:`HelloWorld` template we provide.

This tutorial is divided into six parts:

#. Software Installation
#. Application Server Setup
#. Database Setup
#. Repository setup   
#. Coding 

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
* JRE7 or higher (JRE8 suggested)
* git version control system
* Apache Maven\ :sup:`#`
* An application server (tomcat8 suggested)\ :sup:`#`
  
  :sup:`#`\ These components are optional. You can skip Apache
  Maven installation if you do not use it and use the online
  application server provided by |odh| instead of deploying it
  locally.

On a typical debian-base Linux distribution, this is achieved by
opening a shell/terminal, then issuing the following command, provided
you have the rights to install software:

.. code-block:: bash
	  
   odh@bdp:~$ sudo apt-get install git openjdk-8-jdk postgresql postgis maven tomcat8  

This command ensures that all dependencies are installed as well. If
you have none of these package already installed, you might need to
download ~125Mb of packages.



Application Server Setup
------------------------

Once you installed tomcat, it should start immediately and listen on
port :envvar:`8080` and also restart every time you reboot your
workstation/server on which tomcat is installed. It requires no
changes to the configuration files, as the vanilla installation
suffices for our needs.

You can find the log files of tomcat in the directory :file:`/var/log/tomcat8/catalina.out.`



Application server testing & troubleshooting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can check that tomcat is running by issuing the command

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

While from a browser you should connect to port 8080 and see the
following page:

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


Database Setup
--------------

You should set up the database  as the :envvar:`postgres` user,
therefore you need to become root and then postgres:

.. code-block:: bash


   odh@bdp:~$ sudo -i
   [sudo] password for odh: 
   root@bdp:~# su - postgres
   postgres@bdp:~$ 

Create a database called :strong:`acme` with two users:
:strong:`acmeowner` and :strong:`acmeuser`.

   createdb acme
   createuser acmeowner
   createuser acmeuser

Assign to `acmeowner` full privile
   psql acme
   > alter database acme owner to acmeowner
   > GRANT SELECT ON ALL TABLES IN SCHEMA intime TO acmeuser;
   > GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA intime TO acmeuser;
   > create extension postgis
   psql -U acme acmeowner < schema.dump

Lines 1-4 create the database :strong:`acme` and two users, 
:strong:`acmeowner` who will be the db owner (line 5) and
:strong:`acmeuser` who can access but not modify the DB (lines
6-7).

Line 8 adds the postgis extension to the :strong:`acme` database and
finally line 9 imports the schema in the database.

Repository Setup
----------------

Once the software is installed, you can proceed in setting up the
repositories and configuring them to be used in the application
server.

There are two repositories to clone directly from github,
:strong:`bdp-helloworld` and :strong:`bdp-core`. The former contains
only a sample `Hello World` java class that can be used as a stub to
build more complex projects, while the second one is the core
infrastructure of the |odh|.

.. code-block:: bash
   
   odh@bdp:~$ mkdir ODH
   odh@bdp:~$ cd ODH
   odh@bdp:~$ git clone https://github.com/idm-suedtirol/bdp-core.git
   odh@bdp:~$ git clone https://github.com/idm-suedtirol/bdp-helloworld.git
   odh@bdp:~$ ls -l
   total 8
   drwxrwxr-x 9 odh odh 4096 Jun 13 17:39 bdp-core
   drwxrwxr-x 4 odh odh 4096 Jun 13 17:39 bdp-helloworld
   
Code setup
~~~~~~~~~~

Now, compile the code to be able to use it in the application server.

.. code-block:: bash

   odh@bdp:~$ bdp-core
   odh@bdp:~$ cd dto
   odh@bdp:~$ mvn install
   odh@bdp:~$ cd ../dal
   odh@bdp:~$ vim src/main/resources/META-INF/persistence.xml
   odh@bdp:~$ mvn clean install
   odh@bdp:~$ cd ../writer
   odh@bdp:~$ mvn clean package
   odh@bdp:~$ cd ../reader
   odh@bdp:~$ mvn clean package
   odh@bdp:~$ cd ..
   odh@bdp:~$ mv writer/writer.war ${APPLICATION_SERVER_HOME}
   odh@bdp:~$ mv reader/reader.war ${APPLICATION_SERVER_HOME}
   
.. todo:: How should :strong:`persistence.xml` (line 7) be edited?
	  
The local setup of bdp-core is completed by adding the project to
maven, for an easier management of the project, and by building the
:strong:`writer.war` and :strong:`reader.war` files, that will be then
moved to the application server (lines 3-15).


To verify that the .war files have been deployed correctly, go to the
links http\://{host}:{port}/writer/json and
http\://{host}:{port}/reader/json: you must receive a :strong:`405 GET
method not allowed` error. 



Coding
------


.. todo:: Once you are done with the set up, you can have a look at
   our :strong:`HelloWorld` example and start the development from
   there.
