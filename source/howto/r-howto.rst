.. _howto-r:

How to access Data with R and SPARQL
====================================

.. versionadded:: 2021.04

Datasets and their data in the |odh| can be accessed using R, a
software for statistical analysis.

This howto shows you a method to retrieve data from the |odh|, but
does not address other features like, for example, plotting fetched
data on a map.

It is also assumed you have already installed R on your workstation as
well as the required :strong:`SPARQL` library.


.. dropdown:: Install SPARQL library
   :open:
          
   To install the SPARQL library, simply execute on Debian-like
   systems:


   .. code:: bash
   
      ~# Rscript -e "install.packages('SPARQL')"
      Installing package into ‘/usr/local/lib/R/site-library’
      (as ‘lib’ is unspecified)
      trying URL 'https://cloud.r-project.org/src/contrib/SPARQL_1.16.tar.gz'
      Content type 'application/x-gzip' length 6548 bytes
      ==================================================
      downloaded 6548 bytes

      * installing *source* package ‘SPARQL’ ...
      ** package ‘SPARQL’ successfully unpacked and MD5 sums checked
      ** R
      ** byte-compile and prepare package for lazy loading
      ** help
      *** installing help indices
      ** building package indices
      ** testing if installed package can be loaded
      * DONE (SPARQL)

      The downloaded source packages are in
         ‘/tmp/RtmpISkL9Z/downloaded_packages’

   If you see the message :strong:`* DONE (SPARQL)`, the installation
   was successful.

   Documentation for the library can be found in the library's `PDF
   documentation
   <https://cran.mirror.garr.it/CRAN/web/packages/SPARQL/SPARQL.pdf>`_

In order to fetch data, you need:

1. An endpoint, which for |odh| is https://sparql.opendatahub.bz.it/sparql

2. a SPARQL query, that you can simply copy from one of the precooked
   queries at https://sparql.opendatahub.bz.it/ We'll be using this
   one:

   .. code:: sparql

      PREFIX schema: <http://schema.org/>
      PREFIX geo: <http://www.opengis.net/ont/geosparql#>
      PREFIX noi: <http://noi.example.org/ontology/odh#>

      SELECT ?pos ?posLabel
      WHERE {
        ?p a noi:Pizzeria ;
           geo:asWKT ?pos ;
           schema:name ?posLabel ;
           schema:geo ?geo .
        FILTER (lang(?posLabel) = "it")
      }
      LIMIT 10

3. An R script to put all together

   .. code-block:: R
      :linenos:

      
      library(SPARQL)

      endpoint <- "https://sparql.opendatahub.bz.it/sparql"

      query <- 
      'PREFIX schema: <http://schema.org/>
      PREFIX geo: <http://www.opengis.net/ont/geosparql#>
      PREFIX noi: <http://noi.example.org/ontology/odh#>

      SELECT ?pos ?posLabel
      WHERE {
        ?p a noi:Pizzeria ;
           geo:asWKT ?pos ;
           schema:name ?posLabel ;
           schema:geo ?geo .
        FILTER (lang(?posLabel) = "it")
      }
      LIMIT 10'

      result_set <- SPARQL(endpoint,query)
      print(result_set)

The script above can be saved in a file called :file:`R-demo.r` and
executed using the :command:`Rscript R-demo.r` command. The output
will be similar to::

  ~# Rscript  pippo.r
   Loading required package: XML
   Loading required package: RCurl
   $results
                                                                                   pos
   1  "POINT (11.440394 46.511651)"^^<http://www.opengis.net/ont/geosparql#wktLiteral>
   2  "POINT (11.200728 46.729921)"^^<http://www.opengis.net/ont/geosparql#wktLiteral>
   3      "POINT (11.9412 46.9803)"^^<http://www.opengis.net/ont/geosparql#wktLiteral>
   4      "POINT (11.4278 46.4135)"^^<http://www.opengis.net/ont/geosparql#wktLiteral>
   5  "POINT (11.326362 46.310963)"^^<http://www.opengis.net/ont/geosparql#wktLiteral>
   6  "POINT (12.279453 46.733497)"^^<http://www.opengis.net/ont/geosparql#wktLiteral>
   7  "POINT (10.867335 46.622179)"^^<http://www.opengis.net/ont/geosparql#wktLiteral>
   8  "POINT (11.241217 46.246141)"^^<http://www.opengis.net/ont/geosparql#wktLiteral>
   9   "POINT (11.598339 46.40688)"^^<http://www.opengis.net/ont/geosparql#wktLiteral>
   10     "POINT (12.0114 46.7474)"^^<http://www.opengis.net/ont/geosparql#wktLiteral>
                                            posLabel
   1           "Ristorante Pizzeria Bar Pirpamer"@it
   2                      "Bar Pizzeria Alpenhof"@it
   3            "Ahrner Wirt Ristorante Pizzeria"@it
   4                  "Ristorante Pizzeria Adler"@it
   5                            "Hotel Al Mulino"@it
   6                "Ristorante Pizzeria Zentral"@it
   7        "Hotel Ristorante Bar Rasthof Vermoi"@it
   8                             "Hotel Grünwald"@it
   9                                "Hennenstall"@it
   10 "Après Ski Bar Pizzeria Ristorante "Gassl""@it

In the script, all data fetched are kept into the :strong:`result_set`
variable and can be manipulated at will using  R libaries.
