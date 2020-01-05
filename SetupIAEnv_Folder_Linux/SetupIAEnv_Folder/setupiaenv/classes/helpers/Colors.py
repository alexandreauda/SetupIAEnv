#!/usr/bin/python -u
# coding=utf-8

# Python 2
# Encoding: utf-8

class Colors:
    """Colors: Class (struct) that represent ANSI Escape sequences colors. Useful to print message in color.
        Define two subclasses: fg for foreground and bg for background color.
        Use: Colors.subclass.colorname.
        e.g: Colors.fg.red (to print in red).
             Colors.bg.green (to put the background of the print in green).
        Also, the generic bold disable underline reverse, strike through and invisible work with the main class i.e. Colors.bold (to put the print in bold).
    """

    # ******Public attributes******
    reset = "\033[0m{}\033[00m"
    bold = "\033[01m{}\033[00m"
    disable = "\033[02m{}\033[00m"
    underline = "\033[04m{}\033[00m"
    reverse = "\033[07m{}\033[00m"
    strikethrough = "\033[09m{}\033[00m"
    invisible = "\033[08m{}\033[00m"


    class fg:

        # ******Public attributes******
        black = "\033[30m{}\033[00m"
        red = "\033[31m{}\033[00m"
        green = "\033[32m{}\033[00m"
        orange = "\033[33m{}\033[00m"
        blue = "\033[34m{}\033[00m"
        purple = "\033[35m{}\033[00m"
        cyan = "\033[36m{}\033[00m"
        lightgrey = "\033[37m{}\033[00m"
        darkgrey = "\033[90m{}\033[00m"
        lightred = "\033[91m{}\033[00m"
        lightgreen = "\033[92m{}\033[00m"
        yellow = "\033[93m{}\033[00m"
        lightblue = "\033[94m{}\033[00m"
        pink = "\033[95m{}\033[00m"
        lightcyan = "\033[96m{}\033[00m"


    class bg:
        
        # ******Public attributes******
        black = "\033[40m{}\033[00m"
        red = "\033[41m{}\033[00m"
        green = "\033[42m{}\033[00m"
        orange = "\033[43m{}\033[00m"
        blue = "\033[44m{}\033[00m"
        purple = "\033[45m{}\033[00m"
        cyan = "\033[46m{}\033[00m"
        lightgrey = "\033[47m{}\033[00m"
