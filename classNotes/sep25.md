Sep 22 : Afternoon Notes

## Tips for writing high quality code

### Naming Things
- [Stroop Effect](https://en.wikipedia.org/wiki/Stroop_effect)
- You'll have a hard time ignoring names of variables
- Names should be descriptive (don't go with str1, str2, str3)
- Names should be self-explanatory
- Be consistent, same word mean same thing
- Avoid being abstract
- Avoid thesaurus
- Use intention revealing names
- Use pronounceable names
- Use searchable names (don't use single character names)
- Pick one word per concept and stick to it

### Writing funtions
- Functions should be small
    - function visible without pgup/pgdn
    - if function is visible at once it will make it easier to debug
    - human short term memory is limited - 7+-2 items
    - write functions less than 25 lines
- Function should do one thing
    - if function does more than one thing it will be hard to debug
    - if you need to use 'and' then function is doing multiple things
- No side effects
    - function should not change anything outside of itself
    - function should not change global variables
    - function should not change parameters
    - any assignment statement can result in side effects
- Command/Query Sepration
    - function should either do something or answer something
    - function should not do both
- Minimize number of arguments
    - 0 arguments is ideal
    - not more than 3 arguments
- Use constants for function arguments (C only)
- Don't repeat yourself
    - if you have same code in multiple places, you should write a function
    - don't copy and paste code
    - copy paste is a sign of bad design

### Minimize Mutability
- Minimize set/get 
    - set/get is a violation of encapsulation
    - excessive use of set/get results in code duplication
    - eliminate set
    - minimize get

### No global state
- Types
    - Global variables
    - Class static variables
    - Singletons (class with only one instance)
- Non-Locality
    - Uncertainty about change
    - Change at one place my affect seemingly unrelated code
- Implicit code
- Concurrency
    - Global variables are shared between threads
    - Global variables are shared between processes

### What are your assumptions?
- Document your assumptions
- Explicit and Implicit assumptions
- ``` char filename 256```
    - Explicit assumptions
        - length of filename will not exceed 256
    - Implicit assumption
        - file name can only be latin

