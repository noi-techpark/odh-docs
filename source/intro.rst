
.. _project-intro:

==============
 Introduction
==============

This is the website of the |ODH| documentation, a collection of
technical resources about the |odh| project. The website serves as the
main resource portal for everyone interested in accessing the data or
deploying apps based on :term:`datasets <dataset>` & :term:`API`\s
provided by the |odh| team.

The technical stuff is composed of:

* Catalogue of available datasets.
* How-tos, FAQs, and various tips and tricks for users.
* Links to the full API documentation.
* Resources for developers.
  
For non-technical information about the |odh| project, please point 
your browser to https://opendatahub.bz.it/.

.. _project-overview:

Project Overview
================

The |odh| project envisions the development and set up of a portal
whose primary purpose is to offer a single access point to all (Open)
Data from the region of South Tyrol, Italy, that are relevant for the
economy sector and its actors.

The availability of Open Data from a single source will allow
everybody to utilise the Data in several ways:

* Digital communication channels. Data are retrieved from the |odh|
  and used to provide informative services, like newsletters
  containing weather forecasting, or used in hotels to promote events
  taking place in the surroundings, along with additional information
  like seat availability, description, how to access each event, and
  so on and so forth.
* Applications for any devices, built on top of the data, that can be
  either a :abbr:`PoC (Proof of Concept)` to explore new means or new
  fields in which to use |odh| data, or novel and innovative services
  or software products built on top of the data.
* Internet portals and websites. Data are retrieved from the |odh| and
  visualised within graphical charts, graphs, or maps.

There are many services and software that rely on |odh|\'s Data, which
are listed in the :ref:`applist` section, grouped according to their
maturity: production stage, beta and alpha stage.

.. _domains-diagram:

.. figure:: /images/domain.png
   :width: 99%

   An overview of the |odh| Project.

:numref:`domains-diagram` gives a high level overview of the flow of
data within the |odh|\: at the bottom, :term:`sensors <sensor>` gather
data from various domains, which are fed to the |odh| Big Data
infrastructure and made available through endpoints to (third-party)
applications, web sites, and vocal assistants. A more technical and
in-depth overview can be found in next section,
:ref:`architecture-odh`.
	
All the data within the |odh| will be easily accessible, preferring
open interfaces and APIs which are built on existing standards like
`The Open Travel Alliance <https://opentravel.org/>`_ (OTA), `The
General Transit Feed Specification <https://gtfs.org/>`_ (GTFS),
`Alpinebits <https://www.alpinebits.org/>`_.

The |odh| team also strives to keep all data regularly updated, and
use standard exchange formats for them like `Json
<http://www.json.org/>`_ and the `Data Catalog Vocabulary
<https://www.w3.org/TR/vocab-dcat/>`_ (DCAT) to facilitate their
spreading and use. Depending on the development of the project and the
interest of users, more standards and data formats might be supported
in the future.

.. _architecture-odh:

|ODH| Architecture
------------------

.. include:: /architecture.rst

.. _available-domains:
	     
Available Domains
=================

.. include:: /domains.rst


Available Datasets
==================

The list of available datasets has been moved :doc:`to a dedicated page
<datasets>`.


Accessing data in the |odh|
===========================

There are different modalities to access data that are provided by the
|odh|, that are listed here. Currently, data from the
:strong:`Mobility` and :strong:`Tourism` domains can be accessed, both
from the command line and using a browser. Various dedicated tutorials
are available in the :ref:`howto-list` section; while in section
:ref:`getting-involved` you can find additional ways to interact with
the data and the |odh| team.

Browser access
--------------

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
   http://tourism.opendatahub.bz.it/swagger/, to learn how the REST
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
----------

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
<http://tourism.opendatahub.bz.it/swagger>`_ or `mobility`
(http\://ipchannels.integreen-life.bz.it/<dataset>/swagger-ui.html
[#]_) domains and execute a query: with the output, also the
corresponding :program:`curl` command used to retrieve the data will
be shown.

.. rubric:: Notes

.. [#] You need to provide the dataset name, for example
       http://ipchannels.integreen-life.bz.it/parking/swagger-ui.html,
       see :ref:`mobility-datasets` for full links.

Authentication
--------------

The authentication layer is currently intended for :strong:`internal
use only`. All data in the dataset that you can receive from the |odh|
are free to use and do not require any type of authentication.


The authentication layer can be of interest for developers who want to
collaborate in the development of |odh|\; Details on the implementation
are available in section :ref:`authentication`.
