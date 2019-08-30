.. |li| replace:: :literal:`{Id}`

.. _tourism-data-howto:
   
How to access Tourism Data?
===========================


.. note:: Information in this page might be updated and improved in
   the next future.
   
The purpose of this howto is to quickly introduce the structure of the
API calls, the available filters for the datasets in the Tourism
domain, and give some general and useful information about the Tourism
API.

.. include:: /howto/tourism/access.rst

.. structure of the API Calls

.. _tourism-api-call-structure:

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

.. _common-filters:

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
  `geosorted`, that is, they are listed from the nearest to the most
  far away from the selected point. The distance is calculated as the
  crow flies.
- :strong:`IdFilter` allows to extract from the dataset only the items
  with the given IDs, separated with a :literal:`,`.
- :strong:`Active` and :strong:`OdhActive`. Filters with the same
  name, with one prefixed by :strong:`Odh` refer to the same
  parameter. The difference is however important: :strong:`Active`
  indicates that the item is present in the original dataset provided,
  while :strong:`OdhActive` shows that the item has been verified by
  the |odh| team and is present in the |odh|. See discussion in tip
  :ref:`TT2 <tour-tt2>`.
- :strong:`ODHTag` allows to filter a result set according to tag
  defined by the |odh| team. These tags are mostly related with places
  to see, activities that can be carried out in winter or summer, food
  and beverage, cultural events and so on

  
.. filters in each datasets

Filters specific of a datasets
------------------------------

.. note:: This section will be available soon.


Types of input data
-------------------


.. note:: This section is :strong:`Work in Progress` and will be
   expanded with additional types of input data.

Since calls in the tourism domain are quite generic and revolve around
a few common calls (see section :ref:`tourism-api-call-structure`), we
showed a couple of filters that can be used to reduce the result set
and make the query more precise. Depending on the type of filter, a
different type of data must be entered to have a successful result,
otherwise the filter will not match. In this section we show the most
common types of data that should be provided, besides the common
strings, dates, and integers.

.. _bitmask-value:

:strong:`Bitmask` value	
   A Bitmasks value is a kind of shorthand that can be entered in a
   filter to obtain results for different types of that filter's
   accepted values. Each of the accepted values has a code that is a
   power of two (1, 2, 4, 8, and so on), hence each sum of different
   codes produces a unique number. The advantage is that, instead of
   entering multiple strings that should be matched, you simply need
   to enter a number as a filter, that is the sum of the values'
   corresponding codes. See :ref:`Example 3 <tour-ex3>`.


:strong:`Lists`
   A list is an (unordered) sequence of items. The available values
   are usually listed on the right-hand side of the filter, along with
   the separator, which is a :strong:`comma` (:strong:`,`). In a few
   cases, in which more lists are accepted as filter.

:strong:`Compound values`
   Compound values refer to those values that need a prefix before the
   type of value. See for example :ref:`Example2 <tour-ex2>` for a
   deeper explanation and  :ref:`Example 1 <tour-ex1>` for a sample
   query that fails because  a wrong compound value was supplied.


:strong:`Language`
   The descriptions of items in the dataset appear in three languages:
   Italian, German, and English. To retrieve values only in one
   language, enter :strong:`it`, :strong:`de`, or :strong:`en`,
   respectively.

