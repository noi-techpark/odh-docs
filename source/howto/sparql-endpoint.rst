How to Access |odh| Data Using SPARQL
=====================================

.. versionadded:: 202101

The |odh|\'s dataset can be queried using the SPARQL query language,
using the `Open Data Hub Knowledge Graph Portal
<https://sparql.opendatahub.bz.it/>`_. This howto helps you in
getting acquainted with the functionalities offered by the endpoint.


Layout of the SPARQL endpoint
-----------------------------

The landing page of the portal is shown in :numref:`kg-portal` and consists of three main
zones.

.. _kg-portal:

.. figure:: /images/kg-portal.png

   The landing page of |odh| SPARQL endpoint.

1. The three buttons in the banner at the top of the page.

   .. panels::
      :container: container-fluid pb-3
      :column: col-lg-4 col-md-4 col-sm-6 col-xs-12 p-2
      :header: bg-light text-center


      Playground
      ^^^^^^^^^^
      
      The `Playground` is a space in which to freely write SPARQL
      queries against the |odh| datasets. It is most suited for users
      that already know SPARQL and how to use it to interact with |odh|\.
      +++
      See section :ref:`playground`.
      
      ---
      Regular Queries
      ^^^^^^^^^^^^^^^

      `Regular Queries` are a sample queries that can be used either 
      standalone, to gather example data, or can be edited and
      modified to tweak the results.  
      +++

      See section :ref:`regular-queries`.
      
      ---
      Data Quality Queries
      ^^^^^^^^^^^^^^^^^^^^

      Similar to Regular Queries, `Data Quality Queries` are precooked
      queries that will gather data, but with an emphasis on their
      quality. They can be used to check whether some of the data are
      incomplete. 
      +++
      See section :ref:`data-quality-queries`.

      
2. The main area, consisting of a large textarea, in which to write
   SQARQL queries, and of a number of precooked queries when the `Regular
   Queries` or `Data Quality Queries` buttons are clicked.

   
3. A number of visualisation and download options in the bottom area.


.. _playground:

Working in The Playground
-------------------------

.. _regular-queries:

Working with Regular Queries
----------------------------

.. _data-quality-queries:

Working with Data Quality Queries
---------------------------------
