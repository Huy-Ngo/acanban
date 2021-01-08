Database Design
===============

The collaboration tasks require following data:

- ``User``
- ``Project``
- ``Task``
- Discussion ``Thread``
- ``Comment``
- ``File``

Each of them is described in following sections.

User
----

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

Project
-------

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


Task
----

Each ``Task`` object has following attributes:

``name`` : ``string``
   The name of the task

``creator`` : ``User``
   The user who created the task

``status`` : ``integer``
   The status of the project in the Kanban board: to-do, in progress, or done.

``assigned-to`` : ``User``
   The assignee of the task. Must have role ``student``.

``description`` : ``string``
   The summary of a task

``discussion`` : ``array`` of ``Thread``
   List of ``Thread`` s created for this task

``file`` : ``File``
   Optional file that shows the assignee's work to address the task.

``created_on`` : ``time``
   The date and time the task is created.

``deadline`` : ``time``
   The date and time for the deadline of the task.


Discussion Thread
-----------------

Each ``Thread`` object has following attributes:


``creator`` : ``User``
   The user who created the discussion thread

``title`` : ``string``
   The title of the discussion thread

``content`` : ``string``
   The description of the issue addressed in the thread

``comments`` : ``array`` of ``Comment``
   List of ``Comment`` s on this thread


Comment
-------

Each ``Comment`` object has following attributes:

``creator`` : ``User``
   The user who created the comment

``content`` : ``string``
   The content of the comment

``comments`` : ``array`` of ``Comment``
   List of ``Comment`` s replying to it

File
----

The ``File`` object is needed to store the metadata about the files
used in project.

``cid`` : ``string``
   Content identifier of the file in CID_ v1.

``filename`` : ``string``, *optional*
   Filename of the file.

.. _CID: https://github.com/multiformats/cid
