
# Domain Driven Development
#### Fastapi with Domain Driver Development approach boilerplate


### Introduction to DDD

Domain-Driven Development (DDD) is a software design methodology that emphasizes the importance of modelling complex systems based on the underlying business domain. A key aspect of DDD is its alignment with Clean Architecture principles, which advocate for a separation of concerns and a clear structure that enhances maintainability and testability. Clean Architecture organizes the code into layers, typically including the presentation layer, application layer, domain layer, and infrastructure layer. This layered approach allows developers to isolate business logic from external concerns, such as user interfaces and data storage, making it easier to adapt to changes in technology or business requirements without affecting the core domain logic.

In DDD, external services are integrated through the use of domain repositories and adapters, which play a crucial role in maintaining modularity and flexibility. Repositories serve as an abstraction layer that encapsulates the logic required to access data sources, whether they are databases, external APIs, or other services. For instance, a `ItemRepository` might handle interactions with a database to store and retrieve document entities, while an `SQLStorageAdapter` could manage communication with the SQL Database, be it a remote service or local implementation. By using repositories, the domain layer remains agnostic of the underlying data sources, allowing developers to change or replace these services without impacting the core business logic.

Adapters complement repositories by providing a way to interact with external services in a manner that aligns with the domain model. They translate data and operations between the domain and the external service, ensuring that the domain logic can remain focused on business rules rather than technical details. This modular approach not only enhances the maintainability of the codebase but also facilitates testing, as developers can easily mock or stub external services during unit tests. By adhering to DDD principles and utilizing Clean Architecture, teams can create a robust and scalable software solution that is well-structured, easy to understand, and adaptable to future changes in both the business domain and technology landscape.



### Clean Architecture

Clean Architecture is a software design philosophy that emphasizes the separation of concerns and the organization of code into distinct layers, each with its own responsibilities. The primary goal of Clean Architecture is to create systems that are easy to understand, maintain, and adapt over time. At its core, Clean Architecture advocates for a structure where the business logic is isolated from external concerns, such as user interfaces, databases, and third-party services. This separation allows developers to focus on the core functionality of the application without being tightly coupled to specific technologies or frameworks, promoting a more flexible and resilient design.

The architecture is typically organized into concentric circles, with the innermost circle representing the core domain logic, followed by layers for application services, interfaces, and infrastructure. The innermost layer contains the entities and business rules, while the outer layers handle interactions with external systems and user interfaces. This layered approach ensures that dependencies flow inward, meaning that outer layers can depend on inner layers, but not vice versa. As a result, changes in the outer layers—such as switching to a new database or modifying the user interface—do not impact the core business logic. This design principle enhances the system's adaptability and makes it easier to implement changes without introducing unintended side effects.

The benefits of Clean Architecture are numerous. First, it promotes maintainability by allowing developers to work on different layers independently, reducing the risk of introducing bugs when making changes. Second, it enhances testability, as the core business logic can be tested in isolation from external dependencies, enabling more effective unit testing. Third, Clean Architecture supports scalability, as new features can be added with minimal disruption to existing code. Finally, by adhering to the principles of Clean Architecture, teams can create software that is not only robust and flexible but also easier to understand and communicate about, fostering better collaboration among developers and stakeholders alike.


### Repositories and adapters

Repositories and adapters are essential components in modern software architecture, particularly within the context of Domain-Driven Development (DDD) and Clean Architecture. Repositories serve as an abstraction layer that encapsulates the logic required to access and manipulate data from various sources, such as databases, external APIs, or file systems. By providing a consistent interface for data operations, repositories allow developers to interact with the underlying data storage without needing to understand the specifics of how that data is stored or retrieved. This abstraction not only simplifies the codebase but also promotes a clear separation of concerns, enabling the domain logic to remain focused on business rules rather than technical details.

