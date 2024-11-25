# C++ Theory

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Sources](#sources)
- [Questions](#questions)
  - [Data Structures](#data-structures)
  - [Memory](#memory)
  - [Threads](#threads)
  - [Other](#other)
  - [OO](#oo)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Sources

* Effective C++, Scott Meyers
* Quant Job Interview Questions & Answers, Mark Joshi

## Questions

### Data Structures

* compare STL's `map` and `unordered_map`

|what|`map`|`unordered_map`|
|----|-----|---------------|
|keys|ordered|unordered|
|implementation|BST (red-black tree)|array + linked lists|
|insert/lookup|amortized O(log n)|O(1), can degrade to O(n)|
|hashing|no|yes|
|collisions|no|yes|
|insert/delete||cheaper|
|preferred keys|anything works as a key if can compare|use primitive data types & string work as keys|
|use case|find min/max/next smallest, iterate sorted, large n|order not important, hashing not expensive, small n|

### Memory & Pointers

* compare `new` and `malloc`

|what|malloc|new|
|----|------|---|
|returns|`void` ptr|ptr to obj|
|ctor called|no|yes|
|errors|returns `NULL`|`throw` exception|
|overloading|no|yes|
|requires size|yes|no|
|type|function|operator|

* are you familiar with RAII?
* 3 main storage areas
    * heap: dynamically allocated memory using `malloc`/`new`
    * stack: ordinary/automatic/local vars
    * data segment: static vars, not init until declaration is reached
* diagram
```
stack segment (data local to functions)
- - - - - - -
|
V

the hole

^
|
- - - - - - -
the heap (used for malloc())
-------------
BSS segment (uninitialized data: global/static vars init. to 0 or not init.)
-
data segment (initialized data: global/static vars init. to non-zero)
-------------
text segment (instructions)
```
* compare `unique_ptr` and `shared_ptr`

|what|`unique_ptr`|`shared_ptr`|`weak_ptr`|
|----|------------|------------|----------|
|ownership|exclusive|shared|augmentation of `shared_ptr`|
|copying allowed|no, move-only type|yes|
|size|same as raw ptrs|2x size of raw ptrs|same as `shared_ptr`|
|custom deleters|part of ptr type|not part of type: can store in container even if diff deleters|n/a|
|use case|factory functions, pimpl||detect dangling cache ptrs, observer design pattern, prevention of `shared_ptr` cycles|
|support arrays|yes|no|no|
|convert to opposite type|shared from unique|no|shared from weak|
|ref count|no|yes, dynamically allocated & atomic|weak count|
|control block|no|yes|yes|

### Threads

* compare processes and threads

|process|thread|
|-------|------|
|instance of prog in execution|execution path of a proc|
|independent entity w/ dedicated sys. resources|changes to proc resource by 1 thread visible to others|
|separate address space|same stack space|
|use IPC (pipes/files/sockets)|multi thread per proc|
||multi threads share state|
||multi threads can read/write same mem|
||own registers|
||own stack, but write-able by other threads|

* compare fork and exec
* 4 deadlock conditions
    1. Mutual Exclusion: Only one process can use a resource at a given time.
    2. Hold and Wait: Processes already holding a resource can request new ones.
    3. No Preemption: One process cannot forcibly remove another process’ resource.
    4. Circular Wait: Two or more processes form a circular chain where each process
       is waiting on another resource in the chain.
* deadlock prevention: remove one of the above conditions

### Other

* compare an inline function and a macro
* compare a ptr and a ref

|what|ptr|ref|
|----|---|---|
|syntax|`*` & `->`|`.`|
|`NULL`|yes|no|
|init|no|yes|
|reassignment|yes|no|

* give and compare all the uses of `static`
    * member function
        * not associated with an instance
        * called as `MyClass::MyMethod()`
        * can only operate on `static` members
    * data member
        * one copy for all instances
        * not thread-safe
    * function
        * deprecated in favor of anon namespace
        * scope limited to current file
    * variable
        * global
            * limited scope to current file
        * inside a function
            * auto 0 init
            * prevents re-init on subsequent calls
* list and define ways to cast in C++
    * `(T) expression` (C-style cast)
    * `T(expression)` (function-style cast)
    * const_cast: cast away `const`ness (`const` to non-`const`)
    * dynamic_cast: safe downcasting
    * reinterpret_cast: non-portable conversions
    * static_cast: force implicit conversion (non-`const` to `const`, `int` to
        `double`)

### OO

* what is an abstract class?
* can you throw an exception in a dtor?
    * never! program will likely terminate
* why should *polymorphic* base class have virtual dtors?
* what does the compiler generate for you in every class?
    * C++03: generated by compiler
        * default ctor
        * dtor
        * copy ctor
        * copy assignment `operator=`
    * C++11: generated by compiler
        * default ctor
        * dtor
        * copy ctor (if no user-defined move)
        * copy assignment `operator=` (if no user-defined move)
        * move ctor (if no user defined dtor/copy/move)
        * move assignment `operator=` (if no user-defined dtor/copy/move)
    * rule of 3: if you need 1, you need all 3
        * dtor
        * copy ctor
        * copy assignment `operator=`
    * rule of 5: if you need 1, you need all 5
        * dtor
        * copy ctor
        * copy assignment `operator=`
        * move ctor
        * move assignment `operator=`
    * rule of 0: if user-defined dtor, copy/move ctor, copy/move assignment,
        should deal exclusively w/ ownership
* what is polymorphism?
* describe the order of ctor and dtor calls in polymorphic classes
    * ctor: base class first
    * dtor: derived class first
* should you call virtual functions in ctors and dtors?
* what is public inheritance?
    * public inheritance means "is-a"
    * virtual f. means "interface must be inherited"
    * non-virtual f. means "both interface and implementation must be inherited"
    * every D is-a B, but not vice versa
    * *everything* that applies to base class objects also applies to derived
      class objects
* what is composition?
    * depending on what you are modeling composition means
        * "has-a": application domain
        * "is-implemented-in-terms-of": implementation domain
* what is private inheritance?
    * private inheritance means "is-implemented-in-terms-of"
    * purely an *implementation* technique
    * compilers will *not* convert a derived class object into a base class
      object
    ```
    class Person {...};
    void Person::eat(const Person &p);
    class Student: private Person {...};
    void Student::study(const Student &s);
    Person p;
    Student s;
    eat(p);         // fine
    eat(s);         // error, a Student is not a Person
    ```
    * members inherited from a private base class become *private members* of
      the derived class even if they were protected or public in the base class
    * private inheritance means that implementation *only* should be inherited;
      interface should be ignored
    * D is implemented in terms of B, but D is not a B
* when would you use them?
    * use composition whenever you *can*, use private inheritance whenever you *must*
    * you must when D is not a B but it needs access to protected B class members
      or needs to redefine inherited virtual f.
* why shouldn't you redefine an inherited non-virtual function?
    * you'll hide it
