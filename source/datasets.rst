.. _available_datasets:

Datasets
========

.. versionadded:: 2020.09 New domain category `Other`, which includes
   dataset that do not belong to existing domains

.. versionadded:: 2020.09 New description of domains, new diagrams
   that show the datasets encompassed in each domain

.. versionadded:: 2020.10 Information about licensing of data
   contained in the |ODH| responses

.. versionadded:: 2020.10 Links from the dataset lists to the howto
   section

.. versionadded:: 2021:01 access to data using R

The goal of the Open Data Hub project is to make available datasets containing
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

.. versionchanged:: 2020.09 Updated the list of data providers

A :strong:`Data Provider` is any entity that shares their Open Data
with the Open Data Hub project, allowing their free reuse (ideally under a
free licence like |cc0| or |bysa|) from any third-party that relies on
the Open Data Hub to build their application. These entities can be private
companies or enterprises, public bodies, and even private citizen, if
they have interesting data about South Tyrol to share.

The Open Data exposed by the Open Data Hub originate from data and datasets
owned by different actors (called :strong:`Data Providers`) which are
at this time mostly local public bodies. Since there is no direct
1-to-1 correspondence between Data Providers and datasets, we
currently offer a list of data providers whose data can be pulled
from Open Data Hub\. Indeed, an Open Data Hub dataset can be composed of data deriving
from different providers, while a provider can submit to Open Data Hub
multiple types of data that will belong to more than one dataset.

The Open Data Hub\'s Data Providers are:

* :strong:`Autostrada del Brennero/Brennerautobahn` management of the
  A22 motorway infrastructure
* :strong:`Alperia/Neogy` energy provider for South Tyrol
* :strong:`APPA Bolzano` South Tyrolean agency for the environment
* :strong:`APPA Trento` Trentino Agency of the environment
* :strong:`Bezirksgemeinschaft Burggrafenamt Comunità Comprensoriale
  Burgraviato`
* :strong:`Carsharing Alto Adige` via its technological partner DB
  Rent
* :strong:`CISMA` bluetooth sensors
* :strong:`IDM Südtirol/Alto Adige` trailblazer for economic
  development in South Tyrol
* :strong:`H2 Südtirol Alto Adige` energy company
* :strong:`HGV Hoteliers- und Gastwirteverband`
* :strong:`Inno.vìe` mobility solutions
* :strong:`LTS South Tyrol` Association of Tourism Organisations
* :strong:`Municipality of Bolzano`
* :strong:`Municipality of Merano`
* :strong:`Municipality of Rovereto`
* :strong:`Municipality of Trento`
* :strong:`NOI Techpark` technology and science park of South Tyrol
* :strong:`Route220`, :strong:`Nevicam` and :strong:`Driwe` e-charging
  stations provider
* :strong:`SASA` public transport operator
* :strong:`SIAG` Südtirol Informatica AG - Informatica Alto Adige
* :strong:`Südtirol Wein - Vini Alto Adige` consortium of South Tyrol
  Wines

.. topic:: A note about datasets

   The Open Data Hub contains many datasets: a few have been provided for
   testing purposes, other are meant for internal use only, and other
   contain only a part of their data that is available as Open Data.

   While the goal of the Open Data Hub project is to expose :strong:`only Open
   Data` and the Open Data Hub team members always suggest to use |CC0| to
   third-parties releasing datasets, it is not yet possible for the
   Open Data Hub team to guarantee the availability as open data of all the
   data in the datasets, because the data licensing and its
   distribution rights are decided by the copyright holder of each
   dataset.

   Since some of the datasets may contain data that can not be
   distributed by the Open Data Hub team under an open licence like, e.g.,
   |cc0| or |bysa|, a user will be able to retrieve from each dataset
   only those data that are distributed as :strong:`Open Data`.

At the date of writing, datasets in the :ref:`Mobility
<mobility-datasets>` and :ref:`Tourism <tourism-datasets>` domains are
available.

Accessing data in the Open Data Hub
-----------------------------------

There are different modalities to access data that are provided by the
Open Data Hub, that are listed here. Currently, data from the
:strong:`Mobility` and :strong:`Tourism` domains can be accessed, both
from the command line and using a browser. Non-interactive access
using APIs is also available.  Various dedicated tutorials are
available in the :ref:`howto-list` section; while in section
:ref:`getting-involved` you can find additional ways to interact with
the data and the Open Data Hub team. The remainder of this section describes
all the possibilities to access the Open Data Hub's datasets and their
content.

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

=== ============  =============
API  Tourism      Mobility
=== ============  =============
v1   Recommended   Deprecated
v2   --            Recommended
=== ============  =============


