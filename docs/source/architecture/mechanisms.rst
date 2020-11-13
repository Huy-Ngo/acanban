Architectural Mechanisms
========================

Analysis Mechanisms
-------------------

Concurrency
   A mean to overlap the execution of multiple interacting computational tasks.

Persistency
   A mean to make an element persistent,
   i.e. exists after the application that created it ceases to exist.

Analysis-to-Design-to-Implementation Mechanisms Map
---------------------------------------------------

==================  ==========================  ========================
Analysis Mechanism  Design Mechanism            Implementation Mechanism
==================  ==========================  ========================
Concurrency         Structured concurrency      Trio_
Persistency         Document-oriented database  RethinkDB_
Persistency         Distributed file system     IPFS_
==================  ==========================  ========================

Since most, if not all, of the system's use cases are I/O intensive,
it is natural to employ an asynchronous input/output framework to solve
concurrency issues.  Trio_ is picked for the ease of flow control offered
by `structured concurrency`_, along with the ASGI_ layers like Quart_
and Hypercorn_.

For persistency, there are two separate concerns: storing the system's metadata,
which is a collection of small chunks of plain text, and storing the files
uploaded by the users.  In the former case, RethinkDB_, a `document-oriented
database`_, was chosen for recursive and less-structured data support.
Such database, however, is performance-wise unsuitable for larger files,
so IPFS_, which is a distributed file system that provides similar abstraction,
is used instead in the latter case.

.. _Trio: https://trio.readthedocs.io
.. _RethinkDB: https://rethinkdb.com
.. _IPFS: https://ipfs.io
.. _structured concurrency:
   https://vorpus.org/blog/notes-on-structured-concurrency-or-go-statement-considered-harmful/
.. _ASGI: https://asgi.readthedocs.io
.. _Quart: https://pgjones.gitlab.io/quart-trio
.. _Hypercorn: https://pgjones.gitlab.io/hypercorn
.. _document-oriented database:
   https://en.wikipedia.org/wiki/Document-oriented_database
