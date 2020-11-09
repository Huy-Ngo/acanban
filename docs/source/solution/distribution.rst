Distribution
============

Deployment Model
----------------

.. uml::

   node Client {
      node Browser
   }

   node Server {
      database "JSON-based\nDatabase" as db
      artifact "/etc/systemd/system/gpms.service" as systemd_conf
      component GPMS as gpms
      component hypercorn
      node systemd <<daemon>>
   }

   Browser --- hypercorn: HTTPS
   hypercorn - systemd: run instance
   systemd <- systemd_conf: configure
   hypercorn -- gpms
   gpms - db

Alternative deployment model with load-balancing:

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
      database "JSON-based\nDatabase" as db
   }

   Browser --- balancer: HTTPS

   nginx <. nginx_conf: configure
   nginx "1" --- "1..*" Server

   hypercorn - systemd: run instance
   systemd <. systemd_conf: configure
   hypercorn -- gpms
   gpms "1..*" -- "1" db_server
