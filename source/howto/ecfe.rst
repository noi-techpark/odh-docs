.. |idgb| replace:: it.bz.geobank.

Echarging Stations Howto
------------------------

.. note:: This howto is a stub and will be used mostly to collect
   feedback. It is however structured like my idea for these howots
   and contains almost all the parts that IMHO should be contained in
   the howtos that should be ready for our first milestone.
  
.. parsed-literal::
   
   ID: |idgb|\ echargingstation

.. topic:: Dataset at a glance

   License: |cc0|
   
   Output: JSON, mime-type application/json

   E-mail contact: info\@geobank.bz.it

   The full API documentation can be found at
   :integreen:`EchargingFrontEnd`.

   API version: v1


In this howto, we show how to retrieve information about the available
charging station.


	       
Dataset Information
~~~~~~~~~~~~~~~~~~~

This dataset is used to provide information about charging stations
for electric cars in South Tyrol, their location, and historical usage
data, including their current availability.

The available methods in this API are very generic, so some
post-processing of the JSON that you receive as output will probably be
necessary.


Invoking the API
~~~~~~~~~~~~~~~~

In order to retrieve all the stations' ID, we need the following methods:

#. :command:`get-stations`


get-stations
++++++++++++

The :command:`get-stations` method requires no parameters and retrieves all
the IDs of the charging stations that are part of this dataset.

There are two possibilities to retrieve the
data with the API call:

1. By HTTP request:

   .. parsed-literal::

      :integreen:`emobility/rest/get-stations`

2. Using a command line with a tool like :command:`curl` or
   :command:`wget`:

   .. parsed-literal::

     curl -X GET --header 'Accept: application/json' '\ :integreen:`emobility/rest//get-stations`'


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

Troubleshooting
~~~~~~~~~~~~~~~

If the API call fails, one of the following response code is
returned - they correspond to HTTP status codes :


:strong:`401 Unauthorised`
	The request is valid, but authentication is required and you
	provided none.

:strong:`403 Forbidden`
	The request is valid but could not be completed on the server side.

:strong:`404 Not found`
	There is an syntax error in the call you made or the page is
	not available at this moment.
