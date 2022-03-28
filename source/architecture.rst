
.. _architecture-odh:

|ODH| Architecture
==================

The architecture of the |odh| is depicted in :numref:`arch-odh`, which
shows its composing elements together with its main goal: To gather
data from :strong:`Data Sources` and make them available to
:strong:`Data Consumers`, which are usually third-party applications
that use those data in any way that they deem useful, including (but
not limited to) study the evolution of historical data, or carry out
data analysis to produce :term:`Statistical Graphics`.

.. _arch-odh:

.. figure::  /images/odh-architecture.png
   :scale: 40%
   :align: center

   The |odh| architecture with the components (top) and the data
   formats used (bottom) during each data transformation.

At the core of the |odh| lays :strong:`bdp-core`, a java application
which contains all the business logic and handles all the connections
with the underling database using the |dal|. The |odhc| is composed by
different modules: A :program:`Writer`, that receives data from the
Data Sources and stores them in the Database using the |dal| and a
:program:`Reader` that extracts data form the databases and exposes
them to Data Consumers using APIs on REST endpoints.

Communication with the Data Sources is guaranteed by the :strong:`Data
Collectors`, which are Java applications built on top of the
:program:`dc-interface` that use a |dto| for each different source to
correctly import the data. Dual to the :program:`dc-interface`, the
:program:`ws-interface` allows the export of DTOs to web services,
that expose them to :strong:`Data Consumers`.

The bottom part of :numref:`arch-odh` shows the :term:`Data Format`
used in the various steps of the data flow. Since the data are exposed
in JSON, it is possible to develop applications in any language that
uses them.

Records in the Data Sources can be stored in any format and are
converted into JSON as DTOs. They are then transmitted to the Writer,
who converts them and stores them in the Database using SQL. To expose
data, the Reader queries the DB using SQL, transforms them in JSON's
DTOs to the Web Services who serve the JSON to the Data Consumers.


The Elements of the |odh| in Details
------------------------------------

As :numref:`arch-odh` shows, the |odh| is composed by a number of
elements, described in the remainder of this section in the same order
as they appear in the picture.

.. _data-provider-def:

Data Providers
   A :ref:`Data Provider <data-providers>` is a person, company or
   public body that supplies to the |odh| some data or dataset, which
   usually belongs to a single domain. Data are automatically picked
   up by sensors and stored under the responsibility of the Data
   Provider in some standard format, like for example CSV or
   :term:`JSON`.

   .. note:: Since a data provider may decide at some point to not
      publish its data on the |odh| anymore, or new data providers can
      join the |odh| in the future, they are not an official part of
      the |odh|. You can learn more on this, including the current
      list of data providers, in the :ref:`dedicated section
      <data-providers>` of the documentation.

.. _dataset-def:

Dataset
   A dataset is a collection of records that typically originate from
   one Data Provider, although, within the |odh|\, a dataset can be
   built from data gathered from multiple Data Providers. The
   underlying data format of a dataset :strong:`never` changes.
  
.. _data-collector-def:

Data Collector
   Data collectors form a library of Java classes used to transform
   data gathered from Data Providers into a format that can be
   understood, used, and stored by the |odhc|\. As a rule of thumb,
   one Data Collector is used for one Dataset and uses |dto|\s to
   transfer them to the |odhc|\. They are usually created by extending
   the :program:`dc-interface` in the bpd-core repository.

.. _dto-def:

DTO
   The Data Transfer Object are used to translate the data format used
   by the Data Providers, to a format that the Writer can understand
   and use to transfer the data in the Big Data infrastructure. The
   same DTO is later used by the Reader (see below) to present
   data. DTOs are written in :strong:`JSON`, and are composed of three
   `Entities`: :strong:`Station`, :strong:`Data Type`, and
   :strong:`Record`.

.. _writer-def:

Writer
   With the Writer, we enter in the |odhc|\. The Writer's purpose is
   to receive DTOs from the Data Collectors and store them into the DB
   and therefore implements all methods needed to read the DTO's
   :term:`JSON` format and to write to the database using SQL.

.. _bdp-def:

ODH Core
   The |odhc| lays at the very core of the |odh|\. Its main task is to
   keep the database updated, to be able to always serve up-to-date
   data. To do so, it relies on the Writer, to gather new or updated
   data from the data collectors and keeps a history of all data he
   ever received. It also relies on the Reader to expose data to the
   data consumers. Internal communication uses only SQL commands.

.. _dal-def:

DAL
   The Data Abstraction Layer is used by both the Writer and the
   Reader to access the Database and exchange DTOs and relies on Java
   Hibernate. It contains classes that map the content of a DTO to
   corresponding database tables.

.. _database-def:

   
Database (DB)
   The database represents the persistence layer and contains all the
   data sent by the Writer. Its configuration requires that two users
   be defined, one with full permissions granted -used by the writer,
   and one with read-only permissions, used by the Reader. 

.. _reader-def:

Reader
   The reader is the last component of the Core. It uses the DAL to
   retrieve DTOs from the DB and to transmit them to the web services.

.. _ws-def:
   
Web Services
   The Web Services, which extend the :program:`ws-interface` in the
   |odhc| repository, receive data from the Reader and make them
   available to Data Consumers by exposing APIs and REST
   endpoints. They transform the DTO they get into JSON.

.. _data-consumer-def:
   
Data Consumers
   Data consumers are applications that use the JSON produced by web
   services and manipulates them to produce a useful output for the
   final user. As mentioned in the section :ref:`project-overview`,
   `application` is intended in a broad sense: it can be a web site, a
   software application for any devices, a communication channel, or
   any means to use the data.

Also part of the architecture, but not pictured in the diagram, is the
:file:`persistence.xml` file, which contains the credentials and
postgres configuration used by both the Reader and Writer.

