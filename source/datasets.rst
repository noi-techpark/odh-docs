.. _available_datasets:

Domains and Datasets
====================

.. topic:: What is a Domain?

   .. include:: /includes/domains.rst

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
with the Open Data Hub project, allowing their free reuse (ideally
under a free licence like |cc0| or |bysa|). Data can be picked up by
any third-party to build their application. These entities can be
private companies or enterprises, public bodies, and even private
citizen.

The updated list of Data Providers that contribute to the Open Data
Hub is available on the Open Data Hub's home page:
https://opendatahub.com/community/

.. _datasets-license:

Datasets, Open Data, and Licenses
---------------------------------

The Open Data Hub contains many datasets: a few have been provided for
testing purposes, other are meant for internal use only, and other
contain only a part of their data that is available as Open Data.

While the goal of the Open Data Hub project is to expose :strong:`only
Open Data` and the Open Data Hub team members always suggest to use
|CC0| to third-parties releasing datasets, it is not yet possible for
the Open Data Hub team to guarantee the availability as open data of
all the data in the datasets, because the data licensing and its
distribution rights are decided by the copyright holder of each
dataset.

Since some of the datasets may contain data that can not be
distributed by the Open Data Hub team under an open licence like,
e.g., |cc0| or |bysa|, a user will be able to retrieve from each
dataset only those data that are distributed as :strong:`Open
Data`. The response to a query is in JSON format (although :term:`CSV`
output can be forced) and is :strong:`always` licensed as Open
Data. However, the response may include resources like links to web
pages, streams, or images that are subject to a different, even
proprietary, licence. For more information about this topic, there is
a :ref:`dedicated section in the appendices <license-json-records>`.

At the date of writing, datasets mostly fall in either the
:ref:`Mobility <mobility-datasets>` and the :ref:`Tourism
<tourism-datasets>` domains; while a few more uncategorised datasets
are available.

Authentication
~~~~~~~~~~~~~~

The authentication layer is currently intended for :strong:`internal
use only`. All data in the dataset that you can receive from the Open Data Hub
are free to use and do not require any type of authentication.


The authentication layer can be of interest for developers who want to
collaborate in the development of Open Data Hub; Details on the implementation
are available in section :ref:`authentication-hub`.

.. _mobility-datasets:

.. _tourism-datasets:

.. _other-domains-datasets:

Datasets
--------

.. versionchanged:: 2022.06 API v1 for Mobility domain are no longer
   available.

.. versionchanged:: 2022.10 Removed information about datasets

The list of datasets and all the information associated with them have
been moved to the |odh| main web site with the same categorisation,
hence you can find them in the following pages:

* :home:`Mobility / Mobility <mobility>` datasets
* :home:`Mobility / Traffic <traffic>` datasets
* :home:`Tourism <tourism>` datasets
* :home:`Other <others>` datasets.

To access the dataset, please refer to the
:doc:`/howto/mobility/getstarted` and :doc:`/howto/tourism/getstarted`
howtos, which helps you getting started in retrieving data from the
Mobility and Tourism datasets, and to the other howtos are available
in the :ref:`dedicated section <howto-list>`.

:ref:`mobility-tech` and :ref:`tourism-tech` are still available in
this documentation portal.

.. toctree::
   :hidden:

   mobility-tech
   tourism-tech
