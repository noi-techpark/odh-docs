Quick and (not-so) Dirty Tips for Tourism
-----------------------------------------

This section contains various tips and tricks to improve and tweak the
queries sent to the Tourism datasets, allowing more precise results to
be retrieved. This page is divided into two parts: The first one shows
examples with code (usually the API call), the second is organised
like a FAQ section..

	  
Example Calls
~~~~~~~~~~~~~

.. _tour-ex1:

.. rubric:: EX1. Why does this query return no result?
   
.. code:: http
	  
   http://tourism.opendatahub.bz.it/api/Gastronomy?pagesize=3&categorycodefilter=0&locfilter=reg268

Because there is no value :strong:`reg268` for `locfilter`. You can
return valid IDs to be used as locfilter using this call:

.. code:: http
	     
   http://tourism.opendatahub.bz.it/api/RegionReduced?language=it

An example result for this call is:
	  
.. code:: json
	  
   {
     "Id": "D2633A26C24E11D18F1B006097B8970B",
     "Name": "Alta Badia"
   },

Therefore, use the ID :strong:`regD2633A26C24E11D18F1B006097B8970B` in
`locfilter` to search for Gastronomy in the Alta Badia region.

*****


.. _tour-ex2:

.. rubric:: EX2. The locfilter parameter.

|q| How do I correctly use the `locfilter` parameter?

.. code::

   locfilter =>
   Locfilter (Separator ',' possible values: reg + REGIONID = (Filter by
   Region), reg + REGIONID = (Filter by Region), tvs + TOURISMVEREINID =
   (Filter by Tourismverein), mun + MUNICIPALITYID = (Filter by
   Municipality), fra + FRACTIONID = (Filter by Fraction)),
   (default:'null')

It seems to accept a string, but how is this string built?

|a| `locfilter` accepts a string composed as follows: a region
identifier, followed immediately by a location Identifier.

Location identifier are the following four:

* :strong:`reg`: Region (Italian Regione)
* :strong:`tvs`: Turistic association (German Tourismusverein) 
* :strong:`mun`: Town or city (Italian Comune)
* :strong:`fra`: Suburb or district (Italian frazione)

IDs for each location can be gathered either from the swagger
interface or using an API calls:

* :strong:`reg`::

     http://tourism.opendatahub.bz.it/swagger/ui/index#!/Common/Common_GetRegionsReduced 
     http://tourism.opendatahub.bz.it/api/RegionReduced?language=it 

* :strong:`tvs`::

    http://tourism.opendatahub.bz.it/swagger/ui/index#!/Common/Common_GetTourismvereinReduced
    http://tourism.opendatahub.bz.it/api/TourismAssociationReduced?language=iturismusverein)
    
* :strong:`mun`::
    
    http://tourism.opendatahub.bz.it/swagger/ui/index#!/Common/Common_GetMunicipalityReduced
    http://tourism.opendatahub.bz.it/api/MunicipalityReduced?language=it
    
* :strong:`fra`::
  
    http://tourism.opendatahub.bz.it/swagger/ui/index#!/Common/Common_GetDistrictReduced
    http://tourism.opendatahub.bz.it/api/DistrictReduced?language=it

For example, to retrieve all Gastronomy in the suburb of Lana, first
retrieve its ID, which is:

.. code:: json
	     
      {
        "Id": "79CBD79551C911D18F1400A02427D15E",
	"Name": "Lana"
      },

Then pass the string :strong:`fra79CBD79551C911D18F1400A02427D15E` as
`locfilter`::

  http://tourism.opendatahub.bz.it/api/Gastronomy?locfilter=fra79CBD79551C911D18F1400A02427D15E

*****

.. _tour-ex3:

.. rubric:: EX3. The `categorycodefilter` parameter.
	    
|q| `categorycodefilter` seems similar to the `locfilter`
parameter found in :ref:`this trick <tour-ex2>`, but this does not
accept string?

.. code::

   Category Code Filter (BITMASK values: 1 = (Restaurant), 2 = (Bar /
   Café / Bistro), 4 = (Pub / Disco), 8 = (Apres Ski), 16 =
   (Jausenstation), 32 = (Pizzeria), 64 = (Bäuerlicher Schankbetrieb),
   128 = (Buschenschank), 256 = (Hofschank), 512 = (Törggele Lokale),
   1024 = (Schnellimbiss), 2048 = (Mensa), 4096 = (Vinothek /Weinhaus /
   Taverne), 8192 = (Eisdiele), 16348 = (Gasthaus), 32768 = (Gasthof),
   65536 = (Braugarten), 131072 = (Schutzhütte), 262144 = (Alm), 524288 =
   (Skihütte)

The `categorycodefilter` parameter accepts integers instead of
strings. The code of each category is a power of 2, so to search in
multiple categories, simply :strong:`add` the respective codes and
pass them as value of the parameter. For example, to search for
Restaurants (1) and Pizzerias (32), pass :strong:`33` to
`categorycodefilter`::

  http://tourism.opendatahub.bz.it/api/Gastronomy?categorycodefilter=33



Tips and Tricks
~~~~~~~~~~~~~~~

.. _tour-tt1:

.. rubric:: TT1. Categorycodefilter in the Accomodation dataset.
	    
|q| In the Accommodation dataset there's no `categorycodefilter`
filter, like in the Gastronomy dataset. Is there some equivalent
filter?

|a| Accommodations belong to a different dataset, use
:strong:`categoryfilter` and the 

*****

.. _tour-tt2:

.. rubric:: TT2. `odhactive` and fields starting with `odh`.
	    
|q| What is the purpose of the `odhactive` field? And what are all
the parameters prefixed with :strong:`odh` stand for?
   
|a| `odh` simply stands for |odh|. There are fields like `active` and
`odhactive`. Datasets filtered with the former return all data sent and
validated by the dataset provider, while the latter returns those
validated by the |odh| team as well.


.. _tour-tt3:

.. rubric:: TT3. The `seed` field

|q| What is the `seed` field used for?

|a| `seed` is used in pagination, i.e., when there are two or more
pages of results, to keep the same sorting in all pages. By passing to
the API call the :literal:`null` string, no seed is generated and
there is no sorting; by passing :literal:`0`, a seed is generated and
will be used in pages from 2 onwards; By passing a predefined seed, it
will be applied to all result sets.
