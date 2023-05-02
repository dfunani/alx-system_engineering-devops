# Pre-Amble

## Server

Software hosted (Running) on a network device, allowing that device to provide resources and program functionalities requested by a client. Depending on the network the server is hosted on, public (internet facing) or private (only accessible by authorized network members), will determine how and what server clients can access the network. Server clients are software installed on a network device/host allowing a user to make requests to the server. Giving rise to the Server/Client relationship.

## Domain Names

Human friendly name assigned to a network device corresponding to the logical address of the device (IP Address). Instead of requesting a service from a server at 159.159.179.159, you can use the server's domain name www.*.com

## DNS Server

Server providing usually hosted on a network device such as a router, to provides a mapping of Domain Names to IP addresses. When the request to www.foobar.com is made, the DNS server is requested to provide the IP of the requested domain name. IP packet (request) sent to the www.foobar.com Web Server will contain 8.8.8.8 and not www.foobar.com.

## Web Servers

A type of server that provides functionality and resources to web clients (requestor) using HTTP or HTTPS if the requests and responses are encrypted while in transit. Web servers provide resources using TCP port 80 for HTTP and 443 for HTTPS. Request to web servers are done using a web client eg Google Chrome.

## Application Server

A type of server that provides the resources and functionalities required to use an application appropriately. Application servers are run on TCP ports beyond 1024. Requests to application servers are made by using the application client.

## Database

A software or application hosted on a network device that stores and manages data of known data types. This can be a relational (Structured) or non-relational (Unstructured) Database. Management includes inserting, deleting, updating and querying/selecting data from the database.

## IP/TCP Model

When considering "What is the server using to communicate with the computer of the user requesting the website", we reference:

1. IPv4: Logical Addresses assigned to the server and client (user) to allow packets to be routed through the internet from source to destination.
2. TCP: Guarantees the delivery of the Requests and Responses (IP Packet), by managing the segments of the IP Packet and managing sockets (connections between the server and client) by categorizing IP Packets into service ports, eg port 80 for HTTP web servers.
3. HTTP/HTTPS (Secured/Encrypted): Application level communication standards defining the structure of requests and responses over the internet port 80 or 443 for HTTPS. Encryption refers to securing the IP Packet such that interpreting the IP Packet cannot be done without the Public and Private Key.

## Web Client/Server Explained

A web client-server relationship describes how web clients google chrome make requests and how servers respond to the requests . The client is software installed on a host or device that exists on a users network, allowing the user to make a request to access the webpage such as www.foobar.com. However the requests, also known as IP Packets, are structured:

