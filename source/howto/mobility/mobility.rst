.. _mobility-data-howto:

How to access e-Charging Stations Data?
---------------------------------------

This howto uses the :ref:`E-charging stations dataset <echarging-dataset>`
to showcase a few basic API calls, whose output will be needed in most
complex calls.

.. note:: This how-to is valid for the API v1 |deprecated| version
   only. Please use the :ref:`dedicated howto for API v2
   <get-started-mobility>` instead.
       
Dataset Information
~~~~~~~~~~~~~~~~~~~

This datasets exposes data about the existing e-charging stations in
South Tyrol and their status, including historical data and usage.

==============  ========================================================
Output          JSON, mime-type application/json
E-mail contact  |contact|
API version     :strike:`v1` |deprecated|
Swagger URL     https://swagger.opendatahub.bz.it/?url=https://mobility.api.opendatahub.bz.it/v2/apispec#/Mobility%20V1%20-%20Emobility/
==============  ========================================================

Invoking the API
~~~~~~~~~~~~~~~~
	     
The available methods in this API are very generic, so some
post-processing of the JSON that you receive as output will probably
be necessary.

The API calls shown here can be used with other datasets of the
:ref:`mobility domain <mobility-datasets>`.

You can find all the API's defined methods and documentation at the
URL https://swagger.opendatahub.bz.it/?url=https://mobility.api.opendatahub.bz.it/v2/apispec#/Mobility%20V1%20-%20Emobility/.

The two most basic REST calls are carried out by the methods
:command:`get-stations` and  :command:`get-station-details`.

.. rubric:: get-stations

The :command:`get-stations` method requires no parameters and retrieves all
the IDs of the charging stations that are part of this dataset.

There are two possibilities to retrieve the data with the API call:

1. By HTTP request:

   .. parsed-literal::

      https://swagger.opendatahub.bz.it/?url=https://mobility.api.opendatahub.bz.it/v2/apispec#/Mobility%20V1%20-%20Emobility/get_v1_emobility_rest_get_stations

2. Using a command line with a tool like :command:`curl` or
   :command:`wget`:

   .. parsed-literal::

      curl -X GET --header 'Accept: application/json' '\
      https://swagger.opendatahub.bz.it/?url=https://mobility.api.opendatahub.bz.it/v2/apispec#/Mobility%20V1%20-%20Emobility/get_v1_emobility_rest_get_stations

The result structure is a json list of strings, and an actual outcome
is (shortened for the sake of clarity):

.. code:: json

   [
     "IT*220*EBZ000034",
     "82",
     "DW_000006",
     "DW_000009",
     "IT*220*ETN020016",
     "83",
     "84",
     "DW_000013",
     "DW_000019",
     "85",
   ]

Each of the IDs can then be used in other methods to obtain more
detailed information about the station.

.. rubric:: get-station-details

The :command:`get-station-details` method requires no parameters and
retrieves all the known information for each charging station in the
dataset. Like the previous method, two method can be used for the call:

1. By HTTP request:

   .. parsed-literal::

      https://swagger.opendatahub.bz.it/?url=https://mobility.api.opendatahub.bz.it/v2/apispec#/Mobility%20V1%20-%20Emobility/get_v1_emobility_rest_get_station_details

2. Using a command line with a tool like :command:`curl` or
   :command:`wget`:

   .. parsed-literal::

      curl -X GET --header 'Accept: application/json' '\ 'https://swagger.opendatahub.bz.it/?url=https://mobility.api.opendatahub.bz.it/v2/apispec#/Mobility%20V1%20-%20Emobility/get_v1_emobility_rest_get_station_details


The result structure is a json list of strings, and an actual outcome
is (shortened for the sake of clarity):


.. code-block:: json

   {
     "id": "ASM_00000103",
     "name": "BRIXEN_02",
     "latitude": 46.706333,
     "longitude": 11.651225,
     "municipality": "Brixen - Bressanone",
     "capacity": 2,
     "provider": "Alperia Smart Mobility",
     "city": "BRESSANONE - BRIXEN",
     "state": "ACTIVE",
     "paymentInfo": "https://www.alperiaenergy.eu/smart-mobility/punti-di-ricarica.html",
     "accessType": "PUBLIC",
     "address": "CLUB MAX - Fischzuchtweg - Via del Laghetto"
   }
   {
     "id": "DW-000027",
     "name": "San Vigilio Hotel Sport",
     "latitude": 46.698061,
     "longitude": 11.934766,
     "municipality": "Marèo - Enneberg - Marebbe",
     "capacity": 1,
     "provider": "DriWe",
     "city": "San Vigilio (Marebbe)",
     "state": "ACTIVE",
     "paymentInfo": "http://www.driwe.eu",
     "accessInfo": "24h",
     "accessType": "PRIVATE_WITHPUBLICACCESS",
     "categories": [
	  "EAT&CHARGE",
	  "SLEEP&CHARGE"
     ],
     "address": "Strada al Plan Dessora",
     "reservable": true
   }

As you see from the example, many of the e-charging station's metadata
is shared by all of them including the (unique) ID, name, location
(town or city, address, geographic coordinates), access to it. There
are however additional metadata that are optional (like the station's
category and if it is reservable. 


Troubleshooting
~~~~~~~~~~~~~~~

If the API call fails, one of the following response code is
returned--they correspond to HTTP status codes :

:strong:`401 Unauthorised`
   The request is valid, but authentication is required and you
   provided none. This error will never be publicly seen, because
   authentication is used only by the |odh| team internally.

:strong:`403 Forbidden`
   The request is valid but could not be completed on the server side.

:strong:`404 Not found`	
   There is an syntax error in the call you made or the page is not
   available at this moment.

:strong:`500 Internal Server Error`
   Oh, well. Apparently :strong:`we` have a problem now...
	
