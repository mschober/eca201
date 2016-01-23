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

### This introduces two new keywords
* the `class` keyword
    * used to create a new namespace for methods and variables
* the `pass` keyword
    * place holder when a class or method has an empty body

    ###### Classes are a great way to *encapsulate* associated variables and functions
    * code is easier to maintain by reusing small building blocks
    * making the building blocks simple and focused on 1 *concern* is ideal
    * when building a solution the building blocks can be fit together to solve problems

```python
class HelloWorld(object):
    """
    Invoke me in a terminal with
    python -i hello.py
    """

    def __str__(self):
        """
        Underbar underbar methods (__methodname__) are a convention for methods
        belonging to a class. Some class methos are inherited from the parent
        type Object. You can see the parent hierarchy by doing
        import inspect
        inspect(<object>)
        eg
        inspect(HelloWorld)
        If you help(Object) you'll see where these inherited classes come from.
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
