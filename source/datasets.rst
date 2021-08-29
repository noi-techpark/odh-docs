.. _available_datasets:

Datasets
========

.. versionadded:: 2021.02 |odh| Virtual Knowledge Graph and
   description of underlying Knowledge Model

.. versionchanged:: 2021.05 moved technical information for tourism
   and mobility to this section

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

.. toctree::
   :hidden:

   Technical Information <mobility-tech>
     
This section contains :ref:`technical information <mobility-tech>`
about the datasets in the Mobility Domain and how to access them using
the API that the Open Data Hub team developed and made available.

.. figure:: /images/Mobility-domain.png
   :align: center

   The dataset in the Mobility Domain at a glance.

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
   "Sources", "The list of Data Providers whose data compose the
   dataset"

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

:bdg-link-light:`bluetooth-dataset,it.bz.opendatahub.bluetooth`

.. include:: /datasets/bluetooth.rst

.. _environment-dataset:

:bdg-link-light:`environment-dataset,it.bz.opendatahub.environment`
            
.. include:: /datasets/environment.rst
                         
.. _linkstation-dataset:

:bdg-link-light:`linkstation-dataset,it.bz.opendatahub.linkstation`

.. include:: /datasets/linkstation.rst

.. _parking-dataset:

:bdg-link-light:`parking-dataset,it.bz.opendatahub.parking`

.. include:: /datasets/parking.rst

.. _rwisstation-dataset:

:bdg-link-light:`rwisstation-dataset,it.bz.opendatahub.rwisstation`

.. include:: /datasets/rwisstation.rst

.. _streetelement-dataset:

:bdg-link-light:`streetelement-dataset,it.bz.opendatahub.streetelements`

.. include:: /datasets/streetelements.rst

.. _trafficstation-dataset:

:bdg-link-light:`trafficstation-dataset,it.bz.opendatahub.trafficstation (1)`

.. include:: /datasets/trafficstation.rst

.. _trafficstation-vms-dataset:

:bdg-link-light:`trafficstation-vms-dataset,it.bz.opendatahub.trafficstation (2)`

.. include:: /datasets/trafficstation-vms.rst

.. _weather-dataset:

:bdg-link-light:`weather-dataset,it.bz.opendatahub.weather`

.. include:: /datasets/weather.rst

Mobility
~~~~~~~~

The Mobility/Mobility sub-domain contains data about public
transportation, sharing of transport means, and recharging stations
for e-cars.

.. _bikesharing-dataset:

:bdg-link-light:`bikesharing-dataset,it.bz.opendatahub.bikesharing`

.. include:: /datasets/bikesharing.rst

.. _carpoolinghub-dataset:

:bdg-link-light:`carpoolinghub-dataset,it.bz.opendatahub.carpoolinghub`

.. include:: /datasets/carpoolinghub.rst

.. _carsharing-dataset:

:bdg-link-light:`carsharing-dataset,it.bz.opendatahub.carsharing`

.. include:: /datasets/carsharing.rst

.. _echarging-dataset:

:bdg-link-light:`echarging-dataset,it.bz.opendatahub.echargingstation`

.. include:: /datasets/ecs.rst

.. _sasabus-dataset:

:bdg-link-light:`sasabus-dataset,Public Transportation` |deprecated|

.. include:: /datasets/publictransportation.rst

.. _tourism-datasets:

Datasets in the Tourism Domain
------------------------------

.. versionchanged:: 2021.06 modified URLs of datasets and API; ordered
   Tourism datasets lexicographically

.. toctree::
   :hidden:

   Technical Information <tourism-tech>


This section contains :ref:`technical information <tourism-tech>`
about the dataset in the Tourism Domain and how to access them using
the API that the Open Data Hub team developed and made available.

.. figure:: /images/Tourism-domain.png
   :align: center

   The dataset in the Tourism Domain at a glance.

