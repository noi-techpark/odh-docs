.. _get-started-mobility:

How to Access Mobility Data With API v2
=======================================
		  
The new :strong:`API v2` (see :ref:`the description <ninja api>`) for
the Mobility domain has simplified the access to data; among its
features, we recall that there is now one single endpoint from which
to retrieve data from all datasets.

The starting point for all actions to be carried out on the datasets
made available by the Open Data Hub team is the following:

https://mobility.api.opendatahub.bz.it/

.. figure:: /images/mobility-swagger.png
   :scale: 33%
   :align: right

   The swagger interface of the Mobility API v2.

From this site, links provide access to documentation about data
licencing and use of the API; it is also possible to contact the Open Data Hub
team by sending an email to the issue tracker, to ask questions,
provide feedback, or to report issues.

Getting Started
---------------

  
In the API v2, the central concept is :strong:`Station`: all data come
from a given :literal:`StationType`, whose complete list can be
retrieved by simply opening the secong method of the :strong:`Mobility
V2` controller, :strong:`/v2/{representation}`, then click on
:button:`Try it out` and then on `Execute`.

Station types in the resulting list can be used in the other methods to
retrieve additional data about each of them. To check which station
belongs to which datasets, you can check the list of
:ref:`mobility-datasets`.

