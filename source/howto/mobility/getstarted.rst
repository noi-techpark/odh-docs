.. _get-started-mobility:

How to Access Mobility Data With API v2
=======================================

The new :strong:`API v2` (see :ref:`the description <ninja api>` for
the Mobility domain has simplified the access to data; among its
features, we recall that there is now one single endpoint from which
to retrieve data from all datasets.

The starting point for all actions to be carreid out on the datasets
made available by the |odh| team is the following:

https://mobility.api.opendatahub.bz.it/v2/swagger-ui.html

.. figure:: /images/mobility-swagger.png

   The swagger interface of the Mobility API v2.

From this site, links provide access to documentation about data
licencing and use of the API; it is also possible to contact the |odh|
team by sending an email to the issue tracker, to ask questions,
provide feedback, or to report issues.

Getting Started
---------------

In the API v2, the central concept is :strong:`Station`: all data come
from a given :literal:`StationType`, whose complete list can be
retrieved by simply opening the first method of the
:strong:`data-controller`, :strong:`/api`, then click on :button:`Try
it out` and then on `Execute`.

Station types in the resulting list can be used in the other methods to
retrieve additional data about each of them. To check which station
belongs to which datasets, you can check the list of
:ref:`mobility-datasets`.

Structure of the API calls
--------------------------

In the Mobility domain, there are three methods that can be used to
extract data from the |odh|\'s datasets and allow to incrementally
refine the data retrieved. They are:

#. :literal:`/api/{representation}/{stationTypes}`
#. :literal:`/api/{representation}/{stationTypes}/{dataTypes}`
#. :literal:`/api/{representation}/{stationTypes}/{dataTypes}/{from}/{to}`

These method introduce another facility made available by the API v2:
the type of :literal:`representation`: each result set can be
reproduced as a single, :strong:`flat` or as an indented,
:strong:`tree`\-like JSON file, the former more suitable for machine
consumption, while the latter more convenient for human reading.

The data retrieved by each method are:

#. the data about stations themselfes, that is, the station including
   its meta data and parent stations
#. All the data of the previous call + given data types + the most
   recent measurement (specially suited for real time retrieval of
   data)
#. All the data retrieved by the previous method, but limited to a
   given historical interval (:literal:`from` ... :literal:`to`)

Advanced Data Processing
------------------------

Before introducing advanced data processing techniques, we recall that
queries against the Open Data Hub's datasets always return a
:strong:`JSON` output.

Advanced processing allows to build SQL-style queries using the
:literal:`SELECT` and :literal:`WHERE` keywords to operate on the JSON
fields returned by the calls described in the previous section.
:literal:`SELECT` and :literal:`WHERE` have the usual meaning, with
the former retrieving data from a JSON field, in the form of
:literal:`SELECT=alias[,alias,...]`, and the latter retrieving records
from the JSON output, using the :literal:`WHERE=filter[,filter,...]`
form, with an implicit :strong:`and` among the filters, therefore
evaluation of the filters takes place only if all filters would
individually evaluate to :strong:`true`.

.. _mobility-select-clause:

The :literal:`SELECT` Clause
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In order to build select clauses, it is necessary to know the
structure of the JSON output to a query, therefore we illustrate this
with an example with the following excerpt from the
:ref:`parking-dataset` that represents all data about one parking
station:

.. _select-excerpt:

.. code-block:: json

    {
      "sactive": false,
      "savailable": true,
      "scode": "102",
      "scoordinate": {
        "x": 11.356305,
        "y": 46.496449,
        "srid": 4326
      },
      "smetadata": {
        "state": 1,
        "capacity": 233,
        "mainaddress": "Via Dr. Julius Perathoner",
        "phonenumber": "0471 970289",
        "municipality": "Bolzano - Bozen",
        "disabledtoiletavailable": true
      },
      "sname": "P02 - City parking",
      "sorigin": "FAMAS",
      "stype": "ParkingStation"
    }

You see that there are two hierarchies with two levels in the snippet:
`scoordinate` and `smetadata`; to retrieve only data from them we will
use the `select` clause with the
:literal:`/api/{representation}/{stationTypes}` call; you can
therefore:

* retrieve only the metadata associated with all the stations; the
  select clause would be: :literal:`select=smetadata`
* retrieve all the cities in which there are ParkingStations with
  :literal:`select=smetadata.municipality`
* retrieve all cities and addresses of all ParkingStations:
  :literal:`select=smetadata.municipality,smetadata.mainaddress`

The latter two examples show that to go down one more step into the
hierarchy, you simply add a dot (":literal:`.`") before the attribute
in the next level of the hierarchy. Moreover, you can extract multiple
values from a JSON output, provided you separate them with a comma
(":literal:`,`") and use :strong:`no empty spaces` in the clause. in
the above examples, each of the element within
parentheses--:literal:`smetadata`, :literal:`smetadata.municipality`,
and :literal:`smetadata.mainaddress`\-- is called :strong:`alias`.

Within a :literal:`SELECT` clause, SQL functions are allowed and can
be mixed with aliases, allowing to further process the output, with
the following limitations:

* Only `numeric` functions are allowed, like e.g., :literal:`min`,
  :literal:`max`, :literal:`avg`, and :literal:`count`
* :strong:`No` string selection or manipulation is allowed, but left as
  a post-processing task
* Functions can be use :strong:`only` with the :literal:`flat`
  representation
* When a function is used together with other aliases, these are used
  for grouping purposes. For example:
  :literal:`select=sname,max(smetadata.capacity),min(smetadata.capacity)`
  will return the parking lots with the highest and lowest number of
  available parking spaces. 

.. _mobility-where-clause:

The :literal:`WHERE` Clause
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :literal:`WHERE` clause can be used to define conditions to filter
out unwanted results and can be built with the use of the following
operators:

- `eq`: equal
- `neq`: not equal
- `lt`: less than
- `gt`: greater than
- `lteq`: less than or equal
- `gteq`: greater than or equal
- `re`: regular expression
- `ire`: case insensitive regular expression
- `nre`: negated regular expression
- `nire`: negated case insensitive regular expression
- `bbi`: bounding box intersecting objects (ex., a street that is only partially
  covered by the box)
- `bbc`: bounding box containing objects (ex., a station or street, that is
  completely covered by the box)
- `in`: true if the value of the alias can be found within the given list.
  Example: `name.in.(Patrick,Rudi,Peter)`
- `nin`: False if the value of the alias can be found within the given list.
  Example: `name.nin.(Patrick,Rudi,Peter)`
- `and(filter,filter,...)`: Conjunction of filters (can be nested)
- `or(filter,filter,...)`: Disjunction of filters (can be nested)

As an argument to the `filter`, it is possible to add either a single
value or a list of values; in both cases, operators are used to
determine a condition and only items matching all of the filters will
be included in the answer to the query (implicit `AND`). Like in the
case of SELECT clauses, multiple comma-separated conditions may be
provided. As an example, the following queries use a value and a list
of values, respectively:

* :literal:`where=smetadata.capacity.gt.100` returns only parking lots with more
  than 100 parking spaces
* :literal:`where=smetadata.capacity.gt.100,smetadata.municipality.eq."Bolzano -
  Bozen"` same as previous query, but only parking lots in Bolzano are shown.


Null values
~~~~~~~~~~~

There is currently no mechanism to distinguish whether a JSON field
contains a :literal:`null` value or if the field is
non-existent. However, within a :literal:`WHERE` clause is possible to
filter elements that have :literal:`null` values set by adding to the
query the special parameter :literal:`shownull=true`.
