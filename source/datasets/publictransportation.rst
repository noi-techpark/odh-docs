.. sasa bus


.. panels::
   :container: container-fluid

   -----
   :column: col-lg-4 col-md-4 col-sm-4 col-xs-6 p-2

   .. warning:: This dataset is not supported anymore and will
      be removed from the |odh| in the next future.

   This dataset shows the real time position of buses operated by SASA
   in South Tyrol and, through a few subsets, additional information
   about lines, station boards, and news.

   There are additional subsets that expose data in different formats:

   + info.opensasa.plandata (VDV 451 - VDV 452)
   + info.opensasa.stationboard (JSON)
   + info.opensasa.news (JSON)
   + info.opensasa.rssDE (XML)
   + info.opensasa.rssIT (XML)

   -----
   :column: col-lg-8 col-md-8 col-sm-8 col-xs-6 p-2

   .. csv-table::

      "Output", "geoJSON"
      "E-mail contact", "info\@sasabus\.org"
      "API version", "--"
      "URL", "https://daten.buergernetz.bz.it/dataset/southtyrolean-public-transport
      https://sasabus.org/opendata"
      "Use cases and info", "https://suedtirolmobil.info/,
      https://mobility.meran.eu/, https://analytics.opendatahub.bz.it/,
      https://mobility.bz.it/"
      "Web Component", "`Smart Mobility
      <https://webcomponents.opendatahub.bz.it/webcomponent/7620f04d-ed08-4770-bbda-dfe959ae078e>`_"
      "Sources", "STA, SASA"
