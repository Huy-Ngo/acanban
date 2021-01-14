Project
=======

A ``Project`` object includes the project description as well as the links to participants.

It has following attributes:

``name`` : ``string``
   The name of the project

``description`` : ``string``
   The summary of a project

``supervisors`` : ``array`` of ``string``
   Usernames of supervisors of the project.

``students`` : ``array`` of ``string``
   Usernames of students participating in the project.

``tasks`` : ``array`` of ``Task``
   List of ``Task``\s created for this project.

``created_on`` : ``time``
   The date and time the project is created.

``deadline`` : ``time``
   The date and time for the deadline of the project.

``evaluation`` : ``number``
   Final evaluation of the project.  It can be based on previous evaluation
   of individual tasks.

``report`` : ``File`` or ``array`` of ``File``
   A file that contains the report(s) for the group project.
