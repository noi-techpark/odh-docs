.. linkstation

.. grid::

   .. grid-item-card::

      The data for this dataset are collected by the same Bluetooth-based
      sensors that are used to produce the :ref:`Bluetooth dataset
      <bluetooth-dataset>`. Indeed, the data gathered by the sensors will
      be used to produce statistics about a LinkStation, which is defined
      as the path between an ordered pair of bluetooth stations.

      * the :strong:`valid matches` between pairs of Bluetooth sensors
        (also called Bluetooth stations).
      * The :strong:`number of matches per predefined time interval`
        (e.g., 30 or 60 minutes), like in the Bluetooth dataset
      * The :strong:`estimated travel time and speed` of the vehicle,
        computed for every 15 minutes interval only.

        The definitions and algorithm used in the computations are
        extensively described in Section `Data analysis complexity` of
        `this pdf article
        <https://www.integreen-life.bz.it/it/c/document_library/get_file?uuid=f1702bf2-5ed9-42a5-a85b-42a3d97a3e6b&groupId=17369>`_.

   .. grid-item-card::

      .. csv-table::

         "Output", "JSON, mime-type application/json"
         "E-mail contact", "|contact|"
         "API version", "v2"
         ":literal:`StationType`", "`LinkStation
         <https://mobility.api.opendatahub.bz.it/v2/flat/LinkStation>`_"
         "Use cases and info", "https://analytics.opendatahub.bz.it/"
         "Sources", "A22"
