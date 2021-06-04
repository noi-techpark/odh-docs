Changelog
=========

.. versionadded:: 2021.03 Add extension to provide structured
   Changelogs

.. contents:: Available Changelogs:
   :local:
                  
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

.. changelog::
   :version: 2021.03
   :released: 31 March 2021

   .. change::
      :tags: Improvement
      :tickets: 194

      Add :strong:`changelog` extension.

   .. change::
      :tags: Bugfix
      :tickets: 199

      Fix layout of datasets in :ref:`Other Domains <other-domains-datasets>`.

   .. change::
      :tags: Improvement
      :tickets: 203

      Add AlpineBits to the :ref:`data-access` section.

.. changelog::
   :version: 2021.04
   :released: 30 April 2021


   .. change::
      :tags: Improvement
      :tickets: 206

      Add to each dataset a direct permalink that can be copied and
      sent to third party.

   .. change::
      :tags: Improvement
      :tickets: 208

      * Replace tabs in the howto list with subsections.
      * Remove the mobility howto for deprecated API v1.
      * Reduce size of images in howtos and align them if layout
        allows.

   .. change::
      :tags: Bugfix
      :tickets: 208

      Add correct images to `How to Access Analytics Data in the
      Mobility Domain` howto.

   .. change::
      :tags: New Feature
      :tickets: 204

      New Howto: :ref:`howto-r`

   .. change::
      :tags: Bugfix
      :tickets: 212

      * Remove drop downs from all the lists of :ref:`datasets
        <mobility-datasets>` (Mobility, Tourism, Other)
      * fix the panel's width to avoid scrollbars whenever possible.

   .. change::
      :tags: Bugfix
      :tickets: 213

      Add troubleshooting section to :ref:`R howto <howto-r>`.

.. changelog::
   :version: 2021.05
   :released: 31 May 2021

   .. change::
      :tags: Improvement
      :tickets: 209

      A lot of improvements have been added to the general structure
      of the documentation, the most important being:

      * reorder ToC and make some section more prominent
      * made bash code snippets more usable
      * made accessing methods more immediate to see

      For more details, please check the reference.

   .. change::
      :tags: Improvement
      :tickets: 214
                
      The technical content of the `getting started` howtos has been
      moved to the `Datasets` section, making them
      shorter. Also a few examples have been added to :ref:`get-started-mobility`.

.. changelog::
   :version: 2021.06
   :released: 30 June 2021

   .. change::
      :tags: Change, Improvement
      :tickets: 220

      The Tourism domain was modified and improved in several points,
      which are reflected in the documentation:

      * New Swagger and API URLs
      * Localised methods have been definitely removed
      * A new `extlink` to shorten URLs of tourism API in the
        documentation source code has been introduced
      * The :ref:`tourism-data-howto` article has been modified to
        include the API browsable interface
      * Tourism datasets have been ordered lexicographically
