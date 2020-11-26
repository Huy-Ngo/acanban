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
   usecase "Create discussion thread" as Thread
   usecase "Add comment" as Comment
   usecase "Receive notification" as Notification

   usecase Search
   usecase "Search student" as SearchS
   usecase "Search lecturer" as SearchL
   usecase "Search project" as SearchP

   usecase Authentication
   usecase Register
   usecase Login
   usecase Logout

   usecase "Make Report" as Report
   usecase "Export transcript" as Export

   usecase "Maintain system" as Maintain

   Staff --> Search
   Staff --> Export
   Staff --> Report
   Staff --> Authentication

   Student --> Search
   Student --> CreateP
   Student --> CreateT
   Student --> JoinP
   Student --> JoinT
   Student --> Complete
   Student --> Thread
   Student --> Comment
   Student --> Notification
   Student --> Authentication

   Search <-- Lecturer
   CreateP <-- Lecturer
   JoinP <-- Lecturer
   Thread <-- Lecturer
   Comment <-- Lecturer
   Authentication <-- Lecturer

   Lecturer --> View
   Lecturer --> Evaluate

   Admin --> Maintain

   Search <.. SearchS: <<extends>>
   Search <.. SearchL: <<extends>>
   Search <.. SearchP: <<extends>>

   Register ..> Authentication : <<extends>>
   Login ..> Authentication : <<extends>>
   Logout ..> Authentication : <<extends>>


Create Project
--------------

Brief Description
^^^^^^^^^^^^^^^^^

This use case allows Student or Lecturer to create a new project.

Flow of Events
^^^^^^^^^^^^^^

Basic Flow
""""""""""

1. Student/Lecturer requests to create a project.
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
   In step 4, if the user is Lecturer and the project is existed,
   the system display an error message and terminate the operation.

Special Requirements
^^^^^^^^^^^^^^^^^^^^

None.

Pre-Conditions
^^^^^^^^^^^^^^

User must be Student or Lecturer and be logged in the system
before this use case begins.

Post-Conditions
^^^^^^^^^^^^^^^

A new project is created.

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

1. Student/Lecturer requests to join the project.
2. System processes the request and allows user to join the project.

Alternative Flow
""""""""""""""""

Project is full
   In step 2, if the user is Student and the project already has 6 Student,
   the system will display an error message and cancel the operation.

   In step 2, if the user is Lecturer and the project already has 1 Lecturer,
   the system will display an error message and cancel the operation.

Special Requirements
^^^^^^^^^^^^^^^^^^^^

None.

Pre-Conditions
^^^^^^^^^^^^^^

User must be Student or Lecturer and be logged in the system
before this use case begins.

There must be existing project so that user could join.

Post-Conditions
^^^^^^^^^^^^^^^

The user is now joined a project.

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

1. Student/Lecturer requests to generate tasks the project.
2. System receives the request and requests user to provide **name**, **assignees** and **deadline**.
3. User provides necessary data.
4. System processes the data and updates tasks list.

Alternative Flow
""""""""""""""""

Task is existed
   In step 4, if the user entered a task that is already existed in task list,
   the system will display an error message and terminate the operation.

Missing meta data
   In step 4, if user missed to enter some data, (e.g: deadline for the task),
   the system will display an alert message. User can either fill in
   missing fields or cancel the operation.

Special Requirements
^^^^^^^^^^^^^^^^^^^^

None.

Pre-Conditions
^^^^^^^^^^^^^^

User must be Student or Lecturer and be logged in the system
before this use case begins.

Post-Conditions
^^^^^^^^^^^^^^^

A new tasks is created in task list.

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

1. Student requests to join task(s) in the task list.
2. System receives the request and allows Student to join the task(s).

Alternative Flow
""""""""""""""""

None.

Special Requirements
^^^^^^^^^^^^^^^^^^^^

None.

Pre-Conditions
^^^^^^^^^^^^^^

User must be Student and be logged in the system before this use case begins.

Post-Conditions
^^^^^^^^^^^^^^^

Student is assigned to a task.

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

1. Student requests to complete task(s) in the task list.
2. System receives the request and requests Student to hand in evidences.
3. Student submits files or image as evidences.
4. System receives evidences and marks task(s) as completed.

