.. _how-to-contribute:

How To Contribute
=================

There are different possibilities to participate in the |odh| Project,
including -but not limited to- to report bugs in the API or errors in
the API output, to ask for more datasets to be added to our
repository, to make feature requests or suggestions for improvement.

Depending on your interest on the |odh| Project, we welcome your
participation to the project in one of the roles that we have
envisioned: :ref:`User <user>`, :ref:`App developer <app-developer>`,
:ref:`Core Hacker <core-hacker>`.

You can also help the |odh| project grow and improve by
:ref:`reporting bugs or asking new features <bug-reports>`.

.. _user:
	
As a user I can...
------------------

...install and use an app built on top of the API.
   Browse the list of :ref:`available applications developed by
   third-parties <applist>`, choose one that you are interested in,
   install it and try it out, then send feedback to their developers
   if you feel something is wrong or missing.

...explore the data in the datasets.
   Choose a dataset from the list of :ref:`available_datasets` and
   start gathering data from it, by using the documentation provided
   in this site. You can then provide any kind of feedback on the
   dataset: reports about any malfunctions, suggestions for
   improvements or new features, and so on.

   Moreover, if you are interested in datasets that are not yet in our
   collection, get in touch with the |odh| team to discuss your
   request.

.. _app-developer:

As an App Developer I can...
----------------------------

...harvest data exposed by the dataset.
   Browse the list of :ref:`available_datasets` to see what types of
   data are contained in the datasets, and think how they can be used.

   For this purpose, we maintain an updated list of the
   :ref:`available datasets <available_datasets>` with links to the
   API to access them.


...build an application with the data.
   Write code for an app that combines the data you can harvest from
   the available datasets in various, novel way.

   To reach this goal, you need to access the APIs, their
   documentation, and the datasets. It is then your task to discover
   how you can reuse the data in your code.

...publish my app in |odh|.
   As soon as you have developed a stable version of your app, get in
   touch with us: We plan to maintain an updated list of apps based on
   our dataset included with this documentation.


No software installation is needed: Go to the list of apps (not yet
available, be the first!) or API documentation/datasets and start from
there, and develop in a language of your choice an application that
uses our data.

.. _core-hacker:

As a |odh| Core Hacker I can...
-------------------------------

...help shape the future of |odh|\.
   Participate in the development of |odh|\ : Build new data
   collectors, extend the functionality of the broker, integrate new
   datasets on the existing infrastructure, develop new stable API
   versions.   

   
To be able to become a core hacker, however, requires a few additional
tasks to be carried out:


#. Learn how to successfully integrate your code with the existing
   code-base and how to interact with the |odh| team.  In other words,
   you need to read and accept the :ref:`devel-guidelines` (click on
   the link for a summary), which are available in two extended,
   separate parts: :ref:`platform-guidelines` and
   :ref:`db-guidelines`.

#. Understand the :ref:`architecture <architecture-odh>` of both the
   |odh| and |bdp|\.
#. Learn about the :ref:`dtp-env`.
#. Install the necessary software on your local workstation (be it a
   physical workstation, a virtual machine, or a Docker instance),
   including PostgreSQL with postgis extension, JDK, git.
#. Set up all the services needed (database, application server, and
   so on).
#. Clone our git repositories.  To successfully complete these tasks,
   please read the :ref:`development` tutorial, which guides you
   stepwise through all the required set up and configuration, along
   with some troubleshooting advice.


#. Coding. That's the funniest part, enjoy!

To support the installation tasks and ease the set up of your
workstation, we are developing a script the you will do the job for
you. Stay tuned for updates.

.. _bug-reports:

Bug reporting and feature requests
----------------------------------

This section explains what to do in case you:

1. have found an error or a bug in the APIs;
2. like to suggest or require some enhancement for the APIs;
3. have some requests about the datasets
4. find typos or any error in this documentation repository;
5. have an idea for some specific tutorial.


If your feedback is related to the Open Data Hub Core, including
technical bugs or suggestions as well as requests about datasets
(i.e. points 1. to 3. above), please insert your issues on the
following website:

https://github.com/idm-suedtirol/bdp-core/issues

If your feedback is related to the Open Data Hub Documentation, please
insert your issue on the following website, using the template that
suits your needs:

4. https://github.com/idm-suedtirol/odh-docs/issues/new?template=bug_report.md
5. https://github.com/idm-suedtirol/odh-docs/issues/new?template=feedback.md

.. note:: You need to have a valid github account to report issues and
   interact with the |odh| team.
   
We keep track of your reports in our bug trackers, where you can also
follow progress and comments of the |odh| team members.


