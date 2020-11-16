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
      "id": "uuid",
      "username": "very_unique_username",
      "name": "Foo Bar",
      "email": "foo.bar@example.com",
      "password-hash": "(hash generated for password)",
      "role": "student",
      "major": "ICT", // optional
      "bio": "A self description" // optional
   }

Project
-------

The pattern for project objects is described below:

.. code-block:: json

   {
      "id": "uuid",
      "name": "Project Name",
      "creator": "(creator id)",
      "supervisor": "(supervisor id)",
      "description": "A summary of a project",
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
      "created-on": "(date time in ISO 8601 format)",
      "evaluation": 17,
   }

Task
----

The pattern for project objects is described below:

.. code-block:: json

   {
      "id": "uuid",
      "name": "task name",
      "is-done": true,
      "evaluated": 18,
      "assigned-to": "(user id)",
      "description": "A very long description",
      "deadline": "(date time in ISO 8601 format)",
      "discussion": [
         "list",
         "of",
         "thread",
         "ids"
      ]
   }

Discussion Thread
-----------------

The pattern for thread objects is described below:

.. code-block:: json

   {
      "id": "uuid",
      "title": "Thread Title",
      "content": "The description of the issue addressed in the thread.",
      "comments": [
         // list of comment objects
      ]
   }

Comment
-------

The pattern for comment objects is described below:

.. code-block:: json

   {
      "id": "uuid",
      "content": "The content of the comment.",
      "comments": [
         // list of comment objects
      ]
   }
