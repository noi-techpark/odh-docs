.. _data-access:


Accessing the Open Data Hub
=============================

.. versionchanged:: 2021.08 move `ODH Virtual Knowledge Graph` subsection
   from Dataset section

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


Browser access
--------------

Accessing data in the Open Data Hub by using a browser is useful on
different levels: for the casual user, who can have a look at the
type and quality of data provided; for a developer, that can use
the :term:`REST API` implemented by the Open Data Hub or even check
if the results of his app are coherent with those retrieved with
the API; for everyone in order to get acquainted with the various
methods to retrieve data.

More in detail, these are the possibilities to interact with Open Data Hub's
data by using a browser:

.. grid::
   :gutter: 1

   .. grid-item-card::
      :columns: 4

      Go to the :ref:`applist` section of the documentation,
      particularly sub-sections :ref:`production-stage-apps` and
      :ref:`beta-stage-apps`, and choose one of the web sites and
      portals that are listed there. Each of them uses the data
      gathered from one or more OPEN DATA HUB's datasets to display a
      number of useful information. You can then see how data are
      exposed and browse them.

   .. grid-item-card::
      :columns: 4

      In the same :ref:`applist` section, you can also check the list
      of the :strong:`Alpha Stage Apps` and choose one of them that
      you think you can expand, then get in touch with the authors to
      suggest additional features or collaborate with them to discuss
      its further development to improve it.

   .. grid-item-card::
      :columns: 4

      Access the `ODH Tourism data browser
      <https://databrowser.opendatahub.bz.it/>`_ and search for the
      Open Data available in the Tourism domain. You can simply use
      those data for your convenience, or you might even find a novel
      way to exploit those data and use them in an app or portal you
      are going to develop. A detailed howto is available:
      :ref:`tourism-data-browser-howto` to help you getting acquainted
      with the browser.

   .. grid-item-card::
      :columns: 4

      Go to the :strong:`Swagger interface` of the datasets in the
      Tourism domain, located at
      https://tourism.opendatahub.bz.it/swagger/ui/index to learn how
      the REST APIs are built and how you can script them to fetch
      data for your application. To get started, there is a dedicated
      howto: :ref:`tourism-data-howto` that will guide you in the
      first steps.

   .. grid-item-card::
      :columns: 4

      Access the :strong:`Swagger interface` of the datasets in the
      Mobility domain, located at
      https://mobility.api.opendatahub.bz.it/. Like in the case of the
      tourism' Swagger interface, you can learn REST API call for that
      domain and fetch data for your application. More possibilities
      to interact with the Mobility domain datasets and the
      description of the new APIv2 are described in the
      :ref:`dedicated howto <get-started-mobility>`.

   .. grid-item-card::
      :columns: 4

      Open the :strong:`Analytics for Mobility` web page, at
      https://analytics.opendatahub.bz.it/ This portal uses data in
      the mobility domain to display various information about the
      sensors, including their locations, what they measure, and
      actual data in near-real time. You can retrieve data gathered by
      the sensors directly from the dataset, in almost real-time.

   .. grid-item-card::


      Open the `Open Data Hub Knowledge Graph Portal
      <https://sparql.opendatahub.bz.it/>`_ where you can explore all
      the data that are already available as a virtual knowledge
      graph. Here you can check out some of the precooked query to see
      and modify them to suit your needs with the help of W3C's
      `SPARQL query language
      <https://www.w3.org/TR/sparql11-overview/>`_; SPARQL can be used
      also in the `Playground` to freely query the endpoint.

Programmatic access
-------------------

Programmatic and non-interactive access to the Open Data Hub's dataset
is possible using any of the following methods made  available
by the |odh| team.

.. grid::
   :gutter: 1

   
   .. grid-item-card:: 
      :columns: 6

      .. _ab-access:

      AlpineBits client
      ^^^^^^^^^^^^^^^^^
      .. include:: /includes/AlpineBits.rst

   .. grid-item-card::
      :columns: 6

      .. _r-access:

      Statistical Access with R
      ^^^^^^^^^^^^^^^^^^^^^^^^^
      
      .. include:: /includes/R.rst

   .. grid-item-card::
      :columns: 6
      
      .. _ninja api:

      API
      ^^^
      
      .. include:: /includes/API.rst

   .. grid-item-card::
      :columns: 6
      
      .. _cli-access:

      CLI access
      ^^^^^^^^^^
      .. include:: /includes/CLI.rst

.. odh vkg km

.. include:: /includes/kg.rst

