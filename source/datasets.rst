
.. _available_datasets:

Datasets
========

The goal of the |odh| project is to make available datasets containing
data about the South Tyrolean ecosystem, to allow third parties to
develop novel applications on top of them, consuming the exposed
data. These applications may range from a simple processing of
datasets to extract statistical data and to display the result in
different graphic formats like pie-charts, to far more complex
applications that combine data from different datasets and correlate
them in some useful way.

As seen in :numref:`domains-diagram`, data originate from different
domains (Mobility, Tourism, and so on); they are gathered from sensors
and packed together by :ref:`data-providers`. `Sensors` can be for
example GPS devices installed on buses that send their real-time
geographic position or a small electronic device on a plug of an
e-charging station that checks the if the plug is being used or not,
to let people know that the charging outlet is available.

Datasets are accessible through a :term:`REST API`, the URL of each
endpoint is given along with other information in the description of
each dataset, see the lists of datasets in the remainder of this
section.

.. _data-providers:

Data Providers
--------------

A :strong:`Data Provider` is any entity that shares their Open Data
with the |odh| project, allowing their free reuse (ideally under a
free licence like |cc0| or |bysa|) from any third-party that relies on
the |odh| to build their application. These entities can be private
companies or enterprises, public bodies, and even private citizen, if
they have interesting data about South Tyrol to share.

The Open Data exposed by the |odh| originate from data and datasets
owned by different actors (called :strong:`Data Providers`) which are
at this time mostly local public bodies. Since there is no direct
1-to-1 correspondence between Data Providers and datasets, we
currently offer a list of data providers whose data can be pulled
from |odh|\. Indeed, an |odh| dataset can be composed of data deriving
from different providers, while a provider can submit to |odh|
multiple types of data that will belong to more than one dataset.

The |odh|\'s Data Providers are:

* IDM Südtirol/Alto Adige
* SIAG, Südtirol Informatica AG - Informatica Alto Adige
* SASA, public transport operator
* Alperia/Neogy, energy provider for South Tyrol
* Municipality of Bolzano
* Municipality of Merano
* Municipality of Trento
* Municipality of Rovereto
* APPA, Trentino Agency of the environment
* CISMA, Bluetooth sensors
* Carsharing Alto Adige, via its technological partner DB Rent
* LTS, South Tyrol Association of Tourism Organisations.
* APPA, South Tyrolean agency for the environment.
* InnoVie.
* Südtirol Wein.
* Route220, Nevicam and Driwe e-charging stations provider
 
.. topic:: A note about datasets.

   The |odh| contains many datasets: a few have been provided for
   testing purposes, other are meant for internal use only, and other
   contain only a part of their data that is available as Open Data.

   While the goal of the |odh| project is to expose :strong:`only Open
   Data` and the |odh| team members always suggest to use |CC0| to
   third-parties releasing datasets, it is not yet possible for the
   |odh| team to guarantee the availability as open data of all the
   data in the datasets, because the data licensing and its
   distribution rights are decided by the copyright holder of each
   dataset.

   Since some of the datasets may contain data that can not be
   distributed by the |odh| team under an open licence like, e.g.,
   |cc0| or |bysa|, a user will be able to retrieve from each dataset
   only those data that are distributed as :strong:`Open Data`.

At the date of writing, datasets in the :ref:`Mobility
<mobility-datasets>` and :ref:`Tourism <tourism-datasets>` are available.

Accessing data in the |odh|
---------------------------

There are different modalities to access data that are provided by the
|odh|, that are listed here. Currently, data from the
:strong:`Mobility` and :strong:`Tourism` domains can be accessed, both
from the command line and using a browser. Various dedicated tutorials
are available in the :ref:`howto-list` section; while in section
:ref:`getting-involved` you can find additional ways to interact with
the data and the |odh| team.

.. _ninja api:

API
~~~

Programmatic and non-interactive access to the Open Data Hub's dataset
is possible using the APIs made available by the Open Data Hub Team.

