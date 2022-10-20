
Some datasets in the |odh|, namely :dataset:`Accommodations
<tourism/accommodation_one/>`, :dataset:`Gastronomy
<tourism/activitiesandpois_four/>`, and :dataset:`Events
<tourism/events/>` , are organised into a `Virtual Knowledge Graph`
that can be accessed using SPARQL from the dedicated `SPARQL endpoint
<https://sparql.opendatahub.bz.it>`_. In order to define more precise
queries, this section describes the Knowledge Models (`KM`) underlying
these datasets; the description of each |km| is accompanied by an UML
diagram which shows the KM at a glance.


Besides standard W3C's OWL and RDF vocabularies, the |odh| VKG
uses:

* `schema.org <https://schema.org/>`_ for most of the entities used
* `geosparql
  <http://schemas.opengis.net/geosparql/1.0/geosparql_vocab_all.rdf#>`_
  for geo-references and coordinates of objects
* `Dublin Core's purl
  <https://dublincore.org/specifications/dublin-core/dcmi-terms/>`_
  for linking to related resources

.. grid::

   .. grid-item-card::
      :columns: 8
      
      Common Notation
      ^^^^^^^^^^^^^^^

      Diagrams use UML class diagram formalism widely adopted in
      Knowledge Representation and in particular in the `W3C's
      Recommendation` documents for the Semantic Web.  The following
      additional notation applies:

      Prefix
         The default prefix used for classes and properties is
         :strong:`https://schema.org/`. This means that, unless
         differently stated, the definition of classes and properties,
         including their attributes, rely on a common standard as defined
         in schema.org's vocabulary. As examples, see the
         `LodgingBusiness <https://schema.org//LodgingBusiness>`_ class and
         the `containedInPlace <https://schema.org/containedInPlace>`_
         property.

         .. hint:: Other prefixes are explicitly pre-pended to the
            Class or Property name, like e.g., `noi:numberOfUnits`.

      Arrows
        Arrows with a white tip denote a `sub-class` relationship, while
        black tips denote `object properties`.

      Cardinality
        Cardinality of :strong:`1` is usually not shown, but implied; the
        `look across
        <https://www.quora.com/How-do-we-read-cardinality-in-a-UML-diagram-or-in-E-A-diagram>`_
        notation is used. For example, the image on the right-hand
        side--excerpt from the :ref:`event dataset <event-dataset-kg>`
        VKG--can be read as `0 to N` :strong:`MeetingRoom`\s are
        `ContainedInPlace` :strong:`Place`.


   .. grid-item-card::
      :columns: 4
      :img-background: /images/sparql/cardinality.png
      
.. _mobility-domain-kg:

.. dropdown:: Mobility Domain

   .. grid::
      
      .. grid-item-card::
         :columns: 12

         The entire mobility domain has a unique underlying knowledge
         model, which encompasses all the datasets and therefore also
         allows an easier creation of cross-dataset queries. Since the
         mobility domain gathers data from `sensors`, useful in this
         domain is also the :abbr:`SOSA (Sensor, Observation, Sample, and
         Actuator)` ontology, which uses :strong:`sosa` as prefix. You
         can check the Classes and Properties of SOSA in the `W3C's
         dedicated wiki page
         <https://www.w3.org/2015/spatial/wiki/SOSA_Ontology>`_

         The central concept is :strong:`Station`, of which all
         :literal:`StationType`\s are subclass, while
         :strong:`Observation`, :strong:`LatestObservation`, and
         :strong:`ObservableProperty` are used to provide time-related
         information of the data gathered and relate to
         :strong:`Sensor`. Together with :strong:`Platform`,
         :strong:`Sensor` make the relation between a `Station` and its
         `Sensors`: For example, sensor `EChargingPlug` ``isHostedby`` an
         `EChargingstation` `Platform`, which is also a `Station`.

         The knowledge model is completed by the :strong:`Feature`
         superconcept, which contains also :strong:`Municipality` and
         :strong:`RoadSegment`, the latter defined by an
         `hasOriginStation` and an `hasDestinationStation`.

      .. grid-item-card::
         :columns: 12

         .. figure:: /images/sparql/odh-mobility.png
            :width: 100%

            The UML diagram of the :ref:`Mobility Domain
            <mobility-datasets>`.

.. _accommodation-dataset-kg:

