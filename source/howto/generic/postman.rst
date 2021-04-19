.. role:: orange

How to set up Postman (API Development Environment)?
-----------------------------------------------------

Postman is a popular API development environment, that is, a tool that
is used (among other useful features) to ease the interaction with API
calls to remote sites. In this tutorial, we show the few steps
necessary to set Postman to connect to the |odh| datasets in both the
mobility and tourism domains.

In the remainder of this tutorial, we will use as example the
:ref:`E-chargin station <echarging-dataset>` dataset, located at
https://swagger.opendatahub.bz.it/?url=https://mobility.api.opendatahub.bz.it/v2/apispec#/Mobility%20V1%20-%20Emobility/
for the mobility domain and the :ref:`Accommodation
<accommodation-dataset>` dataset, located at :stinfo:`Accommodation`.


Initial Setup
~~~~~~~~~~~~~

After Postman has been launched, click on the :orange:`New` button,
then on :orange:`Request` to start the configuration of the |odh|
endpoints, like shown in :numref:`postman1`.

.. _postman1:

.. figure:: /images/postman/newrequest.png

   Start of a new request creation.

In the dialog window that opens, write the URL of the endpoint in the
`Request name` textfield and assign it in the ODH collection, see
Figure :numref:`postman2`.

.. hint:: If no collection has already been created, create one by
   clicking on :orange:`+ Create collection`, then write :strong:`ODH` and
   confirm.

Click on :button:`Save to ODH` to start querying the endpoint.

Repeat the procedure for the Accommodation dataset and for any other
dataset you want to query. 

.. _postman2:

.. figure:: /images/postman/newendpoint.png

   Defining a new endpoint in the mobility domain.

It is now possible to start querying the endpoints, by providing next
to the :strong:`GET` button the corresponding call, like shown in
:numref:`postman3` for the E-charging station dataset and in
:numref:`postman3` for the Accommodation dataset. However, while the
former images shows a set of results, on the latter appears the
message `Authorization has been denied for this request.` and the
status :green:`401 Unauthorized`.

.. do not wordwrap the table!
   
.. table::

   +----------------------------------------------+-------------------------------------------+ 
   | .. _postman3:                                | .. _postman4:                             |
   |                                              |                                           |
   | .. figure:: /images/postman/postman8.png     | .. figure:: /images/postman/postman1.png  |
   |    :width: 90%                               |    :width: 90%                            |
   |                                              |                                           |
   |    Querying the `E-charging station`         |    Querying the `Accommodation`           |
   |    endpoint.                                 |    endpoint.                              |   
   +----------------------------------------------+-------------------------------------------+

The reason is that the data contained in that dataset have not (yet)
been published as open data, therefore authentication is necessary.
This is where Postman proves useful, since it can request
authentication tokens (OAuth2 in the case of |odh|), store them, and
use them whenever the are needed.


Getting a new Authorisation Token
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To request a new authorisation token, click on `Authorization` right
below the GET request, then select OAuth 2.0 as the `Type`.

Now, in the right-hand side of the window, write the URL that manages
the tokens (for the tourism domain, this is
http://tourism.opendatahub.bz.it/token and click on the :button:`Get
New Access Token` button (:numref:`postman6`).

.. _postman6:

.. figure:: /images/postman/postman3.png

   Requesting an access token.

In the dialog window that opens fill in all the necessary fields, like
shown in :numref:`postman7`, selecting :strong:`Password Credentials`
as the `Grant Type`, then click on :button:`Request Token`. Make sure
you have received the username and password to obtain the token, and
give it a name easy to remember.

.. _postman7:

.. figure:: /images/postman/postman4.png

   A filled-in token request.

If your credentials are correct and the request is successful, the
dialog window will be replaced by another one containing the access
token and a few details about it, including its validity and expire
date, see :numref:`postman8` and :numref:`postman9`.

.. do not wordwrap the table!
   
.. table::

   +----------------------------------------------+-------------------------------------------+ 
   | .. _postman8:                                | .. _postman9:                             |
   |                                              |                                           |
   | .. figure:: /images/postman/postman5.png     | .. figure:: /images/postman/postman6.png  |
   |    :width: 90%                               |    :width: 90%                            |
   |                                              |                                           |
   |    An access token.                          |    Information about an access token      |
   +----------------------------------------------+-------------------------------------------+


It is now possible to select the token: Select :strong:`Opendatahub
Tourism` from the `Available Tokens` drop-down menu (see
:numref:`postman6`), click on `Body` and repeat the GET request. You
should be able to see now the data in the dataset, like shown in
:numref:`postman10`.

.. _postman10:  

.. figure:: /images/postman/postman7.png

   Access to data requiring authorisation.

.. _postman-export:
   
Data Exporting
~~~~~~~~~~~~~~
   
By default, queries to the Open Data Hub return data in JSON format
and postman does not need any setup for that. It is however possible,
for some datasets in the Tourism domain--check :ref:`export-tourism`
section for the list, to have postman receive data in :abbr:`CSV (Comma
Separated Value)`. The required set up is shown in
:numref:`postman-exp-fig`: in the `Header` tab under the query, add a
key :strong:`Accept` with value :strong:`text/csv`.

.. _postman-exp-fig:

.. figure:: /images/postman/postman-export.png

   Exporting data from the Tourism domain in CSV format.
