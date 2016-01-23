class HelloWorldEmpty:
    """
    http://stackoverflow.com/questions/4015417/python-class-inherits-object
    This is a docstring. It tells you all about the class.
    In an interactive shell you can see this help text in a nice format by doing
    help(<object>)
    eg
    help(HelloWorldEmpty)
    or
    hi = HelloWorldEmpty()
    help(hi)
    """
    # Homework 1 - save a copy of the text from running the help command on this class.
    pass

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
