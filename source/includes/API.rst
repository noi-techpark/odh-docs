
The APIs are composed of a few generic methods, that can be combined
with many parameters to retrieve only the relevant data and then
post-processed in the preferred way.

The following table summarises how the two versions of the API can be
used within the Open Data Hub's domains.

=== ============  =============
API  Tourism      Mobility
=== ============  =============
v1   Recommended  |deprecated|
v2   --            Recommended
=== ============  =============


There are currently two versions of the API, v1 and v2, with the
former now :strong:`deprecated` for the Mobility domain and marked as
such |deprecated| throughout the Open Data Hub documentation. New
users are recommended to use the new API v2, while users of the API v1
are encouraged to plan a migration to the new API.

The new API v2 has a different approach compared to the previous
version, and therefore is not compatible with the API v1, the main
difference being that all data stored in the Open Data Hub can now be
retrieved `from a single endpoint`, while with API v1 there was an
endpoint for each dataset.

This change in approach requires also a breaking change for the users
of API v1. The initial step, indeed, will not be to open the URL of
the dataset and start exploring, but to retrieve the
:literal:`stationType`\s and then retrieve additional data about each
station. A :literal:`stationType` is the main object of a datasets,
about which all the information in a dataset relate to; a dataset
includes at least one :literal:`stationType`.  A new, dedicated howto
describing in detail the new API v2 and a few basic examples is
:ref:`already available <get-started-mobility>` in the dedicated
section of this documentation.

.. note:: It is important to remark that the API v2 is :strong:`only
   available` for datasets in the :strong:`Mobility` Domain.
