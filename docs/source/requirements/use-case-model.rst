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