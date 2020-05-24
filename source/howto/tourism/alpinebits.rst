.. _ab-howto:

How to access AlpineBits data
=============================

The AlpineBits Alliance strives to develop and to spread a standard
format to exchange data. In this howto, we show how to retrieve data
from the AlpineBits endpoint located at
https://alpinebits.opendatahub.bz.it/AlpineBits, by using the (Linux)
command line and in particular the :command:`curl` application.  An
example call can be seen :ref:`at the bottom <ab-request>` of this
howto.

.. note:: Alternative command line programs like :command:`wget` can
   be used as well, simply adapt the parameters described in the
   remainder of this section.

The first important thing to mention is that requests to this endpoint
need a :strong:`POST` method and an authentication token, therefore
you should specify options :literal:`--request POST` and a header
requiring `Basic` authorization and containing your token:
:literal:`--header 'Authorization: Basic <your-token>'`

Next, it is necessary to provide the correct `client protocol version`
and a `client ID`, which are two additional headers, namely
:literal:`--header 'X-AlpineBits-ClientProtocolVersion: 2017-10'` and
:literal:`--header 'X-AlpineBits-ClientID: 'My test request'`.

Concerning the client protocol version, it must be one of the
supported version mentioned in :numref:`ab-matrix`, which also
shows the actions that can be used together with the protocol.


.. _ab-matrix:

.. figure:: /images/AB-actions.png

   Matrix of the protocol versions and supported actions in AlpineBits.

Finally, to retrieve data from the AlpineBits, you need to set the
correct content type and provide an `action`. The content type is
specified in another header by :literal:`--header 'Content-Type:
multipart/form-data'`, while the action is given as a form:
:literal:`--form 'action=getVersion'`.

.. _ab-request:

Summing up what was described above, a call to the AlpineBits endpoint
looks like the following one:
	 
.. code-block:: 
		
   curl --location --request POST \
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
