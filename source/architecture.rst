.. _architecture-odh:

Architecture
============

The architecture of the |odh| is depicted in :numref:`arch-odh`,
which shows its composing elements together with its main goal: To
gather data from :strong:`(Open) Data Sources` (`"datasets"`) and make
them available to :strong:`Data Consumers`, which are usually
third-party applications that use those data in any way that they deem
useful, including (but not limited to) visualisation of diagram,
evolution of historical data, statistical analysis.

.. _arch-odh:

.. figure::  /images/odh-architecture.svg

   The |odh| architecture with the components (top) and the data
   format used (bottom) during the data transformation.


At the core of the |odh| lays the |bdp|, a java application which
contains all the business logic and handles all the connections with
the underling database using the |dal|. The |bdp| is composed by
different modules: A :program:`Writer`, that receives data from the
Data Sources and stores them in the Database using the |dal|


Communication with the Data Sources is guaranteed by the :strong:`Data
Collectors`, which are Java application built on top of the
:program:`dc-interface` that use a |dto| for each different source to
correctly import the data. Dual to the :program:`dc-interface`, the
:program:`ws-interface` allows the export of DTOs to web services,
that expose them to :strong:`Data Consumers`.

The bottom part of :numref:`arch-odh` shows the :term:`data format`
used in the various steps of the data flow.

Records in the Data Sources can be stored in any format and are
converted into JSON as DTOs. They are then transmitted to the Writer,
who converts them and stores them in the Database using SQL. To expose
data, the Reader queries the DB using SQL, transforms them in JSON's
DTOs to the Web Services who serve the JSON to the Data Consumers.


The Elements of the |bdp| in Details
------------------------------------

As :numref:`arch-odh` shows, the |bdp| is composed by a number of
elements, described in the remainder of this section in the same order
as they appear in the picture.

Data Source
   A Data Source is the origin of one ore more datasets; data are
   picked up usually by sensors and stored in some format, like for
   example CSV.

Dataset
   A dataset is a collection of records. Within the |ODH|\, a same
   Data Source may provide more dataset, that include slight different
   data. The underlying data format of a dataset :strong:`never`
   changes.

Data Collectors
   Data collectors are a library of Java classes used to transform
   data coming from Data Sources into a format that can be understood,
   used, and stored by the |bdp|\. As a rule of thumb, each Data
   Collector is used for one Data Source or dataset and use |dto|\s to
   transfer them to the |bdp|\. They are usually created by extending
   the :program:`dc-interface` in the bpd-core repository.

DTO
   The Data Transfer Object are used to translate the data format from
   the various formats used by the Data Sources, to be read from the
   writer and to be exposed by the reader (see below). DTOs are
   written in :strong:`JSON`. and are composed of three `Entities`:
   Station, Data Type, and Record.
   
Writer
   With the Writer, we enter in the core of the |bdp|\. Its purpose is
   to receive DTOs from the Data Collectors and store them into the DB
   and therefore implements all methods to read the DTO's :term:`JSON`
   format and to write to the database using SQL.

DAL
   The Data Abstraction Layer is used by both the Writer and the
   Reader to access the Database and exchange DTOs and relies on Java
   Hibernate.
   
Database (DB)
   The database represents the persistence layer and contains all the
   data sent by the Writer. Its configuration requires that two users
   be defined, one with full permissions granted -used by the writer,
   and one with read-only permissions, used bye the Reader. 

Reader
   The reader is the last component of the Core. It uses the DAL to
   retrieve DTOs from the DB and to transmit them to the web services.

Web Services
   The Web Services, which extend the :program:`ws-interface` in the
   bdp-core repository, receive data from the Reader and make them
   available to Data Consumers by exposing APIs and REST
   endpoints. They transform the DTO they get into JSON. 
   
Data Consumers
   Data consumers are (web-)applications that use the JSON produced by
   web services and manipulates them to produce a useful output for
   the final user.

Also part of the architecture, but not pictured in the diagram, is the
:file:`persistence.xml` file, which contains the credentials and
postgres configuration used by both the Reader and Writer.
