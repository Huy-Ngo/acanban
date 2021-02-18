Academic Evaluation
===================

This section aims to describe basic activities relating to the evaluation.
In order to build the academic integration, we let supervisors do evaluation.
In addition, academic assistant could also track student progress.
Overall, the use cases defined here are the functional requirements
for :ref:`objacademic`.

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

This use case allows Supervisor to evaluate the project.
Its flow of events can be depicted as follows:

1. Supervisor requests to evaluate the project.
2. System receives the request provide an **evaluation** and **comment**.
3. Supervisor provides evaluation with comments.
4. System receives the data and terminate the project.


Make Report
-----------

This use case allows Academic Assistant to make reports
based on the result of the project.
Its flow of events can be depicted as follows:

1. Academic Assistant requests to make a report.
2. System receives the request and displays the result of the project.
3. Academic Assistant requests to make a hard copy.
4. System responds a document file format of the report.
5. Academic Assistant downloads the file for printing purpose later.


Export Transcript
-----------------

This use case allows Academic Assistant to export transcript
based on the evaluation of Supervisor.
Its flow of events can be depicted as follows:

1. Academic Assistant requests to export the transcript.
2. System receives the request and displays the evaluation of Supervisor.
3. Academic Assistant requests to make a hard copy.
4. System responses by a document file format of the transcript.
5. Academic Assistant downloads the file for printing purpose later.
