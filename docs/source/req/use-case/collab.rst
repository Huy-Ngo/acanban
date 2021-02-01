Project Collaboration
=====================

This section aims to describe basic activities relating to the project.
For :ref:`objcollab`, we let users perform basic create-read-update-delete
on projects, along with the help of tasks and discussion.

.. uml::

   skinparam packageStyle rectangle
   left to right direction
   actor "Project Participant" as parti

   rectangle Project {
      usecase "Create project" as CreateP
      usecase "Show project information" as ShowP
      usecase "Edit project information" as EditP
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
   parti --> ShowP
   parti --> EditP
   parti --> CreateT
   parti --> AddMember
   parti --> AssignT
   parti --> Complete
   parti --> Thread
   parti --> Comment
   parti --> View

   Student --|> parti
   Supervisor --|> parti


.. _project create:

Create Project
--------------

This use case allows Student or Supervisor to create a new project.
Its flow of events can be depicted as follows:

1. Student/Supervisor requests to create a project.
2. System receives the request and requests user to enter **name** and **description**.
3. The user provides necessary data.
4. System processes the data and create a new project.


.. _project info:

Show Project Information
------------------------

This use case allows a member to view the project's basic information.
Its flow of events can be depicted as follows:

1. Participant requests to view a project.
2. System respond with the project's basic information.


.. _project edit:

Edit Project Information
------------------------

This use case allows a member to edit a project's basic information.
Its flow of events can be depicted as follows:

1. Participant requests to view a project.
2. System respond with a form for editing basic information.
3. Participant gives disired changes to the project's basic information.
4. System updates the project's information accordingly.


Add Project Members
-------------------

This use case allows the creator of a project to add members to it.
Its flow of events can be depicted as follows:

1. The creator selects other users to add to project.
2. The System adds the selected users as members of the project.


Create Tasks
------------

This use case allows Student or Supervisor to generate tasks for the project.
Its flow of events can be depicted as follows:

1. Student/Supervisor requests to generate tasks the project.
2. System receives the request and requests user to provide **name**, **assignees** and **deadline**.
3. User provides necessary data.
4. System processes the data and updates tasks list.


Assign Tasks
------------

This use case allows a participant to assign a task to someone.
Its flow of events can be depicted as follows:

1. Student selects the task and choose "Assign".
2. Student chooses the participant to assign to.
3. System receives the request and register the participant
   as assigned for that task.


Complete Tasks
--------------

This use case allows Student to complete task(s) in the project.
Its flow of events can be depicted as follows:

1. Student requests to complete task(s) in the task list.
2. System receives the request and requests Student to hand in evidences.
3. Student submits a file or a link as evidence.
4. System receives the evidence and marks task(s) as completed.


Create Discussion Thread
------------------------

This use case allows Student or Supervisor to create a discussion thread.
Its flow of events can be depicted as follows:

1. User requests to create a new discussion thread.
2. System receives the request and requests user to enter
   **title** and **content**.
3. User provides necessary data.
4. System processes the data and create a new thread.


Add Comment
-----------

This use case allows Student or Supervisor to add a comment to a
discussion thread.  Its flow of events can be depicted as follows:

1. User requests to add a new comment to the discussion thread.
2. System receives the request and requests user to enter **comment**.
3. User enters a comment.
4. System processes the data and create a new comment in the thread.
