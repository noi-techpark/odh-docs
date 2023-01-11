.. _howto-r:

How to Access |odh| Data With R and SPARQL
==========================================

Datasets and their data in the |odh| can be accessed using R, a
software for statistical analysis.

This howto shows you a method to retrieve data from the |odh|, but
does not address other features like, for example, plotting fetched
data on a map.
           
It is also assumed you have already installed R on your workstation as
well as the required R's `SPARQL library
<https://cran.mirror.garr.it/CRAN/web/packages/SPARQL/>`_ from a
:abbr:`CRAN (Comprehensive R Archive Network)` mirror.


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

   If you see instead  any :strong:`ERROR`, like those reported below, 
   please refer to section :ref:`r-tbs`::

     Warning messages:
     1: In install.packages("SPARQL") :
       installation of package ‘RCurl’ had non-zero exit status
     2: In install.packages("SPARQL") :
       installation of package ‘SPARQL’ had non-zero exit status

   ..
      Documentation for the library can be found in the library's `PDF
      documentation
      <https://cran.mirror.garr.it/CRAN/web/packages/SPARQL/SPARQL.pdf>`_

In order to fetch data, you need:

1. An endpoint, which for |odh| is https://sparql.opendatahub.com/sparql

2. a SPARQL query, that you can simply copy from one of the precooked
   queries at https://sparql.opendatahub.com/ We'll be using this
   one:

   .. code:: sparql

      PREFIX schema: <https://schema.org/>
      PREFIX geo: <http://schemas.opengis.net/geosparql/1.0/geosparql_vocab_all.rdf#>
      PREFIX noi: <https://noi.example.org/ontology/odh#>

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

      endpoint <- "https://sparql.opendatahub.com/sparql"

      query <- 
      'PREFIX schema: <https://schema.org/>
      PREFIX geo: <http://schemas.opengis.net/geosparql/1.0/geosparql_vocab_all.rdf#>
      PREFIX noi: <https://noi.example.org/ontology/odh#>

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

  ~# Rscript R-demo.r
   Loading required package: XML
   Loading required package: RCurl
   $results
                                                                                   pos
   1  "POINT (11.440394 46.511651)"^^<http://schemas.opengis.net/geosparql/1.0/geosparql_vocab_all.rdf#wktLiteral>
   2  "POINT (11.200728 46.729921)"^^<http://schemas.opengis.net/geosparql/1.0/geosparql_vocab_all.rdf#wktLiteral>
   3      "POINT (11.9412 46.9803)"^^<http://schemas.opengis.net/geosparql/1.0/geosparql_vocab_all.rdf#wktLiteral>
   4      "POINT (11.4278 46.4135)"^^<http://schemas.opengis.net/geosparql/1.0/geosparql_vocab_all.rdf#wktLiteral>
   5  "POINT (11.326362 46.310963)"^^<http://schemas.opengis.net/geosparql/1.0/geosparql_vocab_all.rdf#wktLiteral>
   6  "POINT (12.279453 46.733497)"^^<http://schemas.opengis.net/geosparql/1.0/geosparql_vocab_all.rdf#wktLiteral>
   7  "POINT (10.867335 46.622179)"^^<http://schemas.opengis.net/geosparql/1.0/geosparql_vocab_all.rdf#wktLiteral>
   8  "POINT (11.241217 46.246141)"^^<http://schemas.opengis.net/geosparql/1.0/geosparql_vocab_all.rdf#wktLiteral>
   9   "POINT (11.598339 46.40688)"^^<http://schemas.opengis.net/geosparql/1.0/geosparql_vocab_all.rdf#wktLiteral>
   10     "POINT (12.0114 46.7474)"^^<http://schemas.opengis.net/geosparql/1.0/geosparql_vocab_all.rdf#wktLiteral>
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

.. _r-tbs:

Troubleshooting
---------------

.. rubric:: SPARQL installation fails!

When installing a package, R tries to satisfy all the package's
dependencies and installs any missing library required by the
package. If you still stumble upon errors, like for example::

     Warning messages:
     1: In install.packages("SPARQL") :
       installation of package ‘RCurl’ had non-zero exit status
     2: In install.packages("SPARQL") :
       installation of package ‘SPARQL’ had non-zero exit status

It means that SPARQL's dependency :strong:`RCurl` also failed. In this
case it is not easy to spot the root cause, which is a missing package
in the OS installation, called :strong:`libcurl4-gnutls-dev`. To
install it on a Debian-like system, use as `root` the following command::

  ~# apt-get install libcurl4-gnutls-dev

.. rubric:: I have some strange warning when executing the script!

If you execute a query and the outcome is not a result set but some
error message similar to the following ones, please verify that the
URL of the SPARQL endpoint is correct: :strong:`https\://sparql.opendatahub.com/sparql`

::
   
   Opening and ending tag mismatch: meta line 5 and head
   Opening and ending tag mismatch: meta line 4 and html
   Premature end of data in tag meta line 3
   Premature end of data in tag head line 2
   Premature end of data in tag html line 1
            
