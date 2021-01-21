Technical Choices
=================

Concurrency
-----------

Since most, if not all, of the system's use cases are I/O intensive,
it is natural to employ an asynchronous input/output framework to solve
concurrency issues.  Trio_ was picked for the ease of flow control offered
by `structured concurrency`_.

Web Server and Framework
------------------------

As asynchronous input/output was chosen, `Asynchronous Server Gateway Interface
(ASGI) <ASGI_>`_ was needed to cooperate the asynchronous routines in the application
and the server.  For server, Hypercorn_ was picked for its first-class support
for Trio.  The application was built on top of Quart_, a microframework
similar to Flask_ but for ASGI, for its flexibility.

Templating Language
-------------------

We use Jinja2_ for templating, which is the default choice for Quart.
It provides us with various tools that help secure the website easier.
For example, it allows HTML escaping |~| [jinja2esc]_,
which helps avoid XSS injection.

Persistency
-----------

For persistency, there are two separate concerns: storing the system's metadata,
which is a collection of small chunks of plain text, and storing the files
uploaded by the users.  In the former case, RethinkDB_, a `document-oriented
database`_, was chosen for recursive and less-structured data support.
Such database, however, is performance-wise unsuitable for larger files,
so IPFS_, which is a distributed file system that provides similar abstraction,
is used instead in the latter case.

By choosing RethinkDB instead of SQL,
we do not have to worry about SQL injection or similar database attack.
This is because the query language ReQL is not based on
string parsing |~| [rethinkdbdoc]_, but built as methods
in the implementing language.

.. _Trio: https://trio.readthedocs.io
.. _RethinkDB: https://rethinkdb.com
.. _IPFS: https://ipfs.io
.. _structured concurrency:
   https://vorpus.org/blog/notes-on-structured-concurrency-or-go-statement-considered-harmful/
.. _ASGI: https://asgi.readthedocs.io
.. _Hypercorn: https://pgjones.gitlab.io/hypercorn
.. _Quart: https://pgjones.gitlab.io/quart-trio
.. _Flask: https://flask.palletsprojects.com
.. _document-oriented database:
   https://en.wikipedia.org/wiki/Document-oriented_database
.. _Jinja2: https://jinja.palletsprojects.com
.. [jinja2esc] The Pallets Project.  "Template Designer Documentation".
   *Jinja Documentation (2.11.x)*.  Retrieved 2021-01-18.
   https://jinja.palletsprojects.com/en/2.11.x/templates/#html-escaping
.. [rethinkdbdoc] RethinkDB. "Introduction to ReQL".  Retrieved 2021-01-18.
   https://rethinkdb.com/docs/introduction-to-reql/#reql-embeds-into-your-programming-language
