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

As seen in :numref:`domains`, data originate from different
domains (Mobility, Tourism, and so on); they are gathered from sensors
and packed within :strong:`datasets`. `Sensors` can be for example GPS
devices installed on buses that send their real-time geographic
position.

For each domain the available datasets are listed. Please refer to the
next sections for a complete list.

.. topic:: A note about datasets.

   At the time of writing, only a few datasets are published. As
   mentioned before in this section, the goal is to expose datasets
   containing :strong:`only Open Data`, which is at the moment not the
   case for all datasets. Indeed, some of the datasets contain data
   that can not be distributed under an open licence like, e.g., |cc0|
   or |bysa|. Therefore, to allow the highest possible data to be
   shared, an authentication mechanism has been implemented, to
   prevent access to the data in the datasets that has not yet been
   published as |od|\.  Please refer to section :ref:`authentication`
   for details.

.. _mobility-datasets:

Datasets in the Mobility Domain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this section, the following information are provided for each
listed dataset:

* The licence of the data present in the dataset.
* The output format of the API call.
* An e-mail contact for the dataset.
* The versions of the API that can be used to access the dataset.
* The swagger URL of the APIs.

.. _echarging-dataset:
.. include:: /datasets/ecs.rst

.. _sasabus-dataset: 
.. include:: /datasets/sasa.rst

.. _bluetooth-dataset:
.. include:: /datasets/bluetooth.rst

.. _linkstation-dataset:
.. include:: /datasets/linkstation.rst

.. _weather-dataset:
.. include:: /datasets/weather.rst


.. _tourism-datasets:

Datasets in the Tourism Domain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Like in the previous section, the following information are provided for each
listed dataset:

* The licence of the data present in the dataset.
* The output format of the API call.
* An e-mail contact for the dataset.
* The versions of the API that can be used to access the dataset.
* The swagger URL of the APIs.

.. _poi-dataset:
.. include:: /datasets/poi.rst
	     
.. _museum-dataset:
.. include:: /datasets/museum.rst
