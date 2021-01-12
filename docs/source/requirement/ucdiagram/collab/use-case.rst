Use-Case Model
==============

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


