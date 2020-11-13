Database Design
===============

The database used for the system is document-oriented.  That is, it is stored
and queried in JSON-like format.  The database consists of following patterns:

- user
- project
- task
- discussion thread
- comment

Each of them is described in following sections.

User
----

The pattern for user objects is described below:

.. code-block:: json

   {
      "user-id": "uuid",
      "username": "Foo Bar",
      "email": "foo.bar@example.com",
      "password-hash": "(hash generated for password)",
      "role": "student"
   }

Project
-------

The pattern for project objects is described below:

.. code-block:: json

   {
      "project-id": "uuid",
      "project-name": "Project Name",
      "creator": "(creator id)",
      "participants": [
         "list",
         "of",
         "participants",
         "ids"
      ],
      "tasklist": [
         "list",
         "of",
         "task",
         "ids"
      ],
      "discussion-threads": [
         "list",
         "of",
         "thread"
         "ids"
      ]
      "created-on": "(date time in ISO 8601 format)"
      "evaluation": 17,
   }

Task
----

The pattern for project objects is described below:

.. code-block:: json

   {
      "task-id": "uuid",
      "task-name": "task name",
      "is-done": true,
      "evaluated": 18,
      "assigned-to": "(user id)"
   }

Discussion Thread
-----------------

The pattern for thread objects is described below:

.. code-block:: json

   {
      "thread-id": "uuid"
      "title": "Thread Title",
      "content": "The description of the issue addressed in the thread.",
      "comments": [
         "list",
         "of",
         "comment",
         "id"
      ]
   }

Comment
-------

The pattern for thread objects is described below:

.. code-block:: json

   {
      "comment-id": "uuid",
      "content": "The content of the comment.",
      "comments": [
         "list",
         "of",
         "ids",
         "of the",
         "comments",
         "replying",
         "to this comment"
      ]
   }