There are currently two versions of the API, v1 and v2, with the
former now :strong:`deprecated` for the Mobility domain and marked as
such |deprecated| throughout the Open Data Hub documentation. New users are
recommended to use the new API v2, while users of the API v1 are
encouraged to plan a migration to the new API.

The new API v2 has a different approach compared to the previous
version, and therefore is not compatible with the API v1, the main
difference being that all data stored in the Open Data Hub can now be
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

Accessing data in the Open Data Hub by using a browser is useful on different
levels: for the casual user, who can have a look at the type and
quality of data provided; for a developer, that can use the
:term:`REST API` implemented by the Open Data Hub or even check if the results
of his app are coherent with those retrieved with the API; for
everyone in order to get acquainted with the various methods to
retrieve data.

More in detail, these are the possibilities to interact with Open Data Hub's
data by using a browser:

#. Go to the :ref:`applist` section of the documentation, particularly
   sub-sections :ref:`production-stage-apps` and
   :ref:`beta-stage-apps`, and choose one of the web sites and portals
   that are listed there. Each of them uses the data gathered from one
   or more OPEN DATA HUB's datasets to display a number of useful
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
   Mobility domain, located at
   https://mobility.api.opendatahub.bz.it/. Like in the case of the
   tourism' Swagger interface, you can learn REST API call for that
   domain and fetch data for your application. More possibilities to
   interact with the Mobility domain datasets and the description of
   the new APIv2 are described in the :ref:`dedicated howto
   <get-started-mobility>`.

#. Open the :strong:`Analytics for Mobility` web page, at
   https://analytics.opendatahub.bz.it/ This portal uses data in the
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
from Open Data Hub's dataset is limited, usually they are not more than 3 or
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
<https://mobility.api.opendatahub.bz.it/>`_
domains and execute a query: with the output, also the corresponding
:program:`curl` command used to retrieve the data will be shown.

.. _r-access:

Statistical Access with R
~~~~~~~~~~~~~~~~~~~~~~~~~

`R <https://www.r-project.org/>`_ is a free software for statistical
analysis that creates also graphics from the gathered data.

The Open Data Hub Team has developed and made available `bzar
<https://github.com/noi-techpark/it.bz.opendatahub.analytics.libs/tree/main/api/R>`_,
an R package that can be used to access `BZ Analytics
<https://analytics.opendatahub.bz.it/>`_ data (see also
:ref:`bz-analytics`) and process them using all the R
capabilities. Download and installation instructions, along with
example usage can be found on the `bzar repository
<https://github.com/noi-techpark/it.bz.opendatahub.analytics.libs/tree/main/api/R>`_.

.. _license-json-records:

License of the JSON Responses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Whenever you query the data in the |odh|\, the snippet that you
retrieve always includes a block of information called
:literal:`LicenseInfo`, similar to the following one:

.. code-block:: json
   :linenos:
   :emphasize-lines: 3

   {
      "LicenseInfo": {
        "Author": "",
	"License": "CC0",
	"ClosedData": false,
	"LicenseHolder": "https://www.lts.it"
      }
   }

The highlighted line shows a licence, which in this case is
:strong:`CC0`, i.e., public domain and therefore freely reusable.

This block is always included as a child node within a JSON record
that starts with an ID and a number of additional information, which
may include also hyperlinks to resources that are external to the
|odh|\, like for example this example which refers to a webcam and
contains a link to an external provider where to find actual images
from that webcam (snippet code shortened for the sake of simplicity):

.. code-block:: json
   :linenos:
   :emphasize-lines: 4-5

   {
     "Id": "D3659E1F111C4CDB2EC19F8FC95118B7",
     "Active": true,
     "Streamurl": null,
     "Webcamurl": "https://webtv.feratel.com/webtv/?&pg=5EB12424-7C2D-428A-BEFF-0C9140CD772F&design=v3&cam=6323&c1=0",
     "LicenseInfo": {
       "Author": "",
       "License": "CC0",
       "ClosedData": false,
       "LicenseHolder": "https://www.lts.it"
     }
   }

Whenever hyperlinks like the one shown in line :strong:`5` above
appear, it must not be implied that the license mentioned in the
:literal:`LicenseInfo` block (again, CC0) is applied to them:
everything contained in that link may be covered by a different
licence.

Indeed, the :strong:`Licence` mentioned in :literal:`LicenseInfo`
nodes refer only to content of the parent node--i.e., the one that
starts with :strong:`"Id"`, not to the content of any of the other
children nodes, including :literal:`Streamurl` and
:literal:`Webcamurl`.

Authentication
~~~~~~~~~~~~~~

The authentication layer is currently intended for :strong:`internal
use only`. All data in the dataset that you can receive from the Open Data Hub
are free to use and do not require any type of authentication.


The authentication layer can be of interest for developers who want to
collaborate in the development of Open Data Hub; Details on the implementation
are available in section :ref:`authentication-hub`.