The APIs are composed of a few generic methods, that can be combined
with many parameters to retrieve only the relevant data and then
post-processed in the preferred way.

The following table summarises how the two versions of the API can be
used within the Open Data Hub's domains.

=== ========= =============
API  Tourism  Mobility
=== ========= =============
v1   OK       Deprecated
v2   --       Recommended 
=== ========= =============


There are currently two versions of the API, v1 and v2, with the
former now :strong:`deprecated` for the Mobility domain and marked as
such |deprecated| throughout the |odh| documentation. New users are
recommended to use the new API v2, while users of the API v1 are
encouraged to plan a migration to the new API.

The new API v2 has a different approach compared to the previous
version, and therefore is not compatible with the API v1, the main
difference being that all data stored in the |odh| can now be
retrieved `from a single endpoint`, while with API v1 there was an
endpoint for each dataset.

This change in approach requires also a breaking change for the users
of API v1. The initial step, indeed, will not be to open the URL of
the dataset and start exploring, but to retrieve the
:literal:`stationType`\s and then retrieve additional data about each
station. A :literal:`stationType` is the main object of a datasets,
about which all the information in a dataset relate to; a dataset
includes at least one :literal:`stationType`.  A new, dedicated howto
describing in detail the new API v2 and a few basic examples is
:ref:`already available <get-started-mobility>` in the dedicated section
of this documentation.

.. note:: It is important to remark that the API v2 is :strong:`only
   available` for datasets in the :strong:`Mobility` Domain.
   

Browser access
~~~~~~~~~~~~~~

Accessing data in the |odh| by using a browser is useful on different
levels: for the casual user, who can have a look at the type and
quality of data provided; for a developer, that can use the
:term:`REST API` implemented by the |odh| or even check if the results
of his app are coherent with those retrieved with the API; for
everyone in order to get acquainted with the various methods to
retrieve data.

More in detail, these are the possibilities to interact with |odh|\'s
data by using a browser:

#. Go to the :ref:`applist` section of the documentation, particularly
   sub-sections :ref:`production-stage-apps` and
   :ref:`beta-stage-apps`, and choose one of the web sites and portals
   that are listed there. Each of them uses the data gathered from one
   or more |ODH|\'s datasets to display a number of useful
   information. You can then see how data are exposed and browse them.

#. In the same :ref:`applist` section, you can also check the list of
   the :strong:`Alpha Stage Apps` and choose one of them that you
   think you can expand, then get in touch with the authors to suggest
   additional features or collaborate with them to discuss its further
   development to improve it.  
   
#. Access the `ODH Tourism data browser
   <http://tourism.opendatahub.bz.it/>`_ and search for the Open Data
   available in the Tourism domain. You can simply use those data for
   your convenience, or you might even find a novel way to exploit
   those data and use them in an app or portal you are going to
   develop. A detailed howto is available:
   :ref:`tourism-data-browser-howto` to help you getting acquainted
   with the browser.

#. Go to the :strong:`Swagger interface` of the datasets in the
   Tourism domain, located at
   http://tourism.opendatahub.bz.it/swagger/ui/index, to learn how the REST
   APIs are built and how you can script them to fetch data for your
   application. To get started, there is a dedicated howto:
   :ref:`tourism-data-howto` that will guide you in the first steps.

#. Access the :strong:`Swagger interface` of the datasets in the
   Mobility domain. Check the link for each of them in section
   :ref:`mobility-datasets`. Like in the case of the tourism' Swagger
   interface, you can learn REST API call for that domain and fetch
   data for your application. There is a dedicated howto to learn more
   how to interact with this interface: ref:`mobility-data-howto`

#. Open the :strong:`Analytics for Mobility` web page, at
   https://analytics.mobility.bz.it/. This portal uses data in the
   mobility domain to display various information about the sensors,
   including their locations, what they measure, and actual data in
   near-real time. You can retrieve data gathered by the sensors
   directly from the dataset, in almost real-time.

