.. _ab-howto:

How to access Open Data Hub AlpineBits Server as a client
=========================================================

In this howto, we show how to retrieve data from the AlpineBits Server
endpoint for the Open Data Hub located at
https://alpinebits.opendatahub.bz.it/AlpineBits, by using the (Linux)
command line--in particular the :command:`curl` application, and the
popular `Postman` API development environment.  An example call can be
seen :ref:`at the bottom <ab-request>` of this section.

.. note:: Alternative command line programs like :command:`wget` can
   be used as well: simply adapt the parameters described in the
   remainder of this section.

The first important thing to mention is that requests to this endpoint
need a :strong:`POST` method and an authentication token, therefore
you should specify options :literal:`--request POST` and a header
requiring `Basic` authorization and containing your token:
:literal:`--header 'Authorization: Basic <your-email-address>'`

.. note:: While there is no authorization required to access the Open Data
   Hub AlpineBits Server, we strongly suggest you to insert as token
   your email address for debugging reasons. It will help trace your
   calls in the case you require support from the Open Data Hub Team.

Next, it is necessary to provide the correct `client protocol version`
and a `client ID`, which are two additional headers, namely
:literal:`--header 'X-AlpineBits-ClientProtocolVersion: 2017-10'` and
:literal:`--header 'X-AlpineBits-ClientID: 'My test request'`.

Concerning the client protocol version, it must be one of the
supported version mentioned in :numref:`ab-matrix`, which also
shows the actions that can be used together with the protocol.
 
.. _ab-matrix:

.. table:: Matrix of the protocol versions and supported actions in
   the AlpineBits implementation of the Open Data Hub.

   +--------------------------+---------+---------+---------+---------+
   | Open Data Hub AlpineBits | 2017-10 | 2017-10 | 2018-10 | 2018-10 |
   | Server Actions           |   PUSH  |   PULL  |   PULL  |   PUSH  |
   +--------------------------+---------+---------+---------+---------+
   | FreeRooms                | Yes     | No      | Yes     | No      |
   +--------------------------+---------+---------+---------+---------+
   | GuestRequests            | --      | --      | --      | --      |
   +--------------------------+---------+---------+---------+---------+
   | Inventory Basic          | Yes     | Yes     | Yes     | Yes     |
   +--------------------------+---------+---------+---------+---------+
   | Inventory HotelInfo      | Yes     | Yes     | Yes     | Yes     |
   +--------------------------+---------+---------+---------+---------+
   | RatePlans                | --      | --      | --      | --      |
   +--------------------------+---------+---------+---------+---------+
   | BaseRates                | --      | --      | --      | --      |
   +--------------------------+---------+---------+---------+---------+

Note that PUSH and PULL refer to the action of uploading to and
downloading from AlpineBits Server, respectively.
   
Finally, to retrieve data from the AlpineBits Server, you need to set
the correct content type (i.e., `multipart/form-data`) and provide an
`action`. The content type is specified in another header by
:literal:`--header 'Content-Type: multipart/form-data'`, while the
action is given as a form: :literal:`--form 'action=getVersion'`.

.. _ab-request:

Summing up what was described above, a call to the AlpineBits Server endpoint
looks like the following one:
	 
.. code-block:: 
		
   ~# curl --location --request POST \
   'https://alpinebits.opendatahub.bz.it/AlpineBits' \
   --header 'Authorization: Basic <your-token-here>' \
   --header 'X-AlpineBits-ClientProtocolVersion: 2017-10' \
   --header 'X-AlpineBits-ClientID: 'My test request' \
   --header 'Content-Type: multipart/form-data' \
   --form 'action=getVersion'

Here, you can see that the additional option :literal:`--location` is
used, that will make sure to resend the request in case a
:strong:`3xx` HTTP error code is received, i.e., if the requested
resource has been moved.

Postman Setup
-------------

In Postman, you need to enter the same data as in the call shown in
previous section. The Postman setup equivalent to that call is shown
in the two screenshots.

.. _ab-postman-header:

.. figure:: /images/postman/AB-postman1.png
   :scale: 50%
   :align: center

   Definition of the call's headers.

In the headers you need to add all the parameters as in the curl
version, except for the authentication: this option need to be
specified in the `Authorization` tab of postman. Here, choose
:strong:`Basic Auth` as type and use :strong:`someuser` and
:strong:`secret`  as username and password, respectively.

.. note:: It is suggested to use, instead of `someuser` and `secret`,
   your contact information, in order to be able to contact you for
   some technical reasons.

Next, you need to add, in Postman's `Body` tab, the :literal:`action`.
Choose :strong:`form-data`, enter :strong:`action` as key and the name
of the method to retrieve data, in our example :strong:`getVersion`.

.. _ab-postman-body:

.. figure:: /images/postman/AB-postman2.png
   :scale: 50%
   :align: center

   Definition of the `action` and the outcome of the call.

Once done, make sure to select :strong:`POST`, then click on
:button:`Send` and you will receive the result in the bottom part of
Postman's window, like in :numref:`ab-postman-body`.

.. seealso:: More information about the interaction with AlpineBits
   can be found in the official documentation, available at
   https://www.alpinebits.org/hoteldata/.


