How to Publish your Web Component on the |ODH| Store
====================================================

If you have developed a :term:`Web Component` that you deem useful for
the |odh| project or that can be used on top of data provided by the
|odh|, you can share it and allow other to reuse it, by making it
freely available on |odh|\'s `Web Components Store
<https://webcomponents.opendatahub.bz.it/>`_.

The only requirement for all the Web Components offered through the
Store is that they :strong:`must` be released as an :ref:`Open Source
Licence <odh-license>`, compatible with those used within the |odh|
project.

One of three alternatives can be chosen to publish a Web Component on
the Store: as a :strong:`full open source` project, as a
:strong:`forked` project, or using what we call the  :strong:`external
workflow`; the preferred being the first one.

..  Each alternative has its pros and cons, and for each one the terms

#. When using the :strong:`full open source` path, you simply hand in
   the source code of your Web Component to the |odh| team, no
   additional effort is required from your side. The code
   will be placed in in a GIT repository, and immediately made
   available through the Store. Future versions of the Web component
   are developed under the control of the |odh| team directly within
   this repository. 

#. The :strong:`forked` project way will still see the Web Component's
   source code saved in in a GIT repository, but you own full
   control of it, and decide about its future versions. The difference
   with the previous method is that the updates are done by you in
   your repository and the |odh| team will need to keep its copy
   synchronised with yours.

#. Finally, the :strong:`the external workflow` is the one is which
   nothing is saved in in a GIT repository. You will maintain full
   control of the source code and of the Web Component's development,
   including the right to pull it out of the store. Should you decide
   to follow this path, you will have to satisfy a few more
   requirements, to ensure proper integration with the Store:

   1. You need to install in the root directory of your Web
      Component's source code a suitable :file:`wcs-manifest.json`
      file, that you will receive via pull request.
   2. Your Web component must be saved (better if in `minified` form)
      under a :file:`dist` directory, e.g., as
      :file:`$ROOT/dist/widget.min.js`, where :literal:`$ROOT` is the
      root directory of your repository.
   3. You need to tag a commit on your master branch with a `semantic
      versioning` tag, to communicate to the Store that the
      corresponding version should be published (example, :literal:`git tag -a
      "v1.2.3" -m "v1.2.3"`).
    
   An example of these files and setup can be found in the published
   example of a generic map, that you can find at
   https://github.com/noi-techpark/webcomp-generic-map.

   Finally, to ensure that your Web Component is kept updated in the
   Store, suitable pull requests will be sent to your repository.


In all three cases, a repository called :strong:`origins` (hosted on
`github
<https://github.com/noi-techpark/odh-web-components-store-origins>`_
will hold a reference to each Web Component's repository, from where
all files that are necessary for its deployment including the
`manifest` file, the javascript, and logo if present-to each Web
Component's version. It is therefore important, in case the
:strong:`external workflow` has been chosen, that the URL to the Web
Component be stable, otherwise the Web Component will `not` be
available.
