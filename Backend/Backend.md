# Backend

## Monolith Architecture and MicroService Architecture Pattern

### Articles 

- [Monolith Architecture](https://microservices.io/patterns/monolithic.html)
- [Microservice Architecture](https://microservices.io/patterns/microservices.html)
- [Introduction to Monolithic Architecture and MicroServices Architecture](https://medium.com/koderlabs/introduction-to-monolithic-architecture-and-microservices-architecture-b211a5955c63)

- [Writing Microservices with google cloud functions](https://medium.com/billie-finanzratgeber/w riting-microservices-with-google-cloud-functions-231205d1a94)
- [Serverless vs Microservices — Which Architecture to Choose](https://www.techmagic.co/blog/serverless-vs-microservices-which-architecture-to-choose/)
- [Difference between Microservices and serverless](https://www.geeksforgeeks.org/difference-between-microservices-and-serverless/)

### Videos

- [What is a microservice architecture and it's advantages?](https://www.youtube.com/watch?v=qYhRvH9tJKw)

    - Disadvantages of a monolith architecture 
        - A new member in the team needs to have more context of the entire system as the system is tightly coupled
        - Deployments are complicated
        - Testing the application is tougher
        - Single Point Of Failure

    - Advantages of a microservice architecture
        - Parallel development is easy as services are loosely coupled

- [Microservices interview questions and answers](https://www.youtube.com/watch?v=G0waumbpK48)
- [Microservice vs serverless](https://www.youtube.com/watch?v=xQtyEK5yZFQ)

## HTTP

- [What is HTTP](https://www.cloudflare.com/en-gb/learning/ddos/glossary/hypertext-transfer-protocol-http/)
- [An overview of HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)
- [Journey to HTTP/2](https://kamranahmed.info/blog/2016/08/13/http-in-depth)

## APIs

### API Interceptor

- Interceptor is an API gateway server built for accepting API requests from the client applications and routing them to the appropriate backend services. May it be a single service or multiple services to be called in a single API call, interceptor provides you with the necessary tools to control your API request flow.

### Middleware 

- Middleware is a generic term for any software that fits in between two parts of any software process. So, let's say you have some API on the server. Server (this is in the back end, obviously) receives a request, server processes request, server returns some status. Let's say that you want to set up a filter in between the server receiving the request and processing it, maybe checking whether the user is authenticated and rejecting the request with a 401 if not. 
- Your server software should enable you to use some sort of middleware between receiving the request and your back-end logic. You probably didn't write your own server, right? You're probably using some third-party tool to handle incoming requests and route them to the code you wrote to process them. So if you want it to do something special in the middle of that process, you can't just go in there and change it yourself. Luckily, if that server is well-designed, it will give you the option to pass in some function to call in the middle of that process, and that function is called middleware.

- [Frontend - Middleware - Backend](https://www.reddit.com/r/learnwebdev/comments/lwq2go/confused_about_middleware_backend_fullstack/)

## Controller

### Videos

- [What is an API and how do you design it?](https://www.youtube.com/watch?v=_YlYuNMTCc8)
    - An API shouldnt have any side effects 
        - It should do exactly the task the API name stands for and nothing else
        - The API should be atomic
    - API response
        - Pagination
        - Fragmentation

## Languages 

- Fact : Whatsapp needs only 50 engineers for its 900M users because Erlang is used to implement its concurrency needs. Facebook uses Haskell in its anti-spam system.

- [TypeScript](/Backend/Languages/typeScript.md)
- [JavaScript](/Backend/Languages/javascript.md)
- [Erlang]()
- [Ruby]()
- [Go]()
- [Python]()


## Distributed Systems

- [Distributed Systems](https://www.youtube.com/watch?v=cQP8WApzIQQ&list=PLrw6a1wE39_tb2fErI4-WkMbsvGQk9_UB)


## Projects     


- [Learning Microservices With Express.js & MongoDB](https://www.youtube.com/watch?v=gF8IYisXByw&list=PLDmvslp_VR0xZGhJHMjy5dozCDJYZK6W-)
- [Node JS Microservices Course](https://www.youtube.com/watch?v=UxoklNY7L30&list=PLIGDNOJWiL182j1bD_nQm-SxARR5s977O&index=1)
- [NodeJS Monolithic to Microservice](https://www.youtube.com/watch?v=EXDkgjU8DDU)

## RoadMaps

- [Backend Developer RoadMap](https://roadmap.sh/backend)