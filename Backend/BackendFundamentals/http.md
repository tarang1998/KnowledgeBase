# HTTP

- HTTP stands for Hyper Text Transfer Protocol.
- It is the foundation of data exchange on the web and it is a client-server protocol.It involves client making the request to the server, which then sends a response
- It is an application layer protocol.It is designed to be simple,human readable and is extensible (HTTP Headers introduced in HTTP/1.0 make this protocol easy to extend and experiment with) and has evolved over time
- HTTP is stateless (there is no link between two requests being successfully carried out on the same connection) but not sessionless (Using header extensibility HTTP cookies are added to the workflow that allow the use of stateful session.)
- HTTP does not require the underlying transport layer protocol to be connection based, it only requires it to be reliable. 
- HTTP relies on TCP which is reliable and connection based. 
- The default behaviour of HTTP/1.0 is to open separate TCP connection(which requires several round trips) for each HTTP request/response pair(which is less effecient than sharing a single TCP connection when multiple requests are sent in succession)
- HTTP/1.1 introduced pipelining and persistent connection : the underlying TCP connection can be partially controlled using the connection header.
- HTTP/2 went a step further by multiplexing messages over a single connection, helping keep the connection warm and more efficient

### What can be controlled by HTTP

- The common features controllable by HTTP:

    - Caching : The server can instruct proxies and clients about what to cache and for how long. The client can instruct intermediate cache proxies to ignore the stored documents.
    - Relaxing the origin constraint 
    - Authentication



### HTTP Request

- A HTTP request contains the following components : 

    - HTTP Version Type
    - A URL
    - HTTP Method
    - HTTP request headers
    - Optional HTTP Body


- #### HTTP Methods

    - Also sometimes also refered as HTTP Verb, it indicates the action that the HTTP request expects from the server.

- #### HTTP Request Headers

    - They contain information in key-value pair and are included in every HTTP request
    - Some of the key-value pairs are :
        - User Agent : It is the tool that acts on behalf of the user, primarily a web browser.


- #### HTTP Request Body

    - The body of the HTTP Request contains any information that being submitted to the web server, such as username and password.

### HTTP Response 

- A HTTP Response contains the following information

    - A HTTP Status Code
    - HTTP Response Header
    - Optional HTTP Body

- #### HTTP Status Codes

    - HTTP Status codes are 3 digit codes broken into 5 groups 
        - 1xx Information
        - 2xx Success 
        - 3xx Redirection
        - 4xx Client Error
        - 5xx Server Error

    - 'xx' refers to number between 0-99

- #### HTTP Response Headers

    - Conveys important information like the language and the format of the data being sent in the response body.
 
- #### HTTP Response Body

    - Successful HTTP responses to GET requests generally have a body, which contains the requested information.


## Articles

- [What is HTTP](https://www.cloudflare.com/en-gb/learning/ddos/glossary/hypertext-transfer-protocol-http/)
- [An overview of HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)
- [Journey to HTTP/2](https://kamranahmed.info/blog/2016/08/13/http-in-depth)