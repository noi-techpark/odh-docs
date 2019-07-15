
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

Project Overview
================

The |odh| project envisions the development and set up of a portal
whose primary purpose is to offer a single access point to all (Open)
Data from the region of South Tyrol, Italy, that are relevant for the
economy sector and its actors. This will also allow everybody to
utilise these data in all digital communication channels and build
application on top of the data offered, be them either a :abbr:`PoC
(Proof of Concept)` to explore new means or new field in which to use
|odh| data, or novel and innovative services or software products
built on top of the data. 

.. _domains-diagram:

.. figure:: /images/domain.png
   :width: 99%

   An overview of the |odh| Project.

All the data within the |odh| will be easily accessible, preferring
open interfaces and APIs which are built on existing standards like
`The Open Travel Alliance <https://opentravel.org/>`_ (OTA), `The
General Transit Feed Specification <https://gtfs.org/>`_ (GTFS),
`Alpinebits <https://www.alpinebits.org/>`_.

The |odh| team also strives to keep all data regularly updated, and
use standard exchange formats for them like `Json
<http://www.json.org/>`_ and the `Data Catalog Vocabulary
<https://www.w3.org/TR/vocab-dcat/>`_ (DCAT).

Depending on the development of the project and the interest of users,
more standards and data formats might be supported in the future.


.. _architecture-odh:

|ODH| Architecture
------------------

.. include:: /architecture.rst

.. _available-domains:
	     
Available Domains and APIs
==========================

.. include:: /domains.rst


Available Datasets
==================

The list of available datasets has been moved :doc:`to a dedicated page
<datasets>`.


Accessing data in the |odh|
===========================

There are different modalities to access data that are provided by the
|odh|, that are listed here. Currently, only data from the
:strong:`Mobility` and :strong:`Tourism` domains can be accessed, both
from the command line and using a browser. Various dedicated tutorials
are available in the :ref:`howto-list` section; while in section
:ref:`how-to-contribute` you can find additional ways to interact with
the data and the |odh| team.

Browser access
--------------

By using a browser it is possible to access data in different ways:

#. Go to the :ref:`applist` section of the documentation, particularly
   sub-sections :ref:`production-stage-apps` and :ref:`beta-stage-apps`, and choose
   one of the web sites and portals that are listed there. Each of
   them uses the data gathered from one or more |ODH|\'s datasets to
   display a number of useful information. You can then see how data
   are exposed and browse them.

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
   near-real time. You can retrieve 

CLI access
----------

Command line access proves useful for scripting and quick data
manipulation, for example within applications that gather data and
present them to end users. On the other hand, browser access is useful
on different levels: for the casual user, to have a look at the type
and quality of data provided, or even to use the REST API implemented
by the |odh| in order to get acquainted with the various methods to
retrieve data.

Command line access to the data is usually carried out with the
:program:`wget` utility, used to retrieve information in a
non-interactive way. To learn about the correct syntax and parameter
to use, go to the :strong:`swagger interface` of the `tourism
<http://tourism.opendatahub.bz.it/swagger>`_ or `mobility
<http://ipchannels.integreen-life.bz.it/>`_ [#]_ domains and execute a
query: with the output, also the corresponding :program:`wget` command
used to retrieve the data will be shown.

.. rubric:: Footnotes

.. [#] Add the dataset name, see :ref:`mobility-datasets`. 
