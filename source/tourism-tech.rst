.. technical info for tourism datasets

.. _tourism-tech:

============================================
 Technical Information for Tourism Dataset
============================================

This section contains detailed technical information shared by the
datasets in the Tourism domain. The purpose of this section is
manifold:

* To know which methods are available to gather data from the domains
  via the API calls--see :ref:`tourism-api-call-structure`

* To learn how to improve responses by adding filters to the
  queries.--see :ref:`common-filters`

* Which kind of data are accepted by the API methods--see
  :ref:`tourism-input-data`

.. _tourism-api-call-structure:

Structure of the API calls
==========================

In the Tourism domain, there are a few API calls that allow to extract
the same type of data from the various datasets. Each of these calls
can prove useful in different scenarios, depending on the data
returned and is described in this section, in which the following
conventions are used:

* :literal:`{Name}` is the (case sensitive!) name of the dataset you are
  currently working with, like for example :literal:`Accomodation`.
* :literal:`{Id}` is the unique identifier of an array within the
  dataset, i.e., an item of the dataset. It is usually the first key
  of the resulting JSON output of a query.

The calls defined for every datasets are:

- :literal:`/api/{Name}` Return the whole dataset.
- :literal:`/api/{Name}/{Id}` Return only item with given :literal:`{Id}`\.
- :literal:`/api/{Name}Reduced` Return only the list of Ids and
  respective name of the items in the dataset. It is useful to create
  lists of items or just to have an overview of the dataset's items.
- :literal:`/api/{Name}Changed` Return all items that have changed
  since date :literal:`YYYY-MM-DD`
- :literal:`/api/{Name}Types` Returns all types of data present in
  the dataset, that can be later used to ask more precise queries to
  the dataset.

The following calls have been :strong:`removed` and can not be used
anymore. They have been replaced by a new filter, called `language`,
that operates on the datasets in a similar way to the
:ref:`fields-filter` and is described in section
:ref:`language-filter`.

- :strike:`/api/{Name}Localized Return the whole dataset in only
  the given language (which is a mandatory part of the query)`
- :strike:`/api/{Name}Localized/{Id} Return only item with given Id
  an in given language.`

.. _common-filters:

Filters common to all datasets
==============================

.. note:: Besides the filters available globally, for each dataset
   several additional filters are available. They are described in the
   respective swagger interface.

Filters are used within a dataset and their primary purpose is to
limit the result set according to specific parameters, although they
might not be available in every API call. Information about default
values can be found for each datasets in the `swagger interface
<https://tourism.opendatahub.com/swagger/ui/index>`_ of the API. Some
examples of their use can be found in section :doc:`/howto/tourism/tips`.

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
  the Open Data Hub team and is present in the Open Data Hub. See
  discussion in tip :ref:`TT2 <tour-tt2>`.
- :strong:`ODHTag` allows to filter a result set according to tag
  defined by the Open Data Hub team. These tags are mostly related
  with places to see, activities that can be carried out in winter or
  summer, food and beverage, cultural events and so on

Special common filters
----------------------

This section describes some useful filters that can be used on all
Tourism Datasets. Some of them relies on simpler filters, like
`field`, that is described in the :ref:`fields-filter` section
below. These filters allow to customise queries and have been
introduced for all cases for which there is no existent filter or
sorting possibilities.

.. grid::

   .. grid-item-card::
      :columns: 4
      :padding: 1
      
      rawfilter
      ^^^
      `rawfilter` can be appended to any query with the syntax
      ``?rawfilter=<filter(s)>``, in which <filter> has the generic form
      ``<field>, <value>``. These logical operators can be used to
      combine multiple filters: `eq`, `ne`, `gt`, `ge`, `lt`, `le`,
      `and`, `or`, `isnull`, `isnotnull`, `in`, `nin`

   .. grid-item-card::
      :columns: 4
      :padding: 1

      rawsort
      ^^^
      `rawsort` can be used to sort in ascending order the results of a
      query; its syntax is ``?rawfilter=<filter(s)>``. Here, `<filter>`
      is the name of a field in the result set. Multiple fields can be
      specified as comma separated, e.g.,
      ``?rawfilter=startDate,Detail.en.Title``. If a `<filter>` is prefixed with
      a dash, ``-`` sorting is reverted, i.e., output is shown in
      descending order.

   .. grid-item-card::
      :columns: 4
      :padding: 1

      removenullvalues
      ^^^

      ``?removenullvalues=true`` removes all :strong:`NULL` values from
      the query's output. While usually it's always desirable to have a
      full JSON output to be parsed, removing NULL values proves useful
      to reduce the output size or to verify data quality. By using
      ``removenullvalues``, one can check if all fields of a given entry
      are populated or not.

.. _fields-filter:

The `fields` Filter
-------------------

A recently added filter is the :strong:`fields` filter, which allows
to add to a REST request a parameter that can act on multiple keys of
a dataset entry, selecting only the entries which have a corresponding
value in the dataset. In other words, the purpose of this filter is to
retrieve only relevant information from each item in the datasets and
strip down information that is not needed or not necessary to the
purpose of the query. The `fields` filter can be used on
single-valued parameters as well as on dictionary fields.

Lets take as example the `ODHActivityPOI` dataset and its swagger
interface :stinfo:`/ODHActivityPoi`; the same approach can be used
with other datasets by simply replacing the datasets' name in the URL.

The following query will retrieve from the dataset only those item
which have a :strong:`Type` and a strong:`Active` keys defined in the
dataset::

  https://tourism.opendatahub.com/api/ODHActivityPoi?fields=Type,Active

The following query retrieves information from within a dictionary
field::

  https://tourism.opendatahub.com/api/ODHActivityPoi?fields=Detail.en.Title

In particular, all items which have a `Title` in `en`\ glish within
the `Detail` will appear in the result set of this query.

To show how it works, the following excerpt from the dataset shows how
to discover the :strong:`Detail.en.Title` elements:

.. code-block:: json-object

   "Detail": {
     "en": {
       "Title": "01 Cross Country Stadio Track Dobbiaco/Toblach",
       "Header": null,

.. _language-filter:

The `language` Filter
---------------------

The `language` filter can be seen as a special case of the more
generic `fields` filter, described in the previous section, and is
similar to the second example presented there.

The `language` filter is used to retrieve only the data stored in one
of the languages supported by the Open Data Hub. Let's build on the
example of previous section and use the `ODHActivityPOI` dataset. The
following query will retrieve all the data in the dataset that have
some information stored in English::

  https://tourism.api.opendatahub.com/v1/ODHActivityPoi?language=en

Most of the data in the Open Data Hub datasets are available in three
languages, English, German, and Italian, for which :literal:`en`,
:literal:`de`, and :literal:`it` can be used as value of the
`language` filter. Additional language in which data may be available
are: Dutch (:literal:`nl`), Czech (:literal:`cs`), Polish
(:literal:`pl`), French (:literal:`fr`), and Russian (:literal:`ru`).

.. _search-filter:

The `search` Filter
-------------------

Currently available for only a limited number of datasets, namely
Accommodations, Gastronomies, Events, Activities, Pois,
ODHActivitiesPois, and Article, this filters allows to find whether the
given string is contained in one of the field of the JSON response
sent as answer to a query.

.. _export-tourism:

Exporting and saving data
=========================

Queries to the Open Data Hub datasets always return data in JSON
format and can be saved in that format either from the browser or from
the CLI, in the latter case by simply piping the output to a file.
Additionally, it is mow possible to save data also in :abbr:`CSV (Comma
Separated value)` format.

.. warning:: This feature is currently available only for the following
   datasets:

   Accommodation, Activity, Article, District, Event, Gastronomy,
   MetaRegion, Municipality, ODHActivityPoi, Poi, Region, SkiArea,
   SkiRegion, and TourismAssociation

   However, plans are to soon have all Tourism datasets support it.

Depending on how you access the data, there are different modalities to
retrieve and save data in CSV format:

* when using a browser, append the keyword :literal:`&format=csv` to any
  query and you will be prompted to provide a name to the file that
  will contain the required data. Example:

     :apit:`Activity?fields=Id,Detail.en.Title,ContactInfos.en.CompanyName&pagesize=500`

  This query shows its JSON output on the screen. To save it, right
  click on the page and select `Save as`. ::

     :apit:`Activity?fields=Id,Detail.de.Title,ContactInfos.de.CompanyName&pagesize=500&format=csv`

  Nothing is shown on screen, but a dialog window opens that allows you
  to select a name for the file and the directory where to save it.

* When using a CLI command to query the Tourism endpoint, replace the
  header that you send with the :command:`curl` command:

  .. code:: bash

     ~$ curl -X GET "https://tourism.api.opendatahub.com/v1/Activity?fields=Id,Detail.en.Title,ContactInfos.en.CompanyName&pagesize=500" -H "accept: application/json"

  The output of this query will be in JSON format.

  .. code:: bash

     ~$ curl -X GET "https://tourism.api.opendatahub.com/v1/Activity?fields=Id,Detail.en.Title,ContactInfos.en.CompanyName&pagesize=500" -H "accept: text/csv"

  The output of this query will be in CSV format.

* When using an API Development Environment like Postman, add `accept:
  text/csv` to the Header of the request. See detailed procedure and
  screenshot can be found in the :ref:`postman-export` section of
  Postman's howto.

.. _tourism-input-data:

Types of input data
===================

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
