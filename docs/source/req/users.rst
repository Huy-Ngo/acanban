Types of Users
==============

Firstly, to understand which use cases that need to be implemented,
we analyzed which types of users there are and how they interact
with our system.

The primary users are **students** and their **supervisors**.
They can interact quite similarly with the system:

- Create a new project
- Edit public information about a project
- Invite new members to a project
- Create new tasks
- Evaluate the tasks

However, there are differences between what students and supervisors can do.
Unlike supervisors, students are not allowed to evaluate the project.
On the other hand, supervisors should not be able to do tasks nor to upload
project reports and slides while students can do those tasks.

After the students submit the reports, there will be **judges**
whose responsibility is to assess these reports.  They also evaluate
the groups' project oral defense (also called *presentation*).
They should therefore be allowed to access and evaluate
reports and slides of projects they are assigned.

During the process, **academic assistants** of each faculties should collect
statistical reports of each project and print the results of the subject.

The system's user categories can be summarized in the table below

.. tabularcolumns:: |l|L|L|

==========  =========================  ===============================
Type        Responsibility             Ability                        
==========  =========================  ===============================
Student     progress the project       manage projects,               
                                       manage and complete tasks,     
                                       upload reports and slides      
Supervisor  support the group and      create tasks, evaluate projects
            evaluate the project                                      
Judge       evaluate groups'           access and evaluate            
            reports and presentations  reports and presentation       
Assistant   collect statistical        aggregate and export           
            report and evaluation      projects' evaluation           
==========  =========================  ===============================

In the system, we assigned users of each group a role: ``student``,
``supervisor``, ``assistant``, ``judge``.
