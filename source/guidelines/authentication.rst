
.. _authentication-hub:

Authentication in the Open Data Hub
-----------------------------------

The authentication layer is currently intended for :strong:`internal
use only`, therefore it is :strong:`not` necessary to use
authentication to access data provided by the Open Data Hub.
	   
While the Open Data Hub project strives to offer only Open Data, it
relies on third-party :ref:`data-providers`, which may not offer the
whole content of a dataset for public use. For this reason, an
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
   header as Bearer token.  As an example, in Open Data Hub datasets
   Bearer tokens can be inserted in a :command:`curl` call like
   follows:

   .. code-block:: bash
			    
      ~$ curl -X GET "$HTTP_URL_WITH_GET_PARAMETERS" -H "accept: */*" -H "Authorization: Bearer $TOKEN"


Here, :literal:`$HTTP_URL_WITH_GET_PARAMETERS` is the URL containing the API call
and :literal:`$TOKEN` is the string of the token.

.. _authentication-internal:

Authentication To Internal Infrastructure
-----------------------------------------

.. versionchanged:: 2020.10 Authentication to internal infrastructure
   does not require :literal:`client_secret` and credentials anyumore 

Access to the Open Data Hub's internal infrastructure requires
authentication, which is provided by :strong:`Keycloack`, an Open
Source software that provides Identity and Access Management. In a
nutshell, it acts as a broker to provide Single Sign On to different
web sites and services; it also seamlessly interacts with
Kerberos. More information and use cases can be found in the `official
documentation <https://www.keycloak.org/documentation>`_.

.. note:: By `internal infrastructure` we mean also the access to Open
   Data that are already available to the Open Data Hub Team but not
   yet to the Data Consumers, and therefore require authentication.

Source code for both the authentication server and a few pre-cooked
examples of applications configured to connect to it can be found in
dedicated repository created by the Open Data Hub Team: the
`authentication server
<https://github.com/noi-techpark/authentication-server-examples>`_.

Quick howto
~~~~~~~~~~~

.. note:: This howto describes the :strong:`old guidelines` to access
   authentication to |odh|\s internal infrastructure. A newer version
   of :literal:`odh-generic-client` has been implemented, that does
   not require anymore credentials and a
   :strong:`client_secret`. Therefore, all :command:`curl` examples
   below can be safely used without all the corresponding options;
   credentials can be used for testing purposes, as explained in the
   `repository's README.md
   <https://github.com/noi-techpark/authentication-server-examples/blob/master/readme.md>`_
   file.

   More information in the `dedicated repository
   <https://github.com/noi-techpark/authentication-server-examples>`_.


In order to access the internal infrastructure, you need first to get
a token, then use it together with the API. Both steps can be achieved
using command-line tools, for a programmatic access to the date, which
is the method shown here.

.. rubric:: Request an access token

In order to receive an access token, you need in advance to have credentials for
the Open Data Hub. If you do not have them, please open a ticket on
issues.opendatahub.bz.it or send an email to :email:`help@opendatahub.bz.it`.
The same holds, if you plan to create an application that retrieves closed data
from the Open Data Hub. For this, also other OAuth2 flows exist.

With your username and password, and a client secret (:strong:`my_username`,
:strong:`my_password`, :strong:`the_client_secret`), the access token is granted
to you with the following call:

.. code-block:: bash
   :name: grant-token
   :caption: Receiving an access topic

   curl -X POST -L "https://auth.opendatahub.bz.it/auth/realms/noi/protocol/openid-connect/token" \
   --header 'Content-Type: application/x-www-form-urlencoded' \
   --data-urlencode 'grant_type=password' \
   --data-urlencode 'username=my_username' \
   --data-urlencode 'password=my_password' \
   --data-urlencode 'client_id=odh-generic-client' \
   --data-urlencode 'client_secret=the_client_secret'

Since the token expires after a given amount of time, it might prove
necessary to refresh it, an action that can be done by replacing the
parameters given in the query above with

.. code-block::
   :name: refresh-token
   :caption: Refreshing the access token

   curl -X POST -L "https://auth.opendatahub.bz.it/auth/realms/noi/protocol/openid-connect/token" \
   --header 'Content-Type: application/x-www-form-urlencoded' \
   --data-urlencode 'grant_type=refresh_token' \
   --data-urlencode 'refresh_token=the_refresh_token' \
   --data-urlencode 'client_id=odh-generic-client' \
   --data-urlencode 'client_secret=the_client_secret'

Here, use the refresh token received from :numref:`grant-token`.


.. rubric:: Retrieve data with the token.

Once you received the access token, it is easy to use it in actual
requests. The following API call shows how to get all
:strong:`sname`\s and :strong:`mvalue`\s from the VMS dataset:

.. code-block::
   :name: get-closed-data
   :caption: Retrieving data with the access token

   curl -X GET "https://mobility.api.opendatahub.bz.it/v2/flat/VMS/*/latest?select=sname,mvalue" \
   --header 'Content-Type: application/json' \
   --header 'Authorization: bearer your-access-token'

Currently, data retrieved from the Open Data Hub are always open,
except for some of the latest values and historical data: Only a
subset of `m`\-prefixed data from the :literal:`/latest` and
:literal:`/from/to` API calls can be closed date. See section
:ref:`api-v2-structure`) for more information about the API calls.
