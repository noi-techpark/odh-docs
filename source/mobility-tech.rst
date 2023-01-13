.. tech info for mobility datasets

.. _mobility-tech:

============================================
 Technical Information for Mobility Dataset
============================================

This section contains detailed technical information shared by the
datasets in the Mobility domain.  The purpose of this section is
manifold:

* To understand what output is received as result of a query and its
  structure--see :ref:`mobility-json`

* To know which methods are available to gather data from the domains
  via the API calls--see :ref:`api-v2-structure`
  
* To learn how to improve responses by tweaking queries using SELECT,
  and WHERE clauses, logical operators, and parameters.--see
  :ref:`mobility-advanced`

.. _mobility-json:

The JSON Response Schema
========================

We recall that every query to the mobility datasets will return a
JSON-structured file with a number of information about one station
(or more) and values it collected over time, both real-time and
historical data.

The overall structure of the JSON is the following:

.. code::

   "offset": 0,   
   "data": [],    
   "limit": 200   

Here, `offset` and `limit` are used for limiting the displayed
results. The three keys have the following meaning:

* `limit` gives the maximum number of results that are included in the
  response. It defaults to :strong:`200`.

  .. hint:: By setting the value to :strong:`-1`, `limit` will be
     disabled and all results will be shown.
     
* `offset` allows to skip elements from the result set. The default is
  :strong:`0`, i.e., the results start from the first one.
* `data` is the actual :strong:`payload` of the response, that is, the
  data answering the query; since it changes depending on which API
  call/method is used, it will be described in the next section.

.. hint:: It is possible to simulate pagination when there are many
   results: for example, if there are :strong:`1000` values, by adding
   to successive queries the offsets :strong:`0`, :strong:`200`,
   :strong:`400`, :strong:`600`, and :strong:`800`, the response of
   the query is split on 5 pages of 200 results each.

.. _api-v2-structure:

Structure of the API calls and Payload
======================================

In the Mobility domain, there are different general methods that can
be used to extract data from the Open Data Hub's datasets and allow to
incrementally refine the data retrieved. They are:

#. :literal:`/v2/` gives the list of the Open Data Hub's entry points,
   that is, the possible representations of the data contained in the
   datasets. to be used in the next methods. See :ref:`the details
   below <representation-types>`. 

#. :literal:`/v2/{representation}/` shows all the StationTypes
   available, that is, all the sources that provided data to the Open
   Data Hub.
			
#. :literal:`/v2/{representation}/{stationTypes}` returns data about
   the stations themselves, including metadata associated with each, and
   data about its parent stations, if any.

#. :literal:`/v2/{representation}/{edgeTypes}` returns data related to
   the :ref:`edges <edge-definition>` and their parts, and is very
   similar to the previous call.
		     
#. :literal:`/v2/{representation}/{stationTypes}/{dataTypes}`.  In
   addition to the data of the previous call, it contains the data
   types defined in the dataset.

#. :literal:`/v2/{representation}/{stationTypes}/{dataTypes}/latest`. In
   addition to all the data retrieved by the previous call, this call
   retrieves also the most recent measurement. This method is
   especially suited for real time retrieval of data.
  
#. :literal:`/v2/{representation}/{stationTypes}/{dataTypes}/{from}/{to}`.
   All the data retrieved by method #3, but limited to a
   given historical interval (:literal:`from` ... :literal:`to`).

   .. note:: The interval is `half-open`, i.e., [`from`, `to`),
      meaning that the `from` date is :strong:`included` in the result
      set, while the `to` date is :strong:`excluded`.

.. _representation-types:

Representation types
====================

The first method described in the previous list introduces the
available entry points to the API v2: the types of `representation`
that can be used to browse or access the data provided by the Open
Data Hub Team

The `representation` consists now of a pair of comma-separated
keywords composed of:

1. the already existent `flat` or `tree` AND
2. either `node` and `edge`

