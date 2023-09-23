Sep 22 : Afternoon Notes

### Software Design

#### High Level design
- User interfaces
- Use case scenario
- Deployment View
- Module breakup
- High level sequence diagram

#### Low Level design
- Class diagram
- ER Diagram
- Detailed sequence diagram
- Flowchart

### Where to start?
- Start with deployment view
- What is user interface
- Decide which frameworks and libraries to use
- Decide on third party services
- Cheeck type of application
- Can I break it into modules?
- What are common scenarios?
- Error handling strategy

### How is application deployed?

#### Single Process
- **Class Diagram**

#### Multi Process
- How will I communicate between processes?
- What data will be transferred across process?
- **Data Flow Diagram**

## Single process application
(just repeat process for multi process application)

### Break into modules
- Can I break it into modules?
    - "Component View"
    - "Layer View"
    - Keep dependencies uni-directional
    - Avoid circular dependencies
- What is responsibility of each module?
- Can I identify important classes in the module?
    - "Class Diagram"

### Common Scenarios
- What are common scenarios?
- Can currently identified classes handle these scenarios?
    - "Sequence Diagram"
    - "Interaction Diagram"
- if not, what's missing?

### Error Handling
- What are possible errors?
- How will I handle them?
    - APM (Application Program Monitoring)
- How will they get displayed to user?
- If there a common error handling strategy?

> Book: Beautiful Programming

> Django is a great way to learn python

## Different diagrams

### Data Flow Diagram
- Focus on how data moves between the system
- (in OO focus is on 'actions' not data)
- Starting with DFD is 'procedural design'

### Class Diagarm
- Class is static picture of how classes are related to each other
- Class diagram does not give idea about
    - When class constructed
    - How many instances
    - When class removed
- Need to be paired with a interaction diagram

### Sequence Diagram
- What will happen at what point of time?
- (Maybe use swimlane diagram)

## Key design principles

### The Principles
- Acyclic Dependency
- TELL, don't ASK
- Manage Lifetime of Objects

### Acyclic Dependency
- Dependencies must not create cycles
- There should be no path which includes the same package more than once
- **BREAK THE CYCLE**
    - Abstract interfaces
    - Splitting packages
    - Reorganize Packages

### TELL, don't ASK
- Tell lift I want to go down, don't ask lift to come up
- Procedural gets info and makes decision
- OO tells object to do something
- Encaspulation is not about hiding data, it's about hiding behaviour
> Research Paper: On the criteria of decomposing the system
- Bad example:
    ```
    w = rect.width
    h = rect.height
    area = w * h
    ```
- Good example:
    ``` 
    area = rect.area()
    ```
- Minimize use of set and get methods

### Manage Lifetime of Objects
- Anything your program *acquires* for the time being and *release* when done is a resource
- Resources are limited
- To Decide
    - How will you acquire the resource?
    - How will you release the resource?
    - Who owns the resource?

#### Objects
- Not created by thin air
- Need a constructor
- Not destroyed automatically
- Need a destructor

#### Resource leak
- Resource leak is a coding error in which a resource is acquired but forgot to release
- Resource leak is usually a design level problem
- Don’t acquire a resource and keep it indefinitely
- Decide which object owns or manage lifetime of resources


#### Memory Leak
- Increase memory requirement
- Impacts performance
