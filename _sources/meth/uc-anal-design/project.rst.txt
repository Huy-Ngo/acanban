Project Management
==================

In this section, we present the system design for project management use cases.
Task management use cases, while indeed are part of project management,
are discussed in the next.

Since Quart, the framework we employ, is not strictly object-orientated
and the design involves a lot of short-circuiting, it is represented
via activity diagram instead of the traditional UML diagrams often used
in this context, namely sequence diagrams and collaboration diagrams.

Create Project
--------------

The design for the use case :ref:`project create`
is described in :numref:`p-create`, where the system takes the initial values
from the user to construct a new project and insert it into the database.

.. uml:: uml/p-create.puml
   :scale: 80%
   :caption: Activity diagram illustrating project creation
   :name: p-create

Show Project Information
------------------------

The design for the use case :ref:`project info`
is described in :numref:`p-info`, where the system reply
to a specified project identifier with its basic information,
retrieved from the database.

.. uml:: uml/p-info.puml
   :caption: Activity diagram illustrating showing project's basic information
   :name: p-info

Edit Project Information
------------------------

The design for the use case :ref:`project edit`
is described in :numref:`p-edit`, where the system takes the updated
project information from the user and synchronizes the database accordingly.

.. uml:: uml/p-edit.puml
   :scale: 80%
   :caption: Activity diagram illustrating updating project's basic information
   :name: p-edit

List member
-----------

The function allow listing the members in the projects.

The implementation involves only ``projects`` database table, in which we get
the member list of members. Two fields are being called is ``supervisors`` and
``students``.

When user navigate to member tab, the list of members in the project,
classified as ``supervisors`` and ``students`` is shown in a form.

.. uml:: uml/p-member-list.puml
   :caption: Analysis sequence diagram
      for the member listing process
   :name: p-member-list

Invite member
-------------

Since the project is initialized with only the creator,
we need a function to invite members.
Only who is in the project could introduce a new member.

The design involves the ``projects`` database table,
where the `members` index is to be updated.

When user enters the invited member's name, the project controller checks
the ``projects`` table in the database whether the person is already in
the project, or that user is an assistant, or that user has not registered.
If all three conditions is satisfied, two databases is updated accordingly.

.. uml:: uml/p-member-add-success.puml
   :caption: Analysis sequence diagram for successfully invite member.
   :name: p-member-add-success

If added user is already in the project

.. uml:: uml/p-member-add-exist-name.puml
   :caption: Analysis sequence diagram for adding member
      when user is existed in project.
   :name: p-member-add-exist-name

If added user is an assistant

.. uml:: uml/p-member-add-assistant.puml
   :caption: Analysis sequence diagram for adding member
      when user is an assistant.
   :name: p-member-add-assistant

If the name is not in ``users`` database

.. uml:: uml/p-member-add-not-registered.puml
   :caption: Analysis sequence diagram for adding non-registered user.
   :name: p-member-add-not-registered
