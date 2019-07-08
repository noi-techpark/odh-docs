
The domains intended as sources for data served by the |odh| are
depicted in :numref:`domains-diagram`.
 
The :strong:`API` of a software contains the definition of methods and of
their signatures, that can be invoked to retrieve data from the web
services provided by the software itself. The signature of each method
defines how to invoke the method (i.e., the name of the method), which
parameters should be supplied (i.e., their names and types, if they
are mandatory or not, and what the method returns (i.e., the type and
format of the output produced by the method. By using an API, it is
possible to receive data from the web service and process them.

Currently, the following :term:`APIs <API>` are available from the
|odh|\:

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
--------------

.. note:: The authentication layer is currently intended for internal
   use only.
	  
Authentication in |odh| is mainly used when exposing data to the
consumer, which means by the Reader and in every single web service
accessing the Reader, to allow the access to closed data in each
dataset only to those who are allowed to.

There are currently two different authentication methods available:

* The :strong:`Token-based Authentication`, defined in :rfc:`6750`,
  requires that anyone who wants to access resources supply a valid
  username and password and becomes a Bearer Token that must be used
  to access the data. After the token expires, a new one must be
  obtained. This type of authentication is used for the datasets in
  the tourism domain.

* The :strong:`OAuth2 Authentication` follows the :rfc:`6749` and is
  used for all the datasets in the mobility domain. 

The OAuth2 authentication mechanism  Authentication tokens are
based on :term:`JSON Web Token (JWT) <JSON Web Token>` as defined in
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
