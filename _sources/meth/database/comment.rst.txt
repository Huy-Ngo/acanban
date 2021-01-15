Comment
=======

Each ``Comment`` object has following attributes:

``creator`` : ``User``
   The user who created the comment

``content`` : ``string``
   The content of the comment

``comments`` : ``array`` of ``Comment``
   List of ``Comment``\s replying to it

``created_on`` : ``time``
   The date and time the comment is created.
