# Object Oriented Programming 

- OOPs Concepts:
    - Encapsulation
    - Abstraction
    - Polymorphism
    - Inheritance

- Encapsulation:
    - Encapsulation is a mechanism of wrapping the data (instance variables) and code acting on the data (methods) together as a single unit like a Class.
    - In encapsulation, the variables of a class can be made hidden from other classes, and can be accessed only through the methods of their current class. Therefore, it is also known as data hiding.
    - It can be described as a protective barrier that prevents the code and data being randomly accessed by other code defined outside the class. Access to the data and code is tightly controlled by a class.
    - Encapsulation leads to data hiding.
    - We use access specifiers to hide the data(properties) and methods. Use of private and public comes under this.

- Abstraction:
    - Abstraction is a process of hiding the implementation details from the user, only the functionality will be provided to the user.
    - In other words, the user will have the information on what the object does instead of how it does it.

- Polymorphism 
    - Polymorphism allows us to have perform a single action in different ways (It allows you to define one interface and have multiple implementations)
    - In java Polymorphism is divided into 2 types:
        - Compile Time Polymorphism:
            - It is also known as static Polymorphism or early binding 
            - The object is bound with its functionality at compile time, java knows which method to call by checking the method signatures
            - It can be achieved by function overloading(When functions have the same name but different no. or type of argument) or operator overloading
        - Run Time Polymorphism:
            - It is also known as Dynamic Method Dispatch or late binding 
            - Object is bound with its functionality at runtime
            - It is a process in which a function call to the overridden method is resolved at runtime
            - This time of polymorphism is achieved by method overiding(When the derived class has a definition for one of the member functions of the base class)
    - **Resources**
        - [Polymorhism in Java](https://www.geeksforgeeks.org/polymorphism-in-java/)
        - [Difference between Compile-Time and Run Time Polymorphism](https://www.geeksforgeeks.org/difference-between-compile-time-and-run-time-polymorphism-in-java/)

## Resources
    
- [OOP: Everything you need to know about Object Oriented Programming](https://medium.com/from-the-scratch/oop-everything-you-need-to-know-about-object-oriented-programming-aee3c18e281b)
- [Real-world examples of OOP concepts](https://medium.com/@punitkmr/real-world-examples-for-oop-concepts-abb9475b2095)