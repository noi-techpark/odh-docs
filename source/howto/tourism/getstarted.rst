
.. _tourism-data-howto:
   
How to access Tourism Data?
===========================

.. versionchanged:: 2021.05 moved technical info to dataset section
   
The purpose of this howto is to quickly introduce the structure of the
API calls, the available filters for the datasets in the Tourism
domain, and give some general and useful information about the Tourism
API.
	 
.. _data-access-tourismAPI:
   
Data Access and Manipulation
----------------------------

All the APIs available for the tourism domain can be accessed from the
same URL through their Swagger user interface:
http://tourism.opendatahub.bz.it/swagger/ui/index

.. versionchanged:: 2019-May new and easier procedure to authenticate
   and to store credentials.

With the introduction on the Tourism API graphic interface of a newer
swagger version, supplying and storing the token has become easier,
making older procedures deprecated or obsolete. Moreover, in the new
GUI, for every API method is shown whether it can provide Open Data as
a result and if not, it will be necessary to authenticate.

Authentication is easy and, unlike it happened in the past, it does
require only to supply your credentials. From the swagger UI, click on
the :strong:`Authorize` button on the right-hand side of the page
(shown in the bottom-right corner in :numref:`tourism-ui`).

.. _tourism-ui:

.. figure:: /images/tourism-01.png
   :scale: 33%
   :align: center

   The new Swagger UI for Tourism domain.

A dialog window will pop up; here, supply your username and password,
and click on :strong:`Authorize`. It is not necessary to change any
other parameter.

.. _tourism-auth:

.. figure:: /images/tourism-02.png
   :scale: 33%
   :align: center

   Providing credentials for authentication.

After a few seconds a new dialog replaces the one used for
authentication, whose most important bit is the :strong:`Authorized`
word, that means you are now authenticated. No additional step is now
necessary: the browser will remember the token. Click on
:strong:`Close` to close the dialog window start browsing the Tourism
data.

.. _tourism-auth-ok:

.. figure:: /images/tourism-03.png
   :scale: 33%
   :align: center

   Successful authentication.

To log out, click again on :strong:`Authorize` in the Swagger UI (see
:numref:`tourism-ui`), then on :strong:`Logout`.

Using Command Line Tools
~~~~~~~~~~~~~~~~~~~~~~~~

If you plan to access the API methods with command line tools like
:command:`curl` or :command:`wget`, or only from scripts, you need to
add an authentication header to each call. For example, using curl:

.. code-block:: bash

   ~# curl -X GET --header 'Accept: application/json' \
   --header 'Authorization: Bearer vLwemAqrLKVKXsvgvEQgtkeanbMq7Xcs' \
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
