
.. _platform-guidelines:

Platform Documentation
----------------------

.. versionchanged:: 22.05 Integrate summaries

.. topic:: Changelog
   
   * :strong:`2020-01-20 version 1.1` -- fixed outgoing links
   * 2018-05-28 version 1.0
   * 2018-03-30 version 1.0-beta

+++++
   
This document represents :strong:`Part 1` of the guidelines and
presents the preferred programming languages, databases, and protocols
to be used, data exchange and exposition methods, coding conventions,
and regulates the use of third-party libraries.

There are scenarios where an exemption from the guidelines is acceptable.
The following is a :strong:`non-exhaustive` list of such scenarios.

#. :strong:`Use of foreign technologies`. The development of a |odh|
   component requires the use of platforms, languages or generally
   technologies that are different from the ones listed in the
   guidelines. An example might be a component that depends on an
   already developed custom library written in a programming language
   not listed in the guidelines.
    
#. :strong:`Use of technologies that are not mentioned in the
   guidelines`. Future |odh| component might require technology that
   is not listed at all in the guidelines. An example is a component
   that must be hosted on specific hardware needed for machine
   learning platforms.

A |odh| contributor who runs into such a scenario must contact the
|odh| team to discuss that specific scenario. If the exemption is
reasonable and can be motivated the |odh| team will agree and allow
it. To avoid misunderstandings, contributors must expect to get a
:strong:`written statement` about such a decision.

.. dropdown:: Platform Guidelines Summary

   The `Platform Guidelines` contain the software and programming
   language requirements, coding conventions, and directions for
   development. This section contains :strong:`only` the most
   important points.

   Please check the full version of this document at
   :ref:`platform-guidelines` if you want to know more details, if you
   have some doubt or if what you were looking for is not mentioned in
   this summary.

   * Programming Language is :strong:`Java`, in its latest or second to
     last version.
   * The source code :strong:`must be documented` according to the
     `Javadoc style guide and tags
     <https://www.oracle.com/technical-resources/articles/java/javadoc-tool.html>`_.
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
   * The latest or second to last version `Apache Tomcat
     <https://tomcat.apache.org/>`_ is used to run server application;
     only :strong:`API/REST end points` have direct access to the
     database server.
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

Programing Languages, Environments, and Related Technologies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _java:

Java
++++

The chosen programing language for |odh| is Java, more precisely the Java
Platform, Standard Edition (Java SE).

Source code will be compiled with either the `OpenJDK
<https://openjdk.java.net/>`_ or the `OracleJDK
<https://www.oracle.com/java/technologies/javase-downloads.html>`_,
which share the same code base anyway. Resulting binaries will run in
the corresponding JVM.

Java Version
____________

Java is generally backwards-compatible, so code written for a previous
version of the JDK will likely compile on the next compiler version
and run on the next JVM version. However, contributors ought to use a
reasonably modern version of Java in order to avoid deprecation
warnings and make use of modern language features.

Contributors can expect the |odh| team to use the :strong:`current
stable version` of the language. Of course, a certain delay is to be
expected between the time a Java release becomes generally available
and the time OS vendors and hosting providers make it available. This
delay, that can easily be in the order of one year, must be taken into
account.


Environments
____________

|odh| Java components can be developed as:

* Java :strong:`libraries`.
* Java :strong:`standalone applications`, running headless.
* Java :strong:`server applications` running in Apache Tomcat:
  
  * API/REST end points.
  * Web applications.

More information about standalone and server applications can be found
under section :ref:`Platforms`.

|odh| components :strong:`must not` be developed as fat clients (like
e.g., Swing, SWT).  :strong:`Web applications` are the preferred
technology.

While native Android applications can be developed in Java, they should also be
avoided as they are not a cross platform solution (Android vs. IOS). For the
mobile space, (mobile) web applications or cross platform environments based on
JavaScript are preferred (see section :ref:`js`).

Documentation
_____________

Source code must be commented following the established `Javadoc style
guide and tags
<https://www.oracle.com/technical-resources/articles/java/javadoc-tool.html>`_.

Complex section of the code (for example not-trivial algorithms) must have
dedicated comment sections.

Higher-level documentation must be available as well and if possible,
it :strong:`must be kept` in a simple, text-based format, such as
plain text, MarkDown or HTML. The rationale behind this choice is that
these formats - unlike binary file formats such as ODT or DOCX - can
be versioned in a source code management system.

Builds
______

The |odh| team runs automatized nightly builds (and tests) of |odh|
software components. It must therefore be possible to rebuild the
binaries (JARs or WARs) starting from the source code all the way down
to the complete binaries in a headless environment.

Developers :strong:`must provide` standard build configurations for
one of the usual Free / Open Source Software ("FOSS") build tools used
in the Java space (such as Maven or Ant). Alternatively a simple
Makefile or shell script (the nightly build system runs on Linux) will
suffice.

Considerations about testing are described in another document.

.. _third-party-libs:

