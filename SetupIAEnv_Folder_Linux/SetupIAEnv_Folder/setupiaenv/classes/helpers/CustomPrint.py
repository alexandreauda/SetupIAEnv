#!/usr/bin/python -u
# coding=utf-8

# Python 2
# Encoding: utf-8

""" Import for error handling. """
from __future__ import print_function

# Import colored from termcolor to be able to color the text.
from termcolor import colored

""" Import all the general packages useful. """
# General packages.
import sys

""" Import all the custom classes."""
# Custom class use for colored print.
from setupiaenv.classes.helpers.Colors import Colors


class CustomPrint(object):
    """Class that allow special print like error print, warning print, colored print...

    """

    # ******Static methods******

    # A custom function to print errors in the standard output (terminal). Color the print in red.
    # ex : errorprint("Test") -> Test
    # ex : errorprint("foo", "bar", "baz", sep="---") -> foo---bar---baz
    @staticmethod
    def errorPrint(*args, **kwargs):
        """A custom function to print errors in the standard output (terminal). Color the print in red.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            str: The error message.

        Examples:

            >>> CustomPrint.errorPrint("Hello word!")
            Hello word!

        """
        print(Colors.fg.lightred .format(*args), file=sys.stderr, **kwargs)
        return Colors.fg.lightred .format(*args)

    # A custom function to print warning in the standard output (terminal). Color the print in yellow.
    # ex : warningprint("Test") -> Test
    # ex : warningprint("foo", "bar", "baz", sep="---") -> foo---bar---baz
    @staticmethod
    def warningPrint(*args, **kwargs):
        """A custom function to print warnings in the standard output (terminal). Color the print in yellow.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            str: The warning message.

        Examples:

            >>> CustomPrint.warningPrint("Hello word!")
            Hello word!

        """
        print(Colors.fg.yellow .format(*args), file=sys.stderr, **kwargs)
        return Colors.fg.lightred .format(*args)


    # Use termcolor package: https://pypi.org/project/termcolor/
    @staticmethod
    def highlight(text, color='yellow', attributes='bold'):
        """Format the text with termcolor.

        Args:
            param1 (str): The text to format (color, font, ...).
            color (str, optional): The color of the text.
            attributes (str, optional): The attributes to format the text.

        Returns:
            str: The format text.

        Examples:

            >>> print(CustomPrint.highlight("Hello word!"))
            Hello word!

        """
        if color == 'yellow':
            return str(u'{}'.format(colored(text, 'yellow', attrs=[attributes])))
        elif color == 'red':
            return str(u'{}'.format(colored(text, 'red', attrs=[attributes])))
        elif color == 'grey':
            return str(u'{}'.format(colored(text, 'grey', attrs=[attributes])))
        elif color == 'green':
            return str(u'{}'.format(colored(text, 'green', attrs=[attributes])))
        elif color == 'blue':
            return str(u'{}'.format(colored(text, 'blue', attrs=[attributes])))
        elif color == 'magenta':
            return str(u'{}'.format(colored(text, 'magenta', attrs=[attributes])))
        elif color == 'cyan':
            return str(u'{}'.format(colored(text, 'cyan', attrs=[attributes])))
        elif color == 'white':
            return str(u'{}'.format(colored(text, 'white', attrs=[attributes])))
        elif color == 'white_underline':
            return str(u'{}'.format(colored(text, 'white', attrs=['underline'])))
        else:
            return str(u'{}'.format(colored(text, 'white')))
