	 
.. _data-access-tourismAPI:
   
Data Access and Manipulation
----------------------------

All the APIs available for the tourism domain can be accessed from the
same URL through their swagger interface:
http::/tourism.opendatahub.bz.it/swagger

For most of the Tourism domain datasets you need credentials to access
the data. Go to the abovementioned URL and click on `Expand
Operations` on the far right-hand side of :strong:`Login (Get Bearer
Token)`.  In the panel that opens (see :numref:`tourism-login`), fill
in the :monospace:`username` and :monospace:`password` with your
credentials.

.. note:: :strong:`The Bearer Token Login` method replaces the
   previous one, :strong:`LoginAPI`, which is not available anymore.

.. _tourism-login:

.. figure:: /images/tourism-01.png

   Login mask of the Tourism API.

Click on :button:`Try it out` to generate a new access token that will
be needed for any further request (see :numref:`tourism-token`).

.. _tourism-token:

.. figure:: /images/tourism-02.png

   Token assigned to the user.

After you have clicked on the button, the panel will expand and
present some more data, the most important are the :strong:`Curl` and
:strong:`Response Body` sections. In the first one, you can see the
:strong:`POST` call sent from the API in curl format: you can use its
content to write scripts that fetch data and automatise data fetching.

The :strong:`Response Body` section contains the answer to the call
and is a JSON-formatted string that contains a few data, the most
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
   'http\://tourism.opendatahub.bz.it/api/Gastronomy'

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
