
.. _tourism-data-browser-howto:

How to use the Open Data Hub's Tourism Data Browser?
====================================================

This how-to explains the necessary steps to access and retrieve data
from the |odh|\'s tourism domain.


Data Browsing and Exploring
---------------------------

In order to access the data in the tourism domain, launch a browser
and point it to http://tourism.opendatahub.bz.it/.
   
.. _tourism-login-web:

.. figure:: /images/tourism-04.png

   The home page of the Tourism Data Browser.

Under the header and an informative message, two icons and hyperlink
in the centre of the page allow to reach the `Swagger interface
<http://tourism.opendatahub.bz.it/swagger/ui/index>`_, the quickest place from
where to access the datasets and learn how to programmatically
retrieve the data, and the `Official documentation
<https://opendatahub.readthedocs.io/en/latest/index.html>`_.

The bar at the top of the page allows to carry out a few actions:

* :strong:`ODH Open Data`. This drop-down menu allows to choose the
  dataset from which to browse the data. These can be reached also
  using the hyperlinks in the lower part of the home page.
* :strong:`Register`. This is currently not active, and redirects to
  `Log in`.
* :strong:`Log in`. Allows to access the data browser as a registered
  user, for example to add or edit some data. If you have access
  credentials, write the username (e-mail address) and password that
  were provided to you and click on :button:`Log in`. You will be
  redirected to the home page as a logged in user and from here, you
  will see the box with the permissions you have to access the various
  datasets and be able to modify data.

When you access the :strong:`ODH Data` item in the top menu, you will
be able to select a dataset among those available. As an example,
:numref:`tourism-data-filter` shows what is available in the
:menuselection:`ODH Open Data --> Activities & Pois --> Winter`
filter - in this case a list of activities that can be done during the
winter on the snow.

The page allows to further filter the results, by using search strings
and/or the list of tags underneath, to move between pages of results,
and to change language of the interface (although at the moment the
page is not fully translated in all languages!)
	    
.. _tourism-data-filter:

.. figure:: /images/tourism-05.png

   Accessing the data through filters or menu item.

If you click on the image associated to each item in the list or on
the :strong:`Detail` button, an overlay will pop up, which
contains more detailed information about that activity.

.. note:: Images in the list are displayed only if they are uploaded
   with a CC0 license.

.. _tourism-data-detail:

.. figure:: /images/tourism-06.png

   Detailed view of a :abbr:`POI (Point Of Interest)`.


Logged in Users
---------------

When you access the Tourism Data Browser using credentials that have
been provided to you by the |odh| team, the appearance of the page
slightly changes

.. _tourism-logged-in-web:

.. figure:: /images/tourism-07.png

   The home page after a successful login.


In particular, at the bottom of the page a table with the user's role
and permissions replaces the list of datasets, and an additional menu
item (:strong:`external Data Sources`) appears in the top bar,
allowing access to some more datasets.