Alternative Flow
""""""""""""""""

No evidences provided
   In step 3, if Student do not submit files,
   the system will display an alert message and terminate the operation.

Empty files provided
   In step 4, if Student submits empty files,
   the system will display an alert message and terminate the operation.

Special Requirements
^^^^^^^^^^^^^^^^^^^^

None.

Pre-Conditions
^^^^^^^^^^^^^^

User must be Student and be logged in the system before this use case begins.

Post-Conditions
^^^^^^^^^^^^^^^

The task state is changed to *completed*.

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

User must be Lecturer and be logged in the system before this use case begins.

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
2. System receive the request provide an **evaluation** and **comment**.
3. Lecturer provide evaluation with comments.
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

User must be Lecturer and be logged in the system
before this use case begins.

Post-Conditions
^^^^^^^^^^^^^^^

After this use case ends, other project-related use case could not be executed.

Extension Points
^^^^^^^^^^^^^^^^

None.


Create Discussion Thread
------------------------

Brief Description
^^^^^^^^^^^^^^^^^

This use case allows Student or Lecturer to create a discussion thread.

Flow of Events
^^^^^^^^^^^^^^

Basic Flow
""""""""""

1. User requests to create a new discussion thread.
2. System receives the request and requests user to enter
   **title** and **content**.
3. User provides necessary data.
4. System processes the data and create a new thread.

Alternative Flow
""""""""""""""""

Thread existed
   If in step 5, an user recognizes that another thread has the solution,
   he/she could mark the thread as existed. The system require that user
   to provide clear instruction leading to the existed thread.

Special Requirements
^^^^^^^^^^^^^^^^^^^^

None.

Pre-Conditions
^^^^^^^^^^^^^^

User must be Student or Lecturer and be logged in the system
before this use case begins.

Post-Conditions
^^^^^^^^^^^^^^^

A new discussion thread is created.

Extension Points
^^^^^^^^^^^^^^^^

None.


Add Comment
-----------

Brief Description
^^^^^^^^^^^^^^^^^

This use case allows Student or Lecturer to add a comment to a
discussion thread.

Flow of Events
^^^^^^^^^^^^^^

Basic Flow
""""""""""

1. User requests to add a new comment to the discussion thread.
2. System receives the request and requests user to enter **comment**.
3. User enters a comment.
4. System processes the data and create a new comment in the thread.

Alternative Flow
""""""""""""""""

None.

Special Requirements
^^^^^^^^^^^^^^^^^^^^

None.

Pre-Conditions
^^^^^^^^^^^^^^

User must be Student or Lecturer and be logged in the system
before this use case begins.

Post-Conditions
^^^^^^^^^^^^^^^

A new comment thread is added into the discussion thread.

Extension Points
^^^^^^^^^^^^^^^^

None.


Receive Notification
--------------------

Brief Description
^^^^^^^^^^^^^^^^^

This use case allows Student to receive notification from
both in-app system and email.

Flow of Events
^^^^^^^^^^^^^^

Basic Flow
""""""""""

1. System sends notification to Student.
2. Student receives the notification, by mail or notification bar.

Alternative Flow
""""""""""""""""

None.

Special Requirements
^^^^^^^^^^^^^^^^^^^^

None.

Pre-Conditions
^^^^^^^^^^^^^^

Student could receive notification from theses activities:

- A person ask to join his/her project.
- His/her join request is approved.
- The deadline for his/her tasks is near.
- He/she is assigned to a task.
- His/her task is approved/evaluated.
- His/her project is evaluated
- There is a new reply in his/her watching discussion thread.

Post-Conditions
^^^^^^^^^^^^^^^

A new unread notification is received.

Extension Points
^^^^^^^^^^^^^^^^

None.


Make Report
-----------

Brief Description
^^^^^^^^^^^^^^^^^

This use case allows Staff make report base on the result of the project.

Flow of Events
^^^^^^^^^^^^^^

Basic Flow
""""""""""

1. Staff requests to make a report.
2. System receives the request and displays the result of the project.
3. Staff requests to make a hard copy.
4. System responses by a document file format of the report.
5. Staff downloads the file for printing purpose later.

