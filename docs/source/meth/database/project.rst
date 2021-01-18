Project
=======

A ``Project`` object includes the project description
as well as the links to participants.

``name`` : ``string``
   The name of the project

``description`` : ``string``
   The summary of a project, which gives outsiders a brief idea of
   the objective or the scope of the project.

We separated the list of the members as supervisors and students
so that the view functions do not have to check for their roles all the time.

``supervisors`` : ``array`` of ``string``
   Usernames of supervisors of the project.

``students`` : ``array`` of ``string``
   Usernames of students participating in the project.

As described above, a project should have several tasks,
some revisions for reports and slides:

``tasks`` : ``array`` of ``Task``
   List of ``Task``\s created for this project.

``reports`` : ``Report``
   An object representing the reports for the project.

An important part of the project is the evaluation.
This is the evaluation of the supervisor. (rewrite this paragraph)

``evaluation`` : ``number``
   The evaluation of the work for the project
   that is provided by the supervisor.
   It can be based on previous evaluation of individual tasks.

Additionally, information about the timeframe of the project is also needed.
(TBD)

``created_on`` : ``time``
   The date and time the project is created.

``deadline`` : ``time``
   The date and time for the deadline of the project.
