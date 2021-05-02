
.. _project-intro:

==============
 Introduction
==============

This is the website of the |ODH| documentation, a collection of
technical resources about the |odh| project. The website serves as the
main resource portal for everyone interested in accessing the data or
deploying apps based on :term:`datasets <Dataset>` & :term:`API`\s
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
   :width: 90%

   An overview of the |odh| Project.

:numref:`domains-diagram` gives a high level overview of the flow of
data within the |odh|\: at the bottom, :term:`sensors <Sensor>` gather
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

.. include:: /includes/architecture.rst

.. _available-domains:
	     
Available Domains
=================

.. include:: /includes/domains.rst


Available Datasets
==================

The list of available datasets has been moved :doc:`to a dedicated page
<datasets>`.


