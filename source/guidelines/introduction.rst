Guidelines for Developers
=========================

|odh| is a collection of software, databases, and services coordinated and
hosted by IDM Südtirol / Alto Adige. Currently, |odh| systems are related to
mobility and tourism. In the future |odh| might diversify into more fields.

Companies and developers contributing to |odh| must follow the
guidelines listed in the documents as close as possible.

The aim of the |odh| Developer's Guidelines (:strong:`"The
Guidelines"`) is to simplify the hosting and maintenance of the
software, databases, and services by the |odh| developers and
maintainers at IDM ("the |odh| team").

The Guidelines describe the conventions to which a developer must
adhere, to be able to become an active |odh| developer or to see his
work being incorporated into the |odh|\. They are split in two parts:

* :strong:`Platform Guidelines` explain the preferred programming
  languages, how to expose the data after you manipulated them, the
  use of third-party libraries or plugins, and so on.
* :strong:`Database Guidelines` clarify how to design a database that
  shall become part of the |odh| platform.

Both of them are summarised in the remainder of this section, and can
be found in full version in the pages :ref:`platform-guidelines` and
:ref:`db-guidelines` respectively

Platform Guidelines - Bignami Version
-------------------------------------

The `Platform Guidelines` contain the software and programming
language requirements, coding conventions, and directions for
development. This section contains :strong:`only` the most important
points.

Please check the full version of this document at
:ref:`platform-guidelines` if you want to know more details, if you
have some doubt or if what you were looking for is not mentioned in
this summary.

* Programming Language is :strong:`Java`, in its latest or second to
  last version.
* The source code :strong:`must be documented` according to the
  `Javadoc style guide and tags`_.
* Java components of |odh| can be developed as :strong:`libraries`,
  :strong:`standalone applications`, or :strong:`server applications`
  running in Apache Tomcat.
* The source code is :strong:`built nightly`; :strong:`build
  configuration` should be provided in either Ant or Maven
  (preferred), Makefile, or shell script.
* :strong:`Third party libraries` can be used, provided they are
  established, FOSS-licenced, and do not overlap functionalities. This
  applies also to third party libraries used in application developed
  in other languages.
* Front-end applications can be deployed in :strong:`Javascript`,
  version EC 2015, and must support modern browsers.
* :strong:`Node.js` can be used to deploy headless or server
  applications.
* Web front ends use the :strong:`latest HTML and CSS` versions, must
  work on mobile devices (responsive design) and should implement some
  basic accessibility principle.
* :strong:`JSON` must be used as exchange language, while
  :strong:`XML` is welcomed as well.
* The latest or second to last version `Apache Tomcat`_ is used to run
  server application; only :strong:`API/REST end points` have direct
  access to the database server.
* There's :strong:`no file system persistence`, everything must be
  stored in the DB. JDBC data source and passwords should be stored in
  environmental variables.
* Pay attention to :strong:`RAM usage`, applications will undergo
  :strong:`load testing`.
* :strong:`PostgreSQL` |rdbms| is used, but not in its recent release
  (expect to use 2-3 versions before the latest), `PostGIS
  <https://postgis.net/>`_ spatial extension is required as well.
* Developers will have an unprivileged role to access the DB and must
  follow best practices to query the DB from Java/Javascript.


Database Guidelines - Bignami Version
-------------------------------------


Coming soon...
