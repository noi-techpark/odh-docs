.. _bz-analytics:

How to Access Analytics Data in the Mobility Domain
===================================================

.. versionchanged:: 2021.04 Replace two wrong images with correct ones.

This howto guides you in browsing and querying data from the Mobility
domain using the https://analytics.opendatahub.bz.it/ web site.

.. note:: Access to data on this website is now possible by
   using R. See :ref:`the dedicated section <r-access>`  for
   information and directions.


Introduction
------------

The website https://analytics.opendatahub.bz.it/ gathers data from
datasets in the mobility domain and uses them to draw two types of
diagram: a :ref:`chart <charts>` using historical data and an
interactive :ref:`map <mapoverview>` that show where are located the
sensors on the territory. The latter is the default landing page.

.. _charts:

Charts
------

The charts page contains a number of options to show data, both
historical and current, from the mobility domain. Data are gathered by
sensors which are installed on various locations in South Tyrol and
are operated and governed by different institutions or public and
private companies. While the vast majority of the data comes from
South Tyrol, there are datasets (including the E-mobility, weather,
and traffic domain), which contain data about some neighbouring
Italian provinces and regions.


.. figure:: /images/analytics/analytics-home.png
   :scale: 40%
   :align: center

   The landing page of analytics.mobility.bz.it.

While there are many controllers in the page, that allow to tweak the
search parameter, the basic usage is quite simple and requires
two steps:

#. Select a dataset to be added to the chart, from the drop-down menus
   below the diagram.

#. Restrict the data to be displayed to a date range, either
   a predefined one or a custom one.

A sample display from the weather datasets is shown in
:numref:`analytics-chart-one-dataset`, in which data from only one
temperature sensor are used, and in
:numref:`analytics-chart-one-dataset`, using data from two temperature
sensors.

.. _analytics-chart-one-dataset:

.. figure:: /images/analytics/analytics-chart-onedataset.png
   :scale: 33%
   :align: center

   Sample temperature diagram on Cima Presena.

.. _analytics-chart-two-datasets:

.. figure:: /images/analytics/analytics-chart-twodatasets.png
   :scale: 33%
   :align: center

   Sample temperature diagram on Cima Presena and Cima Paganella.

.. _mapoverview:

Map Overview
------------

In the map overview, there is a map, initially displaying only the
South Tyrol region, with the list of available sensor types on the
left-hand side. When clicking on one or more items, the position of
all sensors will appear on the map, see :numref:`map-overview-image`
for the parking lots available in the Trentino-South Tyrol region.

A signpost with a circled :strong:`+` indicates that there are more
sensors around at that location; this is true especially when the map
encompasses a large area, like e.g., the whole South Tyrol region.
Therefore, by zooming in on the map, or by (repeatedly) clicking on
the :strong:`+`, more signposts will appear, until the :strong:`+`
either disappears or is replaced by a different sign: you have found
the (unique) sensor at that location.

.. _map-overview-image:

.. figure:: /images/analytics/analytics-map-overview.png
   :scale: 33%
   :align: center

   Map with parking lot signposts.

In the case of Parking data--and in a few other datasets, the
:strong:`+` will be replaced by a green, yellow, or red circle,
meaning that there are many, a few, or no free parkings in that lot.

For other types of sensors, the :strong:`+` simply disappears.

When clicking on a single sensors, a panel will appear on the
right-hand side, containing a lot of information about that sensor,
including its unique ID within the dataset, geographic
coordinates. Additional information displayed depend on the dataset.

.. _analytics-signpost-info:

.. figure:: /images/analytics/analytics-signpost-info.png
   :scale: 33%
   :align: center

   Details of a sensor.
