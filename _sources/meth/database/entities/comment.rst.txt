Comment
=======

``Comment`` object represent a comment insides a task's discussion.
It should contain the identifier for the commenter and its content.

``creator`` : ``User``
   The user who created the comment.

``content`` : ``string``
   The content of the comment.

Since the discussion follows a forest structure, each comment recursively
contains a list of replying comment.

``comments`` : ``array`` of ``Comment``
   List of ``Comment``\s replying to it.

To let the user know if the comment is new or old, creation time is also added.

``created_on`` : ``time``
   The date and time the comment is created.
