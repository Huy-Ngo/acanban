Other Use-Cases
===============

As for most web applications, this system is required to perform basic tasks
such as authentication and searching.

.. uml::

   skinparam packageStyle rectangle
   left to right direction
   actor User
   actor "Project Participant" as parti
   actor Student
   actor "Academic Assistant" as assist
   actor Supervisor

   rectangle Search {
      usecase "Search student" as SearchS
      usecase "Search lecturer" as SearchL
      usecase "Search project" as SearchP
   }

   rectangle Authentication {
      usecase Register
      usecase Login
      usecase Logout
   }

   Student --|> parti
   Supervisor --|> parti
   parti --|> User
   assist --|> User

   User --> SearchS
   User --> SearchL
   User --> SearchP
   User --> Register
   User --> Login
   User --> Logout


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
   If in step 2, user uses a username with invalid characters, the system
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

Post-Conditions
^^^^^^^^^^^^^^^

User is now granted a new account and logged in the system.


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

Pre-Conditions
^^^^^^^^^^^^^^

User must own an account before the use case begins.

Post-Conditions
^^^^^^^^^^^^^^^

The user logged in to the system.


Logout
------

Brief Description
^^^^^^^^^^^^^^^^^

This use case allows user to log out of the system.

Flow of Events
^^^^^^^^^^^^^^

Basic Flow
""""""""""

1. User requests to log in to the system.
2. System receives the request and allows user to logout the system.

Pre-Conditions
^^^^^^^^^^^^^^

User must be logged in the system before the use case begins.

Post-Conditions
^^^^^^^^^^^^^^^

The user logged out of the system.


Search Student
--------------

Brief Description
^^^^^^^^^^^^^^^^^

This use case allows User to search for students.

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

1. User enters the name of student that his/her wants to search.
2. System receives the search request including the name, and responds with
   a list of students matched with the provided name.

**Search by year**

1. System displays a list of years.
2. User selects a specific year that he/she wants to search.
3. System receives the search request including the selected year, and responds
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
matching students.

Pre-Conditions
^^^^^^^^^^^^^^

User must be logged in the system before the use case begins.

Post-Conditions
^^^^^^^^^^^^^^^

The system state is unchanged.


Search Supervisor
-----------------

Brief Description
^^^^^^^^^^^^^^^^^

This use case allows user to search in list of lecturers.

Flow of Events
^^^^^^^^^^^^^^

Basic Flow
""""""""""

1. User selects "Supervisor" on search bar.
2. User enters name of lecturer that his/her wants to search.
3. System receives the search request including the name, and responds with
   a list of supervisors matching the provided name.

Alternative Flow
""""""""""""""""

Invalid name
   If, in step 2, user enters a name with invalid characters, the system
   will display an alert message. User could either re-enter the name
   or cancel the operation.

Pre-Conditions
^^^^^^^^^^^^^^

User must be logged in the system before the use case begins.

Post-Conditions
^^^^^^^^^^^^^^^

The system state is unchanged.


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
student names and might want to sort them by *year*.


If, in **Search by name** sub flow, user enters a name which is not matching
with any project name, the system should display a message that there are no
matching projects.

Pre-Conditions
^^^^^^^^^^^^^^

User must be logged in the system before the use case begins.

Post-Conditions
^^^^^^^^^^^^^^^

The system state is unchanged.