CLI access
~~~~~~~~~~

Unlike browser access, that provides an interactive access to data,
with the option to incrementally refine a query, command line access
proves useful for non-interactive, one-directional, and quick data
retrieval in a number of scenarios, including:

* Scripting, data manipulation and interpolation, to be used in
  statistical analysis.
* Applications that gather data and present them to the end users.
* Automatic updates to third-parties websites or kiosk-systems like
  e.g., in the hall of hotels.

Command line access to the data is usually carried out with the
:program:`curl` Linux utility, which is used to retrieve information
in a non-interactive way from a remote site and can be
used with a variety of options and can save the contents it downloads,
which can them be send to other applications and manipulated.

The number of options required by :program:`curl` to retrieve data
from |odh|\'s dataset is limited, usually they are not more than 3 or
4, but their syntax and content might become long and not easily
readable by a human, due to the number of :ref:`filters
<common-filters>` available. For example, to retrieve the list of all
points of interests in South Tyrol, the following command should be
used:

.. code-block:: bash

   curl -X GET "http://tourism.opendatahub.bz.it/api/ODHActivityPoi?pagenumber=1&pagesize=10&type=63&subtype=null&poitype=null&idlist=null&locfilter=null&langfilter=null&areafilter=null&highlight=null&source=null&odhtagfilter=null&odhactive=null&active=null&seed=null&latitude=null&longitude=null&radius=null" -H "accept: application/json"


Your best opportunity to learn about the correct syntax and parameters
to use is to go to the :strong:`swagger interface` of the `tourism
<http://tourism.opendatahub.bz.it/swagger/ui/index>`_ or `mobility
<https://mobility.api.opendatahub.bz.it/v2/swagger-ui.html>`_ domains
and execute a query: with the output, also the corresponding
:program:`curl` command used to retrieve the data will be shown.

Authentication
~~~~~~~~~~~~~~

The authentication layer is currently intended for :strong:`internal
use only`. All data in the dataset that you can receive from the |odh|
are free to use and do not require any type of authentication.


The authentication layer can be of interest for developers who want to
collaborate in the development of |odh|\; Details on the implementation
are available in section :ref:`authentication`.

.. _mobility-datasets:

Datasets in the Mobility Domain
-------------------------------


.. contents:: List of datasets in the mobility domain.
   :local:
	   
This section contains information about the datasets and how to access
them using the API that the |odh| team developed and made available.

The description of each dataset includes the following information:

* The output format of the API call
* An e-mail contact for the dataset
* The versions of the API that can be used to access the dataset
* The (`new!`) swagger URL of the APIs
* The :literal:`stationType` that belong to each dataset

The datasets in the Mobility domain are grouped in :strong:`Traffic`
and :strong:`Mobility` as follows:

.. rubric:: Traffic

.. _rwisstation-dataset:

|idgb|\ rwisstation
~~~~~~~~~~~~~~~~~~~
.. include:: /datasets/rwisstation.rst

.. _streetelement-dataset:

|idgb|\ streetelements
~~~~~~~~~~~~~~~~~~~~~~
.. include:: /datasets/streetelements.rst

.. _linkstation-dataset:

|idgb|\ linkstation
~~~~~~~~~~~~~~~~~~~
.. include:: /datasets/linkstation.rst

.. _bluetooth-dataset:

|idgb|\ bluetooth
~~~~~~~~~~~~~~~~~
.. include:: /datasets/bluetooth.rst
    
.. _weather-dataset:

|idgb|\ weather
~~~~~~~~~~~~~~~
.. include:: /datasets/weather.rst

.. _environment-dataset:

|idgb|\ environment
~~~~~~~~~~~~~~~~~~~
.. include:: /datasets/environment.rst

.. _parking-dataset:

|idgb|\ parking
~~~~~~~~~~~~~~~
.. include:: /datasets/parking.rst

