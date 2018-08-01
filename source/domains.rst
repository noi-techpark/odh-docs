Project Overview
================

In this section you can find an overview of the |odh| Project and an
introduction to the available `Domains`, `APIs`, and `Datasets`.
	  
.. _domains:

.. figure:: /images/domain.png
   :width: 80%

   An overview of the |odh| Project.

In a nutshell, the |odh| Project takes data from multiple domains
(mobility, tourism, meteo), makes them available through the |odh|
with the purpose to allow third party developers (or any interested
user) to use them within their own projects, using the available APIs.

.. _available_datasets:

Domains with Available Datasets
-------------------------------

This part has been moved :doc:`to its own section <datasets>`

Available APIs
--------------

Currently, the following APIs are available from the |odh|\:

#. :strong:`Mobility APIs`
#. :strong:`SASAbus APIs`
#. :strong:`Tourism APIs`.

The first and second APIs provide datasets that belong to the
`Mobility Domain`, while the third one to datasets in the `Tourism
Domain`.

The Mobility APIs allow to access real-time data of the datasets
concerning the e-mobility, including data about e-charging stations,
availability of plugs to recharge e-cars, and so on.

The SASAbus APIs are part of the Mobility domain and allow to access
various type of data about buses and station.

The Tourism API allows to access locations (of hotels,
museums, events, and so on), points of interests, and a number of
other information about the tourism in South Tyrol.

.. _authentication:

Authentication
~~~~~~~~~~~~~~

.. note:: The authentication layer is not yet used.
	  
Authentication in |odh| is mainly used in the part of the |bdp| which
exposes data to the consumer, which means by the Reader and in every
single webservice accessing the Reader. The authentication mechanism
used is OAuth2 and follows the standard :rfc:`6749`, `The OAuth 2.0
Authorization Framework`. Authentication tokens are based on
:term:`JSON Web Token (JWT) <JSON Web Token>` as defined in
:rfc:`7519#section-3`, to send :term:`claims <claim>`.

For those not familiar with the OAuth2 mechanism, here is a quick
description of the client-server interaction:

#. The client requests the permission to access restricted resources
   to the `authorisation server`.
#. The authorisation server replies with a :strong:`refresh token` and an
   :strong:`access token`. The access token contains an expire date.
#. The access token can now be used to access protected resources on
   the `resource server`. To be able to use the access token, add it
   as a Bearer token in the Authorization header of the HTTP
   call. :strong:`Bearer` is a means to use tokens in HTTP
   transactions. The complete specification can be found in
   :rfc:`6750`.
#. If the access token has expired, you'll get a HTTP :literal:`401
   Unauthorized` response. In this case you need to request a new
   access-token, passing your refresh token in the `Authorization`
   header as Bearer token.  As an example, in |odh| datasets Bearer
   tokens can be inserted in a :command:`curl` call like follows:

   .. code-block:: bash
			    
      curl -X GET "$HTTP_URL_WITH_GET_PARAMETERS" -H "accept: */*" -H "Authorization: Bearer $TOKEN"


Here, $HTTP_URL_WITH_GET_PARAMETERS is the URL containing the API call
and "$TOKEN" is the string of the token.
