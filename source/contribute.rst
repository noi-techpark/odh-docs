How To Contribute
=================

There are different possibilities to participate in the |odh| Project,
including -but not limited to- to report bugs in the API or errors in
the API output, to ask for more datasets to be added to our
repository, to make feature requests or suggestions for improvement.

Depending on your interest on the |odh| Project, we welcome your
participation to the project in one of the roles that we have
envisioned:

I am a user
-----------

As a :strong:`user`, you are most probably not interested in the internals of
the project or in the methods exposed by the API, but in using apps
that are built on top of the APIs and providing feedback to their
developers. We keep a list of those application here. (TBD)

You can also browse the list of :doc:`catalogue`, choose a dataset and
start gathering data from it, by using the documentation provided in
this site. You can then provide any kond of feedback, like reports
about any malfunctions, suggestions for improvements or new features,
and so on.

I am an App Developer
---------------------

As an :strong:`App developer`, your interest in the project is to
build your own application on top of the existing API and code and
process the data gathered from the datasets we provide. To do so, you
need to access the API documentation and the dataset, to be able to
see how you can develop your own app on top of what we provide.


I am a |odh| Core Hacker
------------------------

As a :strong:`Core Hacker`, you can actively participate in the
development of |bdp| Core to write your own data collectors to
interact with datasets that are not yet part of |odh|.

Before doing so, however, you first need to fulfil a few requirements
in order to set up your PC, VM, or docker instance and be able to use
the |bdpc| code and API to deploy your own extensions.

Requirements
------------

If you are a :strong:`user` or an :strong:`App developer`, you do not
need to install anything, just go to the list of apps or API
documentation/datasets (TDB) and start from there.

If you are a :strong:`Core Hacker`, you will need to install (on your
workstation, Virtual machine, or Docker instance) the following
software:

* PostgreSQL 9.3 or higher with postgis 2.2 extension.
* An application server (tomcat8 suggested)
* JRE7 or higher (JRE8 suggested)
  
You can then set up PostgreSQL, clone the git repository of the |bdp|
Core, and finally clone our :strong:`HelloWorld` sample repository to
have an idea of how to proceed.

The complete howto can be found :doc:`here <howto/developer>`. (TBD
after issue #30 has been completed)

