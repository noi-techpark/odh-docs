.. |li| replace:: :literal:`{Id}`

Getting Started Guide For Tourism Domain
========================================


.. note:: Information in this page might change in the next future.
   
The purpose of this howto is to quickly introduce the structure of the
API calls, the available filters for the datasets in the Tourism
domain, and give some general and useful information about the Tourism
API.


.. structure of the API Calls

Structure of the API calls
--------------------------

In the Tourism domain, there are a few API calls that allow to extract
the same type of data from the various datasets. Each of these calls
can prove useful in different scenarios, depending on the data
returned and is described in this section, in which the following
conventions are used:

* :literal:`{Name}` is the (case sensitive!) name of the dataset you are
  currently working with, like for example :literal:`Accomodation`. 
* |li| is the unique identifier of an array within the
  dataset, i.e., an item of the dataset. It is usually the first key
  of the resulting JSON output of a query.

The calls defined for every datasets are:

- :literal:`/api/{Name}` Return the whole dataset.
- :literal:`/api/{Name}/{Id}` Return only item with given |li|\.
- :literal:`/api/{Name}Localized` Return the whole dataset in only
  the given language (which is a mandatory part of the query).
- :literal:`/api/{Name}Localized/{Id}` Return only item with given Id
  an in given language.
- :literal:`/api/{Name}Reduced` Return only the list of Ids and
  respective name of the items in the dataset. It is useful to create
  lists of items or just to have an overview of the dataset's items.
- :literal:`/api/{Name}Changed` Return all items that have changed
  since date :literal:`YYYY-MM-DD`	    
- :literal:`/api/{Name}Types` Returns all types of data present in
  the dataset, that can be later used to ask more precise queries to
  the dataset.

.. common filters

Filters common to all datasets
------------------------------

Filters are used within a dataset and their primary purpose is to
limit the result set according to specific parameters. They might not
be available in every API call. information about default values can
be found for each datasets in the `swagger interface
<http::/tourism.opendatahub.bz.it/swagger>`_ of the API. Some examples
of their use can be found in section :doc:`tips`.

.. note:: This section is :strong:`Work in Progress` and might be
   expanded.

- :strong:`Seed` is used to set pagination. See tip :ref:`TT3
  <tour-tt3>`.
- :strong:`Locfilter` is a composed parameters that uniquely
  identifies a location within South Tyrol. See example :ref:`EX2
  <tour-ex2>` for a detailed example.
- :strong:`Latitude` and :strong:`Longitude` are used to identify the
  (absolute) positioning of a location, point of interest, event, or
  any other type of object. They must be entered in decimal form
- :strong:`Radius` it is the distance in meter prom a geographical
  point. It can be used together with latitude and longitude to
  broaden the search for an object. The results are automatically
  `geosorted` from the nearest to the most far away from the selected
  point.  
- :strong:`IdFilter` allows to extract from the dataset only the items
  with the given IDs, separated with a :literal:`,`.
- :strong:`Active` and :strong:`OdhActive`. Filters with the same
  name, with one prefixed by :strong:`Odh` refer to the same
  parameter. The difference is however important: :strong:`Active`
  indicates that the item is present in the original dataset provided,
  while :strong:`OdhActive` shows that the item has been verified by
  the |odh| team and is present in the |odh|. See discussion in tip
  :ref:`TT2 <tour-tt2>`.


.. filters in each datasets

Filters specific of a datasets
------------------------------

.. note:: This section will be available soon.


..
   Accommodation

   http://tourism.opendatahub.bz.it/api/AccommodationTypes

   Board à per il boardiflter

   Type à per il typefilter

   Category à per il categoryfilter

   Theme à per il themefilter

   Badge à per il badgefilter

   SpecialFeature à per featurefilter



   Qua si trovono tutti “Features” che un accommodation puo avere

   http://tourism.opendatahub.bz.it/api/AccommodationFeatures


   Gastronomy



   http://tourism.opendatahub.bz.it/api/GastronomyTypes
   CategoryCode à categorycodefilter

   Etc…



   Event

   http://tourism.opendatahub.bz.it/api/EventTopics
   eventTopic à topicfilter





   Activity

   http://tourism.opendatahub.bz.it/api/ActivityTypes
   activitytypefilter


   Poi

   http://service.suedtirol.info/api/PoiTypes
   poi type filter




   ODH Activity POI



   Qua ce da dire che ODH Activity Poi é una specie di container di tutti Activities & Pois provvenienti da diverse Sources.

   Qua noi ne dobbiamo parlare internamente perché per un terzo é difficile capire perché esistono 3 Endpoints con Activity + Pois .... magari lascieremo solo questo........



   http://tourism.opendatahub.bz.it/api/ODHActivityPoiTypes
   per il filtro

   type, subtype, poitype







   Articles



   http://tourism.opendatahub.bz.it/api/ArticleTypes
   per l’articlestypefilter




   Common sarebbe il menu dove sono tuti calls con

   -Regions, Metaregions, Districts, Municipality, Skiarea, Skiregion, Tourismassociations etc…

   Common non ha tipi dentro



   Poi esistono ancora



   Webcams

   -Lista di Webcams

