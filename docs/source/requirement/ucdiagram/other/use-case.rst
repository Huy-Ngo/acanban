Use-Case Model
==============

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

