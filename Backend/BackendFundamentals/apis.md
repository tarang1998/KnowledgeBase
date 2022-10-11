# APIs

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