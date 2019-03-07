Tourism API Howto
=================

This howto explains how to use the Tourism API developed by the |odh|
team.

There are two possibilities to interact with the data exposed by the
|odh|'s Tourism API: You can simply browse the data using the
dedicated portal or you can retrieve data and manipulated them within
your application. The former method is described in
:ref:`data-explore-tourismAPI`, while the latter is described in the
next section.

.. _data-access-tourismAPI:

Data Access and Manipulation
----------------------------

All the APIs available for the tourism domain can be accessed from the
same URL through their swagger interface:
http::/tourism.opendatahub.bz.it/swagger

For most of the Tourism domain datasets you need credentials to access
the data. Go to the abovementioned URL and click on `Expand
Operations` on the far right-hand side of :strong:`LoginAPI`.  In the
panel that opens (see :numref:`tourism-login`), fill in the
:monospace:`loginmodel` with your username and password.

.. _tourism-login:

.. figure:: /images/tourism-01.png

   Login mask of the Tourism API 


To make it simpler, you can click on the `Example value` on the
right-hand side of the page and fill in the appropriate values for
:strong:`username` and :strong:`pswd`. Click on :button:`Try it out`
to generate a new access token that will be needed for any further
request (see :numref:`tourism-token`).

.. _tourism-token:

.. figure:: /images/tourism-02.png

   Successful Token received from the LoginAPI.

After you have clicked on the button, the panel will expand and
present some more data, the most important are the :strong:`Curl` and
:strong:`Response Body` sections. In the first one, you can see the
:strong:`POST` call send from the API in curl format: you can use its
content to write scripts that fetch data and automatise data fetching.

The :strong:`Response Body` section contains the answer to the call
sent and is a JSON-formatted string that contains a few data, the most
important of which are:

* The :strong:`access_token`, needed for any access to the data
* The :strong:`expires_in`, the validity in seconds of the access
  token before its expiration.

To avoid writing every time the token in the API methods, copy and
paste :strong:`only` the token without quotes from the response body
into the textfield on the right-hand side textfield on top of the page
(see :numref:`tourism-add-token`), then click on
:greenswbutton:`Explore` to store the token and cache it for
all the next queries.

.. _tourism-add-token:

.. figure:: /images/tourism-03.png

   Caching the received token into the tourism' swagger interface.

Using Command Line Tools
~~~~~~~~~~~~~~~~~~~~~~~~

If you plan to access the API methods with command line tools like
:command:`curl` or :command:`wget`, or only from scripts, you need to
add an authentication header to each call. For example, using curl:

.. parsed-literal::

   curl -X GET --header 'Accept: application/json' --header \\
   'Authorization: Bearer vLwemAqrLKVKXsvgvEQgtkeanbMq7Xcs' \\
   'http://tourism.opendatahub.bz.it/api/Gastronomy'

.. note:: The string of the token is shortened for the sake of
   clarity. 

It is important to mention that the authorisation header reaquires the
following syntax: :strong:`Authorization: Bearer`, followed by the
whole `string` of the token.

One you have retrieved the data, which come in JSON format, you can
process and manipulate them with a tool like `jq
<https://github.com/stedolan/jq>`_.

.. seealso:: More detailed documentation of the exposed API methods
   can be found on http://tourism.opendatahub.bz.it/Help.

   
.. _data-explore-tourismAPI:

Data Browsing and Exploring
---------------------------

If you need to only browse data, you can do so by pointing a browser
to http://tourism.opendatahub.bz.it/. On the right-hand side of the
page, you can see a box that shows the permissions to access data that
you have as a (non-logged in) user, while the remainder of the page
provides an overview of the various component of the project and its
architecture.

If you try to access the :strong:`ODH Data` item in the top menu, you
will see that it is empty. In order to access data, you need to click
on the :strong:`Login` button on the top right corner of the page.

.. _tourism-login-web:

.. figure:: /images/tourism-04.png

   Logging in to the CMS portal.

Write the username (email address) and password that was provided to
you and click on the :button:`Log in`. You will be redirected to the
home page as a logged in user and from here, you will see the box with
the permissions you have to access the various types of data.

If you now try to access the :strong:`ODH Data` item in the top menu,
you will be able to select some dataset. As an example,
:numref:`tourism-data-filter` shows what is available in the
:menuselection:`ODH Data --> Activities & Pois --> Winter` filter - in
this case a list of activities that can be done during the winter on
the snow.

The page allows to further filter the results, by using search strings
and/or the list of tags underneath, to move between pages of results,
and to change language of the interface (although at the moment the
page is not fully translated in all languages!)
	    
.. _tourism-data-filter:

.. figure:: /images/tourism-05.png

   Accessing the data through filters or menu item.

If you click on one of the images in the list will pop up an overlay
with more detailed information about that activity.

.. _tourism-data-detail:

.. figure:: /images/tourism-06.png

   Detailed view of a :abbr:`POI (Point Of Interest)`.