In both the :strong:`flat` and :strong:`tree` representations, all the
metadata and available data are shown and browsable, the difference
being that in `flat`, while
`tree` keeps the hierarchical structure of the metadata.

The `node` and `edge` describe a :literal:`StationType` and the
connection between two :literal:`StationType`\s, respectively.


.. _edge-definition:

.. _node-definition:

.. grid::
   :gutter: 1

   .. grid-item-card::
      :columns: 6

      Flat
      ^^^^

      In the `flat` representation, all metadata and available data can
      be accessed and browsed. However, no hierarchy appears and data and
      metadata are shown at the same level.

   .. grid-item-card::
      :columns: 6

      Tree
      ^^^^^

      In the `tree` representation, all metadata and available data can
      be accessed and browsed as in `flat`, but in this case, any
      hierarchy of data or metadata is preserved and shown.


   .. grid-item-card::
      :columns: 6

      Node
      ^^^^^

      A node is a measurement station and contains all metadata
      associated to it. The :strong:`node` representation corresponds to
      the `old` (pre-2020.10) output of the API calls, therefore it can
      safely be omitted for backward compatibility. As an example, valid
      for all methods listed in the :ref:`previous section
      <api-v2-structure>`, these API calls are equivalent.

        :literal:`/v2/tree,node/{stationTypes}`

        :literal:`/v2/flat,node/{stationTypes}`

        :literal:`/v2/tree/{stationTypes}`

        :literal:`/v2/flat/{stationTypes}`


      .. note:: While only :strong:`available` nodes are exposed by the
         |odh|\, the resulting JSON response might still include the
         `savailable` field, short for station available.

   .. grid-item-card::
      :columns: 6

      Edge
      ^^^^^

      An Edge is a connection between two stations, improved with
      additional information, including some descriptive field and
      geometries that describe the connection on a map. Internally, an
      edge is composed of three parts (all calles `stations`): a start
      station (beginning of the edge), an end station and a station
      describing the edge. Whenever retrieving an Edge, all metadata
      referring directly to it begin with `e`, like for example
      `eactive`, `eavailable`, and so on.

      .. note:: While only :strong:`available` edges are exposed by the
         |odh|\, the resulting JSON response might still include the
         `sbavailable`, `seavailable` and `eavailable` fields, referring
         to start station, end station, and edge description,
         respectively.

      Moreover, there are neither measurements nor types associated with
      edges.
   
Valid combinations are therefore: `flat,node`; `tree,node`;
`flat,edge`; `tree,edge`; if neither `node` or `edge` are provided,
the default :strong:`node` will be used.

An additional representation is `apispec`, which allows to see and
reuse the API specification in an OpenAPI v3 YAML format, suitable for
swagger-like access to the data.

In the reminder of this section we show examples of some of the above
mentioned API methods and describe the outcome, including the various
keys and types of data returns by the call.

:literal:`/v2/{representation}/{stationTypes}`
----------------------------------------------

To describe the outcome of this method in details, we will use the
following snippet.

.. code-block::
   :linenos:
   :emphasize-lines: 10-19,31-40
   :caption: An excerpt of information about a charging station.
   :name: apiv2-stations

       {
      "pactive": false,
      "pavailable": true,
      "pcode": "AER_00000005",
      "pcoordinate": {
        "x": 11.349217,
        "y": 46.499702,
        "srid": 4326
      },
      "pmetadata": {
        "city": "BOLZANO - BOZEN",
        "state": "ACTIVE",
        "address": "Via Cassa di Risparmio  - Sparkassenstraße 14",
        "capacity": 2,
        "provider": "Alperia Smart Mobility",
        "accessType": "PUBLIC",
        "paymentInfo": "https://www.alperiaenergy.eu/smart-mobility/punti-di-ricarica.html",
        "municipality": "Bolzano - Bozen"
      },
      "pname": "BZ_CASSARISP_01",
      "porigin": "ALPERIA",
      "ptype": "EChargingStation",
      "sactive": false,
      "savailable": true,
      "scode": "AER_00000005-1",
      "scoordinate": {
        "x": 11.349217,
        "y": 46.499702,
        "srid": 4326
      },
      "smetadata": {
        "outlets": [
          {
            "id": "1",
            "maxPower": 22,
            "maxCurrent": 31,
            "minCurrent": 0,
            "hasFixedCable": false,
            "outletTypeCode": "Type2Mennekes"
          }
        ],
        "maxPower": 7015,
        "maxCurrent": 31,
        "minCurrent": 6,
        "municipality": "Bolzano - Bozen",
        "outletTypeCode": "IEC 62196-2 type 2 outlets (all amperage and phase)"
      },
      "sname": "BZ_CASSARISP_01-253",
      "sorigin": "ALPERIA",
      "stype": "EChargingPlug"
    }
    
