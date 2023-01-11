.. _quickstart:

============
 Quickstart
============

.. versionadded:: 2022.03 Quickstart section

This section helps you in getting quickly in touch with the most
popular tools developed by |odh| to interact with the dataset and
the whole ecosystem.

At the time of writing, all tools that have been developed are
available online: they are summarised in the following table.

.. grid::
   :gutter: 3

   .. grid-item-card::
      :columns: 6

      Data Browser
      ^^^^^

      The |odh| `Tourism Data Browser
      <https://databrowser.opendatahub.com/>`_ allows to access all
      the Open Data available in the Tourism domain by simply browsing
      the content of the various datasets.

      You can simply use those data for your convenience, or you might
      even find a novel way to exploit those data and use them in an
      app or portal you are going to develop. A detailed howto is
      available: :ref:`tourism-data-browser-howto` to help you getting
      acquainted with the browser.

      Currently, the Data Browser is being developed to be able to
      access also data in the Mobility domain as well.

   .. grid-item-card::
      :columns: 6

      Analytics tools
      ^^^^^

      Open the :strong:`Analytics for Mobility` web page, at
      https://analytics.opendatahub.com/ This portal uses data in
      the mobility domain to display various information about the
      sensors, including their locations, what they measure, and
      actual data in near-real time. You can retrieve data gathered by
      the sensors directly from the dataset, in almost real-time.

   .. grid-item-card::
      :columns: 6

      Swagger API interface
      ^^^^^

      The |odh| team has developed REST APIs to programmatically
      access both the Tourism and Mobility domains. You can access
      their swagger interface to browse the data and learn how to use
      the API. You will be guided in building the query and will
      receive as a result both all the data satisfying the query and
      the full query in a format that you can use with the
      :command:`curl` command from a shell or a script.

      .. tab-set::

         .. tab-item:: Mobility resources

            * :octicon:`triangle-right` The URL of the Swagger
              interface is https://mobility.api.opendatahub.com/

            * :octicon:`triangle-right` Check out the `Mobility
              dedicated howto` (:ref:`get-started-mobility`) that will
              guide you in the first steps.

         .. tab-item:: Tourism resources

            * :octicon:`triangle-right` The URL of the Swagger
              interface is
              https://tourism.opendatahub.bz.it/swagger/ui/index

            * :octicon:`triangle-right` Check out the `Tourism
              dedicated howto` (:ref:`tourism-data-howto`) that will
              guide you in the first steps.

   .. grid-item-card::
      :columns: 6

      Web Component Store
      ^^^^^

      Web Components are a W3C's effort to provide standard components
      for the Web. Anyone can create a Web Component, using standard
      languages like CSS, JSON, HTML and share it with other, in this
      cae with the |Odh| community.

      If you have developed a :term:`Web Component` that you deem
      useful for the |odh| project or that can be used on top of data
      provided by the |odh|, you can share it and allow other to reuse
      it, by making it freely available on |odh|\'s `Web Components
      Store <https://webcomponents.opendatahub.com/>`_.

      The only requirement for all the Web Components offered through
      the Store is that they :strong:`must` be released as an
      :ref:`Open Source Licence <odh-license>`, compatible with those
      used within the |odh| project.

      To help you in the process of publishing your Web Component in
      |odh|'s store, check the howto: :ref:`webcomponents`.

.. seealso:: More information about the |odh| project, its goal, and
   possibility to interact or collaborate with it can be found in
   sections :ref:`project-overview`, :ref:`getting-involved`,
   :reF:`architecture-odh`, :ref:`available_datasets`,
   :ref:`data-access`.
