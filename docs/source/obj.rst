Objective
=========

In this project, we aimed to develop a collaboration platform
for students and mentors.  The resulting system should be able to
not only integrate well into their workflows and academic management tasks
but also effectively perform on back-end servers often with limited resources
and across a wide variety of end-user machines.

The Collaboration Platform
--------------------------

At the lowest level, discussion would be facilitated through comment threads,
organized into logical tasks.  The tasks would be categorized by stages
such as *to-do*, *doing* and *done*.  These stages would then be visualized
as columns in a `Kanban board`_ to aid managing and prioritizing tasks.

The Academic Integration
------------------------

In addition to discussion and job scheduling, the system-to-be would
support academic tasks.  To mentors and committees, these are grading
and giving feedback.  To academic assistants, these include (but not
limited to) exporting transcripts and statistical reports, and tracking
students' overall progress to provide help if necessary.

The Applicable Web Application
------------------------------

The system should be implemented as a web application for
portability |~| [mikkonen2008]_.  It should be easy to be adopted by users on
different devices network connection quality, whilst being simple enough
to be maintained by a few administrators to run on modest hardware.

.. _Kanban board: https://en.wikipedia.org/wiki/Kanban_board
.. [mikkonen2008] Tommi Mikkonen and Antero Taivalsaari.
   "Web Applications---Spaghetti Code for the 21st Century".
   *2008 Sixth International Conference on Software Engineering Research,
   Management and Applications*, p. 319--328, Prague, 2008.
   :doi:`10.1109/SERA.2008.16`.
