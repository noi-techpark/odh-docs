.. bluetooth

.. grid::

   .. grid-item-card:: 

      The data for this datasets are collected by experimental
      Bluetooth-based sensors and detectors currently located on various
      points of the streets of Bolzano and soon in other location of
      South Tyrol. Gathered data are then processed to obtain useful
      information about the traffic; therefore, data in this dataset are:

      * The total number of vehicles detected
      * An estimation of heavy and light vehicles

      Collected data are also split within intervals (of e.g.,15, 30
      minutes), for statistical and historical offline
      analysis. Moreover, the data gathered by the Bluetooth devices
      are used in the :ref:`linkstation dataset
      <linkstation-dataset>`.

   .. grid-item-card::

      .. csv-table::

         "Output", "JSON, mime-type application/json"
         "E-mail contact", "|contact|"
         "API version", "v2"
         ":literal:`StationType`", "`BluetoothStation
         <https://mobility.api.opendatahub.bz.it/v2/flat/BluetoothStation>`_"
         "Use cases and info", "https://analytics.opendatahub.bz.it/"
         "Sources", "CISMA"