Use of Third-Party Libraries
____________________________

Most Java projects use one or more third-party libraries. Regarding
the use of such libraries in |odh|\ , the following guidelines apply:

*  The library must be stable, well known and well supported.
*  The library must be distributed under a FOSS license.
*  Avoid creating pile-ups of libraries with overlapping functionality.

.. _js:

JavaScript
++++++++++

While the primary programing language for |odh| is Java, there are use
cases where JavaScript is accepted or even dictated by the environment
(like e.g, web front ends).

The |odh| team endorses the language revision :strong:`ECMAScript
2015` (a.k.a. ES 6) and encourages a modern, expressive use of the
language (e.g. block scoped variables, function expressions, promises
and many more).

The usage of JavaScript falls into the two categories: Web front ends
and Node.js, as detailed in the next sections.

JavaScript Web Front Ends
_________________________

Most modern web applications will use JavaScript in the web front end. The
|odh| team is agnostic about how the front end is implemented (classic
web application vs. single page web application).
 
In the likely case that JavaScript front end libraries and frameworks are used,
the following guidelines apply:
 
* The library or framework must be stable, widely used and well
  supported - avoid using cutting edge libraries with APIs that are
  not settled yet.
* The library or framework must be distributed under a FOSS license.
* The library or framework must be cleanly imported into the project
  with one of these methods:
   
  * By means of a JavaScript package manager with a configuration
    file (such as :command:`npm` and :command:`package.json`).
  * Manually, by using a clearly labelled `include path` (such as
    :file:`import /vendor/name/version/file.js`).
  
To avoid having to support many programing languages, source code
:strong:`must not` be developed in a transpiled language
(e.g. TypeScript or CoffeeScript),
 
In terms of browser compatibility, developers can use ES 2015, as
said.  According to the `ECMA Compatibility table
<https://kangax.github.io/compat-table/es6/>`_, ES2015 is well
supported in all modern browsers (Chrome, Firefox, Safari, Edge) both
in desktop and mobile version.

Generally speaking, support of legacy browsers (MS Internet Explorer) is not
an issue. Cross-browser testing is, of course, still necessary and expected.

If a build system such as `webpack <https://webpack.js.org/>`_ is
needed, its use must be clearly documented as the |odh| team must
integrate it into their nightly builds system.


JavaScript Running in Node.js
_____________________________

Besides the front end, JavaScript code can be also used for headless or server
applications, provided they have limited complexity.

In case the developer needs to create large pieces of business logic or complex
web applications, Java ought to be the preferred environment.

Most front end guidelines mentioned in the previous section apply here
as well, in particular those about :ref:`libraries
<third-party-libs>`. A complete :file:`package.json` file is a must
here. It is required that the Node.js project be installed simply by
running :command:`npm install`.

Use cases for Node.js in the |odh| are:

*  Simple REST end points.
*  Simple web applications.
*  Tools that operate on JSON data.
*  Scripting / glue code.


The |odh| team generally uses an `LTS release
<https://github.com/nodejs/Release>`_ of Node.js, adopted soon after
it becomes available, although some time might be needed for the
hosting provider to make it available.

SQL
+++

See section :ref:`pgsql-guidelines` below.

HTML and CSS
++++++++++++

Web front ends are, of course, developed using HTML and CSS in their current
versions.

It is important that all web pages render correctly in all modern browsers
(Chrome, Firefox, Safari, Edge). 

Generally speaking, support of legacy browsers (MS Internet Explorer)
is not an issue.  Cross-browser testing is, of course, still necessary
and expected.  A minimum requirement is that all HTML validates
against `the W3C validator <https://validator.w3.org/>`_.

As most web traffic is nowadays coming from mobile devices, all general purpose
web UIs exposed to end users should be implemented to work well on mobile
devices by using standard techniques, such as :strong:`responsive design`.

In the development of the web front-end, Accessibility principles
should be taken into account when designing web pages.

XML and JSON
++++++++++++

:strong:`XML` and :strong:`JSON` are both important data description
languages, heavily used in the context of Java, JavaScript, web
applications, and APIs; therefore they are both used and welcome in
the |odh|.

:strong:`JSON` is of particular interest as that is the preferred data
exchange format for REST endpoints. It also plays a role in the
persistence layer, as |odh| allows the use of JSON records in
PostgreSQL tables (see section :ref:`pgsql-guidelines` below).


.. _platforms:

Platforms and Architectural Considerations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _apache-tomcat:

Java server applications running in Apache Tomcat
+++++++++++++++++++++++++++++++++++++++++++++++++

`Apache Tomcat <https://tomcat.apache.org/>`_ is a well established,
light weight FOSS web server that implements among others the Java
Servlet specification.

The |odh| team generally uses the latest or second to last release of
Tomcat, to run Java server applications in the previously mentioned
contexts:

* API/REST end points.
* Web applications.

The desired design is that :strong:`only API/REST end points` directly
access the database server, while web applications just talk to the
API/REST end points.


