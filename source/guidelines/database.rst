.. _db-guidelines:

|odh| Database Guidelines - Full Version
--------------------------------------------------------------

This document represents Part 2 of the |odh| Developer's Guidelines and
clarifies the database design criteria for developers who contribute
their own databases designs to the |odh| platform.

Basic information about the PostgreSQL versions, PostgreSQL extensions
and how to access PostgreSQL from Java or JavaScript, intended for
developers that contribute code that just uses an existing database,
are explained in the :ref:`platform-guidelines` document as
well. Please refer to that document for a general introduction to the
scope of the present guidelines.

Database design methodology
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The |odh| team is generally agnostic about database design and acknowledges
the existence of different design and development methodologies.

Specifically, the following methodologies are well known and acceptable:

#. :strong:`Relational Model`. The data schema is implemented using
   normalized relations with standard SQL concepts (schemas, tables,
   columns and keys). The :command:`CREATE` statements are written by
   the developer.

#. :strong:`Object-Relational Mapping (ORM)`. The underlying data
   schema is based on the relation modal, but the :command:`CREATE`
   statements are generate by an ORM framework that automatically maps
   entities to relations.

#. :strong:`Semi-structured Data`. Entities are stored in a
   semi-structured format. For the |odh| the preferred format is JSON.
   Specifically, the recommended design is to map each entity to its
   own table. The table should have at least two columns: one
   traditional ID column and one JSON data column. The (simple)
   :command:`CREATE` statements are written by the developer.  The
   JSON data column must use the PostgreSQL native data type
   :strong:`jsonb` (see `binary stored JSON`_ in PostgreSQL
   documentation).

PostgreSQL supports all three methodologies well. It is also possible to have a
hybrid design mixing 1. and 3.

A developer contributing a database design to |odh| must provide the
|ddl| , a.k.a. `schema files` containing the :command:`CREATE` statements.

Like all source code files, the `schema files` must be commented in-line and
accompanied by additional, higher level documentation.

Besides source code file comments, database objects must also be
commented with the SQL :command:`comment` command (see :ref:`Sample Code 1
<example-sql>` below).

Updates must be provided in the form of :command:`ALTER` statements,
so the modifications can be easily applied to existing databases (see
:ref:`Sample Code 2 <update-sql>` below).

All database designs should contain a version table, where the version is
stored (and updated with each update).

The |odh| team likes to stress this point: :strong:`do not just commit
database schema dumps`, but rather treat SQL-DDL files as source code
and cleanly distinguish the initial creation and later updates.

.. _example-sql:

.. topic:: Sample Code 1: A DDL source file called :file:`foo.sql`

   .. code-block:: sql
      
      -- foo.sql
      -- a document with appendices
      --
      -- changelog:
      -- version 1.0
      --
      -- copyright, author etc.
      
      create sequence foo_seq;
   
      create table doc (
          id      int default nextval('foo_seq'),
	  title   text not null,
	  body    text,
	  primary key(id)
      );

      comment on table doc is 'stores foo documents';

      create table appendix (
          id      int default nextval('foo_seq'),
	  section char(1) not null,
	  body    text,
	  doc_id  int not null,
	  primary key(id),
	  foreign key (doc_id) references doc(id)
      );
 
      comment on table appendix is 'stores appendices to foo documents';
   
      create table foo_version (
          version varchar not null
      );

      insert into foo_version values ('1.0');

.. _update-sql:

.. topic:: Sample Code 2: Update to schema of `foo.sql`, version 2.0:

   .. code-block:: sql
		   
      -- foo.sql
      -- a document with appendices
      --
      -- changelog:
      -- version 2.0 - added a field
      -- version 1.0
      --
      -- copyright, author etc.
      
      BEGIN;
      
      alter table doc add column publication_date date default current_date;
      
      update foo_version set version = '2.0';
      
      COMMIT;
     
The explicit transaction (:command:`BEGIN` - :command:`COMMIT`)
will make sure the DDL update is applied cleanly or not at
all. Note that DDL statements in PostgreSQL are transactional.
 	

If methodology 2 (ORM) is chosen, the contributor should provide the
cleanest DDL output the framework provides.
 
Contributors can expect their database design to be stored into a
schema whose name is determined by the |odh| team and executed as a
non-privileged user account that has the given schema in its default
:strong:`search_path` (see `DDL schema path`_ in PostgreSQL
documentation).

Unless there is a specific reason, contributed designs must use
:strong:`only a single schema` without using its explicit name,
because that will be determined by the :strong:`search_path`.

Contributors are invited to make good use of standard database
features, including -but not limited to:

- Sequences.
- Primary and foreign keys.
- Unique constraints.
- Check constraints.
- Not null constraints.
- Default values.
- Views.

Stored procedures and functions, foreign data wrappers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The |odh| team would like to avoid stored procedures and functions as
far as possible. :strong:`Business logic` should be implemented in the
middle tier, :strong:`not` in the database system.

Hence, the general rule is that database designs submitted to the
|odh| :strong:`must` not contain business logic operations.

However, (small) utility procedures and functions, especially with
respect to triggers, are allowed. When used, these procedures and
functions must be written in `PL/PgSQL`_. Other server-side languages,
even the trusted ones, are neither allowed, nor can they be expected
to be available.

