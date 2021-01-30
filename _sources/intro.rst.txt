Introduction
============

Motivation
----------

Group project and internship are annual activities for master students
and last year bachelor students in
University of Science and Technology of Hanoi (USTH).
With the university's projected growth, managing them is becoming a complicated
yet important task.  The management is required for both students and the school staff.
From students' and supervisors' perspective, there should be a tool that helps
manage numerous tasks in their projects.  From faculties' academic assistants'
perspective, a system that helps collect projects' progress and evaluation
is of great importance, since manual input for students' grade is an exhausting task
and can lead to error.

Therefore, a collaborative platform that students and supervisors can use
in their project, which also support academic evaluation and report, is needed.
This tool should help students manage their projects seamlessly, and academic
assistants collect statistical reports quickly.

Background
----------

Project management is a common problem, which is why it is unsurprising
that there have been a variety of project management systems.
Students and supervisors have already been using some of these systems
to manage their tasks.  We studied these systems to see how projects
are commonly and effectively managed.

Trello_,a popular web service for keeping track of tasks, uses `Kanban board`_.
A Kanban board consists of several columns, each of which contains some tasks
in a certain stage, such as *to-do*, *in progress*, *in review*, and *done*.
User can move a task from a column to another.  As this workflow is easy to learn,
it is also used by other popular collaborative platforms,
such as Jira_, Asana_, GitHub_, or Tuleap_.

Some other software, such as GanttProject_, ProjectLibre_, or `Microsoft Project`_
is modeled after another tool: `Gantt chart`_.  Gantt chart is a way of using bar chart
to visualize the schedule for the project.  This method simplifies scheduling
independent tasks to be worked on at the same time to save wait time.

Although many of project management systems above
are targeting software development projects,
The application of Kanban board and Gantt chart
as project management tools can benefit any other fields.
In fact, using Kanban board in other fields is also known
to improve productivity by saving time and aid internal communication. |~| [willeke]_

As effective and popular as existing project management systems are,
they do not support academic evaluation, which is one of our main motivations.
Extending existing free software could be an approach to achieve our target.
However, the complexity of those systems makes it impractical
to study within a short period.
Therefore, we started this project to create from scratch
an academic-oriented project management system.

Objective
---------

In this project, we aimed to develop a collaboration platform
for students and mentors.  The resulting system should be able to
not only integrate well into their workflows and academic management tasks
but also effectively perform on back-end servers often with limited resources
and across a wide variety of end-user machines.

.. _objcollab:

The Collaboration Platform
""""""""""""""""""""""""""

At the lowest level, discussion would be facilitated through comment threads,
organized into logical tasks.  The tasks would be categorized by stages
such as *to-do*, *doing* and *done*.  These stages would then be visualized
as columns in a `Kanban board`_ to aid managing and prioritizing tasks.

The Academic Integration
""""""""""""""""""""""""

In addition to discussion and job scheduling, the system-to-be would
support academic tasks.  To mentors and committees, these are grading
and giving feedback.  To academic assistants, these include (but not
limited to) exporting transcripts and statistical reports, and tracking
students' overall progress to provide help if necessary.

.. _appapp:

The Applicable Web Application
""""""""""""""""""""""""""""""

The system should be implemented as a web application for
portability |~| [mikkonen2008]_.  It should be easy to be adopted by users on
different devices network connection quality, whilst being simple enough
to be maintained by a few administrators to run on modest hardware.

Report Structure
----------------

The report contains following sections:

1. **Introduction**: Introduce the motivation and background of the problem
   and some related works.
2. **Objective**: Further define the objective and scope of the project.
3. **Requirements**: List all important use cases with their specifications.
4. **Methodology**: Steps we made to develop the system:
   technical choices, analysis, design, and implementation.
5. **Results and Discussion**: The result and what we learned from this project.
6. **Conclusion and Future Work**: Our conclusion after the project
   and work that can be done to improve the system.

.. _Kanban board: https://en.wikipedia.org/wiki/Kanban_board
.. _Gantt chart: https://en.wikipedia.org/wiki/Gantt_chart
.. _Asana: https://asana.com/
.. _GitHub: https://github.com/
.. _Jira: https://www.atlassian.com/software/jira
.. _Trello: https://trello.com/
.. _Tuleap: https://www.tuleap.org/
.. _GanttProject: https://www.ganttproject.biz/
.. _Microsoft Project: http://office.microsoft.com/project/
.. _ProjectLibre: https://www.projectlibre.com/
.. [willeke] Marian H.H. Willeke,
   "Agile in Academics: Applying Agile to Instructional Design".
   *2011 Agile Conference*, p. 246-251, Salt Lake City, UT, 2011.
   :doi:`10.1109/AGILE.2011.17`.
.. [mikkonen2008] Tommi Mikkonen and Antero Taivalsaari.
   "Web Applications---Spaghetti Code for the 21st Century".
   *2008 Sixth International Conference on Software Engineering Research,
   Management and Applications*, p. 319--328, Prague, 2008.
   :doi:`10.1109/SERA.2008.16`.
