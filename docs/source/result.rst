Results and Discussion
======================

Results
-------

In this project, we clarified the requirements for the software,
defined the system architecture, and drafted some analysis and design
for the required use cases.

Based on the previous analysis and design,
we have successfully implemented some of the use cases:

- Authentication
- Create and edit group projects
- Invite new members to a project
- Upload reports and slides
- Supervisors can evaluate students' work

The current implemented source code is published on GitHub [1]_
under `Affero General Public License`_.
It is deployed on USTH ICTLab's server [2]_.

Discussion
----------

System's flaws
""""""""""""""

All of these use cases have been implemented in a simplistic manner,
which satisfied our goal of accessibility from all devices.

Nonetheless, there are numerous flaws that we have found in our system:

- Important features that have not been implemented:

  - Notification
  - Create, view, and complete tasks on a simple Kanban board
  - Discussion

- Actors whose functionality have not been implemented: judges and assistants
- Registration currently allows anyone to have as many accounts as they want,
  which is not secure.
- There has not been checking for maximum grade and minimum grade fraction.
- File types for reports and slides are not ensured yet.
- There has not been a graphical user interface for administration.
- The user interface is not very attractive.

Difficulties
""""""""""""

During the project, we met several difficulties in different aspects.

The primary obstacle for us was the lack of time spent for the project.
This lack of time dedicated to the project was because of poor time management.
Moreover, there had been other time-consuming projects and labworks in other courses,
which make the management harder.

Another problem was the collaboration: There were several conflicts among
some members' expectations of the project and workflows. People tended to work
at different time in day, which made code reviews take a longer time than it should.
Some members were not too keen on the project and did not spend enough time for it.

There were also some technical struggles: Not everyone in the group was familiar
with web development in Python, let alone the framework. This revealed another
issue, which is communication -- some members did not reach out to others,
which made it hard for the others to help.

As our project aimed to develop a project collaboration platform,
we can analyze these difficulties to add features that can mitigate them. 

.. _Affero General Public License: https://www.gnu.org/licenses/agpl-3.0.html
.. [1] https://github.com/Huy-Ngo/acanban
.. [2] https://acanban.ga
