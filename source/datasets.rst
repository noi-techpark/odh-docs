Datasets
========


The goal of the |odh| Project is to make available datasets containing
data about the South Tyrolean Ecosystem, to allow third parties to
develop novel applications on top of them, consuming the exposed
data. These applications may range from a simple processing of
datasets to extract statistical data and to display the result in
different graphic formats like pie-charts, to far more complex
applications that combine data from different datasets and correlate
them in some useful way.

.. note:: This page was last updated on |today|, hence all information
   about the availability of datasets is correct as of this date. This
   page will be updated in due time as soon as more material will be
   made available.

   This page will be soon removed, as all the information statically
   provided here will be in the near future be replaced by :ref:`the
   broker service <broker>`, which dynamically maintains the list.

As seen in :numref:`domains`, data originate from different
domains (Mobility, Tourism, and so on); they are gathered from sensors
and packed within :strong:`datasets`. `Sensors` can be for example GPS
devices installed on buses that send their real-time geographic
position or a small electronic device on a plug of an e-charging
station that checks the if the plug is being used or not, to let
people know that the charging outlet is available.

.. topic:: A note about datasets.

   At the time of writing, only a few datasets are published. As
   mentioned before in this section, the goal is to expose datasets
   containing :strong:`only Open Data`, which is at the moment not the
   case for all datasets. Indeed, some of the datasets contain data
   that can not be distributed under an open licence like, e.g., |cc0|
   or |bysa|. Therefore, to allow the highest possible data to be
   shared, an authentication mechanism has been implemented, to
   prevent access to the data in the datasets that has not yet been
   published as |od|\.

   Datasets which require authentication are marked with the |auth|
   badge. If you are interested in accessing closed data, you can try
   to contact the dataset owner or express your interest to the |odh|
   team.

   Please refer to section :ref:`authentication` for details.

For each domain the available datasets are listed. Please refer to the
next sections for a complete list. 

.. _mobility-datasets:

Datasets in the Mobility Domain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. contents:: List of datasets in the mobility domain.
   :local:

In this section, the following information are provided for each of
the above-listed dataset:

* The licence of the data present in the dataset.
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

Like in the previous section, the following information are provided
for each of the above-listed dataset:

* The licence of the data present in the dataset.
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

.. _broker:

The Broker
~~~~~~~~~~

The |ODH| Broker is a recently introduced online service
(November 2018) that gives an overview and quick access of the
datasets available within the |odh| project.

The service is accessible at the URL https://api.opendatahub.bz.it and
consists of a web page, divided in two parts:

* The :strong:`list of datasets` accessible through the broker, which
  are all the datasets containing publicly accessible data. This list
  is dynamically created when the page is loaded, therefore is is
  always up to date. Each dataset can be clicked to open a panel with
  additional information about it.

* An overview of the :strong:`REST API` provided by the broker, a few
  methods that allow to query the existing datasets. Results are in
  `JSON-LD <https://json-ld.org/>`_ format and use the `DCAT
  vocabulary <https://www.w3.org/TR/vocab-dcat/>`_. This means that all
  the keyword in the result set belong to a W3C standard, allowing the
  data in the result set to be reused and combined with results from
  foreign datasets that use the same vocabulary.

The results obtained by querying the broker give a number of metadata
about one or more datasets, including the :strong:`Contact` for
information or reuse of the dataset, and the :strong:`Base URL`,
allowing for quick and direct access to the data, using the ODH APIs,
described in the :strong:`Documentation` URL.

.. note:: While the :strong:`Base URL`, when accessed, may give an
   error, the API calls work and produce correct results. For example,
   consider the :strong:`it.bz.opendatahub.echargingstation`
   dataset. Calling the method :strong:`get-station-details` by using
   its base URL,
   https://api.opendatahub.bz.it/it.bz.opendatahub.echargingstation,
   actually produce the expected result, i.e., the list of stations
   in the dataset with all the information attached to it:

   .. parsed-literal::

      curl
      "https://api.opendatahub.bz.it/it.bz.opendatahub.echargingstation/rest/get-station-details"
      | jq '.' | head -10

      [
        {
	  "_t": "it.bz.idm.bdp.dto.emobility.EchargingStationDto",
	  "id": "ASD_00000038",
	  "name": "CAMPING_LATSCH",
	  "latitude": 46.622135,
	  "longitude": 10.863569,
	  "municipality": "Latsch - Laces",
	  "capacity": 1,
	  "provider": "Alperia Smart Mobility",


Broker's REST API
-----------------

The methods available are the following.
    
* :literal:`GET /datasets` Returns a list of all datasets in form of a
  :strong:`dcat:Catalog`.

 
* :literal:`GET /datasets/{id}` Retrieve the metadata of a single
  dataset by its identifier, which corresponds to the
  :strong:`identifier` key that you can find in the in the outcome of
  the previous method's call. See also the excerpt below. The result
  set is a :strong:`dcat:Dataset`\.
  
* :literal:`GET /datasets/search/{query}` Execute a custom, case
  insensitive query on the available datasets. All the fields within
  the result set of the :literal:`GET /datasets` query will be
  considered for an answer. Multiple words can be used as query string.
  
The outcome of the query looks like the following excerpt which is, as
mentioned in the previous section in JSON-LD format and uses the
standard DCAT vocabulary. 

.. parsed-literal::

   {
      "title": "it.bz.opendatahub.echargingstation",
      "publisher": {
        "title": "Alperia, route220, Nevicam, Driwe",
        "@type": "http:\/\/www.w3.org\/ns\/org#Organization",
        "@context": {
          "title": "http:\/\/purl.org\/dc\/terms\/title"
        }
      },
      "keyword": [
        "echarging",
        "mobility",
        "realtime"
      ],
      "identifier": "it.bz.opendatahub.echargingstation",
      "distribution": [
        {
          "license": "https:\/\/creativecommons.org\/publicdomain\/zero\/1.0\/",
          "format": "application\/json",
          "accessURL": "https:\/\/api.opendatahub.bz.it\/it.bz.opendatahub.echargingstation",
          }
        }
      ],
      "description": "Real time information about the echarging statons",
      "contactPoint": {
        "hasEmail": "info@geobank.bz.it"
      },
      "@type": "http:\/\/www.w3.org\/ns\/dcat#Dataset",
      "@id": "https:\/\/api.opendatahub.bz.it\/datasets\/it.bz.opendatahub.echargingstation",      
    }

.. note:: References to some of the definitions of the vocabulary have
   been deleted from the excerpt for the sake of clarity.
