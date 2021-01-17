System Architecture
===================

All the data and business logic handling is done on the server side in order
to reduce workload for clients.

Since client only renders UI from HTML sent from server and send requests
to the server, its internal details are not discussed in this section.

:numref:`arch` describes the architecture for our system.
When a user access the site, a HTTPS request is sent to the server.
The ASGI web server Hypercorn will take this request.
Acanban module will process the request and make query to RethinkDB or IPFS
if needed and respond to the client.


.. uml::
   :caption: Server-Client architecture
   :name: arch

   left to right direction

   node Client {
      node Browser
   }

   node Server {
      database "RethinkDB" as db
      component Acanban
      component Hypercorn
      component IPFS
   }

   Browser --- Hypercorn: HTTPS
   Hypercorn -- Acanban
   IPFS - Acanban
   Acanban - db

Alternatively, a load balancer such as nginx can be added to distribute
the requests to multiple server as is shown in :numref:`arch-alt`.
Multiple instances of acanban are run to process incoming requests.
They can write concurrently to a shared database.


.. uml::
   :caption: Alternative architecture with load balancer
   :name: arch-alt


   node Client {
      node Browser
   }

   node "Load Balancing Server" {
      component NGINX as nginx <<load balancer>>
   }

   rectangle "Load Balancing Cluster" as balance_cluster {
      node "Web Server" as server_1 {
         component Acanban as acanban_1
         component Hypercorn as hypercorn_1
      }

      node "Web Server" as server_2 {
         component Acanban as acanban_2
         component Hypercorn as hypercorn_2
      }

      node "Web Server" as server_3 {
         component Acanban as acanban_3
         component Hypercorn as hypercorn_3
      }
   }

   rectangle "Database Cluster" as db_cluster {

      node "Database Server" as db_1 {
         database "RethinkDB" as r_1
         component "IPFS" as ipfs_1
      }

      node "Database Server" as db_2 {
         database "RethinkDB" as r_2
         component "IPFS" as ifps_2
      }

      node "Database Server" as db_3 {
         database "RethinkDB" as r_3
         component "IPFS" as ipfs_3
      }
   }

   Browser --- nginx: HTTPS

   nginx  --- hypercorn_1
   nginx  --- hypercorn_2
   nginx  --- hypercorn_3

   hypercorn_1 - acanban_1
   hypercorn_2 - acanban_2
   hypercorn_3 - acanban_3
   acanban_1  --- db_1
   acanban_1  --- db_2
   acanban_2  --- db_2
   acanban_2  --- db_3
   acanban_2  --- db_1
   acanban_3  --- db_1
   acanban_3  --- db_3

However, we do not implement this architecture within the scope of this project,
due to following reasons:

- We do not have several servers to implement.
- For intended use, the expected requests can go up to as many as 1000.
  Load balancing for such few requests is overhead.
