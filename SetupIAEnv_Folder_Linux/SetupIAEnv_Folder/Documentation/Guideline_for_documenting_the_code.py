# Guideline for documenting the code. (Example Google Style Python Docstrings)

# See: https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html

# See the following list to test the function with doctest: https://docs.python.org/3/library/doctest.html#module-doctest

# Follow the guideline + add your own comments.

#***************************************************************************


module_level_variable1 = 12345
"""int: Module level variable documented inline.
    ...
    ...
"""

module_level_variable2 = 98765
"""int: Module level variable documented inline.
    ...
    ...
"""


def module_level_function(param1, param2=None, *args, **kwargs):
    """This is an example of a module level function.

    Args:
        param1 (int): The first parameter.
            Second line of description should be indented.
        param2 (:obj:`str`, optional): The second parameter. Defaults to None.
            Second line of description should be indented.
        *args: Variable length argument list.
            ...
        **kwargs: Arbitrary keyword arguments.
            ...

    Returns:
        bool: True if successful, False otherwise.
            ...

    Raises:
        AttributeError: The ``Raises`` section is a list of all exceptions
            that are relevant to the interface.
        ValueError: If `param2` is equal to `param1`.
            ...

    Examples:
        Examples should be written in doctest format, and should illustrate how
        to use the function.

        >>> print(module_level_function(2, "Hello word", "foo", "bar", toto="toto1"))
        True

        >>> print(module_level_function(2, "2", "foo", "bar", toto="toto1"))
        Traceback (most recent call last):
            ...
        ValueError: param1 may not be equal to param2

    """
    # Code of the function.
    if str(param1) == param2:
        raise ValueError('param1 may not be equal to param2')
    return True



class ExampleClass(object):
    """The summary line for a class docstring should fit on one line.

    # If the class has public attributes, they may be documented here
    # in an ``Attributes`` section and follow the same formatting as a
    # function's ``Args`` section. Alternatively, attributes may be documented
    # inline with the attribute's declaration (see __init__ method below).

    # Properties created with the ``@property`` decorator should be documented
    # in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`str`): Description of `attr2`.

    """
    # Code of the class.

    # ******Public attributes******
    # ...
    attr1 = '...'

    # ...
    attr2 = '...'


    # ******Constructor by default******


    # ******Constructor with parameters******
    def __init__(self, param1, param2=2, param3,[]):
        """Example of docstring on the __init__ method.

        Args:
            param1 (str): Description of `param1`.
                ...
            param2 (:obj:`int`, optional): Description of `param2`. Multiple
                lines are supported.
            param3 (:obj:`list` of :obj:`str`, optional): Description of `param3`.
                ...

        """
        # Assign the arguments.
        self.attr1 = 'param1'
        self.attr2 = 2
        #: list of str: Doc comment *before* attribute, with type specified
        self.attr3 = ['attr3']


    # ******Attributes/Getters and Setters******
    @property
    def readonly_property(self):
        """str: Properties should be documented in their getter method."""
        return 'readonly_property'

    @property
    def readwrite_property(self):
        """:obj:`list` of :obj:`str`: Properties with both a getter and setter
        should only be documented in their getter method.

        # If the setter method contains notable behavior, it should be
        # mentioned here.
        """
        return ['readwrite_property']

    @readwrite_property.setter
    def readwrite_property(self, value):
        self._value = value


    # ******Class methods******

    #***Special methods***
    def __special__(self):
        pass


    #***Private methods***
    def _private(self, param1, param2):
        """(Private method) Private methods description.

        # Private members are any methods or attributes that start with an
        # underscore and are *not* special. By default they are not included
        # in the output.

        Args:
            param1 (str): The first parameter.
                ...
            param2 (str): The second parameter.
                ...

        Returns:
            True if successful, False otherwise.
                ...

        Raises:
            AttributeError: The ``Raises`` section is a list of all exceptions
                that are relevant to the interface.
            ValueError: If `param2` is equal to `param1`.
                ...

        """
        pass


    #***Public methods***
    def example_method(self, param1, param2):
        """Class methods are similar to regular functions.

        Args:
            param1 (str): The first parameter.
                ...
            param2 (str): The second parameter.
                ...

        Returns:
            True if successful, False otherwise.
                ...

        Raises:
            AttributeError: The ``Raises`` section is a list of all exceptions
                that are relevant to the interface.
            ValueError: If `param2` is equal to `param1`.
                ...

        Examples:
            ...

            >>> ExampleClass("foo", 3, "test").example_method("hello", "master")
            True

        """
        # Code of the function.
        if str(param1) == param2:
            raise ValueError('param1 may not be equal to param2')
        return True



    