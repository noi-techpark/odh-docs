Licenses and TOS for the |odh| material
=======================================

.. versionadded:: 2021.08 statistics about Tourism's Open Data and
   images with CC0 licence.

.. versionchanged:: 2021.08 move `Licenses for ODH resources` subsection
   from Dataset section

The resources that are part of the |odh| Project are subject to
different licenses, which are described in section
:ref:`odh-license`\. Derivative material built using |odh| material is
also subjected to different licenses, depending on its purpose, as
shown in :numref:`floss-lm`.

.. _floss-lm:

.. figure:: images/FLOSS-LM.png
   :scale: 50%
   :align: center

   Licenses for the |odh| and derivative material.

The FLOSS four freedoms
-----------------------

The `four essential freedoms` are the four basic principle to which a
software program must comply to be defined free software. As stated on
the `What is free software?
<https://www.gnu.org/philosophy/free-sw.html>`_ web page (on which you
can find a lot more information and details), they are:

* The freedom to run the program as you wish, for any purpose
  (:strong:`freedom 0`).
* The freedom to study how the program works, and change it so it does
  your computing as you wish (:strong:`freedom 1`).. Access to the
  source code is a precondition for this.
* The freedom to redistribute copies so you can help others
  (:strong:`freedom 2`).
* The freedom to distribute copies of your modified versions to others
  (:strong:`freedom 3`). By doing this you can give the whole
  community a chance to benefit from your changes. Access to the
  source code is a precondition for this.

.. _odh-license:

Licenses for |odh| resources
----------------------------

The |odh| Project processes dataset, possibly supplied by third-party
sources (i.e., :ref:`data-providers`), which may contain closed data;
however, only Open Data are returned to the users' queries.

According to the main goal of the |odh| Project, we have defined
licenses for its different components and we use badges across the
documentation for a better visibility. As a rule of thumb, we try to
do our best to deliver :strong:`Open Data`, by developing
:strong:`Free/Open Source software` that is publicly available on
github, and by using an :strong:`Open Standard` for the API used to
access data.

These licenses are applied to the |odh| components:

* All the :strong:`software` released within the |odh| is Free software and
  complies with the GPLv3 license.  |gpl| Code repositories can be
  found at https://github.com/noi-techpark.
* The :strong:`Datasets` currently expose only Open Data that are in
  the public domain, so they are released as CC0. |cc0|
* The :strong:`APIs` have no license yet, since we are in the process to define
  which among the CC licenses could fit best. See :numref:`dac-lm` for
  an overview and quick description of CC licenses and derivative
  material.

CC0 Licensed Data
~~~~~~~~~~~~~~~~~

Open Data Hub provides a live updated table about the number of CC0
licensed data it contains. Please note, this data is calculated on
some datasets and does not consider all datasets of the whole Open
Data Hub yet.

https://databrowser.opendatahub.bz.it/Home/LicenseStatus

.. note:: There is an additional clarification about the licence for
   any content that is retrieved from the datasets in JSON format,
   which is detailed in Section :ref:`license-json-records`.

.. _dac-lm:

.. figure:: images/DAC-LM.png
   :scale: 50%
   :align: center

   Creative Common Licenses and derivative material.

.. include:: /includes/json-license.rst

   
APIs Terms of Service
---------------------

The |odh| project is already used in production for NOI internal
projects, and in particular it is the data hub used by the South
Tyrolean tourism portal, https://www.suedtirol.info/en/.

The public API are in early development and therefore should be still
considered as a :strong:`beta` version. If any third party would like
to use a stable version of the APIs in its production environment, a
special agreement must be signed with `NOI techpark
<https://noi.bz.it/en>`_. You can contact |contact| for any information.
