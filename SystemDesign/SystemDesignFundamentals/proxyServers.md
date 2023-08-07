
# Proxy Servers

- Proxy server refers to a server that acts as an intermediary between the request made by clients, and a particular server for some services or requests for some resources.
- The basic purpose of Proxy servers is to protect the direct connection of Internet clients and internet resources. 
 
- Types of Proxy Servers:
    - Forward Proxy (Client facing proxy)
        - The server doesnt know about the client which has made the request
        - Benifits:
            - Used for anonymity. Disguises the client's IP address - (Improved Privacy)
            - Used to block malicious traffic from reaching an original web server - (Improved Security ).
            - Used to block access to certain sites (Control of the internet usage of employees and children).
            - To cache the responses from the server
            - Accessing geo-location Restricted Content

    - Reverse Proxy
        - A server side proxy
        - Benifits:
            - Can be used for traffic control, load balancing, logging
            - Caching responses
            - Mitigate DDOS attacks
            - Canary Deployment(The practice of making staged releases)
        - It could be a single point of failure
    
### Resources 

- [What is Proxy Server?](https://www.geeksforgeeks.org/what-is-proxy-server/)
- [What is a Proxy Server? - 2 ](https://www.educative.io/answers/what-is-a-proxy-server)
- [Proxies | System Design Tutorials](https://www.youtube.com/watch?v=Nu-4Q3OoR4E)