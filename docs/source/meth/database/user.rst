User
====

A ``User`` object represents either a student, a supervisor,
or an academic assistant.  The object contains the user's projects
as well as other contact information, which allows the users to communicate
with each other.

Each ``User`` object has following attributes:

``username`` : ``string``
   A unique name with which the user can refer to one another.
   It is also the primary key and allows the user to sign in.

``name`` : ``string``
   The legal name of the user

``email`` : ``string``
   The email that is used to contact with the user.

``password`` : ``string``
   The password for the user's account, encrypted with a hash function

``role`` : ``string``
   The role of the user in this system.  It can be:

   - ``student``: Students who are participating a group project or internship
   - ``supervisor``: The supervisor of project(s)
   - ``assistant``: The academic assistant of a department
   - ``admin``: The system admin

``projects`` : ``array`` of ``string``, *optional*
   UUIDs of projects the user participates in,
   if perse is a student or a supervisor.

``department`` : ``string``, *optional*
   The department of the user, such as ``ICT``, ``SA``, or ``LS``.
   Required for students and assistants.

``student-id`` : ``string``, *optional*
   Only applicable for users with role ``student``:
   A unique identifier assigned to students to be used outside this system

``bio`` : ``object``, *optional*
   A self-description of the user. It can have following fields:

   - ``description``: A markdown text describing the user
   - ``institution``: The institution the user is working at, mainly for supervisors
   - ``interest``: Research interests of a supervisor or student