.. _trafficstation-dataset:

|idgb|\ trafficstation
~~~~~~~~~~~~~~~~~~~~~~
.. include:: /datasets/trafficstation.rst

.. rubric:: Mobility
   
.. _carsharing-dataset:

|idgb|\ carsharing
~~~~~~~~~~~~~~~~~~
.. include:: /datasets/carsharing.rst

.. _carpoolinghub-dataset:

|idgb|\ carpoolinghub
~~~~~~~~~~~~~~~~~~~~~
.. include:: /datasets/carpoolinghub.rst

.. _bikesharing-dataset:

|idgb|\ bikesharing
~~~~~~~~~~~~~~~~~~~
.. include:: /datasets/bikesharing.rst

.. _echarging-dataset:

|idgb|\ echargingstation
~~~~~~~~~~~~~~~~~~~~~~~~
.. include:: /datasets/ecs.rst

.. _sasabus-dataset:

Public Transportation
~~~~~~~~~~~~~~~~~~~~~
.. include:: /datasets/sasa.rst

.. _noiplace-dataset:

NOI-Place
~~~~~~~~~
.. include:: /datasets/noiplace.rst

.. _creative-industries-dataset:

Creative Industries
~~~~~~~~~~~~~~~~~~~
.. include:: /datasets/creativeindustries.rst


.. _tourism-datasets:

Datasets in the Tourism Domain
------------------------------

.. contents:: List of datasets in the tourism domain.
   :local:

The following information is provided
for each of the above-listed dataset:

* The output format of the API call.
* An e-mail contact for the dataset.
* The versions of the API that can be used to access the dataset.
* The swagger URL of the APIs.

.. note:: There is one :literal:`StationType`, namely :strong:`MobileStation` which
   is a mobile probe no longer active. It will always return an empty
   set of values, because historical data are not available in the |odh|\.
  
.. _accommodation-dataset:

|lts|\ accommodation
~~~~~~~~~~~~~~~~~~~~
.. include:: /datasets/accommodation.rst

.. _package-dataset:

it.hgv.package
~~~~~~~~~~~~~~
.. include:: /datasets/package.rst

.. _poi-dataset:

|lts|\ poi
~~~~~~~~~~
.. include:: /datasets/poi.rst

.. _activity-dataset:

|lts|\ activity
~~~~~~~~~~~~~~~
.. include:: /datasets/activity.rst

.. _event-dataset:

|lts|\ event
~~~~~~~~~~~~
.. include:: /datasets/event.rst

.. _activity_poi-dataset:

|lts|\ activity_poi
~~~~~~~~~~~~~~~~~~~
.. include:: /datasets/activity_poi.rst
	     
.. _gastronomy-dataset:

|lts|\ gastronomy
~~~~~~~~~~~~~~~~~
.. include:: /datasets/gastronomy.rst

.. _location-dataset:

|idgb|\ location
~~~~~~~~~~~~~~~~
.. include:: /datasets/location.rst

.. _ski-dataset:

|idgb|\ ski
~~~~~~~~~~~
.. include:: /datasets/ski.rst

.. _snowreport-dataset:

|idgb|\ snowreport
~~~~~~~~~~~~~~~~~~
.. include:: /datasets/snowreport.rst
	     
.. _webcam-dataset:

|idgb|\ webcam
~~~~~~~~~~~~~~
.. include:: /datasets/webcam.rst
	     
.. _weather-siag-dataset:

|idgb|\ weather-siag
~~~~~~~~~~~~~~~~~~~~
.. include:: /datasets/weather-siag.rst
	     
.. _siag.weather-dataset:

|idsiag|\ weather
~~~~~~~~~~~~~~~~~
.. include:: /datasets/siag.weather.rst

.. _museum-dataset:

|idsiag|\ museum
~~~~~~~~~~~~~~~~
.. include:: /datasets/museum.rst

