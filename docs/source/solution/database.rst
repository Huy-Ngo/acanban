Database Design
===============

The database used for the system is document-oriented.  That is, it is stored
and queried in JSON-like format.  The database consists of following objects:

- ``User``
- ``Project``
- ``Task``
- Discussion ``Thread``
- ``Comment``
- ``File``

Each of them is described in following sections.

User
----

Each ``User`` object has following attributes:

``id`` : ``string``
   A UUID for the object

``username`` : ``string``
   A unique name with which the user can refer to one another.
   It also allows the user to sign in.

``name`` : ``string``
   The legal name of the user

``email`` : ``string``
   The email that is used to contact with the user.

``password-hash`` : ``string``
   The password for the user's account, encrypted with a hash function

``role`` : ``string``
   The role of the user in this system.  It can be ``student``,
   ``supervisor``, ``staff``, and ``admin``

``major`` : ``string`` *optional*
   The major of a user with role ``student``.

``student-id`` : ``string``
   Only applicable for users with role ``student``:
   A unique identifier assigned to students to be used outside this system

``bio`` : ``string`` *optional*
   A self-description of the user

Project
-------

Each ``Project`` object has following attributes:

``id`` : ``string``
   A UUID for the object

``name`` : ``string``
   The name of the project

``creator`` : ``User``
   The creator of the project.

``supervisor`` : ``User``
   The supervisor of the project, must be a ``User`` with role ``supervisor``.

``description`` : ``string``
   The summary of a project

``participants`` : ``array`` of ``User``
   List of ``User`` s who participate in this project.

``tasks`` : ``array`` of ``Task``
   List of ``Task`` s created for this project.


Task
----

Each ``Task`` object has following attributes:

``id`` : ``string``
   A UUID for the object

``name`` : ``string``
   The name of the task

``creator`` : ``User``
   The user who created the task

``is-done`` : ``boolean``
   Whether the task is done

``evaluation`` : ``number``
   The evaluation of the task

``assigned-to`` : ``User``
   The assignee of the task. Must have role ``student``.

``description`` : ``string``
   The summary of a task

``deadline`` : ``string``
   Deadline for the task, in ISO 8601 format

``discussion`` : ``array`` of ``Thread``
   List of ``Thread`` s created for this task


Discussion Thread
-----------------

Each ``Task`` object has following attributes:


``id`` : ``string``
   A UUID for the object

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

``id`` : ``string``
   A UUID for the object

``creator`` : ``User``
   The user who created the comment

``content`` : ``string``
   The content of the comment

``comments`` : ``array`` of ``Comment``
   List of ``Comment`` s replying to it

File
----

``address`` : ``string``
   The IPFS address for the file object, which is also used as primary key.

``name`` : ``string``
   The file name
