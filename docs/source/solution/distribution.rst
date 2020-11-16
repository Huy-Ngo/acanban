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
      artifact "/etc/systemd/system/gpms.service" as systemd_conf
      component GPMS as gpms
      component hypercorn
      node systemd <<daemon>>
      component IPFS
   }

   Browser --- hypercorn: HTTPS
   hypercorn - systemd: run instance
   systemd <- systemd_conf: configure
   hypercorn -- gpms
   gpms - IPFS
   IPFS - db

Alternative deployment model with load-balancing and a separate data server:

.. uml::

   node Client {
      node Browser
   }

   node "Load Balancing Server" as balancer {
      component NGINX as nginx <<load balancer>>
      artifact "/etc/nginx/sites-available/gpms" as nginx_conf
   }

   node Server {
      artifact "/etc/systemd/system/gpms.service" as systemd_conf
      component GPMS as gpms
      component hypercorn
      node systemd <<daemon>>
   }

   node "Database Server" as db_server {
      database "RethinkDB" as db
      component IPFS
   }

   Browser --- balancer: HTTPS

   nginx <. nginx_conf: configure
   nginx "1" --- "1..*" Server

   hypercorn - systemd: run instance
   systemd <. systemd_conf: configure
   hypercorn -- gpms
   gpms "1..*" -- "1" db_server
