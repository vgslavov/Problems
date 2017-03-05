# C++

## Sources

* Effective C++, Scott Meyers
* Quant Job Interview Questions & Answers, Mark Joshi

## Questions

* compare STL's `map` and `unordered_map`
* compare an inline function and a macro
* compare a ptr and a ref
* compare `new` and `malloc`
* compare processes and threads
* give and compare all the uses of `static`
    * member function
    * data member
    * function
    * variable
* what is an abstract class?
* can you throw an exception in a dtor?
* why should *polymorphic* base class have virtual dtors?
* what does the compiler generate for you in every class?
* what is polymorphism?
* describe the order of ctor and dtor calls in polymorphic classes
* should you call virtual functions in ctors and dtors?
* are you familiar with RAII?
* list and define ways to cast in C++
    * `(T) expression` (C-style cast)
    * `T(expression` (function-style cast)
    * const_cast
    * dynamic_cast
    * reinterpret_cast
    * static_cast
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
