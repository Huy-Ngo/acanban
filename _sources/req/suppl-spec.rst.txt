Supplementary Specification
===========================

Besides the functionalities specified in the Use-Case model,
following are more specifications for non-functional requirements.

Usability
---------

The system should be intuitive to any users.
Users should be able to use it with little to no training.

In order to achieve this, we derived specific design contraints:

- The user interface should not contain superfluous and distracting features.
- The user's projects should be easily found as soon as the user sign in
  (for students and supervisors).
- All bodies of text should be readable and legible.
  Text font should thus be decided by the user
  since each user finds a different font easier to read.
- Error messages should be informative

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

The user interface must be functional on both desktop or laptop computers,
tablet, and on smartphones.

The file system must support uploading various file formats
that are used for discussing and reporting project results:

- Document: docx, pdf, tex, md, rst, plain text, etc.
- Audiovisual: png, jpg/jpeg, tiff, ogg, mp3, mp4, etc.
- Presentation: pptx, tex, pdf

Security
--------

The system must not allow internal information to be accessed and modified
by an unauthorized user.  Passwords should be all stored as hash.

The systems should not be vulnerable to common security threat, such as
XSS, SQL injection, DDoS attack.

The connection to the server must use HTTPS protocol,
that is, it must be encrypted with TLS/SSL.

Legal Constraints
-----------------

The resulted software should be released under a copyleft free license,
namely Affero General Public License version 3.0,
in order to persist digital freedom for education.