Datasets presented here are related to all kind of touristic
activities in South Tyrol. By exploring this domain, it is possible to
find information about winter and summer offers from local touristic
boards, information about weather, hotels and accommodation, Points of
Interests, and a lot more.

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
   "Sources", "The list of Data Providers whose data compose the
   dataset"
   "SPARQL Endpoint", "Dataset is accessible through the `SPARQL
   Endpoint <https://sparql.opendatahub.bz.it>`_ [#]_"

.. [#] This information is provided only if the dataset is accessible
   through SPARQL.

.. seealso:: The following howto will help you access data in the
   Tourism domain:

    :doc:`/howto/tourism/getstarted` Access and technical details
    about the available data

    :doc:`/howto/tourism/browse` Browse Open Data offered by the |odh|
   
    :doc:`/howto/tourism/tips` Quick tips and troubleshooting
	 
    Other howtos are available in the :ref:`dedicated section <howto-list>`.
   
.. _accommodation-dataset:

:bdg-link-light:`accommodation-dataset,it.bz.opendatahub.accommodation`

.. include:: /datasets/accommodation.rst

.. _activity-dataset:

:bdg-link-light:`activity-dataset,it.bz.opendatahub.activity`

.. include:: /datasets/activity.rst

.. _activity_poi-dataset:

:bdg-link-light:`activity_poi-dataset,it.bz.opendatahub.activity_poi`

.. include:: /datasets/activity_poi.rst

.. _common-dataset:

:bdg-link-light:`common-dataset,it.bz.opendatahub.common`

.. include:: /datasets/common.rst

.. _event-dataset:

:bdg-link-light:`event-dataset,it.bz.opendatahub.event`

.. include:: /datasets/event.rst

.. _eventshort-dataset:

:bdg-link-light:`eventshort-dataset,it.bz.opendatahub.eventshort`

.. include:: /datasets/eventshort.rst

.. _gastronomy-dataset:

:bdg-link-light:`gastronomy-dataset,it.bz.opendatahub.gastronomy`

.. include:: /datasets/gastronomy.rst

.. _location-dataset:

:bdg-link-light:`location-dataset,it.bz.opendatahub.location`

.. include:: /datasets/location.rst

.. _package-dataset:

:bdg-link-light:`package-dataset,it.bz.opendatahub.package`

.. include:: /datasets/package.rst

.. _poi-dataset:

:bdg-link-light:`poi-dataset,it.bz.opendatahub.poi`

.. include:: /datasets/poi.rst

.. _ski-dataset:

:bdg-link-light:`ski-dataset,it.bz.opendatahub.ski`

.. include:: /datasets/ski.rst

.. _snowreport-dataset:

:bdg-link-light:`snowreport-dataset,it.bz.opendatahub.snowreport`

.. include:: /datasets/snowreport.rst

.. _venue-dataset:

:bdg-link-light:`venue-dataset,it.bz.opendatahub.venue`

.. include:: /datasets/venue.rst

.. _weather-forecast-dataset:

:bdg-link-light:`weather-forecast-dataset,it.bz.opendatahub.weather-forecast`

.. include:: /datasets/weather-forecast.rst

.. _webcam-dataset:

:bdg-link-light:`webcam-dataset,it.bz.opendatahub.webcam`

.. include:: /datasets/webcam.rst

.. _other-domains-datasets:

Datasets in Other Domains
-------------------------

.. _creative-industries-dataset:

:bdg-link-light:`creative-industries-dataset,Creative Industries`

.. include:: /datasets/creativeindustries.rst

.. _noiplace-dataset:

:bdg-link-light:`noiplace-dataset,NOI-Place`

.. include:: /datasets/noiplace.rst

.. _alpinebits-dataset:

:bdg-link-light:`alpinebits-dataset,https\://alpinebits.opendatahub.bz.it/AlpineBits`

.. include:: /datasets/alpinebits.rst

.. odh vkg km
   
.. include:: /includes/kg.rst

