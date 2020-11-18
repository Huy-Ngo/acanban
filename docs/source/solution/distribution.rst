Distribution
============

Deployment Model
----------------

.. uml::

   node Client {
      node Browser
   }

   node Server {
      database "RethinkDB" as db
      artifact "acanban.service" as systemd_conf
      component Acanban
      component Hypercorn
      node systemd <<daemon>>
      component IPFS
   }

   Browser --- Hypercorn: HTTPS
   Hypercorn - systemd: run instance
   systemd <- systemd_conf: configure
   Hypercorn -- Acanban
   Acanban - IPFS
   Acanban - db

Alternative deployment model with load-balancing and a separate data server:

.. uml::

   node Client {
      node Browser
   }

   node "Load Balancing Server" as balancer {
      component NGINX as nginx <<load balancer>>
      artifact "/etc/nginx/sites-available/acanban" as nginx_conf
   }

   node Server {
      artifact "acanban.service" as systemd_conf
      component Acanban
      component Hypercorn
      node systemd <<daemon>>
   }

   node "Database Server" as db_server {
      database "RethinkDB" as db
      component IPFS
   }

   Browser --- balancer: HTTPS

   nginx <. nginx_conf: configure
   nginx "1" --- "1..*" Server

   Hypercorn - systemd: run instance
   systemd <. systemd_conf: configure
   Hypercorn -- Acanban
   Acanban "1..*" -- "1" db_server
