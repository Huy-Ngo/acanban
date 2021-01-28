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
is described in :numref:`p-create`.

.. uml:: uml/p-create.puml
   :caption: Activity diagram illustrating project creation
   :name: p-create

Show Project Information
------------------------

The design for the use case :ref:`project info`
is described in :numref:`p-info`.

.. uml:: uml/p-info.puml
   :caption: Activity diagram illustrating showing project's basic information
   :name: p-info

Edit Project Information
------------------------

The design for the use case :ref:`project edit`
is described in :numref:`p-edit`.

.. uml:: uml/p-edit.puml
   :caption: Activity diagram illustrating updating project's basic information
   :name: p-edit
