
.. role:: greenbtn
.. role:: blackbtn
   
How to insert and modify NOI Events?
====================================

After reading this article, you will be able to use the |odh| tourism
portal to insert, modify, and delete events that take place at NOI
Techpark in Bolzano (in the remainder, :strong:`NOI events`).

Preliminaries
-------------

Since you must login to create events, you need valid credentials to
be able to add NOI events, that you should have received from the
|odh| team.

Go to http://tourism.opendatahub.bz.it and click on Log in (top right
corner)

.. figure:: /images/events/login.png
   :width: 90%

   Upper section of the tourism portal.

Provide your credentials, then you will be redirected to your
homepage, that shows among other information, the roles you have
within the |odh|\.


Creation of a new NOI Event
---------------------------

Once logged in, click on :menuselection:`ODH Data --> Events NOI -->
Events EURAC NOI` (see :numref:`newevent`).

.. note:: The drop-down menu that you will see might differ from those
   shown in the screenshot, depending on your permissions.
   
.. _newevent:

.. figure:: /images/events/newevent.png
   :scale: 70%

   Menu item to create a new event

You will now see a list of events that will take place at Bolzano's
NOI Techpark today or in the next days. For each event, the
description, start and end date, and the location where it takes place
are shown. If the event is marked as :strong:`Active`, it is displayed
on the official NOI web page at https://today.noi.bz.it/.

.. figure:: /images/events/eventlist.png
   :width: 90%

   List of events.

In order to add a new event, click on the :greenbtn:`New` button to
create a new event.

In the dialog that opens, fill in all the fields you deem necessary,
but at least the title, organiser, location, and time.

.. figure:: /images/events/createevent.png
   :width: 90%

   An example event with a few details provided.

Remember to tick the `Active` and `noi.bz.it Active` checkboxes: The
latter allows the event to show up on https://today.noi.bz.it/.

If the event is set to take place in more rooms, click on the
:button:`Room Management` button to add more rooms and time slots to
the event.

If the event has a web page and/or a video trailer, you can add a link
to them in the `Web Page (URL)` and `Video (URL)` text-fields.

It is even possible to add images to the event, by clicking on the
`Images` tab on top of the dialog and then on :button:`Choose File` to
upload a file. For each image, a few information can be added:

* The author's name.
* The licence used for the image, either :strong:`Proprietary` or
  :strong:`CC0`. |cc0-badge|

  .. hint:: We prefer that a :strong:`CC0` licence be used; it is
     neccessary to have the rights to upload the photo with
     :strong:`CC0`.

* The position of the image within the gallery, if you upload more
  than one image. Image in position :strong:`0` will be the cover page
  of the gallery

When you have provided all the necessary information, click on
:blackbtn:`Create` to create the event, which will now show up in the
list.

.. _listedevent:

.. figure:: /images/events/listedevent.png
   :width: 90%

   List with the new event.

Note that the title of the event is shown in the list in the language
selected in the GUI (German in :numref:`listedevent`).
	   
If you later need to modify the event, click  on the :button:`Edit`
button next to the event in the event list. For example, suppose the event
used throughout this howto needs to be modified, because the meeting
had to be postponed by one hour (10:00 to 13:00, instead of 9:00 to
12:00). Also the room is not available anymore, therefore it must be
changed as well. These changes are shown in picture
:numref:`modifyevent`.

.. _modifyevent:

.. figure:: /images/events/modifyevent.png
   :width: 90%

   Changing  event's details.
   
Click on :blackbtn:`Save` to save the modified event.

To delete an event, click on the :blackbtn:`Delete` button next to the
event, then confirm your choice in the confirmation dialog that will
appear.
