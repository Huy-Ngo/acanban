Database Design
===============

For academic evaluation, some extra information is needed.
The following tables has extra fields:

- ``Project``
- ``Task``

Each of them is described in following sections.


Project
-------

Each ``Project`` will be evaluated by the supervisor, and must have
a final report.  Therefore, we need following fields:

``evaluation`` : ``number``
   Final evaluation of the project.  It can be based on previous evaluation
   of individual tasks.

``report`` : ``File`` or ``array`` of ``File``
   A file that contains the report(s) for the group project.


Task
----

Evaluation of the tasks can be useful for the final evaluation of the project.

``evaluation`` : ``number``
   The evaluation of the task
