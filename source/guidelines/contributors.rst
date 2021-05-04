=============================================
 GITHUB Quick Documentation for Contributors
=============================================

This section guides you in setting up on your local workstation the
(forked) git repositories needed to contribute to the |odh| project,
along with some troubleshooting concerning pull requests and merge
conflicts. For more detailed help, please refer to the online Github
help, at https://help.github.com/en.



Prerequisites
=============

In the following documentation some example names are used. Please
replace them with your names:

- You need an account on Github to be able to fork projects and
  contribute to the |odh| project.
- Replace :literal:`$USERNAME` with your username on GitHub.
- Replace :literal:`$BRANCH` with the branch name you will
  develop in your forked version.


Project Checkout
================

Before starting the development, you need to fork the original
(upstream) repository.

1. Navigate to the repository on GitHub, e.g.,
   https://github.com/noi-techpark/bdp-core.

2. Create a fork of the repository by clicking on the :strong:`Fork`
   button. If you are not logged in, you will be asked for a github
   username and password.

   .. figure:: /images/contributors/fork.png
      :scale: 33%
      :align: center

      Fork the repository.

3. Navigate to your forked repository on GitHub, e.g.,
   https://github.com/$USERNAME/bdp-core.

4. Check out the forked repository on your local machine, using the
   link that appears in your repository (see :numref:`checkout-pic`):

   .. code-block:: bash
		  
      ~$ git clone git@github.com:$USERNAME/bdp-core.git

   .. _checkout-pic:
   
   .. figure:: /images/contributors/checkout.png
      :scale: 33%
      :align: center
	      
      Clone the repository.

Create a pull request
=====================

In order to let your contribution be accepted in the |odh| code base,
you need to follow the following steps.

1. Checkout the :strong:`development` branch:
   
   .. code-block:: bash
		   
      ~$ git checkout development

2. Create a new branch from the :strong:`development` branch locally
   on your machine:
   
   .. code-block:: bash

      ~$ git checkout -b test-branch

3. Make some changes to the code and commit them:

   .. code-block:: bash

      ~$ git add -A
      ~$ git commit -m "Some commit message"

4. Push the new branch to GitHub:

   .. code-block:: bash   
		   
      ~$ git push --set-upstream origin test-branch

5. Navigate to your feature branch on Github
   (https://github.com/$USERNAME/bdp-core/pull/new/$BRANCH)
   to create a new pull request (see :numref:`create-pr`).

   .. _create-pr:

   .. figure:: /images/contributors/create-pull-request-development.png
      :scale: 33%
      :align: center
	      
      Create a pull request.

   You can write some description as well, to describe your changes.

6. Commit and push any changes of the pull request to this new branch.

7. For every commit the continuous integration pipeline will execute
   the tests and display the results in the pull request, like shown
   in :numref:`pr-ok`

   .. _pr-ok:

   .. figure:: /images/contributors/show-pull-request-ok-development.png
      :scale: 33%
      :align: center
      
      Show outcome of a pull request.

8. In addition, the detailed logs can be viewed under
   https://ci.opendatahub.bz.it.

.. _syncing-a-fork:
   
Syncing a Fork
==============

Your forked repository does not receive the updates of the original
repository automatically. To sync for example the
:strong:`development` branch of the two repositories and to keep the
forked repository up-to-date with all the latest changes of the
:strong:`development` branch from the original repository, the
following steps have to be performed.

Before you can sync your fork with the original repository (an
upstream repository), you must configure a remote that points to the
upstream repository in Git. A more detailed description for the
following steps can be found in the online Github help
https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/configuring-a-remote-for-a-fork


1. List the current configured remote repository for your fork.

   .. code-block:: bash

      ~$ git remote -v
    

2. Specify a new remote upstream repository that will be synced with the fork.

   .. code-block:: bash

      ~$ git remote add upstream https://github.com/noi-techpark/bdp-core.git
    

3. Verify the new upstream repository you've specified for your fork.

   .. code-block:: bash

      ~$ git remote -v
    
You need sync a fork of a repository to keep it up-to-date with the
original repository (upstream repository). A more detailed description
for the following steps can be found in the online Github help
https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork

1. Fetch the branches and their respective commits from the upstream
   repository. Commits to :strong:`development` will be stored in a
   local branch, :strong:`upstream/development`

   .. code-block:: bash

      ~$ git fetch upstream
    
2. Check out your fork's local :strong:`development` branch.
   
   .. code-block:: bash

      ~$ git checkout development
   
3. Merge the changes from :strong:`upstream/development` into your
   local :strong:`development` branch. This brings your fork's
   development branch into sync with the upstream repository, without
   losing your local changes.

   .. code-block:: bash

      ~$ git merge upstream/development
    
Resolving Merge Conflicts
=========================

When creating and working on a pull request, it could happen that the
destination branch of the original repository will change. These
changes could result in merge conflicts when pulling your code, like
shown in :numref:`merge-conflict-picture`.

.. _merge-conflict-picture:

.. figure:: /images/contributors/merge-conflicts-conflicts-development.png
   :scale: 33%
   :align: center
	   
   A Merge Conflict.

To resolve merge conflicts, the following steps must be performed.

1. :ref:`Sync your forked repository <syncing-a-fork>` and make sure
   your local destination (development) branch is up to date with the
   original (upstream) repository branch.

2. Check out your feature branch (replace `$BRANCH` with the actual
   branch name).

   .. code-block:: bash

      ~$ git checkout $BRANCH  

3. Merge the changes of the development branch to the feature branch.

   .. code-block:: bash

      ~$ git merge development

   The command will output the files with merge conflicts. See sample
   output in :numref:`merge-conflict-output`.

   .. _merge-conflict-output:

   .. figure:: /images/contributors/merge-conflicts-output-development.png
      :scale: 33%
      :align: center
	      
      Merge conflicts output.

4. Go the the listed files of the previous output and resolve all
   merge conflicts. The conflicts in the files begin with
   :literal:`<<<<<<<` and end with :literal:`>>>>>>>`. The
   :literal:`=======` separates the two versions.

   .. figure:: /images/contributors/merge-conflicts-solving-development.png
      :scale: 33%
      :align: center
	      
      Solving a merge conflicts.

   You can resolve a conflict by simply deleting one of the two
   versions of the code :strong:`and` the inserted helper lines
   beginning with :literal:`<<<<<<<`, :literal:`=======`, and
   :literal:`>>>>>>>`.

   If none of the two versions is completely correct, then you can
   delete the conflict entirely and write your own code to solve the
   conflict.

5. Add all resolved files to the index, commit the changes and push the
   changes to the server.
   
    .. code-block:: bash

       ~$ git add -A
       ~$ git commit
       ~$ git push
    

6. After resolving the merge conflicts, the pull request can be
   accepted.

   .. figure:: /images/contributors/merge-conflicts-resolved-development.png 
      :scale: 33%
      :align: center
	      
      A solved merge conflict. 

A more detailed description can be found in the online Github help:
https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/resolving-a-merge-conflict-using-the-command-line.
