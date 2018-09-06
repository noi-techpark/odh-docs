.. _authentication-howto:

How to use authentication
=========================

As described in section :ref:`authentication`, there are two methods
to access protected data in the dataset: Basic and OAuth2
authentication. Both authentication methods can be used within a
browser or from the command line, with only slight differences. In
this section we show how to use authentication within the |odh|\,
provided that you owe an username and a password to access the closed
data in the datasets.

To obtain the credentials, please address your enquiry to the contact
email of the dataset you would like to access.


Basic authentication
--------------------

Basic authentication can be used with the :ref:`tourism-datasets`.

.. rubric:: If you use a browser.

Go to the swagger interface of the API (in our example we use the
:ref:`accomodation dataset <accomodation-dataset>`). Here,
authentication can be used simply by trying to execute an API call. As
:numref:`basic-auth` shows, click on the :button:`Try it out!` button
and a new dialog will appear, in which you can supply the username and
password. This method is convenient if you need to call one method at
a time.
 
.. _basic-auth:

.. figure:: /images/basic-auth.png
   :width: 80%

   Authentication for one API call. 

However, if you need to execute multiple API call on the same dataset,
a more useful method is to insert the username and password directly
in the two appropriate fields on top of swagger interface (they are
framed in red in :numref:`advanced-auth`).

.. _advanced-auth:

.. figure:: /images/advanced-auth.png
   :width: 80%

   Authentication for multiple API call.

.. rubric:: If you use the Command Line Interface.

Open a shell on your workstation and use a tool like :command:`curl`
or :command:`wget`, with the appropriate options:

.. option:: -X

   Specify the request method (GET)

.. option:: --header, -H

   Add extra header information to be included in the request.

Note that the :option:`--header` option is used twice: The first to
receive the answer in :strong:`text/html` format, the second to
provide the credentials required to access protected content.

.. code:: bash

   curl -X GET --header 'Accept: text/html' --header 'Authorization: Basic dGVzdDp0ZXN0aGFsbG8=' 'http://service.suedtirol.info/api/Accommodation'

   
OAuth2 authentication
---------------------

OAuth2 authentication can be used in all the :ref:`mobility-datasets`
that are marked with the |auth| badge, so pick one dataset and go to
its swagger interface, whose URL is provided together with the
information of the dataset.

.. note:: As of |today|\, authentication is not yet publicly
   available, so the following guidelines can not yet be put in
   practice.

.. rubric:: If you use a browser
	  
Make sure you have obtained a valid username and password, then open
the :command:`/rest/refresh-token` method and write you username and
password in the two :strong:`user` and :strong:`pw` fields,
respectively, as shown in :numref:`token-request`. 

.. _token-request:
.. figure:: /images/token-request.png
   :width: 80%

   Request a new OAuth2 token.

If your credentials are valid, you will receive a new token, otherwise
the response will be a :strong:`401 Unauthorized` error message.

The token you received can be used in any of the API's methods that
require authorisation. A sample call is shown in figure
:numref:`oauth-success`. Note the syntax of the :file:`Autorization`
parameter: You must use prefix the authentication token with the
:strong:`Bearer` string, followed by an empty space, then by the
token.


.. _oauth-success:
.. figure:: /images/emobility-200.png
   :width: 80%

   A successful call to a method requiring authentication.

In case you do not respect the Authorization+space+token sequence, use
additional separators in the sequence (like :numref:`oauth-failure`
shows), or use an invalid token, you will receive an :strong:`401 -
Unauthorized` HTTP response.

.. _oauth-failure:
.. figure:: /images/emobility-401.png
   :width: 80%

   A failed call to a method requiring authentication.

.. rubric:: If you use the Command Line Interface.

Like in the case of basic authentication, API calls can be done using
a tool like :command:`curl` or :command:`wget`, with the same
:option:`-X` and :option:`--header` options, with the slight
difference that the :option:`--header` option is used twice: The first
to require the format of the response, the second to provide the
credentials.

.. code:: bash

   curl -X GET "http://bdp-test-env.b7twwguhyj.example.com/emobility/rest/get-records?station=83&name=CP1-Tignale&seconds=50" --header "Accept: */*" --header 'Authorization: Bearer <token>'

Make sure to replace the <token> with the actual token you received.
