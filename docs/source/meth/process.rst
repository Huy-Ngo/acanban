.. _proc:

Development Process
===================

From requirement, analysis and design documents to implementation
were version controlled through git_.  For achieving better productivity
and quality, we attempted to define a rigorous yet flexible workflow,
detailed in the following subsections.

Collaboration Model
-------------------

The development mostly took place on GitHub_, except for realtime communication
which occured either on a Matrix_ chat room or in the physical world.

At the high level, the works were split into multiple subprojects [#ghproj]_,
where each project contained multiple self-contained tasks,
which were to be resolved by patches separated by logical changes |~| [sep]_.
Projects are visually presented as Kanban boards including at the minimum
of three columns: *To do*, *In progress* and *Done*.

In the time dimension, we divided the development period into multiple
short iterations, whose length varied based on our schedule [#vary]_.
At the beginning of every iteration, we selected tasks from the *To do*
column to *In progress*.  In addition to inital planning, tasks were also added
to *To do* as we discovered new issues during discussions or development,
and were democratically and appropriately assigned to the group members.

At a lower level, each task was resolved via a self-contained patch.
This means implementation patches must be accompanied by the tests
coverring the change.  How patches were checked (including executing
automated tests) are detailed in the next subsection.

At the end of an iteration, we publish a (pre-)release to PyPI_
and deploy it to a test deployment server [#vm]_
kindly provided by `USTH ICTLab`_.

Quality Assurance
-----------------

In order to ensure the correctness of the implementation, we tried to take
quality assurance as seriously as we can.  To begin with, a git branch
was chosen to be the ``main`` one for patches to base on.  It was protected
from being pushed directly onto without the reviewing process, which comprised
of automated checks and peer reviews.

From the beginning, continuous integration (CI) was set up for both
the implementation and this report itself [#ci]_.  For the paper, it simply
tried to compile the original source written in reStructuredText into PDF_
for the ease of viewing for the peer reviewers.  The software, however,
were subjected to the following assertions: 

* Style checker (flake8_ and isort_), which statically analysed
  the Python source files for errors and inconsistencies
* Type checker (mypy_), which examined the Python AST_
  for static typing issues to detect common bugs
* Testing and coverage, which automatically ran the tests
  and report the test coverage

We actively worked to enforce 100% :term:`branch coverage <Branch coverage>`,
most of which are covered by unit tests, which helped discover mistakes
as well as regressions in later modifications.  Integration testing, however,
could often be tedious |~| [intest]_, and thus we chose to not imposing it.
In compensation, we examined the test deployment at the end of iterations
for bugs not having been caught by the test suite.

At the same time, patches were reviewed manually by at least one other
team member.  This is not only for maintaining quality standards but also
to make the team more well aware of changes happening to the shared code base.
Once approval was granted and automated checks were passing,
the patch was rebase on top of the ``main`` branch.
Continuous integration was then run again, for continuous integration.

.. _git: https://git-scm.com
.. _GitHub: https://github.com/Huy-Ngo/acanban
.. _Matrix: https://matrix.org
.. _PyPI: https://pypi.org/project/acanban
.. _USTH ICTLab: https://ictlab.usth.edu.vn
.. _PDF: https://www.iso.org/standard/75839.html
.. _flake8: https://flake8.pycqa.org
.. _isort: https://pycqa.github.io/isort
.. _mypy: https://mypy.readthedocs.io
.. _AST: https://docs.python.org/3/library/ast.html
.. [#ghproj] https://github.com/Huy-Ngo/acanban/projects
.. [#vary] Unfortunate for us, the group project took place
   during the examination season, and thus our time pool shrunk
   on weeks with higher density of exams for other courses.
.. [#vm] https://acanban.ga
.. [#ci] https://builds.sr.ht/~huyngo/acanban
.. [sep] The kernel development community.
   *Submitting patches: the essential guide to getting your code
   into the kernel*.  The Linux Kernel documentation.  Retrieved 2021-02-04.
   https://www.kernel.org/doc/html/latest/process/submitting-patches.html#separate-your-changes
.. [intest] Michael Steindl and Juergen Mottok.
   "Optimizing software integration by considering
   integration test complexity and test effort".
   *Proceedings of the 10th International Workshop on Intelligent Solutions
   in Embedded Systems*, Klagenfurt, 2012, p. |~| 63-68.
