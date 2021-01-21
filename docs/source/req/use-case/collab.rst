Project Collaboration
=====================

.. uml::

   skinparam packageStyle rectangle
   left to right direction
   actor "Project Participant" as parti

   rectangle Project {
      usecase "Create project" as CreateP
      usecase "Add project member" as AddMember
   }
   
   rectangle Task {
      usecase "Create task" as CreateT
      usecase "Assign task" as AssignT
      usecase "Complete task" as Complete
      usecase "View task" as View
   }

   rectangle Discussion {
      usecase "Create discussion thread" as Thread
      usecase "Add comment" as Comment
   }

   parti --> CreateP
   parti --> CreateT
   parti --> AddMember
   parti --> AssignT
   parti --> Complete
   parti --> Thread
   parti --> Comment
   parti --> View

   Student --|> parti
   Supervisor --|> parti


Create Project
--------------

Brief Description
^^^^^^^^^^^^^^^^^

This use case allows Student or Supervisor to create a new project.

Flow of Events
^^^^^^^^^^^^^^

Basic Flow
""""""""""

1. Student/Supervisor requests to create a project.
2. System receives the request and requests user to enter **name** and **description**.
3. The user provides necessary data.
4. System processes the data and create a new project.

Alternative Flow
""""""""""""""""

Missing information
   In step 4, if the user missed some information, the system will display
   an alert message. The user can either select to cancel operation
   or fill in missing fields.

Existing project
   In step 4, if the user is Supervisor and the project is existed,
   the system display an error message and terminate the operation.

Pre-Conditions
^^^^^^^^^^^^^^

User must be Student or Supervisor and be logged in the system
before this use case begins.

Post-Conditions
^^^^^^^^^^^^^^^

A new project is created.


Add Project Members
-------------------

Brief Description
^^^^^^^^^^^^^^^^^

This use case allows the creator of a project to add members to it.

Flow of Events
^^^^^^^^^^^^^^

Basic Flow
""""""""""

1. The creator selects other users to add to project.
2. The System adds the selected users as members of the project.

Pre-Conditions
^^^^^^^^^^^^^^

The user must have created the project.

Post-Conditions
^^^^^^^^^^^^^^^

Selected user(s) are added to the project.


Create Tasks
------------

Brief Description
^^^^^^^^^^^^^^^^^

This use case allows Student or Supervisor to generate tasks for the project.

Flow of Events
^^^^^^^^^^^^^^

Basic Flow
""""""""""

1. Student/Supervisor requests to generate tasks the project.
2. System receives the request and requests user to provide **name**, **assignees** and **deadline**.
3. User provides necessary data.
4. System processes the data and updates tasks list.

Alternative Flow
""""""""""""""""

Task exists
   In step 4, if the user enters a task that already exists in the task list,
   the system will display an error message and terminate the operation.

Missing metadata
   In step 4, if user forgets to enter some data, (e.g: deadline for the task),
   the system will display an alert message. User can either fill in
   missing fields or cancel the operation.

Pre-Conditions
^^^^^^^^^^^^^^

User must be Student or Supervisor and be logged in the system
before this use case begins.

Post-Conditions
^^^^^^^^^^^^^^^

A new task is created in task list.


Assign Tasks
------------

Brief Description
^^^^^^^^^^^^^^^^^

This use case allows a participant to assign a task to someone.

Flow of Events
^^^^^^^^^^^^^^

Basic Flow
""""""""""

1. Student selects the task and choose "Assign".
2. Student chooses the participant to assign to.
3. System receives the request and register the participant
   as assigned for that task.

Pre-Conditions
^^^^^^^^^^^^^^

User must be a participant and be logged in the system before this use case begins.

Post-Conditions
^^^^^^^^^^^^^^^

Student is assigned to a task.


Complete Tasks
--------------

Brief Description
^^^^^^^^^^^^^^^^^

This use case allows Student to complete task(s) in the project.

Flow of Events
^^^^^^^^^^^^^^

Basic Flow
""""""""""

1. Student requests to complete task(s) in the task list.
2. System receives the request and requests Student to hand in evidences.
3. Student submits a file or a link as evidence.
4. System receives the evidence and marks task(s) as completed.

Alternative Flow
""""""""""""""""

No evidence provided
   In step 3, if Student does not submit a file or a link,
   the system will display an alert message and terminate the operation.

Empty file provided
   In step 4, if Student submits an empty file,
   the system will display an alert message and terminate the operation.

Pre-Conditions
^^^^^^^^^^^^^^

User must be Student and be logged in the system before this use case begins.

Post-Conditions
^^^^^^^^^^^^^^^

The task state is changed to *completed*.


View result
-----------

Brief Description
^^^^^^^^^^^^^^^^^

This use case allows Supervisor to view result of the project.

Flow of Events
^^^^^^^^^^^^^^

Basic Flow
""""""""""

1. Supervisor requests to view the result of the participating project.
2. System receives the request and provides results.

Pre-Conditions
^^^^^^^^^^^^^^

User must be a Supervisor and be logged in the system before this use case begins.

Post-Conditions
^^^^^^^^^^^^^^^

The system state is unchanged.


Create Discussion Thread
------------------------

Brief Description
^^^^^^^^^^^^^^^^^

This use case allows Student or Supervisor to create a discussion thread.

Flow of Events
^^^^^^^^^^^^^^

1. User requests to create a new discussion thread.
2. System receives the request and requests user to enter
   **title** and **content**.
3. User provides necessary data.
4. System processes the data and create a new thread.

Pre-Conditions
^^^^^^^^^^^^^^

User must be Student or Supervisor and be logged in the system
before this use case begins.

Post-Conditions
^^^^^^^^^^^^^^^

A new discussion thread is created.


Add Comment
-----------

Brief Description
^^^^^^^^^^^^^^^^^

This use case allows Student or Supervisor to add a comment to a
discussion thread.

Flow of Events
^^^^^^^^^^^^^^

Basic Flow
""""""""""

1. User requests to add a new comment to the discussion thread.
2. System receives the request and requests user to enter **comment**.
3. User enters a comment.
4. System processes the data and create a new comment in the thread.

Pre-Conditions
^^^^^^^^^^^^^^

User must be Student or Supervisor and be logged in the system
before this use case begins.

Post-Conditions
^^^^^^^^^^^^^^^

A new comment thread is added into the discussion thread.
