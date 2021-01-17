Security
========

Authentication
--------------

In order to protect the data from unauthorized users, we must first verify
their identity, i.e., authenticate the users.

Register
''''''''

TBD

Log In
''''''

TBD

Authorization
-------------

After authenticated, the users are authorized according to their role
and their identity.
For example, a user with role "assistant" cannot participate in a project,
or student cannots edit a projects they do not participate in.

Encrypted Connection
--------------------

To protect the data sent through HTTP, we upgraded it to HTTPS by creating
a TLS certificate on the server side.
Furthermore, the server is configured to use secure cookies, that is, cookies
that can only be sent via HTTPS.

Injection Attacks
-----------------

XSS Attack
''''''''''

Jinja by default escapes all HTML tags.  This means that if an attacker tries
to inject a script into the content, for example, setting project description
as ``<script>sendSensitiveData()</script>``, the script tags would appear
as is and not parsed as a script element.

Moreover, the server is configured to use same-site and HTTP-only cookies,
which renders any cookie-stealing JavaScript useless.
