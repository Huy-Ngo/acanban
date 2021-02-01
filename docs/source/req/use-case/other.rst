Other Use-Cases
===============

As for most web applications, this system is required to perform basic tasks
such as authentication and searching.  In other words, those defined here
are the bridges between the non-functional requirements (of :ref:`appapp`)
and the use cases previously declared.

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

This use case allows user to create his/her own account.
Its flow of events can be depicted as follows:

1. User requests sign up for the system.
2. System receives the request and requests user to enter
   **username**, **password**, **name**, **role**, **and email**
3. User provides necessary information.
4. System requests user to verify by his/her provided email.
5. User verifies by his/her provided email.
6. System allows user to log in the system with newly created account.


Login
-----

This use case allows user to log in the system.

1. User requests to log in the system.
2. System receives the request and requests user enter **username** and **password**.
3. User provides username and password.
4. System validates the entered username and password and allows user to log in
   the system.


Logout
------

This use case allows user to log out of the system.
Its flow of events can be depicted as follows:

1. User requests to log in to the system.
2. System receives the request and allows user to logout the system.


Search Student
--------------

This use case allows User to search for students.
Its flow of events can be depicted as follows:

1. User selects "Student" on search bar.
2. Sytem requests for the search query.
3. User enters the name of student that his/her wants to search.
4. System receives the search request including the name, and responds with
   a list of students matched with the provided name.


Search Supervisor
-----------------

This use case allows user to search in list of lecturers.
Its flow of events can be depicted as follows:

1. User selects "Supervisor" on search bar.
2. User enters name of lecturer that his/her wants to search.
3. System receives the search request including the name, and responds with
   a list of supervisors matching the provided name.


Search Project
--------------

This use case allows user to search in list of projects.
Its flow of events can be depicted as follows:

1. User selects "Project" on search bar.
2. Sytem requests for the search query.
3. User enters name of project that his/her wants to search.
4. System receives the search request including the name, and responses with
   a list of projects matched with the provided name.
