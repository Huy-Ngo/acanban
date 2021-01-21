Academic Evaluation
===================

.. uml::

   left to right direction
   actor "Academic Assistant" as assist
   actor Supervisor

   usecase Evaluate

   usecase "Make Report" as Report
   usecase "Export transcript" as Export

   assist --> Export
   assist --> Report

   Supervisor --> Evaluate


Evaluate
--------

Brief Description
^^^^^^^^^^^^^^^^^

This use case allows Supervisor to evaluate the project.

Flow of Events
^^^^^^^^^^^^^^

Basic Flow
""""""""""

1. Supervisor requests to evaluate the project.
2. System receives the request provide an **evaluation** and **comment**.
3. Supervisor provides evaluation with comments.
4. System receives the data and terminate the project.

Alternative Flow
""""""""""""""""

Missing information

   If in step 3, the Supervisor forgets to fill in a necessary field,
   the system will display an alert message.
   Supervisor can either fill in missing fields or cancel the operation. 

Pre-Conditions
^^^^^^^^^^^^^^

User must be a Supervisor and be logged in the system
before this use case begins.

Post-Conditions
^^^^^^^^^^^^^^^

After this use case ends, other project-related use cases could not be executed.


Make Report
-----------

Brief Description
^^^^^^^^^^^^^^^^^

This use case allows Academic Assistant to make reports
based on the result of the project.

Flow of Events
^^^^^^^^^^^^^^

Basic Flow
""""""""""

1. Academic Assistant requests to make a report.
2. System receives the request and displays the result of the project.
3. Academic Assistant requests to make a hard copy.
4. System responds a document file format of the report.
5. Academic Assistant downloads the file for printing purpose later.

Alternative Flow
""""""""""""""""

Project is not finished
   If in step 2, Student has not provided the result, the system will display
   a message that the report is not yet ready and terminate the operation.
   The system will then notify Student by sending an email or via
   notification bar.

Pre-Conditions
^^^^^^^^^^^^^^

User must be Academic Assistant and be logged in the system before this use case begins.

Academic Assistant must search and select the project(s) before the use case begins.

Post-Conditions
^^^^^^^^^^^^^^^

The system state is unchanged.


Export Transcript
-----------------

Brief Description
^^^^^^^^^^^^^^^^^

This use case allows Academic Assistant to export transcript based on the evaluation of Supervisor.

Flow of Events
^^^^^^^^^^^^^^

Basic Flow
""""""""""

1. Academic Assistant requests to export the transcript.
2. System receives the request and displays the evaluation of Supervisor.
3. Academic Assistant requests to make a hard copy.
4. System responses by a document file format of the transcript.
5. Academic Assistant downloads the file for printing purpose later.

Alternative Flow
""""""""""""""""

Not yet evaluated
   If in step 2, Supervisor has not given the evaluation, the system will display
   a message that the transcript is not ready yet and terminate the operation.
   The system will then notify Supervisor by sending an email or via
   notification bar.

Pre-Conditions
^^^^^^^^^^^^^^

User must be Academic Assistant and be logged in the system before this use case begins.

Academic Assistant must search and select the project(s) before the use case begins.

Post-Conditions
^^^^^^^^^^^^^^^

The system state is unchanged.
