Security
========

Secure Against DoS & DDoS Attacks
---------------------------------

Reduce Attack Surface Area
^^^^^^^^^^^^^^^^^^^^^^^^^^

One way to mitigate DDoS attacks is to minimize the surface area that can be attacked thereby limiting the options for attackers and allowing us to build protections in a single place. 

We want to ensure that we do not expose our application or resources to ports, protocols, or applications from where they do not expect any communication. Thus, minimizing the possible points of attack and letting us concentrate our mitigation efforts. 

   Placing our computation resources behind `CDNs <https://en.wikipedia.org/wiki/Content_delivery_network>`_ or `Load Balancers <https://en.wikipedia.org/wiki/Load_balancing_(computing)>`_ and restricting direct Internet traffic to certain parts of our infrastructure. Or we can just use firewalls or ACLs to filter our site in/out traffic.

*Since we do not know the detail on bandwidth capacity and server capacity. I'll look into it further once we have been informed. However, there is this* `open-source DoS protection <https://github.com/AltraMayor/gatekeeper/wiki>`_ *repo that I think could be useful*


Secure RethinkDB Cluster
------------------------

https://rethinkdb.com/docs/security/

Transport Layer Security
^^^^^^^^^^^^^^^^^^^^^^^^^^

Websites can use TLS to secure all communications between their servers and web browsers. Securing RethinkDB in this fashion is similar to securing a web site with a self-signed SSL certificate: create a private key and a certificate, then tell the server to use them. 

OpenSSL can be used to generate a private key and a certificate and then we can tell RethinkDB to use that certificate and secure the web administration UI.


Binding the web interface port
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Binding the web interface port can prevent direct access from remote machines. We can bind it to an IP address, and the most secure is to bind it to a localhost and then connect via a proxy. It is important to note that not using a proxy can lead to exploits.