You immediately notice that all the keys in the first level start
either with a :strong:`p` (`pactive`, `pcoordinate`, and so on) or an
:strong:`s` (`sactive`, `scoordinate`, and so on): the former,
:strong:`p`, refers to data about the `parent` stations, :strong:`s`
to data of the station itself. Besides the initial `p` or `s`, the
meaning of the key is the same. In the snippet above, you see that all
the data about a station are grouped together and come after the data
of its parent (see lines.

.. _apiv2-keys-1:

The meaning of the keys are:

* :strong:`active`: the station is actively sending data to the Open Data Hub. A
  station is automatically marked as not active (i.e.,
  :literal:`pactive` = false) when it does not send data for a given
  amount of time (24 hours).
* :strong:`available`: data from this station is available in the Open Data
  Hub.

  .. note:: `active` and `available` might seem duplicates, but a
     station can be available but not active or vice-versa: In the
     former case, it means that its historical data have been recorded
     and can be accessed, although it currently does not send any data
     (for example, due to a network error or because it is not working
     or because it has been decommissioned); in the latter case, the
     station has started to send its data but they are not yet
     accessible (for example, because the are still being
     pre-processed by the Open Data Hub).
     
* :strong:`code`: a unique :strong:`ID`\entifier 
* :strong:`coordinate`: the station's geographical coordinates
* :strong:`metadata`: it may contain any kind of information about the station
  and mostly depends on the type of the station and the data it
  sends. In the snippets above, lines 10-16 contain information about
  the location of a charging station, while lines 28-38 technically
  describe the type of plugs available to recharge a car.

  .. hint:: The metadata has only one limitation: it must be either a
     JSON object or :literal:`NULL`.
     
* :strong:`name`: a (human readable) name of the station
* :strong:`origin`: the `source` of the station, which can be anything, like for
  example the name of the :ref:`data-providers`, the spreadsheet or
  database that contained the data, a street address, and so on.
* :strong:`type`: the type of the station, which can be a MeteoStation,
  TrafficStation, EChargingPlug, Bicycle, and so on.
  
  .. note:: The name of the StationType is :strong:`Case Sensitive`!
     You can retrieve all the station types with the following API call.

     .. code::
	
	~$ curl -X GET "https://mobility.api.opendatahub.com/v2/tree" -H "accept: application/json" 

:literal:`/v2/{representation}/{stationTypes}/{dataTypes}/latest`
-----------------------------------------------------------------

This API call introduces two new prefixes to the keys, as shown in :numref:`apiv2-datatypes`.

.. code-block::
   :linenos:
   :emphasize-lines: 2-6,8-11
   :caption: An excerpt of information about a charging station.
   :name: apiv2-datatypes


   {
      "tdescription": "",
      "tmetadata": {},
      "tname": "number-available",
      "ttype": "Instantaneous",
      "tunit": "number of available vehicles / charging points",
      
      "mperiod": 300,
      "mtransactiontime": "2018-10-24 01:05:00.614+0000",
      "mvalidtime": "2020-05-01 07:30:00.335+0000",
      "mvalue": 1,
   }

The new prefixes are :strong:`t` and :strong:`m`. The `t` prefix
refers to :strong:`Data Types`, i.e., how the values collected by the
sensors are measured. See below for a more detailed description of
data types and some tip about them.  The `m` prefix refers to a
:strong:`measurement`, that is, how often the data are collected,
timestamp of the measure, when it is transmitted to be stored, and
other information.

Alongside all keys present in :numref:`apiv2-stations` (see
:ref:`previous section <apiv2-keys-1>`), :numref:`apiv2-datatypes`
contains the additional key:

* :strong:`ttype`: the type of the data, which can be expressed as
  either a custom string, like in the example above, or as a DB
  function like COUNT, SUM, AVERAGE, or similar
* :strong:`tunit` the unit of measure
* :strong:`mperiod`: the time in seconds between two consecutive
  measures
* :strong:`mtransactiontime`: timestamp of the transmission of the
  data to the database
* :strong:`mvalidtime`: timestamp of the measurement. It is either the
  moment in time when the measurement took place or the time in the
  future in which the next measure will be collected.
* :strong:`mvalue`: the absolute value of the measure, represented in
  either `double precision` or `string` format. It must be paired with
  the `t` keys to understand its meaning.

:numref:`apiv2-datatypes` represents an `EChargingStation` with one
available charging point; the last measure was taken on `2020-05-01
07:30:00.335+0000` and will be repeated every 5 minutes (`300`
seconds). Moreover, the station appears to not transmit its data
anymore, so historical data might not be available.
	
.. topic:: Data types in the datasets.

   Data types are not normalised; that is, there is no standard or
   common unit across the datasets. Indeed, each data collector
   defines its own data types and they may vary quite a lot from one
   dataset to another. There is also neither a common representation
   format for data types, therefore a same unit can appear quite
   different in different datasets. For example, to express
   `microseconds`, one dataset can use

   .. code::
      
      "tdescription": "Time interval measured in microseconds",
      "tmetadata": {},
      "tname": "Time interval",
      "ttype": "Instantaneous",
      "tunit": "ms",

   While another:
   
   .. code::
      
      "tdescription": "Microseconds between two consecutive measures",
      "tmetadata": {},
      "tname": "Time interval",
      "ttype": "COUNT",
      "tunit": "milliseconds",

   We can see that, although we might understand that the measures
   from the two datasets are indeed expressed in milliseconds, this is
   not true for machine-processed data

   
:literal:`/v2/{representation}/{stationTypes}/{dataTypes}/{from}/{to}`
----------------------------------------------------------------------

This method does not add any other keys to the JSON response; all the
keys described in the previous two section are valid and can be used.

.. _mobility-advanced:
	 
Advanced Data Processing
========================
		    
Before introducing advanced data processing techniques, we recall that
queries against the Open Data Hub's datasets always return a
:strong:`JSON` output.

Advanced processing allows to build SQL-style queries using the
:literal:`SELECT` and :literal:`WHERE` keywords to operate on the JSON
fields returned by the calls described in the previous section.
:literal:`SELECT` and :literal:`WHERE` have the usual meaning, with
the former retrieving data from a JSON field, in the form of
:literal:`SELECT=target[,target,...]`, and the latter retrieving records
from the JSON output, using the :literal:`WHERE=filter[,filter,...]`
form, with an implicit :strong:`and` among the filters, therefore
evaluation of the filters takes place only if all filters would
individually evaluate to :strong:`true`.


.. _mobility-select-clause:

The :literal:`SELECT` Clause
----------------------------

In order to build select clauses, it is necessary to know the
structure of the JSON output to a query, therefore we illustrate this
with an example with the following excerpt from the :dataset:`Parking
dataset <traffic/parking/>` that represents all data about one parking
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
:literal:`/v2/{representation}/{stationTypes}` call; you can
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
(":literal:`,`") and use :strong:`no empty spaces` in the clause. In
the above examples, each of the element within
parentheses--:literal:`smetadata`, :literal:`smetadata.municipality`,
and :literal:`smetadata.mainaddress`\-- is called :strong:`target`.

Within a :literal:`SELECT` clause, SQL functions are allowed and can
be mixed with targets, allowing to further process the output, with
the following limitations:

* Only `numeric` functions are allowed, like e.g., :literal:`min`,
  :literal:`max`, :literal:`avg`, and :literal:`count`
* :strong:`No` string selection or manipulation is allowed, but left as
  a post-processing task
* When a function is used together with other targets, these are used
  for grouping purposes. For example:
  :literal:`select=sname,max(smetadata.capacity),min(smetadata.capacity)`
  will return the parking lots with the highest and lowest number of
  available parking spaces. 

.. _mobility-where-clause:

The :literal:`WHERE` Clause
---------------------------

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
- `in`: true if the value of the target can be found within the given list.
  Example: `name.in.(Patrick,Rudi,Peter)`
- `nin`: False if the value of the target can be found within the given list.
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
  Bozen"` same as previous query, but only parking lots in Bolzano are
  shown.

In these two examples we use a number in the filter (i.e., gt.\
:strong:`100`), which is by default automatically recognised as a
number and the required math is calculated out of the box. In case
there is a query in which you use a number, but need to consider it as
a string, you need to use double quotes, like gt.\ :strong:`"100"`.

.. _logical-operators:

Logical Operators
-----------------

Besides the operators described in section
:ref:`mobility-where-clause`, |odh| supports the use of logical
operators :literal:`and` and :literal:`or` in the :literal:`WHERE`
clause, like these examples show.

.. code-block::
   :linenos:

   and(x.eq.3,y.eq.5)
   x.eq.3,y.eq.5

   or(x.eq.3,y.eq.5)
   or(x.eq.3,and(y.gt.5,y.lt.10))

Logical operators are followed by a comma-separated list of `targets`,
which can be filters (see previous section for some example), or other
logical operators. In complex logical expression, parentheses are
employed to assign precedence. Lines 1 and 2 above are equivalent,
because the default logical operator is :literal:`and`.

The above example will be translated into Postgres as follows:

.. code-block::
   :linenos:

   (x = 3 AND y = 5)
   (x = 3 AND y = 5)
   
   (x = 3 OR y = 5)
   (x = 3 OR (y > 5 AND y < 10))

Additional Parameters
---------------------

There are a couple of other parameter that can be given to the API
calls and are described in this section.

.. rubric:: :literal:`shownull`
         
In order to show :strong:`null` values in the output of a query, add
:literal:`shownull=true` to the end of your query.

.. rubric:: :literal:`distinct`

Results in query responses contain unique results, that is, if for
some reason one element is retrieved multiple times while the query is
executed, it will be nonetheless shown only once, for performance
reasons. It is however possible to retrieve each single result and
have it appear in the response by adding :literal:`distinct=true` to
the API call.

.. warning:: Keeping track of all distinct values might be a
   resource-intensive process that significantly rises the response
   time, therefore use it with care.

.. rubric:: :literal:`timezone`

By default, the timestamp of the |odh| responses is given in
:strong:`UTC` time zone. The use of the :literal:`timezone` parameter
allows to modify the timestamp whenever desirable. To use it, simply
append the parameter to your API call.

   :literal:`/flat/ParkingStation/occupied/latest?timezone=UTC-2`
	    
	    
   :literal:`/flat/ParkingStation/occupied/latest?timezone=Europe/Rome`


.. note:: As argument to the :literal:`timezone` parameter, you can
   use any allowed value in `Java's Time zone implementation
   <https://docs.oracle.com/javase/8/docs/api/java/time/ZoneId.html#of-java.lang.String-java.util.Map->`_.