.. _mobility-datasets:

Datasets in the Mobility Domain
-------------------------------

.. versionchanged:: 2020.06 Direct link to the browsable version of
   the datasets.

.. versionchanged:: 2020.09 Improved description of datasets in the
   mobility domain, including external links, use cases, and Data
   Providers.

.. versionchanged:: 2020.09 added dropdowns to the list of datasets to
   improve usability
   
.. figure:: /images/Mobility-domain.png
   :align: right
   :scale: 120 %

   The dataset in the Mobility Domain at a glance.

This section contains information about the datasets in the Mobility
Domain and how to access them using the API that the Open Data Hub
team developed and made available.

.. note:: Recall that the API v1 for the Mobility Domain is now :strong:`deprecated`.

The description of each dataset includes the following information:

.. csv-table::

   "Output", "The output format of the API call"
   "E-mail contact", "An e-mail contact for the dataset"
   "API version", "The versions of the API that can be used to access
   dataset"
   ":literal:`StationType`", "The direct link to each
   :literal:`stationType` included in the dataset"
   "Use cases and info", "Link to web sites that use the dataset and to
   use cases based on the dataset"
   "Web component", "Link to Web Components developed on top of the
   dataset (optional)"
   "Sources", "The list of Data Providers whose data compose the dataset"

.. note:: There is one :literal:`StationType`, namely
   :strong:`MobileStation` which is a mobile probe no longer
   active. It will always return an empty set of values, because
   historical data are not available in the Open Data Hub.			   

The datasets in the Mobility domain are grouped in :strong:`Traffic`
and :strong:`Mobility` sub-domains as follows:

.. seealso:: The following howto will help you access data in the
   Mobility domain:

    :doc:`/howto/mobility/getstarted` Access and technical details about the available data

    Other howtos are available in the :ref:`dedicated section <howto-list>`.

Traffic
~~~~~~~

The Mobility/Traffic sub-domain contains data about traffic (like e.g., real time
traffic load of a street, environmental measurement) that are useful
to plan a trip with an own means of transport, for example a car, or a bike.

.. _bluetooth-dataset:

.. dropdown:: :strong:`it.bz.opendatahub.bluetooth`

   .. include:: /datasets/bluetooth.rst

.. _environment-dataset:

.. dropdown:: :strong:`it.bz.opendatahub.environment`

   .. include:: /datasets/environment.rst

.. _linkstation-dataset:

.. dropdown:: :strong:`it.bz.opendatahub.linkstation`

   .. include:: /datasets/linkstation.rst

.. _parking-dataset:

.. dropdown:: :strong:`it.bz.opendatahub.parking`
   :animate: fade-in-slide-down

   .. include:: /datasets/parking.rst

.. _rwisstation-dataset:

.. dropdown:: :strong:`it.bz.opendatahub.rwisstation`

   .. include:: /datasets/rwisstation.rst

.. _streetelement-dataset:

.. dropdown:: :strong:`it.bz.opendatahub.streetelements`

   .. include:: /datasets/streetelements.rst

.. _trafficstation-dataset:

.. dropdown:: :strong:`it.bz.opendatahub.trafficstation (1)`

   .. include:: /datasets/trafficstation.rst

.. _trafficstation-vms-dataset:

.. dropdown:: :strong:`it.bz.opendatahub.trafficstation (2)`

   .. include:: /datasets/trafficstation-vms.rst

.. _weather-dataset:

.. dropdown:: :strong:`it.bz.opendatahub.weather`

   .. include:: /datasets/weather.rst

Mobility
~~~~~~~~

The Mobility/Mobility sub-domain contains data about public
transportation, sharing of transport means, and recharging stations
for e-cars.

.. versionchanged:: 2020.09 Improved description of datasets in the
   mobility/mobility domain, including new information

.. deprecated:: 2020.10 Public Transportation dataset

.. _bikesharing-dataset:

.. dropdown:: :strong:`it.bz.opendatahub.bikesharing`

   .. include:: /datasets/bikesharing.rst

.. _carpoolinghub-dataset:

.. dropdown:: :strong:`it.bz.opendatahub.carpoolinghub`

   .. include:: /datasets/carpoolinghub.rst

.. _carsharing-dataset:

.. dropdown:: :strong:`it.bz.opendatahub.carsharing`

   .. include:: /datasets/carsharing.rst

.. _echarging-dataset:

.. dropdown:: :strong:`it.bz.opendatahub.echargingstation`

   .. include:: /datasets/ecs.rst

.. _sasabus-dataset:

.. dropdown:: :strong:`Public Transportation` |deprec|

   .. include:: /datasets/publictransportation.rst

.. _tourism-datasets:

