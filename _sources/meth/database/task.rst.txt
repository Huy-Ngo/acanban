Task
====

Each ``Task`` object has following attributes:

``name`` : ``string``
   The name of the task

``creator`` : ``User``
   The user who created the task

``status`` : ``integer``
   The status of the project in the Kanban board: to-do, in progress, or done.

``assigned_to`` : ``User``
   The assignee of the task. Must have role ``student``.

``description`` : ``string``
   The summary of a task

``discussion`` : ``array`` of ``Comment``
   List of ``Comment``\s created for this task

``file`` : ``File``
   Optional file that shows the assignee's work to address the task.

``created_on`` : ``time``
   The date and time the task is created.

``deadline`` : ``time``
   The date and time for the deadline of the task.

``evaluation`` : ``number``
   The evaluation of the task