Adapters complement repositories by acting as intermediaries that facilitate communication between the application and external services. They translate data formats and operations between the domain model and the external systems, ensuring that the application can interact with these services in a way that aligns with its internal logic. For example, an adapter might handle the conversion of data from a third-party API into a format that the domain model can understand, or vice versa. This modular approach allows for greater flexibility, as developers can easily swap out or modify adapters without affecting the core business logic. As a result, the application can evolve and integrate new technologies or services with minimal disruption.

The use of repositories and adapters brings several significant benefits, including enhanced modularity and testability. Modularity is achieved by isolating data access and external service interactions from the core business logic, allowing teams to work on different components independently. This separation makes it easier to manage and maintain the codebase, as changes to one part of the system do not ripple through the entire application. Additionally, the abstraction provided by repositories and adapters facilitates testability, as developers can easily mock or stub these components during unit testing. This means that the core business logic can be tested in isolation, ensuring that it behaves as expected without relying on external systems. Overall, the use of repositories and adapters contributes to a more organized, maintainable, and testable codebase, ultimately leading to higher-quality software.

### Services

The Services module is a crucial component of the application architecture, encapsulating the business logic and use cases that drive the functionality of the system. This module acts as an intermediary between the domain layer and the external components, ensuring that the core business rules are applied consistently across various use cases. By centralizing the business logic within the Services module, developers can maintain a clear separation from the adapters and specific implementations of remote services. This design allows for greater flexibility, as changes to the underlying technology or external services do not necessitate modifications to the business logic itself.

Furthermore, the Services module promotes reusability and maintainability by providing a structured approach to implementing use cases. Each service can be designed to handle specific business operations, making it easier to understand and manage the application’s behavior. This modularity also facilitates testing, as services can be independently tested in isolation from the adapters and external dependencies. By adhering to this approach, teams can ensure that the application remains robust and adaptable, capable of evolving alongside changing business requirements and technological advancements.


### Benefits

Key Points on Domain-Driven Development (DDD), Clean Architecture, Repositories, and Adapters

* **Domain-Driven Development (DDD)**:
  * Focuses on modelling complex systems based on the underlying business domain.
  * Encourages collaboration between domain experts and developers to create a shared understanding.
  * Utilizes a "Ubiquitous Language" to ensure clear communication among stakeholders.
  * Introduces "Bounded Contexts" to define boundaries for different models within the system.


* **Clean Architecture**:
  * Emphasizes separation of concerns by organizing code into distinct layers (e.g., domain, application, interface, infrastructure).
  * Ensures that dependencies flow inward, allowing outer layers to depend on inner layers but not vice versa.
  * Promotes maintainability, testability, and scalability by isolating business logic from external concerns.
  * Facilitates easier adaptation to changes in technology or business requirements.
    

* **Repositories**:
  * Serve as an abstraction layer for data access, encapsulating logic for interacting with various data sources.
  * Provide a consistent interface for data operations, simplifying the codebase and promoting separation of concerns.
  * Allow the domain logic to remain focused on business rules without being coupled to specific data storage technologies.


* **Adapters**:
  * Act as intermediaries that facilitate communication between the application and external services.
  * Translate data formats and operations between the domain model and external systems.
  * Enable flexibility by allowing easy swapping or modification of external service interactions without affecting core logic.


* **Benefits of Using Repositories and Adapters**:
  * Modularity: Isolates data access and external service interactions from core business logic, allowing independent development and maintenance.
  * Testability: Facilitates easier unit testing by enabling developers to mock or stub repositories and adapters, allowing core logic to be tested in isolation.
  * Maintainability: Changes to one component do not ripple through the entire application, leading to a more organized and manageable codebase.
  * Flexibility: Supports the integration of new technologies or services with minimal disruption to existing functionality.


## Try it out

Get poetry at https://python-poetry.org

> poetry install

> poetry shell
 
> uvicorn fast_ddd.main:app

Open browser and visit at http://localhost:8000/docs
