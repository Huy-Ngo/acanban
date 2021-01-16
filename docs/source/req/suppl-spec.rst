Supplementary Specification
===========================

Besides the functionalities specified in the Use-Case model,
following are more specifications for non-functional requirements.

Usability
---------

The system should be intuitive to any users.
Users should be able to use it with little to no training.

To achieve this, the interface should:

- not contain superfluous and distracting features
- the user's projects should be easily found as soon as the user sign in
  (for students and supervisors)
- All bodies of text should be readable and legible.
  Text font should thus be decided by the user
  since each user finds a different font easier to read.


Reliability
-----------

The system must be available 99.99% of the time (that is,
there must be no more than a few seconds of outage a day).

Performance
-----------

The system should be able to support up to 1000 users
simultaneously performing different tasks at any given time.

Supportability
--------------

The user interface must be functional on both desktop computers
as well as on smartphones.

Security
--------

The system must not allow internal information to be accessed and modified
by an unauthorized user.

The systems should not be vulnerable to common security threat, such as
XSS, SQL injection, DDoS attack.

Legal Constraints
-----------------

The resulted software should be released under a copyleft free license,
namely Affero General Public License version 3.0,
in order to persist digital freedom for education.
