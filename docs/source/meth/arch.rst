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


.. uml:: arch-alt.puml
   :caption: Alternative architecture with load balancer
   :name: arch-alt

However, we do not implement this architecture within the scope of this project,
due to following reasons:

- We do not have several servers to implement.
- For intended use, the expected requests can go up to as many as 1000.
  Load balancing for such few requests is overhead.
