# API Design
- API Paradigms 
    - REST (Representational State Transfer)
        - It's a software architectural style that describes how an API should function.
        - REST APIs use HTTP requests to access and modify data. They use GET, PUT, POST, and DELETE operations to read, update, create, and delete data 
        - REST APIs are often used with JSON for request payloads and responses 
        - Stateless : No client information is stored between get requests and each request is separate and unconnected.
        - One of the most common problems with REST is that of over and underfetching. This happens because the only way for a client to download data is by hitting endpoints that return fixed data structures.
    - GraphQL 
        - GraphQL enables declarative data fetching where a client can specify exactly what data it needs from an API. Instead of multiple endpoints that return fixed data structures, a GraphQL server only exposes a single endpoint and responds with precisely the data a client asked for. It avoids the problem of over and under fetching
        - GraphQL uses a strong type system to define the capabilities of an API. All the types that are exposed in an API are written down in a schema using the GraphQL Schema Definition Language (SDL). This schema serves as the contract between the client and the server to define how a client can access the data.
        - Queries can impact server performance
        - Only POST request 
    - gRPC 
        - gRPC is an open-source API architecture based on the Remote Procedure Call (RPC) model.
        - gRPC offers bidirectional streaming communication. This means both the client and the server can send and receive multiple requests and responses simultaneously on a single connection.



- Backward Compatability and Versioning 
    - New Changes in the API should not break the existing functioning of the system
    - Examples for maintaining backward compatibility and versioning 
        - REST 
            - POST : /api/v2/products (Current clients)
            - POST : /api/v1/products (Old clients)
        - GraphQL 
            - products_v2
            - products

- Best Practices 
    - Rate Limiter
    - CORS 



## Resources 

- [How to GraphQL](https://www.howtographql.com/basics/0-introduction/)