Alternative Flow
""""""""""""""""

Project has not done
   If in step 2, Student has not provided the result, the system will display
   a message that the report is not yet ready and terminate the operation.
   The system will then notify Student by sending an email or via
   notification bar.

Special Requirements
^^^^^^^^^^^^^^^^^^^^

None.

Pre-Conditions
^^^^^^^^^^^^^^

User must be Staff and be logged in the system before this use case begins.

Staff must search and select the project(s) before the use case begins.

Post-Conditions
^^^^^^^^^^^^^^^

The system state is unchanged.

Extension Points
^^^^^^^^^^^^^^^^

None.


Export Transcript
-----------------

Brief Description
^^^^^^^^^^^^^^^^^

This use case allows Staff to export transcript based on the evaluation of Lecturer.

Flow of Events
^^^^^^^^^^^^^^

Basic Flow
""""""""""

1. Staff requests to export the transcript.
2. System receives the request and displays the evaluation of Lecturer.
3. Staff requests to make a hard copy.
4. System responses by a document file format of the transcript.
5. Staff downloads the file for printing purpose later.

Alternative Flow
""""""""""""""""

Not yet evaluated
   If in step 2, Lecturer has not given the evaluation, the system will display
   a message that the transcript is not ready yet and terminate the operation.
   The system will then notify Lecturer by sending an email or via
   notification bar.

Special Requirements
^^^^^^^^^^^^^^^^^^^^

None.

Pre-Conditions
^^^^^^^^^^^^^^

User must be Staff and be logged in the system before this use case begins.

Staff must search and select the project(s) before the use case begins.

Post-Conditions
^^^^^^^^^^^^^^^

The system state is unchanged.

Extension Points
^^^^^^^^^^^^^^^^

None.


Register
--------

Brief Description
^^^^^^^^^^^^^^^^^

This use case allows user to create his/her own account.

Flow of Events
^^^^^^^^^^^^^^

Basic Flow
""""""""""

1. User requests sign up for the system.
2. System receives the request and requests user to enter
   **username**, **password**, **name**, **role**, **and email**
3. User provides necessary information.
4. System requests user to verify by his/her provided email.
5. User verifies by his/her provided email.
6. System allows user to log in the system with newly created account.

Alternative Flow
""""""""""""""""

Invalid username
   If in step 2, user uses an username with invalid characters, the system
   will display an alert message. User could either re-enter his/her username or
   cancel the operation.

Existed username
   If in step 2, user enters an existed username, the system will display
   an alert message. User could either select another username
   or cancel the operation.

Invalid email
   If in step 2, user enters an invalid email, the system will display
   an alert message. User could either re-enter his/her email
   or cancel the operation.

Special Requirements
^^^^^^^^^^^^^^^^^^^^

None.

Pre-Conditions
^^^^^^^^^^^^^^

None.

Post-Conditions
^^^^^^^^^^^^^^^

User is now granted a new account and be logged in the system.

Extension Points
^^^^^^^^^^^^^^^^

None.


Login
-----

Brief Description
^^^^^^^^^^^^^^^^^

This use case allows user to log in the system.

Flow of Events
^^^^^^^^^^^^^^

Basic Flow
""""""""""

1. User requests to log in the system.
2. System receives the request and requests user enter **username** and **password**.
3. User provides username and password.
4. System validates the entered username and password and allows user to log in
   the system.

Alternative Flow
""""""""""""""""

Incorrect username/password
   If in step 2, user enters username or password incorrectly, the system
   will display an error message and terminate the operation.

Invalid username
   If in step 2, user enters and invalid character for username, the system
   will display an error message and terminate the operation.

Special Requirements
^^^^^^^^^^^^^^^^^^^^

None.

Pre-Conditions
^^^^^^^^^^^^^^

User must own an account before the use case begins.

Post-Conditions
^^^^^^^^^^^^^^^

The user is logged in the system.

Extension Points
^^^^^^^^^^^^^^^^

None.


Logout
------

Brief Description
^^^^^^^^^^^^^^^^^

This use case allows user to logout the system.

Flow of Events
^^^^^^^^^^^^^^

Basic Flow
""""""""""

1. User requests to log in the system.
2. System receives the request and allows user to logout the system.

