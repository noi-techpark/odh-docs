
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
   
.. note:: This page was last updated on |today| and all information
   about the availability of datasets is correct as of this date. This
   page will be updated in due time as soon as more material will be
   made available.

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
~~~~~~~~~~~~~~

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
currently offer only a list of data providers whose data can be pulled
from |odh|\. Indeed, an |odh| dataset can be composed of data deriving
from different providers, while a provider can submit to |odh|
multiple types of data that will belong to more than one dataset.

The |odh|\'s Data Providers are:

* IDM Südtirol/Alto Adige.
* SIAG, Südtirol Informatica AG - Informatica Alto Adige.
* SASA, public transport operator.
* Alperia, energy provider for South Tyrol.
* Municipality of Bolzano.
* Municipality of Merano.
* Carsharing Alto Adige.
* DB rent.
* LTS, South Tyrol Association of Tourism Organisations.
* APPA, South Tyrolean agency for the environment.
* InnoVie.
* Südtirol Wein.
 
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

At the date ow writing, only datasets about the Mobility and Tourism
domains are available; the available datasets in each domain are
listed below.

.. _mobility-datasets:

Datasets in the Mobility Domain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. contents:: List of datasets in the mobility domain.
   :local:

In this section, the following information is provided for each of
the above-listed dataset:

* The output format of the API call.
* An e-mail contact for the dataset.
* The versions of the API that can be used to access the dataset.
* The swagger URL of the APIs.


.. _weather-dataset:
.. include:: /datasets/weather.rst

.. _environment-dataset:
.. include:: /datasets/environment.rst

.. _parking-dataset:
.. include:: /datasets/parking.rst

.. _bluetooth-dataset:
.. include:: /datasets/bluetooth.rst

.. _trafficstation-dataset:
.. include:: /datasets/trafficstation.rst

.. _linkstation-dataset:
.. include:: /datasets/linkstation.rst

.. _streetelement-dataset:
.. include:: /datasets/streetelements.rst


.. _rwisstation-dataset:
.. include:: /datasets/rwisstation.rst

.. _carsharing-dataset:
.. include:: /datasets/carsharing.rst

.. _bikesharing-dataset:
.. include:: /datasets/bikesharing.rst

.. _echarging-dataset:

|idgb|\ echargingstation
------------------------

.. include:: /datasets/ecs.rst


.. _carpoolinghub-dataset:
.. include:: /datasets/carpoolinghub.rst

.. _sasabus-dataset: 
.. include:: /datasets/sasa.rst


.. _tourism-datasets:

Datasets in the Tourism Domain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. contents:: List of datasets in the tourism domain.
   :local:

Like in the previous section, the following information is provided
for each of the above-listed dataset:

* The output format of the API call.
* An e-mail contact for the dataset.
* The versions of the API that can be used to access the dataset.
* The swagger URL of the APIs.


.. _accommodation-dataset:
.. include:: /datasets/accommodation.rst

.. _package-dataset:
.. include:: /datasets/package.rst

.. _poi-dataset:
.. include:: /datasets/poi.rst

.. _activity-dataset:
.. include:: /datasets/activity.rst

.. _event-dataset:
.. include:: /datasets/event.rst

.. _activity_poi-dataset:
.. include:: /datasets/activity_poi.rst
	     
.. _gastronomy-dataset:
.. include:: /datasets/gastronomy.rst

.. _location-dataset:
.. include:: /datasets/location.rst

.. _ski-dataset:
.. include:: /datasets/ski.rst

.. _snowreport-dataset:
.. include:: /datasets/snowreport.rst
	     
.. _webcam-dataset:
.. include:: /datasets/webcam.rst
	     
.. _weather-siag-dataset:
.. include:: /datasets/weather-siag.rst
	     
.. _siag.weather-dataset:
.. include:: /datasets/siag.weather.rst

.. _museum-dataset:
.. include:: /datasets/museum.rst

