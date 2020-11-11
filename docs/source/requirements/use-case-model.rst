Use-Case Model
==============

.. uml::
    left to right direction
    actor Student
    actor Staff
    actor Admin
    actor Lecturer
    
package Project {
    usecase "Create project" as CreateP
    usecase "Join project" as JoinP
    usecase "Create tasks" as CreateT
    usecase "Join tasks" as JoinT
    usecase "Complete tasks" as Complete
    usecase "View results" as View
    usecase Evaluate
    usecase "Send message" as Msg
}

    usecase Search
    
package something-need-to-name {   
    usecase Register
    usecase Login
    usecase Logout
}

package Result {
    usecase "Make Report" as Report
    usecase "Export transcript" as Export
}

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
    
    Lecturer <|-- Student
    Lecturer --> View
    Lecturer --> Evaluate
    
    Admin <|-- Lecturer
    Admin <|-- Staff
    Admin --> Maintain


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
    In step 3, if the user missed some information, the system display an error message.
    The user can either select to cancel operation or fill in missing fields.

Special Requirements
^^^^^^^^^^^^^^^^^^^^

None.

Pre-Conditions
^^^^^^^^^^^^^^

User must be Student or Lecturer and be logged into the system before this use case begins.

Post-Conditions
^^^^^^^^^^^^^^^

The system state is unchanged.

Extension Points
^^^^^^^^^^^^^^^^

None.