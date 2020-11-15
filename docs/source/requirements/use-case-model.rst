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
   Student --> Msg
   Student --> Authentication

   Search <-- Lecturer
   CreateP <-- Lecturer
   JoinP <-- Lecturer
   Msg <-- Lecturer
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
   In step 2, if the user is Student and the project already has 6 Student,
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
4. System receive evidences and mark task(s) as completed.

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


Send Message
------------

Brief Description
^^^^^^^^^^^^^^^^^

This use case allows Student and Lecturer to communicate with each other.

Flow of Events
^^^^^^^^^^^^^^

Basic Flow
""""""""""

1. User 1 request to create a new thread.
2. System receive the request and reponse with a thread form.
3. User 1 fill in the thread form.
4. System receive the form and create a new thread.
5. User 2 comments on the thread for discussion.

Alternative Flow
""""""""""""""""

Thread existed
   If in step 5, User 2 recognizes that another thread has the solution,
   User 2 could mark the thread as existed. The system require User 2
   to provide clear instruction leading to the existed thread.

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


Make Report
-----------

Brief Description
^^^^^^^^^^^^^^^^^

This use case allows Staff make report base on the result of the project.

Flow of Events
^^^^^^^^^^^^^^

Basic Flow
""""""""""

1. Staff request to make a report.
2. System receive the request and the result of the project.
3. Staff request to make a hard copy.
4. System response by a document file format of the report.
5. Staff download the file for printing purpose later.

Alternative Flow
""""""""""""""""

Project has not done
   If in step 2, Student has not provided the result, the system will display
   a message that the report is not ready yet and terminate the operation.
   The system will then notify Student by sending an email or via
   notification bar.

Special Requirements
^^^^^^^^^^^^^^^^^^^^

None.

Pre-Conditions
^^^^^^^^^^^^^^

User must be Staff and be logged into the system before this use case begins.

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

1. Staff request to export the transcript.
2. System receive the request and display the evaluation of Lecturer.
3. Staff request to make a hard copy.
4. System response by a document file format of the transcript.
5. Staff download the file for printing purpose later.

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

User must be Staff and be logged into the system before this use case begins.

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

1. User request sign up for the system.
2. System receive the request and request user to enter
   **username**, **password**, **name**, **role**, **and email**
3. User provides necessary information.
4. System request user to verify by his/her provided email.
5. User verify by his/her provided email.
6. System allow user to log in the system with newly created account.

Alternative Flow
""""""""""""""""

Invalid username
   If in step 2, user uses an username with invalid characters, the system
   will display an alert message. User could either change his/her username or
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

1. User request to log in the system.
2. System receives the request and request user enter **username** and **password**.
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

1. User request to log in the system.
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

1. User select "Student" on search bar.
2. Sytem request user to select which type of search, including:

  - **Search by name**: this allows user to search for specific student name.
  - **Search by year**: this allows user to get a list of students in a specific year.

Sub Flow
""""""""

**Search by name**

1. User enters name of student that his/her wants to search.
2. System receive the search request including the name, and response with
   a list of students matched with the provided name.

**Search by year**

1. System display a list of years.
2. User selects a specific year that his/her wants to search.
3. System receive the search request including the selected year, and response
   with a list of students studing in that year.

Alternative Flow
""""""""""""""""

Invalid name
   If, in **Search by name** sub flow, user enters a name with invalid characters,
   the system will display an alert message. User could either re-enters the name
   or cancel the operation.

Special Requirements
^^^^^^^^^^^^^^^^^^^^

If, in **Search by name** sub flow, user has successfuly receive the list of
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

1. User select "Lecturer" on search bar.
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

1. User select "Project" on search bar.
2. Sytem request user to select which type of search, including:

  - **Search by name**: this allows user to search for specific project name.
  - **Search by year**: this allows user to get a list of projects in a specific year.

Sub Flow
""""""""

**Search by name**

1. User enters name of project that his/her wants to search.
2. System receive the search request including the name, and response with
   a list of projects matched with the provided name.

**Search by year**

1. System display a list of years.
2. User selects a specific year that his/her wants to search.
3. System receive the search request including the selected year, and response
   with a list of students studing in that year.

Alternative Flow
""""""""""""""""

Invalid name
   If, in **Search by name** sub flow, user enters a name with invalid characters,
   the system will display an alert message. User could either re-enters the name
   or cancel the operation.

Special Requirements
^^^^^^^^^^^^^^^^^^^^

In **Search by name** sub flow, user has successfuly receive the list of
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