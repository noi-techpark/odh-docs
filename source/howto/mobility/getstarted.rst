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

Advanced methods
----------------

There are three more methods that can be used to extract data from the
|odh|\'s datasets. They allow to incrementally refine the data
retrieved. They are:

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
