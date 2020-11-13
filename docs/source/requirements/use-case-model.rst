Use-Case Model
==============

.. uml::

   left to right direction
   actor Student
   actor Staff
   actor Admin
   actor Lecturer

   usecase "Create project" as CreateP
   usecase "Join project" as JoinP
   usecase "Create tasks" as CreateT
   usecase "Join tasks" as JoinT
   usecase "Complete tasks" as Complete
   usecase "View results" as View
   usecase Evaluate
   usecase "Send message" as Msg

   usecase Search

   usecase Register
   usecase Login
   usecase Logout

   usecase "Make Report" as Report
   usecase "Export transcript" as Export

   usecase "Maintain system" as Maintain

   Staff --> Search
   Staff --> Export
   Staff --> Report
   Staff --> Login
   Staff --> Register
   Staff --> Logout

   Student --> Search
   Student --> CreateP
   Student --> CreateT
   Student --> JoinP
   Student --> JoinT
   Student --> Complete
   Student --> Msg
   Student --> Login
   Student --> Register
   Student --> Logout

   Lecturer --> View
   Lecturer --> Evaluate

   Admin --> Maintain

   Lecturer <|-- Student

   Admin <|-- Lecturer
   Admin <|-- Staff


Create Project
--------------

Brief Description
^^^^^^^^^^^^^^^^^

This use case allows Student or Lecturer to create a new project.

Flow of Events
^^^^^^^^^^^^^^

Basic Flow
""""""""""

1. Student/Lecturer request to create a project.
2. System receive the request and request user to fill in a form.
3. The user turn in the form.
4. System process the form and create a new project.

Alternative Flow
""""""""""""""""

Missing information
   In step 4, if the user missed some information, the system display an error message.
   The user can either select to cancel operation or fill in missing fields.

Existing project
   In step 4, if the user is Lecturer and the project is existed,
   the system display an alert message and cancel the operation.

Special Requirements
^^^^^^^^^^^^^^^^^^^^

None.

Pre-Conditions
^^^^^^^^^^^^^^

User must be Student or Lecturer and be logged into the system
before this use case begins.

Post-Conditions
^^^^^^^^^^^^^^^

The system state is unchanged.

Extension Points
^^^^^^^^^^^^^^^^

None.


Join Project
------------

Brief Description
^^^^^^^^^^^^^^^^^

This use case allows Student or Lecturer to join an existing project.

Flow of Events
^^^^^^^^^^^^^^

Basic Flow
""""""""""

1. Student/Lecturer request to join the project.
2. System process the request and allow user to join the project.

Alternative Flow
""""""""""""""""

Project is full
   In step 2, if the user is Student and the project already has 5 Student,
   the system display an error message and cancel the operation.

   In step 2, if the user is Lecturer and the project already has 1 Lecturer,
   the system display an error message and cancel the operation.

Special Requirements
^^^^^^^^^^^^^^^^^^^^

None.

Pre-Conditions
^^^^^^^^^^^^^^

User must be Student or Lecturer and be logged into the system
before this use case begins.

There must be existing project so that user could join.

Post-Conditions
^^^^^^^^^^^^^^^

The system state is unchanged.

Extension Points
^^^^^^^^^^^^^^^^

None.


Create Tasks
------------

Brief Description
^^^^^^^^^^^^^^^^^

This use case allows Student or Lecturer to generate tasks for the project.

Flow of Events
^^^^^^^^^^^^^^

Basic Flow
""""""""""

1. Student/Lecturer request to generate tasks the project.
2. System receive the request and request user to provide meta data.
3. User provides necessary data.
4. System receive the data and update tasks list.

Alternative Flow
""""""""""""""""

Task is existed
   In step 4, if the user entered a task that is already existed in task list,
   the system display an error message and terminate the operation.

Missing meta data
   In step 4, if user missed to enter some data, (e.g: deadline for the task),
   the system display an alert message. User can either fill in missing fields
   or cancel the operation.

Special Requirements
^^^^^^^^^^^^^^^^^^^^

None.

Pre-Conditions
^^^^^^^^^^^^^^

User must be Student or Lecturer and be logged into the system
before this use case begins.

Post-Conditions
^^^^^^^^^^^^^^^

The system state is unchanged.

Extension Points
^^^^^^^^^^^^^^^^

None.


Join Tasks
----------

Brief Description
^^^^^^^^^^^^^^^^^

This use case allows Student to join task(s) in the project.

Flow of Events
^^^^^^^^^^^^^^

Basic Flow
""""""""""

1. Student request to join task(s) in the task list.
2. System receive the request and allow Student to join the task(s).

Alternative Flow
""""""""""""""""

None.

Special Requirements
^^^^^^^^^^^^^^^^^^^^

None.

Pre-Conditions
^^^^^^^^^^^^^^

User must be Student and be logged into the system
before this use case begins.

Post-Conditions
^^^^^^^^^^^^^^^

The system state is unchanged.

Extension Points
^^^^^^^^^^^^^^^^

None.


Complete Tasks
--------------

Brief Description
^^^^^^^^^^^^^^^^^

This use case allows Student to complete task(s) in the project.

Flow of Events
^^^^^^^^^^^^^^

Basic Flow
""""""""""

1. Student request to complete task(s) in the task list.
2. System receive the request and request Student to hand in evidences.
3. Student submit files or image as evidences.
4. System receive evidences and mark task(s) as completed

Alternative Flow
""""""""""""""""

No evidences provided
   In step 3, if student did not submit files,
   the system display an alert message and terminate the operation.

Empty files provided
   In step 4, if student submit empty files,
   the system display an alert message and terminate the operation.

Special Requirements
^^^^^^^^^^^^^^^^^^^^

None.

Pre-Conditions
^^^^^^^^^^^^^^

User must be Student and be logged into the system
before this use case begins.

Post-Conditions
^^^^^^^^^^^^^^^

The system state is unchanged.

Extension Points
^^^^^^^^^^^^^^^^

None.


View result
-----------

Brief Description
^^^^^^^^^^^^^^^^^

This use case allows Lecturer to view result of the project.

Flow of Events
^^^^^^^^^^^^^^

Basic Flow
""""""""""

1. Lecturer request to view the result of the participating project.
2. System receive the request and provides results.

Alternative Flow
""""""""""""""""

None.

Special Requirements
^^^^^^^^^^^^^^^^^^^^

None.

Pre-Conditions
^^^^^^^^^^^^^^

User must be Lecturer and be logged into the system
before this use case begins.

Post-Conditions
^^^^^^^^^^^^^^^

The system state is unchanged.

Extension Points
^^^^^^^^^^^^^^^^

None.


Evaluate
--------

Brief Description
^^^^^^^^^^^^^^^^^

This use case allows Lecturer to evaluate the project.

Flow of Events
^^^^^^^^^^^^^^

Basic Flow
""""""""""

1. Lecturer request to evaluate the project.
2. System receive the request provide an evaluation form.
3. Lecturer fill in the form and submit.
4. System receive the data and terminate the project.

Alternative Flow
""""""""""""""""

Missing information

   If in step 3, the Lecturer missed to fill in a necessary field,
   the system display an alert message. Lecturer can either fill in missing fields
   or cancel the operation. 

Special Requirements
^^^^^^^^^^^^^^^^^^^^

None.

Pre-Conditions
^^^^^^^^^^^^^^

User must be Lecturer and be logged into the system
before this use case begins.

Post-Conditions
^^^^^^^^^^^^^^^

After this use case ends, other project-related use case could not be executed.

Extension Points
^^^^^^^^^^^^^^^^

None.