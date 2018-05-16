How To Contribute
=================

There are different possibilities to participate in the |odh| Project,
including -but not limited to- to report bugs in the API or errors in
the API output, to ask for more datasets to be added to our
repository, to make feature requests or suggestions for improvement.

Depending on your interest on the |odh| Project, we also welcome your
participation to the project as either a developer or user.

I am a user
-----------

As a user, simply go to the list of :doc:`catalogue`, choose a dataset
and start gathering data from it, by using the documentation provided
in this site. You can then report any malfunctions, suggest new
methods that could be implemented, and so on.

I am a developer
----------------

As a developer, you can actively participate in the development of
|odh| or build your own application on top of the API and the code and
datasets that we provide.

Before doing so, however, you first need to fulfil a few requirements
in order to set up your PC, VM, or docker instance and be able to use
the |odh| coda and API.

Requirements
~~~~~~~~~~~~

You need the following software:

* PostgreSQL 9.3 or higher with postgis 2.2 extension.
* An application server (tomcat8 suggested)
* JRE7 or higher (JRE8 suggested)
  
You can then set up PostgreSQL, clone the git repository, and finally
clone our :strong:`HelloWorld` sample repository.

The complete howto can be found :doc:`here <howto/developer>`. (TBD
after issue #30 has been completed)