.. dropdown:: Accommodation Dataset

      .. grid::
         :gutter: 1
                  
         .. grid-item-card::
            :columns: 12
            
            .. postalAddress has one attribute more in Event than in other
               datasets.

            Central class in this dataset is :strong:`LodgingBusiness`, to
            which belong multiple :strong:`Accommodation`\s.

            A :strong:`LodgingBusiness` has as attributes `geo:asWKT`,
            `email`, `name`, `telephone`, and `faxNumber` and relations

            * `address` to class :strong:`PostalAddress`, which
              consists of `streetAddress`, `postalCode`, and
              `AddressLocality`
            * `geo`, i.e., a geographical location, to class
              :strong:`GeoCoordinates`, consisting of `latitude`,
              `longitude`, and `elevation`

            There are (sub-)types of :strong:`LodgingBusiness`--called
            :strong:`Campground`, :strong:`Hotel`, :strong:`Hostel`, and
            :strong:`BedAndBreakfast`--sharing its attributes and relations.

            An :strong:`Accommodation` is identified by a `name` and a
            `noi:numberOfUnits` and has relations

            * `containedInPlace` to :strong:`LodgingBusiness`
              (multiple :strong:`Accommodation`\s can belong to it)
            * `occupancy` to :strong:`QuantitativeValue`, which gives
              the `maxValue` and `minValues` of available units of
              accommodation and a `unitCode`.

            +++

            `noi:numberOfUnits` is the number of available
            rooms, suites, apartments, etc. that are available in that
            :strong:`Accommodation`

            `geo:asWKT` is a method used by opengis.net's `geosparql
            <https://www.geosparql.org/>` to express geographic coordinates
            in a standard, textual form based on :abbr:`WKT (Well-known
            text)`.

         .. grid-item-card::
            :columns: 12

            .. figure:: /images/sparql/odh-accommodation.png
               :width: 100%

               The UML diagram of the :dataset:`Accommodations
               <tourism/accommodation_one/>` dataset.

.. _gastronomy-dataset-kg:

.. dropdown:: Gastronomy Dataset

   .. grid::
      :gutter: 1

      .. grid-item-card::

         The main class of this dataset is :strong:`FoodEstablishment`,
         described by `geo:asWKT`, `description`, `name`, `telephone`,
         and `url`.

         A :strong:`FoodEstablishment` has

         * a :strong:`PostalAddress`--consisting of
           `streetAddress`, `postalCode`, and `AddressLocality`--as
           `address`
         * a :strong:`GeoCoordinates`--`latitude`, `longitude`, and
           `elevation`--as a geographical location `geo`

         There are different (sub-)\types of
         :strong:`FoodEstablishment`, all sharing the same attributes:
         :strong:`Restaurant`, :strong:`FastFoodRestaurant`,
         :strong:`BarOrPub`, :strong:`Winery`, and
         :strong:`IceCreamShop`.


         +++

         `geo:asWKT` is a method used by opengis.net's `geosparql
         <https://www.geosparql.org/>` to express geographic coordinates
         in a standard, textual form based on :abbr:`WKT (Well-known
         text)`.

      .. grid-item-card::

          .. figure:: /images/sparql/odh-food-establishment.png
             :width: 100%

             The UML diagram of the :dataset:`Gastronomy
             <tourism/activitiesandpois_four/>` dataset.


.. _event-dataset-kg:

.. dropdown:: Event Dataset

   .. grid::
      :gutter: 1

      .. grid-item-card::

         The main classe in this dataset is :strong:`Event`, described by
         a `startDate`, an `endDate`, and a `description`.  Every
         :strong:`Event` has an `organizer`, either a :strong:`Person` or
         an :strong:`Organization` and a `location`.

         A :strong:`Person`--identified by `givenName`, `familyName`,
         `email`, and `telephone`--`worksFor` an :strong:`Organization`,
         which has a `name` and an `address`, i.e., a
         :strong:`PostalAddress` consisting of `streetAddress`,
         `postalCode`, `AddressLocality`, and `AddressCountry`.

         Finally, an :strong:`Event` has as `location` a
         :strong:`MeetingRoom`--identified by a `name`-- which is
         `containedInPlace` a :strong:`Place`--which has also a `name`

      .. grid-item-card::

         .. figure:: /images/sparql/odh-event.png
            :width: 100%

            The UML diagram of the :dataset:`Events <tourism/events/>` 
            dataset.

.. seealso::

   The :ref:`SPARQL howto <howto-sparql>`, which guides you in
   interacting with the SPARQL endpoint.

   W3C Recommendation for `OWL2
   <https://www.w3.org/TR/2012/REC-owl2-syntax-20121211/>`_ and `RDF
   <https://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/>`_.

   Official Specification of `UML Infrastructure
   <https://www.omg.org/spec/UML/2.1.2/Infrastructure/PDF/>`_ are
   available from `Object management group <https://www.omg.org/>`_
