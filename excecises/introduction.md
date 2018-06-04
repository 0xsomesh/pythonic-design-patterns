# Introduction

**1. What is Design Pattern?**  
Design patterns are description of communicating objects and classes that are customized to solve a general design problem in a particlar context. They are used to create resuable object oriented design of softwares.

**2. List down four essential elements of patterns**  
Four elements of a pattern are:
 * Pattern Name (Name of design pattern)
 * Problem (architectural problem, the pattern will solve)
 * Solution (the way, pattern will solve the problem)
 * Consequences (trade-offs, pros, cons, alternatives etc)

**3. What is MVC architecture?**  
MVC is acronymn for Model View Controllers architecture. MVC architecture abstracts the Model (Application Object), Controllers(The business logic) and Views (the client side representation of data). MVC architecture allows multiple views for a single model while using controllers to control display of data according to business logic. Variuos frameworks such as Django, Flask follow MVC architecture.

**4. What are all the criterias used to classify a design pattern?**  
Design Patterns can be classified by two criterias:
 * Purpose : What a pattern does? (creational, structural and behavioural)
 * Scope : Where does pattern apply? (Classes and Objects)

**5. Name three classification of design patterns based on purpose of the desing pattern**  
 * Creational : Defines object creation
 * Structural : Defines the composition of objects and Classes
 * behavioural : Defines the interation of objects and classes

**6. Name two classification of design patterns based on scope of the design pattern.**  
 * Class Patterns : Patterns which are applied to classes
 * Object Patterns : Patterns which are applied to objects

**7. Write notes on Objects, Method and Requests.**
 * Object : Object can be defined as the model instantiated by the class with a state and methods associated with it to make some changes in the state.
 * Methods : Methods are the functions defined in a class to perform changes in the objects of that class.
 * Requests : Requests are the call to these methods by the client.

**8. What is encapsulation?**  
Encapsulation in simple terms is data hiding. We restrict the drirect access of variables from objects via implemeting Variuos methods in a class to get, set, update the state variables also known as attributes.

**9. What is Facade and Flyweight pattern?**  
 * Facade pattern : Facade pattern is a common interface to variuos interfaces. It can be visualzed as a juntion.
 * Flyweight pattern : Flyweight pattern use sharing to support a large number of objects efficiently.

**10. Write notes on Opertaion's signature in an Object**  
Opertaion's signature is the name of Opertaion, parameters it takes and the return type. Every operation performed on an object has its own signature.

**11. Write notes on interfaces in Object oriented systems.**  
Interface of an object is the set of all operation signatures of that object.

**12. What is dynamic binding of an object?**  
When a request is made by the client, it depends on the operation as well as on the object, recieving the request, what will the response be. Run-time binding of requests and objects or opertaion of those objects is called dynamic binding.

**13. Write notes on Abstract Class.**  
Abstract class is defined as the class with no implementation of operations. It is basically a interface template to its sub-classes. Its sub-classes implements the opertaions defined in the abstract class to maintain the same interface.

**14. Define Concrete class**  
Concrete class is a class which has its implemetion of operation defined in itself. In simple terms a class which is not an  abstract class is concrete  class.


**15. Define mixin class.**  
Mixin classes use multiple inheritance to provide some functionality or additional operation signature to the exsisting class.

**16. Name two techniques for reusing functionaliy in Object oriented systems.**  
 * White-Box reuse
 * Black-Box reuse

**17. Define White-Box reuse.**  
White-Box reuse can be defined as using inheritance to reuse the methods imlemented in another class. This is reuse by sub-classing.

**18. Define Black-Box reuse.**  
Black-Box reuse can be defined as using operations of other classes to reuse the implementation. In this method we call explicitly to another object's opertaion from within our object. This is done by object composition which needs to have well defined interfaces between objects.

**19. What are the dis-advantages of class inheritance?**  
 * Since inheritance is defined in complie time we can not change the implementations on the run-time.
 * It breaks encapsulation as the implementations in parent class are exposed to sub-class.
 * Any changes in parent class forces sub-class to change accordingly.

**20. What is delegation?**  
Delegation is basically passing on the request to another object at the run-time. In delegation two objects are involved, one recieving object and one delegate object to which request is delegated. It makes composition powerful for reuse.

**21. What are the main advantages of delegation?**  
Its really easy to compose behaviours at the run-time.

**22. What are all the disadvantages of delegation?**  
Delegation comes with run-time inefficiencies as it involves dynamic binding. Dynamic, more parameterized software is harder to understand too than a static counter-part.

**23. Write notes on aquaintance relationship of an object.**  
Aquaintance relationship can be defined as the 'knows - of' relationship between objects. It is a looser coupling than aggregation. Aquaintanted objects call each other operations but are not dependent.
