Development, Testing, and Production Environments
=================================================

.. note:: Information in this section is still provisional!

:numref:`dtp` shows the various environments which compose the whole
|odh| development process.

.. _dtp:

.. figure:: /images/DTP.svg

   Diagram showing the development, testing, and production
   environments in the |odh| project.


On the right-hand side, the internal structure of development is
shown, while on the left-hand side, how external, and potentially
worldwide collaborators can contribute to and interact with the |odh|
team.

Internally, two distinct and separate environments exist: testing and
production. The former is updated daily, while the latter only when
the expected result (be it a new feature, a bug fix, or anything else)
is ready to be published.

Both environments are updates with Continuous Integration using
Jenkins, which monitors the git repositories and updates the
environemnts.

External developers can push their own code to the git repositories
(provided they have been granted with the permission to do so) and
expect their work to be reviewed and tested by the |odh| team.
 
.. todo:: Add link to developers resources.
