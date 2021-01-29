User Interface and User Experience
==================================

This section is dedicated to the design of user interface and user experience,
in order to support the goal of achieving :ref:`appapp`.  Generally,
the application should be portable across different input/output devices,
as well as being easy to adopt by the end-users.

Navigation
----------

For the ease of navigation, the organization of web pages must
be well-structured.  Furthermore, it is important to avoid having deadends,
which negatively impact the traversability.  With these principles im mind,
we then designed the navigation graph.  For every user, the following
auxiliary endpoints are available, as illustrated in :numref:`auxnav`.

* ``/register``: Registration form
* ``/login``: Login form
* ``/u/<username>``: User information, including per project
* ``/u/<username>/edit``: Form for updating user information
* ``/``: User dashboard containing the list of projects
  perse participates in
* ``/p``: List of public projects
* ``/p/create``: Form for project creation
* ``/p/<uuid>``: Project's page

.. uml::
   :caption: Auxiliary endpoints
   :name: auxnav

   (*) --> "/register" as register
   (*) --> "/login" as login
   login --> "/" as root
   register --> root
   root --> "/p" as projects
   projects --> "/p/create"
   projects --> "/p/<uuid>" as project

   root --> "/u/<username>" as user
   user --> "/u/<username>/edit"
   user --> project
   root --> project
   root --> user
   projects --> user

Each project's page is divided into several tabs, namely ``info``, ``edit``,
``members``, ``tasks``, ``report`` and ``slides``, as shown in :numref:`pnav`.

* ``/p/<uuid>/info`` (GET): Project's basic information
* ``/p/<uuid>/edit`` (GET and POST): Form for updating
  project's basic information
* ``/p/<uuid>/members`` (GET): Project's member listing
* ``/p/<uuid>/invite`` (POST): Form for adding a member
* ``/p/<uuid>/leave`` (POST): Form for leaving the project
* ``/p/<uuid>/tasks`` (GET): Tasks overview (Kanban board)
* ``/p/<uuid>/report`` (GET): Report revisions and evaluation
* ``/p/<uuid>/report/upload`` (POST): Form for uploading report revision
* ``/p/<uuid>/report/eval`` (POST): Form for evaluating report
* ``/p/<uuid>/slides`` (GET): Slides revisions and evaluation
* ``/p/<uuid>/slides/upload`` (POST): Form for uploading slides revision
* ``/p/<uuid>/slides/eval`` (POST): Form for evaluating report
* ``/ipfs/<cid>`` (GET): IPFS gateway proxy for file downloading

.. uml::
   :caption: Project's endpoints
   :name: pnav

   left to right direction

   (*) --> "/p/<uuid>" as root
   root --> "/p/<uuid>/info" as info
   info --> "/p/<uuid>/edit" as edit
   info --> "/p/<uuid>/members" as members
   info --> "/p/<uuid>/tasks" as tasks
   info --> "/p/<uuid>/report" as report
   info --> "/p/<uuid>/slides" as slides

   members --> "/u/<username>"
   members --> "/p/<uuid>/invite"
   members --> "/p/<uuid>/leave"

   report --> "/p/<uuid>/report/upload"
   report --> "/ipfs/<cid>" as ipfs
   report --> "/p/<uuid>/report/eval"

   slides --> "/p/<uuid>/slides/upload"
   slides --> ipfs
   slides --> "/p/<uuid>/slides/eval"

Project's tabs are mutually interlinked but for brevity they are not connected
in the figure.  Additionally, POST-only endpoints redirects back to referrer
upon success.

Due to complexity, task-related endpoints are documented
separately in :numref:`tnav`, which consists of the ones listed below.
Pages in ``/p/<uuid>/tasks``, including the Kanban board,
exclusively serves :ref:`objcollab`.

* ``/p/<uuid>/tasks/<index>`` (GET): Task's description and discussion
* ``/p/<uuid>/tasks/<index>/comment`` (POST): Form for posting a comment
* ``/p/<uuid>/tasks/<index>/upload`` (POST): Form for uploading a file
* ``/p/<uuid>/tasks/eval`` (POST): Form for evaluating all tasks

.. uml::
   :caption: Task endpoints
   :name: tnav

   (*) --> "/p/<uuid>/tasks" as tasks
   tasks --> "/p/<uuid>/tasks/<index>" as task
   task --> "/p/<uuid>/tasks/<index>/comment"
   task --> "/p/<uuid>/tasks/<index>/upload"
   task --> "/ipfs/<cid>"
   tasks --> "/p/<uuid>/tasks/eval"

Graphical User Interface
------------------------

At the higher level, we concentrated in making user interface that works well
for mobile devices.  Mobile first design might not always make the best use
of screen estate on larger devices, however we were confident that
such trade-off is worth the high portability and compability that we can bring
to the wide range of users.  That being said, we actively tried to compensate
through responsive design.  One case in point is the Kanban board,
which is rendered as a single column of different colors on handheld devices,
while expands to multiple columns (as often seen traditionally)
on a wider monitor.

We also strongly focused on accessibility.  The colors of relatively
high contrast and appropriate line length were chosen.  We also made use of
markup elements in the standardized manner with the hope of providing
compability for less common web browsers and supporting software
for visually impaired people.
