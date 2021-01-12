Use-Case Model
==============

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


