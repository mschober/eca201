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
        """
        The __str__ method is usig the classname as the string to return when printing.
        What is __repr__ for then? Python does something different when you let the interpreter
        inspect and display a variable without a print statement explicitly. This is the
        representation of the object and calls the __repr__ method. By having
        __repr__ delegate to __str__ both styles will print the same thing.
        """
        return self.__str__()
