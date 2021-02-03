Project Management
==================

In this section, we present the system design for project management use cases.
Task management use cases, while indeed are part of project management,
are discussed in the next.

Create Project
--------------

The function allow creating projects.

The implementation involves two database tables:

- ``users`` database table, where ``role`` index is checked.
- ``projects`` database table, where new document is created.

When user requests to create project, the project controller checks
with ``quart_auth`` whether the person is authenticated.  The controller then
checks in ``users`` database that if the current user is not assistant.
When both conditions are satisfied, controller returns a form for user to
create project. After user fills in the form, the controller requests updating
``project`` database accordingly.

.. uml:: uml/p-create-success.puml
   :scale: 80%
   :caption: Activity diagram illustrating the successful project creation
   :name: p-create-success

If user is not authenticated, controller should inform that user
has not logged in.

.. uml:: uml/p-create-not-auth.puml
   :scale: 80%
   :caption: Analysis sequence diagram for create project by 
             non-authenticated user.
   :name: p-create-not-auth

If user is an assistant, controller should inform that user are not allowed
to create projects.

.. uml:: uml/p-create-assistant.puml
   :scale: 80%
   :caption: Analysis sequence diagram for create project by assistant.
   :name: p-create-assistant

Show Project Information
------------------------

The function allow showing project information.

The implementation involves only ``project`` database table,
where ``id``, ``students`` and ``supervisors`` indexes are visited

When user requests to create project, the project controller checks
with ``quart_auth`` whether the person is authenticated.  The controller then
checks in ``project`` database that if the current user is a member of project,
and if the project id is existed in database table.
When three conditions are satisfied, controller show the project information.

.. uml:: uml/p-info-success.puml
   :caption: Analysis sequence diagram for successfully show
             project information.
   :name: p-info-success

If ``quart_auth`` returns user is not authenticated, 
controller should inform accordingly.

.. uml:: uml/p-info-not-auth.puml
   :caption: Analysis sequence diagram for showing project information
             when user is not authenticated.
   :name: p-info-not-auth

If project id is not in the database, controller must show the error

.. uml:: uml/p-info-no-id.puml
   :caption: Analysis sequence diagram for showing project information
             when project id does not exist.
   :name: p-info-no-id

If user is not in the project, controller must show the error

.. uml:: uml/p-info-not-member.puml
   :caption: Analysis sequence diagram for showing project information
             when user is not a project's member.
   :name: p-info-not-member

Edit Project Information
------------------------

The function allow editing project information.

The implementation involves only ``project`` database table,
where ``id``, ``students`` and ``supervisors`` indexes are visited

When user navigate to edit tab, the project controller checks whether or not
the person is authenticated.  After that, it checks if the current user
is a member of project, and if the project id is existed in database table.
If all conditions are satisfied, controller shows the form for user to fill in.
When user fills the form, controller updates the ``project`` table with
the extracted data

.. uml:: uml/p-edit-success.puml
   :scale: 80%
   :caption: Analysis sequence diagram for successfully edit
             project information.
   :name: p-edit-success

If user is not authenticated

.. uml:: uml/p-edit-not-auth.puml
   :scale: 80%
   :caption: Analysis sequence diagram for editing project with
             un-authenticated user.
   :name: p-edit-not-auth

If project not exists in ``projects`` database table

.. uml:: uml/p-edit-no-id.puml
   :scale: 80%
   :caption: Analysis sequence diagram for editing projects
             when project id does not exist.
   :name: p-edit-no-id

If user is not a member in the project

.. uml:: uml/p-edit-not-member.puml
   :scale: 80%
   :caption: Analysis sequence diagram for editing projects
             when user is not a member of the project.
   :name: p-edit-not-member

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
