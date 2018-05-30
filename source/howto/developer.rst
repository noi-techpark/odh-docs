.. _tutorial-devel:

.. geobank #10


How to set up a DTO locally
===========================

This tutorial will guide you in the set up of the local infrastructure
to be able to deploy a new Data Collector Object starting from a
simple :strong:`HelloWorld` template we provide.

This tutorial is divided into  parts:

#. Software Installation
#. Repository and Application Server Setup
#. Database Setup
#. Coding

Software Installation
---------------------

You need the install the following software:

* PostgreSQL 9.3 or higher with postgis 2.2 extension.
* An application server (tomcat8 suggested)
* JRE7 or higher (JRE8 suggested)
* git version control system
* Apache Maven

On a typical debian-base Linux distribution, this is achieved by
opening a shell/terminal, then issuing the following command, provided
you have the rights to install software:

.. code-block:: bash
	  
   sudo apt-get install git maven openjdk-8-jre postgresql postgis tomcat8

This commands ensures that all dependencies are installed as well. On
non-debian systems the command is similar; but alternatively, you can
use your preferred package manager.

Repository and Application Server Setup
---------------------------------------

Once the software is installed, you can proceed set up the
repositories and database.

There are two repositories to clone directly from github,
:strong:`bdp-helloworld` and :strong:`bdp-core`. The former contains
only a sample `hello world` java class that can be used as a stub to
build more complex projects, while the second one is the core
infrastructure of the |odh| (lines 1 and 2 below).

.. code-block:: bash
   :linenos:

   git clone https://github.com/idm-suedtirol/bdp-helloworld.git
   git clone https://github.com/idm-suedtirol/bdp-core.git
   cd bdp-core
   cd dto
   mvn install
   cd dal
   vim src/main/resources/META-INF/persistence.xml
   mvn clean install
   cd ../writer
   mvn clean package
   cd ../reader
   mvn clean package
   cd ..
   mv writer/writer.war /path/to/application/server/
   mv reader/reader.war /path/to/application/server/

The local setup of bdp-core is completed by adding the project to
maven, for an easier management of the project, and by building the
:strong:`writer.war` and :strong:`reader.war` files, that will be then
moved to the application server (lines 3-15).

.. todo:: How should :strong:`persistence.xml` (line 7) be edited?

Database Setup
--------------

The setup of the database is quite simple and achieved in a bunch of commands:

.. code-block:: bash
   :linenos:

   createdb acme
   createuser acmeowner
   createuser acmeuser
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

Application server deployment
-----------------------------

To verify that the .war files have been deployed correctly, go to the
links http\://{host}:{port}/writer/json and
http\://{host}:{port}/reader/json: you must receive a :strong:`405 GET
method not allowed` error. 


Coding
------


.. todo:: Once you are done with the set up, you can have a look at
   our :strong:`HelloWorld` example and start the development from
   there.
