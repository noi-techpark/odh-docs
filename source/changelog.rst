.. _changelogs:

Changelogs
==========

.. versionchanged:: 2022.10 this section has been split, now there is
   a dedicated Changelog page for each year.

This section contains the Changelog of the |odh| project's
documentation.

* Previous to June 2020, we maintained no changelog.
* The list of changes made from June, 2020 to February, 2021 can be
  :download:`downloaded <changelog.txt>` as a text file.

* Since March 2021 we adopted a more structured approach: This section
  indeed will contain an entry for each change made to the
  documentation.

.. note:: We do not schedule regular releases of the documentation, we
   rather publish new versions `"When they are ready"`, therefore each
   `version` is identified by a string :strong:`YYYY.MM`, in which
   `YYYY` is the year and `MM` the month of the release.

.. card:: Latest changes

   In the **2023.07** release we started to restructure the |odh|
   technical documentation, because part of it was already included in
   the new |odh| portal. Most of the changes in this release are
   related to this new arrangement of the existing documentation.
          
   .. changelog::
      :version: 2023.07
      :released: 31 July 2023

      .. change::
         :tags: Changes
         :tickets: 277

         The list of :ref:`data-providers` is now available on
         https://opendatahub.com/community/.

      .. change::
         :tags: Changes
         :tickets: 278

         All the information about the licenses used for |odh|
         resources are grouped together in the same section,
         :ref:`datasets-license`, .
              
      .. change::
         :tags: Changes
         :tickets: 279

         The material in section :ref:`devels-resources` was mostly
         outdated or obsolete, and has been replaced with a summary
         and a link to developer's `Flight Rules
         <https://github.com/noi-techpark/documentation/blob/main/README.md>`_,
         which are constantly updated by the developers themselves.

      .. change::
         :tags: Changes
         :tickets: 280

         All the content of the :ref:`quickstart` has been moved to the
         |odh| Portal and is now replaced with a link to the Portal's *Quickstart*.

      .. change::
         :tags: improvements
         :tickets: 281

         The ``hidemail.py`` python script used to obfuscate e-mail
         addresses with a proper Sphinx extension.

      .. change::
         :tags: Improvements
         :tickets: 288

         A few changes to make this technical documentation site more
         similar to the |odh| portal. In particular, 

         * The logo is updated
         * There are some new CSS rules
         * The *Open Sans* fonts are now used throughout the Documentation
         * External links open in a new tab
         * A favicon was added
         
      .. change::
         :tags: Bugfix
         :tickets: 289

         As required by the readthedocs.org rules, configuration file
         :file:`.readthedocs.yaml` is included in the docs for a
         correct build.
         
*****

.. toctree::
   :hidden:
   :glob:
          
   changelogs/*