![Ethernet Frame](https://i.imgur.com/XELubVG.png "Ethernet Frame")

With the structure above in mind, making a request to "www.foobar.com" would result in an ethernet frame containing "www.foobar.com" as the destination for the IP Packet, which would be invalid. To correct this, when the request is made to www.foobar.com, a request is then sent to the DNS server.

A DNS server is a type of server hosted on a network device, usually the Local area network's router. The DNS server will resolve the clients request for the IP address of the requested domain name, foobar.com, by return the IP address 8.8.8.8.

The DNS provided IP address is then used in the ethernet frame, along with the tcp port for the desired HTTP service. Commonly used TCP ports and services hosted on those ports:

* 20 and 21 - FTP Server
* 22 - SSH Server
* 25 - SMTP Server
* 80 - HTTP Server
* 443 - HTTPS Server
* 110 - iPOP3 Server
* 143  - iMAP4 Server

The updated Etherenet Frame:

In most cases, the user client is on a private network, called a local area network (a connection of host network interface cards, where all member hosts share a subnet such as 255.255.255.0). When a client makes a request, depending on whether the request is to a host on the same network or an external network.

### Internal Request

The request is to a host on the same network, the ethernet frame (request) is sent directly to the host device using the hosts MAC Address (Physical address). The requesting host obtains the MAC addresses of hosts on the local network, by using the ARP (Address Resolution Protocol) Table, which is an IP/Mac Address translation table maintained in the requesting hosts. ARP tables are populated dynamically through the ARP broadcast protocol. ARP uses the IP address to identify the MAC address that is requested.

Therefore if the web server is hosted on the local network too, then requests from the local client will be sent directly to the web server:

![Ethernet Frame](https://i.imgur.com/86rVZX7.png "Ethernet Frame")

The request is to a host, that is not on the same network as the client, then the request must be routed to the correct network. The destination network may be on the internet (public network) or a intranet (private network). Only difference is when a request is to over the internet, therefore the destination is a public network, the source IP must be a public IP address.

# External Network

Under normal circumstances, the user client is hosted in a private network run by an ISP. The ISP provides a router, which will serve as the network's default gateway in and out of the local network. This means that each member host of a private network, is assigned a private IP, using the Routers DHCP server. DHCP is a software service that provides IP address to hosts on the network. Private IPv4 addresses take the following form:

1. 10.0.0.0 - 10.255.255.255
2. 172.16.0.0 - 172.31.255.255
3. 192.168.0.0 - 192.168.255.255

All other IPv4 forms are considered Public excluding:

1. 168.254.0.0 - 168.254.255.255 Linked IPv4 (Back Up if DHCP fails)
2. 240.0.0.0 - 254.255.255.255

## Intranet

If a request is sent from the client, on a particular network, to a server on another private network that is connected to the client network, also known as the INTRANET. With intranet communication, both the Source and Destination IPs will be private. However, because they're on separate but connected networks, they cannot communicate directly with each other, as is the case with internal network communications. This gives rise to the main role of a router, provide a default gateway for local hosts to communicate with hosts on other networks on a particular INTRANET. Therefore the Ethernet Frame for an IP packet bound for a destination outside the LAN, will behave differently:

![Ethernet Frame](https://i.imgur.com/ZT3KYpu.png "Ethernet Frame")

The Ethernet Frame will be routed to the LAN's router by way of the default gateway IP address. The only difference from Internal Requests, is that the destination MAC Address is changed to the Mac Address of the Default Gateway. The router will then read the IPv4 data, destination IP, and route the IPv4 Packet towards the destination network, using a Routing Table.

## Internet

If a request is sent from the client, on a particular network (192.168.5.5), to a server on a public network (8.8.8.8) that is connected to the client network, by way of an internet gateway. With internet communication, both the Source and Destination IPs must be private. Using the internet connection, all hosts in public facing network can then communicate with other hosts on another public facing network. With public or internet communication, the router provides the client a public IP, using a Network Address Translation (NAT) table, which maps the private IPs on the network to a public IP for communications with public networks on the internet. Therefore the Ethernet Frame for an IP packet bound for a destination outside the LAN, will behave differently:

![Ethernet Frame](https://i.imgur.com/BKuCW5g.png "Ethernet Frame")

The Etherenet Frame will be routed to the LAN's router by way of the default gateway IP address. The destination MAC Address is changed to the Mac Address of the Default Gateway Router. The Router using the NAT Table, will update the Source IP to a public IP. The router will then read the IPv4 data, destination IP, and route the IPv4 Packet towards the destination network, using a Routing Table. With an internet communication, the IP Packet is routed through the ISP's network of routers to the destination network on the internet.

# Simple Web Stack Infrastructure

In this client server relationship, a client (192.168.5.5) makes a request for a webpage www.foobar.com, using a web browser. A DNS server provides the Client with an IPv4 address, which allows the client to generate an Ethernet Frame/IP Packet. The frame is routed through the network of routers to the destination network (8.8.8.8) using the IPv4, TCP and HTTP/s protocols.

The frame is successfully delivered to destination network 8.8.8.8, which will be a network or host device running the relevant software to run as a respective server example (Web Servers). Since many services can be run on one host device, each service gets designated a TCP port such as 80 for Web Servers. The router connected to the network 8.8.8.8, will evaluate the IP Packet and identity the TCP port of the request and will route the IP packet to the relevant service port. The server will then respond with the requested web pages, renderable on the web client.

A load balance is added between the Network Access Point and the Gateway Router. The Load Balancer then routes IP Packets to either server network. This involves having an instances of the Web and Applications Server running on multiple networks with a Load Balancer routing to which ever server is least busy. The Load Balancer is then responsible for routing to and from the various instances of the web server available.

The server is set up using NGINX cloud server, which assists in delivering the web pages stored or provided by the application server, to the requesting client.
The application server, also known as the controller in the MVC model, provides the functionalities that generate the web pages to be delivered. We have made use of Linux Apache server running PHP code-base
The code-base which is the Application's code, which in this case will be PHP code. This is maintained in a GIT repository or a MySQL database in this case.
The database is a MySQL DB, and is used as the primary storage for the application server and the supporting components.

# Issues

Security - Server is hosted on port 80 as an HTTP server, so the IP Packets transmitted are unencrypted and vulnerable to interception. No Firewalls to control access to the server.
Monitoring - Server has no services set up to monitor IP packets in and out of the server.
Scalability - If more storage or more instances of the application or web server are required, there is no easy way of increasing capacity. More databases cannot be connected without adversely affecting the existing server.
Separation of concerns - Anyone with access to the network can access every component of the web server, eg can access the database or the code-base. Its better suited to have a network appropriately separated to ensure access to the web server is limited to only accessing the required services and nothing more.