Alternative Flow
""""""""""""""""

None.

Special Requirements
^^^^^^^^^^^^^^^^^^^^

None.

Pre-Conditions
^^^^^^^^^^^^^^

User must be logged in the system before the use case begins.

Post-Conditions
^^^^^^^^^^^^^^^

The user is logged out the system.

Extension Points
^^^^^^^^^^^^^^^^

None.


Search Student
--------------

Brief Description
^^^^^^^^^^^^^^^^^

This use case allows user to search in list of students.

Flow of Events
^^^^^^^^^^^^^^

Basic Flow
""""""""""

1. User selects "Student" on search bar.
2. Sytem requests user to select which type of search, including:

  - **Search by name**: this allows user to search for specific student name.
  - **Search by year**: this allows user to get a list of students in a specific year.

Sub Flow
""""""""

**Search by name**

1. User enters name of student that his/her wants to search.
2. System receives the search request including the name, and responses with
   a list of students matched with the provided name.

**Search by year**

1. System displays a list of years.
2. User selects a specific year that his/her wants to search.
3. System receives the search request including the selected year, and responses
   with a list of students studing in that year.

Alternative Flow
""""""""""""""""

Invalid name
   If, in **Search by name** sub flow, user enters a name with invalid characters,
   the system will display an alert message. User could either re-enter the name
   or cancel the operation.

Special Requirements
^^^^^^^^^^^^^^^^^^^^

If, in **Search by name** sub flow, user has successfully received the list of
student name and want to sort it, he/she could select to sort it by *year* or *major*.

If, in **Search by name** sub flow, user enters a name which is not matched
with any student name, the system should display a message that there are no
matching student.

Pre-Conditions
^^^^^^^^^^^^^^

User must be logged in the system before the use case begins.

Post-Conditions
^^^^^^^^^^^^^^^

The system state is unchanged.

Extension Points
^^^^^^^^^^^^^^^^

None.


Search Lecturer
---------------

Brief Description
^^^^^^^^^^^^^^^^^

This use case allows user to search in list of lecturers.

Flow of Events
^^^^^^^^^^^^^^

Basic Flow
""""""""""

1. User selects "Lecturer" on search bar.
2. User enters name of lecturer that his/her wants to search.
3. System receive the search request including the name, and response with
   a list of lecturer matched with the provided name.

Alternative Flow
""""""""""""""""

Invalid name
   If, in step 2, user enters a name with invalid characters, the system
   will display an alert message. User could either re-enters the name
   or cancel the operation.

Special Requirements
^^^^^^^^^^^^^^^^^^^^

None.

Pre-Conditions
^^^^^^^^^^^^^^

User must be logged in the system before the use case begins.

Post-Conditions
^^^^^^^^^^^^^^^

The system state is unchanged.

Extension Points
^^^^^^^^^^^^^^^^

None.


Search Project
--------------

Brief Description
^^^^^^^^^^^^^^^^^

This use case allows user to search in list of projects.

Flow of Events
^^^^^^^^^^^^^^

Basic Flow
""""""""""

1. User selects "Project" on search bar.
2. Sytem requests user to select which type of search, including:

  - **Search by name**: this allows user to search for specific project name.
  - **Search by year**: this allows user to get a list of projects in a specific year.

Sub Flow
""""""""

**Search by name**

1. User enters name of project that his/her wants to search.
2. System receives the search request including the name, and responses with
   a list of projects matched with the provided name.

**Search by year**

1. System displays a list of years.
2. User selects a specific year that his/her wants to search.
3. System receives the search request including the selected year, and responses
   with a list of projects in that year.

Alternative Flow
""""""""""""""""

Invalid name
   If, in **Search by name** sub flow, user enters a name with invalid characters,
   the system will display an alert message. User could either re-enter the name
   or cancel the operation.

Special Requirements
^^^^^^^^^^^^^^^^^^^^

In **Search by name** sub flow, user has successfully received the list of
student name and might want to sort it by *year*.


If, in **Search by name** sub flow, user enters a name which is not matched
with any project name, the system should display a message that there are no
matching project.

Pre-Conditions
^^^^^^^^^^^^^^

User must be logged in the system before the use case begins.

Post-Conditions
^^^^^^^^^^^^^^^

The system state is unchanged.

Extension Points
^^^^^^^^^^^^^^^^

None.