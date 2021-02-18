Entity Set
==========

Since each user can have zero, one, or several projects and
a group project can have several participating users, we model
the relation between them as many-to-many.

In each project, there could be many tasks which participants would complete
to advance the progress of the project.  There should be thus a one-to-many
relation between ``Project`` and ``Task``, and between user and task.

For each task, we designed a comment thread, in which students can discuss
their problems, or ask their supervisors for help, to resolve them faster.
Since there can be many comments in a task, the relation between ``Task``
and ``Comment`` should be one-to-many.

There can be comments replying to other comments, constructing a tree
data structure.  This structure is described by a self-referential one-to-many
relation.

Additionally, there should be a ``Artifact`` entity
for storing reports and slides. Each project can have one report and one slide.

We allowed uploading multiple revisions of reports and slides,
considering that the group can continually update their reports and presentations.
Each ``Artifact`` entity thus can have multiple associated ``File`` as revisions.

However, a file does not necessarily tie to any project,
since they can be referred in comments or by academic assistants
in their statistical reports.

Visually, the relations between entities described above
can be represented in :numref:`rel`.

.. uml:: rel.puml
   :caption: Relationship between entities in the database
   :name: rel

In each entity, there are other attributes and metadata which assists
the management.  They are described in the following sections.

.. toctree::
   :maxdepth: 2

   user
   project
   task
   artifact
   comment
   file