Datasets in the Tourism Domain
------------------------------

.. figure:: /images/Tourism-domain.png
   :align: right
   :scale: 120 %

   The dataset in the Tourism Domain at a glance.


This section contains information about the dataset in the Tourism
Domain and how to access them using the API that the Open Data Hub
team developed and made available.

Datasets presented here are related to all kind of touristic
activities in South Tyrol. By exploring this domain, it is possible to
find information about winter and summer offers from local touristic
boards, information about weather, hotels and accommodation, Points of
Interests, and a lot more.

.. versionchanged:: 2020.09 Removed datasets not offered directly from
   Open Data Hub (siag.museum and siag.weather)

.. versionchanged:: 2020.09 Renamed weather-siag dataset to
   weather-forecast

.. versionchanged:: 2020.09 Ordered datasets in alphabetical order

.. versionadded:: 2020.09 Added article, common, venue and eventshort datasets

.. versionchanged:: 2020.10 Changed identifier of datasets activity,
   event, gastronomy, package, and POI

.. versionadded:: 2020.10 API URL for all Tourism datasets.

The following information is provided for each dataset in the Tourism domain:

.. csv-table::

   "Output", "The output format of the API call"
   "E-mail contact", "An e-mail contact for the dataset"
   "API version", "The versions of the API that can be used to access
   the dataset"
   "Swagger URL", "The URL of the swagger interface to the data"
   "API URL", "The URL of the browsable version of the dataset"
   "Use cases and info", "Link to web sites that use the dataset and
   to use cases based on the dataset"
   "Android App", "Link to app for mobile phones developed using the
   data in the dataset"
   "Sources", "The list of Data Providers whose data compose the dataset"

.. seealso:: The following howto will help you access data in the
   Tourism domain:

    :doc:`/howto/tourism/getstarted` Access and technical details
    about the available data

    :doc:`/howto/tourism/browse` Browse Open Data offered by the |odh|
   
    :doc:`/howto/tourism/tips` Quick tips and troubleshooting
	 
    Other howtos are available in the :ref:`dedicated section <howto-list>`.
   
.. _package-dataset:

.. dropdown:: :strong:`it.bz.opendatahub.package`

   .. include:: /datasets/package.rst

.. _activity-dataset:

.. dropdown:: :strong:`it.bz.opendatahub.activity`

   .. include:: /datasets/activity.rst

.. _event-dataset:

.. dropdown:: :strong:`it.bz.opendatahub.event`

   .. include:: /datasets/event.rst

.. _gastronomy-dataset:

.. dropdown:: :strong:`it.bz.opendatahub.gastronomy`

   .. include:: /datasets/gastronomy.rst

.. _poi-dataset:

.. dropdown:: :strong:`it.bz.opendatahub.poi`

   .. include:: /datasets/poi.rst

.. _accommodation-dataset:

.. dropdown:: :strong:`it.bz.opendatahub.accommodation`

   .. include:: /datasets/accommodation.rst

.. _activity_poi-dataset:

.. dropdown:: :strong:`it.bz.opendatahub.activity_poi`

   .. include:: /datasets/activity_poi.rst

.. _common-dataset:

.. dropdown:: :strong:`it.bz.opendatahub.common`

   .. include:: /datasets/common.rst

.. _eventshort-dataset:

.. dropdown:: :strong:`it.bz.opendatahub.eventshort`

   .. include:: /datasets/eventshort.rst

.. _location-dataset:

.. dropdown:: :strong:`it.bz.opendatahub.location`

   .. include:: /datasets/location.rst

.. _ski-dataset:

.. dropdown:: :strong:`it.bz.opendatahub.ski`

   .. include:: /datasets/ski.rst

.. _snowreport-dataset:

.. dropdown:: :strong:`it.bz.opendatahub.snowreport`

   .. include:: /datasets/snowreport.rst

.. _venue-dataset:

.. dropdown:: :strong:`it.bz.opendatahub.venue`

   .. include:: /datasets/venue.rst

.. _weather-forecast-dataset:

.. dropdown:: :strong:`it.bz.opendatahub.weather-forecast`

   .. include:: /datasets/weather-forecast.rst

.. _webcam-dataset:

.. dropdown:: :strong:`it.bz.opendatahub.webcam`

   .. include:: /datasets/webcam.rst


Datasets in Other Domains
-------------------------

.. _creative-industries-dataset:

Creative Industries
~~~~~~~~~~~~~~~~~~~
.. include:: /datasets/creativeindustries.rst

.. _noiplace-dataset:

NOI-Place
~~~~~~~~~
.. include:: /datasets/noiplace.rst

.. _alpinebits-dataset:

https\://alpinebits.opendatahub.bz.it/AlpineBits
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. include:: /datasets/alpinebits.rst
