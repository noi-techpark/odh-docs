
.. _authentication:

Authentication
--------------

The authentication layer is currently intended for :strong:`internal
use only`, therefore it is :strong:`not` necessary to use
authentication to access data provided by the Open Data Hub.
	   
While the Open Data Hub project strives to offer only Open Data, it relies on
third-party :ref:`data-providers`, which may not offer the whole
content of a dataset for public use. For this reason, an
authentication mechanism has been implemented, which does however have
no impact on users and on their use of the data.

Indeed, authentication in Open Data Hub is mainly used when exposing data to
the consumer, which means by the Reader and in every single web
service accessing the Reader, to allow the access to closed data in
each dataset only to those who are allowed to, i.e., developers and
members of the Open Data Hub team.

In the remainder of this section, we describe how authentication works
within the Open Data Hub, because this information might be of interest to
user that might become app developers for the Open Data Hub team; further
information about how to use authentication can be found in the
:ref:`dedicated howto <authentication-howto>`.

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
:rfc:`7519#section-3`, to send :term:`claims <Claim>`.

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
   header as Bearer token.  As an example, in Open Data Hub datasets Bearer
   tokens can be inserted in a :command:`curl` call like follows:

   .. code-block:: bash
			    
      curl -X GET "$HTTP_URL_WITH_GET_PARAMETERS" -H "accept: */*" -H "Authorization: Bearer $TOKEN"


Here, $HTTP_URL_WITH_GET_PARAMETERS is the URL containing the API call
and "$TOKEN" is the string of the token.
