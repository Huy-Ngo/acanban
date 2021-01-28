Results and Discussion
======================

Results
-------

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

.. figure:: screenshots/registration.png

   The registration page

.. figure:: screenshots/login.png

   The login page

.. figure:: screenshots/home_login.png

   The home page when the user is logged in

.. figure:: screenshots/profile-edit.png

   The profile edit page

.. figure:: screenshots/project-info.png

   The info page for a project

.. figure:: screenshots/project-edit.png

   Editing a project's information

.. figure:: screenshots/new-project.png

   Creating a new project

.. figure:: screenshots/report.png

   Viewing and uploading project report

.. figure:: screenshots/presentation.png
   :figwidth: 40%

   Viewing and uploading presentation slides

.. figure:: screenshots/mob-home.jpeg
   :figwidth: 40%

   Home page is responsively designed for mobile

.. figure:: screenshots/mob-project.jpeg

   Responsive design for project view

Discussion
----------

All of these use cases have been implemented in a simplistic manner,
which satisfied our goal of accessibility from all devices.

Nonetheless, there are numerous flaws that we have found in our system:

- Important features that have not been implemented:

  - Notification
  - Create, view, and complete tasks on a simple Kanban board
  - Discussion
  - Jury's evaluation of reports and presentation
  - Statistical reports for academic assistant

- Registration currently allows anyone to have as many accounts as they want,
  which is not secure.
- There hasn't been checking for maximum grade and minimum grade fraction.
- File types for reports and slides are not ensured yet.
- The user interface is not very attractive.

.. _Affero General Public License: https://www.gnu.org/licenses/agpl-3.0.html
.. [1] https://github.com/Huy-Ngo/acanban
.. [2] https://acanban.ga
