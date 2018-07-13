Project Overview
================

In this section you can find an overview of the |odh| Project and an
introduction to the available `Domains`, `APIs`, and `Datasets`.
	  
.. _domains:

.. figure:: /images/domain.png
   :width: 80%

   An overview of the |odh| project.

In a nutshell, the |odh| project takes data from multiple domains
(mobility, tourism, meteo), makes them available through the |odh|/Big
Data Platform with the purpose to allow third party developers (or any
interested parties) to use them within their own projects, using the
available APIs.

.. _available_datasets:

Domains with Available Datasets
-------------------------------

The goal of the |odh| project is to make available datasets containing
|od| about the South Tyrolean Ecosystem, to allow third party to
develop novel applications on top of them. These new application may
range from a simple processing the datasets to extract statistical
data and display the result in different graphic formats like
pie-charts, to far more complex applications that combine data from
different datasets and correlate them in some useful way.


.. note:: This page was written on |today|, hence all information
   about the availability of datasets, domains, API is correct as of
   this date. This page will be updated in due time as soon as more
   material will be made available.

As seen in :numref:`domains`, data originate from different
domains (Mobility, Tourism, and so on); they are gathered from sensors
and packed within :strong:`datasets`. `Sensors` can be for example GPS
devices installed on buses that send their real-time geographic
position

For each domain are listed the available datasets. Currently, this
section only contains datasets from the `Mobility` domain, but expect
more to be published.

.. topic:: A note about datasets.

   At the time of writing, only a few datasets are published. As
   mentioned before in this section, the goal is to expose datasets
   containing :strong:`only Open Data`, which is at the moment not the
   case for all datasets. Indeed, some of the datasets contain data
   that can not be distributed under an open licence like, e.g., CC0
   |cc0| or CC-BY-SA |bysa|. Therefore, to allow the highest possible
   data to be shared, an authentication mechanism has been
   implemented, to prevent access to the data in the datasets that has
   not yet been published as |od|\.  Please refer to section
   :ref:`authentication` for details.

Datasets in the Mobility Domain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. it.bz.geobank.echargingstation allows access to e-charging stations
   in South Tyrol and their status, including historical data and
   usage.  :integreen:`EchargingFrontEnd`.  |cc0|
#. info.opensasa.realtime Shows the real time position of buses
   operated by SASA in South Tyrol.  :sasabus:`opendata`
   |bysa|

   ..  note:: This dataset includes also the following subsets:
	      
       + info.opensasa.plandata
       + info.opensasa.stationboard
       + info.opensasa.news
       + info.opensasa.rssDE
       + info.opensasa.rssIT

#. it.bz.geobank.bluetooth	:integreen:`BluetoothFrontEnd` |cc0|
#. it.bz.geobank.linkstation	:integreen:`LinkFrontEnd` |cc0|

   
Datasets in the Tourism Domain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There is currently no dataset that contains |od| that can be accessed.


Available APIs
--------------

Currently, the following API are available directly from |odh|\:

#. :strong:`Mobility API`
#. :strong:`SASAbus API`
#. :strong:`Tourism API`.

The first and second APIs can be used with all the datasets that
belong to the `Mobility Domain`, while the third one with those that
are part of the `Tourism Domain`.

The Mobility API allows to access real-time data of the datasets
concerning the e-mobility, including data about e-charging station,
availability of plugs to recharge e-cars, and so on.

The SASAbus API is part of the Mobility domain and allows to access
various type of data about buses and station.


.. _authentication:

Authentication
~~~~~~~~~~~~~~

Authentication in |odh| is mainly used in the part of the tool which
exposes data to the consumer, which means in the Reader of the
core-module and in every single webservice accessing the Reader. The
authentication mechanism used is Oauth2 and follows the standard
:rfc:`6749`, `The OAuth 2.0 Authorization Framework`. Authentication
tokens are based on JWT as defined in :rfc:`7519#section-3`, `JSON Web
Token (JWT)` to send claims.

For those not familiar with the OAuth2 mechanism, here is a quick
description of the client-server interaction:

#. The client requests the permission to access restricted resources
   to the `authorisation server`.
#. The authorisation server replies with a :strong:`refresh token` and an
   :strong:`access token`. The access token contains an expire date.
#. The access token can now be used to access protected resources on
   the `resource server`. To be able to use the access token, add it
   as a Bearer token in the Authorization header of the HTTP
   call. :strong:`Bearer` is a means to use tokens in HTTP transaction. The
   complete specification can be found in :rfc:`6750`.
#. If the access token has expired, you'll get a HTTP :literal:`401
   Unauthorized` response. In this case you need to request a new
   access-token, and passing your refresh token in the Authorization
   header as Bearer token.  As an example, in |odh| datasets Bearer
   tokens can be inserted in a :command:`curl` call like follows:

   .. code-block:: bash
			    
      curl -X GET "$HTTP_URL_WITH_GET_PARAMETERS" -H "accept: */*" -H "Authorization: Bearer $TOKEN"