An example of such an allowed instance of a procedure is an audit
trigger that, for any changes made to :strong:`Table A` generates a
log entry that is stored in :strong:`Table B`.

Foreign data wrappers (`SQL/MED`_) :strong:`must not` be used.

Indices and Partioning
~~~~~~~~~~~~~~~~~~~~~~

The submitted database designs must include creation of indices on
tables.

Of course, the |odh| team will monitor database performance and might
be able to add indices at a later time. However, not anticipating
obvious index candidates is considered a bug.

The database design contributor knows best what tables and what
columns will benefit from indices, when the number of records grows.

In particular, if methodology 3 (JSON) is chosen, PostgreSQL provides
specialized multi-dimensional indices of type GIN to index the `jsonb
data type`_.

If the contributor anticipates designs with large tables (say more
than 100M records or more than 5 GB on disk) and expects queries
needing to sequentially scan those tables, :strong:`declarative
partitioning` should be considered. The contributor must then contact
the |odh| team to agree on a declarative partitioning scheme in
advance.


Encoding, collation and localization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All |odh| PostgreSQL databases use the :envvar:`UTF8` character
encoding as default encoding and this :strong:`must not be overridden` by a
database design contributor.

The |odh| team wishes to avoid any character encoding issues by using
UTF8 for everything.

The `default collation` is :envvar:`en_US`. For PostgreSQL
running on Linux this collation already behaves reasonably for German
and Italian::

     select * from t order by s collate "en_US";
      t 
     ---
      A
      À
      Ä
      B 
     (4 rows)

A contributor is free to add a custom collation such as
:envvar:`de_DE` or :envvar:`it_IT`, either at the DDL level or the
query level (see `PostgreSQL documentation on collation <collation>`_),
although there is most likely no need to apply other collations.

A database design :strong:`must not` use the :envvar:`money`
type. Currency amounts must be stored in fields of type
:envvar:`numeric` and the currency must be stored separately.

One important aspect concerns :strong:`dates` and :strong:`timestamps`.

Since the |odh| applications span multiple regions and time zones, it is very
important to be precise about date and time formats and time zone information.

Dates must be stored in the appropriate :envvar:`date` data
type. Dates stored in this data type will be automatically converted
into the client native format when queried. :strong:`Never store dates
as text` because this creates ambiguity. For example, what date
represent the string :envvar:`10-07-2018`? Is it the seventh of
October 2018 or the tenth of July 2018?

The same holds true for timestamps that must be stored in the
appropriate :envvar:`timestamp` data type. Besides avoiding format
ambiguities, this data type also includes also the time zone.

.. note:: PostgreSQL supports also a :envvar:`timestamp without time
   zone` data type, according to the SQL standard. However, this data
   type :strong:`must not be used` as it does not store the vital time
   zone information.

Here ist the output of two queries executed almost at the same time on two
PostgreSQL servers running in different time zones.

This is UTC (no daylight saving).

.. code-block:: sql

  # select now();
              now              
  -------------------------------
   2018-05-28 00:28:25.963945+00
  (1 row)


And this is CET (with daylight saving), 2 hours ahead of UTC::

  # select now();
              now              
  -------------------------------
  2018-05-28 02:28:27.121242+02
  (1 row)

You can see that these two queries were executed (almost) at the same
time thanks to the time zone information (:strong:`+00`
vs. :strong:`+02`). Without time zone information, the two time stamps
appear as separated by two hours.

.. Note:: When using the :envvar:`date` and :envvar:`timestamp` data
   types there is no format issue at all, as the PostgreSQL client
   libraries automatically convert from and to the client native
   format. For example a Java :envvar:`Date` object is automatically
   converted to an SQL :envvar:`date` value.

Sometimes developers need to convert to and from text. In case a
contributing developer wishes to do this using PostgreSQL functions,
they must use functions :strong:`to_date()` and :strong:`to_char()`
(see `PostgreSQL documentation on function formatting <function
formatting>`_).

For example:

.. code-block:: sql
		
   -- insert into date field d converting from German text:
   # insert into dates (d) values (to_date('28.5.2018', 'DD.MM.YYYY'));

   -- select date field d and convert to German text:
   # select to_char(d, 'DD.MM.YYYY') from dates;
     to_char   
   ------------
    28.05.2018
   (1 row)

Sometimes timestamps are stored as numbers, the so called Unix time
stamp (see `unix timestamp`_ on wikipedia).

This is also acceptable, as the Unix time stamp always follows UTC and
is therefore unambiguous.

For JSON data, contributors must make sure that the textual
representation of dates and timestamps follow the ISO standard
:strong:`ISO_8601` (see more `on Wikipedia <iso 8601>`_. Examples:

 * `"ts":"2018-05-28T00:54:28.025Z"`
 * `"d":"2018-05-28"`

PostgreSQL accepts these strings as inputs for :envvar:`timestamp` and
:envvar:`date` types even as text (there is an implicit type cast).

Also note JavaScript has a :envvar:`Date.prototype.toISOString()`
method.



.. check all internal references! &arr;
   sectioning correspondences:
   txt     rst
   #       ----
   ##      ~~~~
   ###     ++++
   ** **   ++++ (to verify) or ____
