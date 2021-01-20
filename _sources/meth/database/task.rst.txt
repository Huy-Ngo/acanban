Task
====

To identify the tasks, the tasks' names and descriptions are needed.

``name`` : ``string``
   The name of the task

``creator`` : ``User``
   The user who created the task

``description`` : ``string``
   The summary of a task

Since tasks should be assigned to someone to perform the tasks,
there should be a field for linking to the assignee.
Moreover, there should be a status to track if the task is in progress
or has been done.
The user can upload a report or add a link to show their work
to address the task.

``assigned_to`` : ``User``
   The assignee of the task. Must have role ``student``.

``status`` : ``integer``
   The status of the project in the Kanban board: to-do, in progress, or done.

``work`` : ``string`` (URL)
   The URL to the work by the assignee that addresses the task.
   It can be a link to a file hosted on the acanban server
   (if the user uploads it to acanban)
   or an external link (e.g. to a GitHub pull request, or to a document hosted
   by some other services)

To facilitate collaboration, there should be a discussion thread for participants
to discuss the problems of the tasks:

``discussion`` : ``array`` of ``Comment``
   List of ``Comment``\s created for this task

Like for projects, creation date and deadline are added so that participants
can keep their progress.  It can also help sort the tasks by timeline.

``created_on`` : ``time``
   The date and time the task is created.

``deadline`` : ``time``
   The date and time for the deadline of the task.

Even though individual tasks are not required to be evaluated and the evaluation
does not add to the final evaluation, an evaluation field was designed for tasks
so that the assignees can receive a measurable feedback on their work.

``evaluation`` : ``number``
   The evaluation of the task
