Functional Decomposition
========================

From the project objectives, we applied divide-and-conquer strategy:
decomposed each expected functionality and thereby outlined the use cases
we need to implement.

The work breakdown structure (WBS) diagram in :numref:`wbs`
summarizes the decomposition we made.

.. uml:: wbs.puml
   :caption: The features the system was expected to have.
   :name: wbs

In the following two sections, we will justify this breakdown.

Building a Collaboration Platform
---------------------------------

For the users to collaborate, they should be able to create projects and tasks.
They should be also able to edit them in case they make some mistakes or they
need to update.

Each task should be assigned to some members.  After it is done, the member
should be able to complete it.  As they do task, they may need to discuss the problem.

Academic Integration
--------------------

Group projects are evaluated according to three criteria:

#. The project outcome
#. The written reports
#. The presentation, also called oral defense

The first one is evaluated by the supervisor; the latter two are evaluated
by the judge.

The system should therefore allow students to upload their reports,
and supervisors and judges to evaluate them.

After the evaluation is made, the result is aggregated by each faculty's
academic assistants, who then export the results or make statistical reports.
