User
====

A ``User`` object represents either a student, a supervisor,
or an academic assistant.  The object contains the user's projects
as well as other contact information, which allows the users to communicate
with each other.

Since all users of this system have similar basic information, such as username
and password, we represented them all as ``User`` object, and restrict their
behaviors according to a field ``role``.

Each ``User`` object has following attributes:

``username`` : ``string``
   A unique name with which the user can refer to one another.
   It is also the primary key and allows the user to sign in.

``name`` : ``string``
   The legal name of the user.  This is required for group members to recognize
   each other, and for the academic assistants to collect their results.

``email`` : ``string``
   The email address that is used to contact with the user.

``password`` : ``string``
   The password for the user's account, encrypted with a hash function.

``role`` : ``string``
   The role of the user in this system.  It can be:

   - ``student``: Students who are participating in a group project or internship.
   - ``supervisor``: The supervisor of project(s).
   - ``assistant``: The academic assistant of a department.
   - ``admin``: The system admin.

``projects`` : ``array`` of ``string``, *optional*
   UUIDs of projects the user participates in,
   if perse is a student or a supervisor.

``department`` : ``string``, *optional*
   The department of the user, such as ``ICT``, ``SA``, or ``LS``.
   Required for students and assistants.

``student-id`` : ``string``, *optional*
   Only applicable for users with role ``student``:
   A unique identifier assigned to students to be used outside this system.

``bio`` : ``object``, *optional*
   A markup text describing the user.  This is not necessary, but it can be
   helpful for a supervisor to have a biography to show their credibility in
   their respective field.
