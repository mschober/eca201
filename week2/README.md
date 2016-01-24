### Hello Object World
* In the canonical "Hello World!" tradition, lets see our first class...
* copy/paste the code block below into a python shell
[inherit from object]: http://stackoverflow.com/questions/4015417/python-class-inherits-object

```python
class HelloObjectWorld(object):
    """
    This is a docstring. It tells you all about the class.
    In an interactive shell you can see this help text in a nice format by doing
    help(<object>)
    eg
    help(HelloWorldEmpty)
    or
    hi = HelloWorldEmpty()
    help(hi)
    """
    pass
```

* if you got back to the `>>>` the paste went well!
* you can see the result of building this class in the variable space
* run `dir()` in the shell
* you'll see a listing of the current *namespace*

```python
>>> dir()
['HelloObjectWorld', '__builtins__', '__doc__', '__name__', '__package__']
```

* the class is now visible
* before diving into creating an *instance* of the class commonly referred to as an *object*, look at the *multiline* string in the class
* using the `help()` function you see the help page for that object
* give it a try, you'll see why [*docstrings*](https://www.python.org/dev/peps/pep-0257/#what-is-a-docstring) are handy

---

### The above class definition introduces two new keywords
* the `class` keyword
    * used to create a new [*namespace*](https://docs.python.org/2/tutorial/classes.html#python-scopes-and-namespaces) for methods and variables

    ###### When a class definition is entered, a new namespace is created, and used as the local scope -> [:tm:](https://docs.python.org/2/tutorial/classes.html#class-definition-syntax)
* the `pass` keyword
    * place holder when a class or method has an empty body

    ###### Classes are a great way to *encapsulate* associated variables and functions
    * code is easier to maintain by reusing small building blocks
    * making the building blocks simple and focused on [*one concern*](https://blog.8thlight.com/uncle-bob/2014/05/08/SingleReponsibilityPrinciple.html) is ideal
    * when building a solution the building blocks can be fit together to solve problems

---

### Classes help build blocks
* An empty body isn't real exciting for a new class, but its nice to [*stub in*](https://en.wikipedia.org/wiki/Method_stub) a new idea and keep the code compiling
* Before entring the brave new world of writing your own custom classes, take a look at some default behavior
* The following block of code introduces the idea of *private* methods and variables
    * [ __underbar_underbar ](https://docs.python.org/2/tutorial/classes.html#private-variables-and-class-local-references)
* copy/paste the code block into a python shell
* run `help(HelloToStringInheritance)` to see the help page

```python
class HelloToStringInheritance(object):
    def __str__(self):
        """
        Underbar underbar methods (__methodname__) are a convention for methods
        belonging to a class. Some class methods are inherited from the parent
        type Object. You can see the parent hierarchy by doing
        ObjectType.__bases
        eg
        HelloToStringInheritance.__bases__
        
        This class inherits from the simple type object. 
        Objec has a private method __str__ which can be overriden
        to define how the object is printed.
        """
        return self.__class__.__name__
    def __repr__(self):
        return self.__str__()
if __name__ == "__main__":
    hi =  HelloWorld()
    print hi
```


### Homework
* save a copy of the text from running the help command from HelloObjectWorld.
* 
