.. _howto-sparql:

How to Access |odh| Data Using SPARQL
=====================================

.. versionchanged:: 2023.1 notify users of SPARQL endpoint reachable
   upon request only.

.. warning:: The SPARQL endpoint is currently not active, but can be
   activated upon request to |contact|. However, the ODH SPARQL
   portal, which contains sample data and queries, can be accessed at
   https://sparql.opendatahub.com/.

The |odh|\'s dataset can be queried using the SPARQL query language,
using the `Open Data Hub Knowledge Graph Portal
<https://sparql.opendatahub.com/>`_. This howto helps you in getting
acquainted with the functionalities offered by the endpoint. However,
this howto does not cover SPARQL: if you are not familiar with it,
here is some reference:

* The `SPARQL Query Language Recommendation
  <https://www.w3.org/TR/sparql11-query/>`_ is the official and
  normative W3C definition of SPARQL and also contains a lot of
  examples and querie to learn from

* A `tutorial about SPARQL
  <https://jena.apache.org/tutorials/sparql.html>`_ written by Apache
  Jena's team. Oriented toward Jena, it nonetheless includes and
  explains a lot of basic notions

.. _sparql-gui:

Data Available in the Portal
----------------------------

The landing page of |odh|\'s SPARQL endpoint contains the following elements:

1. The buttons in the banner at the top of the page.

   .. grid:: 6
      :gutter: 1

      .. grid-item-card::
         :columns: 4

         Playground
         ^^^^^^^^^^

         The `Playground` is a space in which to freely write SPARQL
         queries against the |odh| datasets. It is most suited for users
         that already know SPARQL and how to use it to interact with |odh|\.
         +++
         See section :ref:`playground`.

      .. grid-item-card::
         :columns: 4

         Regular Queries
         ^^^^^^^^^^^^^^^

         `Regular Queries` are a sample queries that can be used either
         standalone, to gather example data, or can be edited and
         modified to tweak the results.
         +++

         See section :ref:`regular-queries`.

      .. grid-item-card::
         :columns: 4

         Data Quality Queries
         ^^^^^^^^^^^^^^^^^^^^

         Similar to Regular Queries, `Data Quality Queries` are precooked
         queries that will gather data, but with an emphasis on their
         quality. They can be used to check whether some of the data are
         incomplete.
         +++
         See section :ref:`data-quality-queries`.

      .. grid-item-card::
         :columns: 6

         Mobility
         ^^^^^^^^

         `Mobility` queries are sample queries against all the datasets
         in the entire mobility domain. They can be used as they are or
         modified and tweaked to extract more precise data.
         +++

         You can refer to section :ref:`playground`.

      .. grid-item-card::
         :columns: 6

         Tourism and Mobility
         ^^^^^^^^^^^^^^^^^^^^

         `Tourism and Mobility` queries combine datasets from the tourism
         domain with observations gathered by sensors in the mobility domain.
         +++

         You can refer to section :ref:`playground`.

2. The main area, consisting of a large textarea, in which to write
   SQARQL queries, and of a number of precooked queries when the `Regular
   Queries` or `Data Quality Queries` buttons are clicked. The three
   buttons on the textarea's top right corner can be used to

   * :fa:`share-alt` Copy the URL of the query and share it, store it
     for future use, or use it in scripts.
   * :fa:`expand-arrows-alt` maximise the textarea
   * :fa:`caret-square-right` execute the query. If the query contains
     some syntactic error, it is accompanied by a yellow question mark
     :octicon:`alert;1em;sd-text-warning sd-bg-black` and it is not
     executed, but an error message is displayed

3. A number of visualisation and download options in the bottom
   area. Also this part of the area can be maximised

   * `Table`. A simple table with a result on each row
   * `Response`. The actual JSON received as result
   * `Pivot Table`. Analyse statistically the query result
   * `Google chart`. Use the data retrieved within a Google Chart. The
     default representation is a simple table, more can be employed,
     by clicking on the :button:`Chart Config` button on the
     right-hand side.
   * `Geo`. See on a map the location of the results
   * :fa:`download` download the result set as a CSV file

.. _playground:

Working in The Playground
-------------------------

The playground is the place in which you can build you queries against
the |odh| endpoint. Queries can be built using built-in or custom
prefixes as well as all SPARQL operators. There is a validation of the
queries, therefore in case of mistakes a red warning icon
:octicon:`issue-opened;1em;sd-text-danger` will appear on the left-hand side
of the offending line.

.. note:: Generic queries might return hundreds or thousands of
   results, so the use of the :literal:`LIMIT` clause helps to receive
   quicker answers.

.. _regular-queries:

Working with Regular Queries
----------------------------

Regular queries are predefined queries that give a glimpse of the data
contained in the |odh|\. Regular queries are rather generic and can be
used as starting point for more precise and refined queries. They can
be edited directly in the textarea or copy and pasted in the Playground.

.. _data-quality-queries:

Working with Data Quality Queries
---------------------------------

Data quality queries are built with purpose to verify if there are
incomplete or wrong data in a dataset.