Automatic Deployment
____________________

Each Tomcat instance normally runs a few web applications, hence
expect a |odh| web application's WAR file to be bundled together with
other WAR files to run on a given instance.

The automatic build systems takes care of this bundling and
deploying. It is therefore very important that all WARs can be build
automatically, as mentioned in the :ref:`section about Java <java>`.


No File System Persistence
__________________________

Currently, the |odh| team uses Amazon Web Services for Tomcat hosting,
in particular the managed service known as `Elastic Beanstalk`. While
there is no hard dependency on this provider -that could be changed at
any point in the future, the architectural design of Elastic Beanstalk
has partly modelled/shaped the engineering choices of the |odh| team
in the design of its web application.


First and foremost, servers are considered volatile. This means a
|odh| component running in Tomcat :strong:`can not expect` to see a
persistent file system!

All web applications must therefore be developed with the database as
:strong:`the only persistent storage layer`. This architectural choice
has a few advantages:

* Web applications can be distributed over more than one web server
  (horizontal scaling), increasing availability and performance.
* Backup and disaster recovery is very much simplified - a failing
  instance can just be replaced by a new instance and the application
  can be deployed again.

Developers must pay particular attention to this point: :strong:`There
is no persistent file system`. Hence no changeable configuration
files, no application specific log files. Everything is stored in the
database.

Data Source
___________

One subtle point is the question `"Where is the JDBC data source and password
stored?"`. It cannot be stored in a file and it must not be stored in the
source code or context files. The recommended way to store this information is
in Java environment properties.

The system will set these variables when launching Tomcat::
   
   JDBC_CONNECTION_DRIVER=org.postgresql.Driver
   JDBC_CONNECTION_STRING=jdbc:postgresql://host:5432/db?user=username&password=secret

The developer can then read them with:

.. code-block:: java

   System.getProperty("JDBC_CONNECTION_DRIVER");
   System.getProperty("JDBC_CONNECTION_STRING");

RAM Usage
_________
 
The |odh| encompasses a considerable number of web applications that
are bundled together to run on a few Tomcat server instances. Contrary
to popular belief, RAM is not an infinite resource. Contributors are
kindly reminded to pay attention to the RAM usage of their web
applications, since load testing is expected.


Java standalone applications, running headless
++++++++++++++++++++++++++++++++++++++++++++++

Besides wapplications running in Tomcat, the |odh| also has headless
standalone applications written in Java or JavaScript/Node.js.

These are meant for special use cases, such as compute intensive jobs or
batch processing, made upon request.

Almost everything said in the previous section about Tomcat, applies here as
well.

Again, the preferred way to run these applications is in an environment where
servers are volatile and the only persistence layer is the database.

.. _pgsql-guidelines:

PostgreSQL
__________

`PostgreSQL <https://www.postgresql.org/>`_ is one of the most
established |rdbms| on the market and is generally described as being
by far the most advanced FOSS RDBMS and therefore it has been chosen
as the primary database system for |odh|.

There is a :strong:`new major release` of PostgreSQL per year and each
release is supported for 5 years, according to `the versioning policy
<https://www.postgresql.org/support/versioning/>`_. Contrary to the
case of the other products mentioned in these guidelines, the |odh|
team generally will :strong:`not run the latest` or even previous
version of PostgreSQL.  Expect the version available for |odh| to lag
about 2-3 years behind the latest available release.

Extensions
``````````

Most, if not all of the `extensions distributed with PostgreSQL
<https://www.postgresql.org/docs/10/contrib.html>`_, can be expected
to be available, together with the third-party `spatial query
extension PostGIS <https://postgis.net/>`_ is also available.

Other extensions are very likely :strong:`not available`, so ask the
|odh| team if in doubt.

Accessing the Database
``````````````````````

Application developers will get one or more unprivileged database roles to
access the database. Access will be done via JDBC when using Java, or via any
of the available PostgreSQL modules for Node.js when using JavaScript.

The data source strings must be parsed from the environment variables
(see section :ref:`Apache-Tomcat`).

The maximum number of concurrent database sessions will be generally
limited per role, therefore each developer must clarify with the |odh|
team what an acceptable number is, depending on the application.

Since PostgreSQL will refuse a connection if that number is exceeded,
developers must take this number into account, whether they configure
a connection pool or not.

|odh| databases generally are configured to accept connections only from the known hosts where the application
servers are deployed.

Contributors must follow well known best practices when querying
the database from Java or JavaScript:

* When processing large datasets, consider setting smaller values of
  :envvar:`fetchsize` or equivalent parameter to avoid buffering huge result
  sets in memory and running out of RAM.
* When performing a huge number of DML statements consider switching
  off any client side autocommit feature and rather bundle statements
  into transactions.
* Do :strong:`not` open transactions without closing them, in other
  words, do :strong:`not` leave sessions in transaction!
    

Database Design and Usage
_________________________

This section has been moved into its own document, :ref:`db-guidelines`.
