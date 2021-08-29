.. parking

.. grid::

   .. grid-item-card::
      :columns: 4

      This dataset contains two types of data:

      * Parking stations - off street parking data (currently for the
        cities of Bolzano, Merano, Trento, Rovereto), with slot
        availability and predictions

      * Parking sensors - on street parking data (currently Bolzano,
        soon Merano). Single parking slots on streets, can be within a
        virtual area

   .. grid-item-card::
      :columns: 8

      .. csv-table::

         Output, "JSON, mime-type application/json"
         E-mail contact, contact
         API version, "`v1` deprecated, v2"
         :literal:`StationType`, "`ParkingStation <https://mobility.api.opendatahub.bz.it/v2/flat/ParkingStation>`_, `ParkingSensor <https://mobility.api.opendatahub.bz.it/v2/flat/ParkingSensor>`_"
         Use cases and info, "https://parking.bz.it
         https://mobility.meran.eu
         https://analytics.opendatahub.bz.it
         https://mobility.bz.it"
         Sources, "Municipalities of Bolzano, Merano, Trento and Rovereto"
