Security
========

Authentication
--------------

In order to protect the data from unauthorized users, we must first verify
their identity, i.e., authenticate the users.

Register
''''''''

To register for an account, the user should fill a form
with personal information:

- real name
- username
- password
- the user's role, which can be student, supervisor, or assistant

When user submits a form to register for an account, the register controller
will check the database to see if the username exists.  If the username
does not exist, the controller will continue to create an account
in the database.  The password is stored in the database as a hash
for security.

After the successful account creation, the user will be
redirected to the home page.

.. uml:: register.puml
   :caption: Analysis sequence diagram
      for the basic flow of registration process
   :name: reg-basic

If the username or email is taken,
the controller should inform so to the user.

.. uml:: register-exist-mail.puml
   :caption: Analysis sequence diagram
      for the alternative flow of the registration process
      where the mail is taken
   :name: reg-exist-email

.. uml:: register-exist-username.puml
   :caption: Analysis sequence diagram
      for the alternative flow of the registration process
      where the username is taken
   :name: reg-exist-name

Another exceptional flow happens when the user request an invalid role.
This should not happen when the user submit the form via browser,
but it can happen if someone is submitting it via a nonstandard way.

.. uml:: register-wrong-role.puml
   :caption: Analysis sequence diagram
      for the alternative flow of the registration process
      where the role is invalid
   :name: reg-role

In order to prevent faking identity, we intended to require a token
for registration.  This token is provided by the system administrator
and each person can only receive one token, so if they use it
for faking identity, they cannot create their account anymore and
have to suffer th consequence.

Alternatively, the administrator can remove the register endpoint
and generate the accounts for each user.

However, we did not implement either of these schemes.

Log In
''''''

The user can log in to the site in the login endpoint.
After submitting the form with their username and password,
they should be logged in.

.. uml:: login.puml
   :caption: Analysis sequence diagram
      for the basic flow of login
   :name: log-basic

However, if the user tries to log in with a non-existent account,
the controller should raise an error and inform the user so.

.. uml:: login-no-user.puml
   :caption: Analysis sequence diagram
      for the alternative flow of login
      where there is no user with the username
   :name: log-no-user

If the user input wrong password, the user should also not be logged in
and be informed of wrong password.

.. uml:: login-wrong-pass.puml
   :caption: Analysis sequence diagram
      for the alternative flow of login
      where the 
   :name: log-wrong-path

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
