Glossary
========

.. glossary::

   Accessibility

      Accessibility_ means that the technology is developed so that people
      with disabilities can use them.  It also benefits people without
      disabilities, such as people using devices with small screens
      or using slow Internet connection.

      In this document, *accessibility* usually refers to the latter sense.

   Asynchronous Server Gateway Interface (ASGI)

      ASGI_ is a spiritual successor to :pep:`WSGI <3333>`,
      the long-standing Python standard for compatibility between web servers,
      frameworks, and applications.

      WSGI succeeded in allowing much more freedom and innovation
      in the Python web space, and ASGI’s goal is to continue this onward
      into the land of asynchronous Python.

   Branch coverage

      A coverage criteria where each control structure's branch
      has been executed by the test suite.

   Cluster

      A set of machines that are connected
      and work together to be viewed as a single system.

   Cross-site scripting (XSS) attack

      Cross-site scripting (XSS) is a code injection attack where
      the attacker inserts client-side scripts into web pages.

   Distributed Denial of Service (DDoS) attack

      Denial of Service (DoS) attack is an attack where
      the attacker overloads the system with requests.
      DDoS is the distributed DoS attack, that is, the requests are flooding
      from multiple sources.

   Hypertext Transfer Protocol (HTTP)

      An application-level protocol for distributed, collaborative,
      hypermedia information systems [#http]_.

   InterPlanetary File System (IPFS)

      IPFS_ is a protocol and peer-to-peer network for storing and sharing data
      in a distributed file system.  It uses content-addressing
      to uniquely identify each file in a global namespace
      connecting all computing devices.

   Metadata

      Data that describes the information rather than containing
      the information itself.  This can include primary key of a table,
      creation date, etc.

   Participant

      People who participate in a project.

   Request

      A :term:`HTTP <Hypertext Transfer Protocol (HTTP)>` message
      from a client to a server including
      the protocol version in use, the method to be applied to
      and the identifier of the resource [#resource]_.

   Response

      A :term:`HTTP <Hypertext Transfer Protocol (HTTP)>` messge
      a server responds with, after receiving and interpreting
      a :term:`request <Request>` message [#response]_.

   SQL injection

      SQL injection is an attack where a malicious piece of code is passed
      in an SQL query, which changes the query to the query the attacker wants.

      For example, the attacker may try to create a student with name
      ``John' DROP TABLE Students; --`` and delete the whole table in doing so,
      if the vulnerability is not handled.

   Supervisor

      A person, normally a lecturer, that supervises, supports, and evaluate
      one or several project groups.

.. _Accessibility: https://www.w3.org/WAI/fundamentals/accessibility-intro/#what
.. _ASGI: https://asgi.readthedocs.io
.. _IPFS: https://ipfs.io
.. [#http] :rfc:`2616#section-1`
.. [#resource] :rfc:`2616#section-5`
.. [#response] :rfc:`2616#section-6`
