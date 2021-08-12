Unlike browser access, that provides an interactive access to data,
with the option to incrementally refine a query, command line access
proves useful for non-interactive, one-directional, and quick data
retrieval in a number of scenarios, including:

* Scripting, data manipulation and interpolation, to be used in
  statistical analysis.
* Applications that gather data and present them to the end users.
* Automatic updates to third-parties websites or kiosk-systems like
  e.g., in the hall of hotels.

Command line access to the data is usually carried out with the
:program:`curl` Linux utility, which is used to retrieve information
in a non-interactive way from a remote site and can be used with a
variety of options and can save the contents it downloads, which can
them be send to other applications and manipulated.

The number of options required by :program:`curl` to retrieve data
from Open Data Hub's dataset is limited, usually they are not more
than 3 or 4, but their syntax and content might become long and not
easily readable by a human, due to the number of :ref:`filters
<common-filters>` available. For example, to retrieve the list of all
points of interests in South Tyrol, the following command should be
used:

.. code-block:: bash
		
   ~$ curl -X GET "https://tourism.opendatahub.bz.it/api/ODHActivityPoi?pagenumber=1&pagesize=10&type=63&subtype=null&poitype=null&idlist=null&locfilter=null&langfilter=null&areafilter=null&highlight=null&source=null&odhtagfilter=null&odhactive=null&active=null&seed=null&latitude=null&longitude=null&radius=null" -H "accept: application/json"


Your best opportunity to learn about the correct syntax and parameters
to use is to go to the :strong:`swagger interface` of the `tourism
<https://tourism.opendatahub.bz.it/swagger/ui/index>`_ or `mobility
<https://mobility.api.opendatahub.bz.it/>`_ domains and execute a
query: with the output, also the corresponding :program:`curl` command
used to retrieve the data will be shown.
