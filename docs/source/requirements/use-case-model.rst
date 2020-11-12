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

This use case allows Student or Lecturer create a new project.

Flow of Events
^^^^^^^^^^^^^^

Basic Flow
""""""""""
1. Student/Lecturer request to create a project.
2. System accepts the request and request user to fill in a form.
3. The user turn in the form.
4. System process the form and create a new project.

Alternative Flow
""""""""""""""""
Invalid/Missing information
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
--------------

Brief Description
^^^^^^^^^^^^^^^^^

This use case allows Student or Lecturer join an existing project.

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

Post-Conditions
^^^^^^^^^^^^^^^

The system state is unchanged.

Extension Points
^^^^^^^^^^^^^^^^

None.