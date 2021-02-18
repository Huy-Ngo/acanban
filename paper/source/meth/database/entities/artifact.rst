Artifact
========

The ``Artifact`` object is used for storing artifacts with multiple revisions
and can be academically evaluated.  The evaluation can come with a comment
so that the students can improve their skills in the future.

``comment`` : ``string``
   Evaluation comment.

``grade`` : ``float``
   Evaluated grade.

``revisions`` : ``array`` of ``string``
   UUIDs of previously uploaded revisions.
