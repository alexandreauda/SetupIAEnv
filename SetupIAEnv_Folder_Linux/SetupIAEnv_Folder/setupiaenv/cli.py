#!/usr/bin/python -u
# coding=utf-8

# Python 2
# Encoding: utf-8

""" Import for error handling. """
from __future__ import print_function

# Import Pillow to manipulate images. (Needed for misc).
from PIL import Image, ImageTk

""" Import all the general packages useful. """
# General packages.
import sys
import os
import errno
import ntpath

""" Import packages useful for the ArgumentParser (with password)."""
# argparse is useful to use the argumentParser.
import argparse

""" Import all the custom classes."""
# Custom class to print errors, warnings, ...
from setupiaenv.classes.helpers.CustomPrint import CustomPrint
# Custom class that provide various sys static functions.
from setupiaenv.classes.helpers.SysTools import SysTools


# Import Tkinter.
try:
    # for Python3
    import tkinter   ## notice lowercase 't' in tkinter here
except ImportError:
    CustomPrint.warningPrint("Warning: Fail to import tkinter. Import Tkinter instead.")
    # for Python2
    import Tkinter   ## notice capitalized T in Tkinter 


""" Implementation of custom functions."""


class CliManagementSetupIAEnv():
    """Class for the management of cli for SetupIAEnv.

    """


    @staticmethod
    def __meta_data_script(progName):
        """(Private static method) Define meta-data of the script (name, version, description, help, ...).

        Args:
            progName (str): the name of the script that call gen_cli_args().

        Returns:
            str: progName. Program name of the script that call gen_cli_args().
            str: progNameHard. Program name of the application (setupiaenv).
            str: progVersion. Version number of the script.
            str: versionCodeName. Code name of the current version of the script.
            str: versionText. Well format text that give progVersion, and versionCodeName information.
            str: progDescription. The Description of the program.
            str: progExample_text. The examples given to help the user to run the script.
            str: progMiscExample_text. The example given in the setupiaenv misc menu.

        """

        # Hard code progName.
        progNameHard = 'setupiaenv'

        # The version of the script.
        progVersion = '1.0.0'

        # The version code name.
        versionCodeName = 'First version'

        # Text display when user ask the version of the program.
        versionText =""" 
        {} - {}
        {} - {}
        {} - {}
        """.format(CustomPrint.highlight('Program Name', 'red'),CustomPrint.highlight(progName, 'yellow'),CustomPrint.highlight('Version', 'red'),CustomPrint.highlight(progVersion, 'yellow'), CustomPrint.highlight('Codename', 'red'), CustomPrint.highlight(versionCodeName, 'yellow'))



        # Give the description of the script.
        progDescription = """                                                                        
              _______. _______ .___________. __    __  .______    __       ___       _______ .__   __. ____    ____ 
            /       ||   ____||           ||  |  |  | |   _  \  |  |     /   \     |   ____||  \ |  | \   \  /   / 
           |   (----`|  |__   `---|  |----`|  |  |  | |  |_)  | |  |    /  ^  \    |  |__   |   \|  |  \   \/   /  
            \   \    |   __|      |  |     |  |  |  | |   ___/  |  |   /  /_\  \   |   __|  |  . `  |   \      /   
        .----)   |   |  |____     |  |     |  `--'  | |  |      |  |  /  _____  \  |  |____ |  |\   |    \    /    
        |_______/    |_______|    |__|      \______/  | _|      |__| /__/     \__\ |_______||__| \__|     \__/     
                                

                                      Setup IA and machine-learning environnement

                                                  {} - {}
                                               {} - {}

        """.format(CustomPrint.highlight('Version', 'red'),CustomPrint.highlight(progVersion, 'yellow'), CustomPrint.highlight('Codename', 'red'), CustomPrint.highlight(versionCodeName, 'yellow'))



        # Give examples of how to use the script (general menu).
        progExample_text = """Examples:
        
        {}:
        python {} -h
        setupiaenv -h
        
        {}:
        python {} -v
        setupiaenv -v
        
        {}:
        python {} -h
        setupiaenv -h

        {}:
        python {} misc -h
        setupiaenv misc -h

        {}:
        setupiaenv -b -a -envName iaenv -gpu

        setupiaenv -b -a -envName iaenv

        setupiaenv -b -a -envName iaenv -gpu -sys
        (execute: "setupiaenv -h" to see more options)

        setupiaenv misc -l
        (execute: "setupiaenv misc -h" to see more options)

        {}: 
        "python {}" can be replace by: "setupiaenv"
        """.format(CustomPrint.highlight('Get help', 'white_underline'), progName, CustomPrint.highlight('Get version', 'white_underline'), progName, CustomPrint.highlight('Print sub-command graph help', 'white_underline'), progName, CustomPrint.highlight('Print sub-command misc help', 'white_underline'), progName, CustomPrint.highlight('Typical command', 'white_underline'), CustomPrint.highlight('Note', 'white_underline'), progName)



        # Give examples of how to use the script (misc menu).
        progMiscExample_text = """Examples:
        
        {}:
        python {} misc -h
        setupiaenv misc -h
        
        {}:
        python {} misc -v
        setupiaenv misc -v
        
        {}:
        python {} misc -l
        setupiaenv misc -l

        {}:
        python {} misc -bc
        setupiaenv misc -bc

        {}:
        python {} misc -sc
        setupiaenv misc -sc

        {}:
        python {} misc -a
        setupiaenv misc -a

        {}:
        python {} misc -Il
        setupiaenv misc -Il

        {}:
        python {} misc -FIl
        setupiaenv misc -FIl

        {}: 
        "python {}" can be replace by: "setupiaenv"
        """.format(CustomPrint.highlight('Get help', 'white_underline'), progName, CustomPrint.highlight('Get version', 'white_underline'), progName, CustomPrint.highlight('Print setupiaenv logo', 'white_underline'), progName, CustomPrint.highlight('Make me a big coffee', 'white_underline'), progName, CustomPrint.highlight('Make me a small coffee', 'white_underline'), progName, CustomPrint.highlight('Gives the Answer to the Ultimate Question of Life, the Universe, and Everything', 'white_underline'), progName, CustomPrint.highlight('Display image of setupiaenv logo with the default Image Viewer', 'white_underline'), progName, CustomPrint.highlight('Display image of setupiaenv logo in Full Screen', 'white_underline'), progName, CustomPrint.highlight('Note', 'white_underline'), progName)
        
        # Return all the meta-data of the script.
        return (progName, progNameHard, progVersion, versionCodeName, versionText, progDescription, progExample_text, progMiscExample_text)


    @staticmethod
    def __printsetupiaenvLogo():
        """(Private static method) Print the logo of setupiaenv in ascii-art.

        Returns:
            str: setupiaenv_logo. The string of the ascii-art logo.

        """
        
        # Define the string of the ascii-art logo.
        setupiaenv_logo = """
             _______. _______ .___________. __    __  .______    __       ___       _______ .__   __. ____    ____ 
            /       ||   ____||           ||  |  |  | |   _  \  |  |     /   \     |   ____||  \ |  | \   \  /   / 
           |   (----`|  |__   `---|  |----`|  |  |  | |  |_)  | |  |    /  ^  \    |  |__   |   \|  |  \   \/   /  
            \   \    |   __|      |  |     |  |  |  | |   ___/  |  |   /  /_\  \   |   __|  |  . `  |   \      /   
        .----)   |   |  |____     |  |     |  `--'  | |  |      |  |  /  _____  \  |  |____ |  |\   |    \    /    
        |_______/    |_______|    |__|      \______/  | _|      |__| /__/     \__\ |_______||__| \__|     \__/     
                                                                                                                   
        """

        # Print the logo.
        print(setupiaenv_logo)

        # Return the string of the ascii-art logo.
        return setupiaenv_logo



    @staticmethod
    def __printCoffee():
        """(Private static method) Print a big cup of coffee in ascii art.

        Returns:
            str: coffee_logo. The string of the ascii-art coffee.

        """

        # Define the string of the ascii-art big coffee.
        coffee_logo = """
                         (
                          )     (
                   ___...(-------)-....___
               .-""       )    (          ""-.
         .-'``'|-._             )         _.-|
        /  .--.|   `""---...........---""`   |
       /  /    |                             |
       |  |    |                             |
        \  \   |                             |
         `\ `\ |                             |
           `\ `|                             |
           _/ /\                             /
          (__/  \                           /
       _..---""` \                         /`""---.._
    .-'           \                       /          '-.
   :               `-.__             __.-'              :
   :                  ) ""---...---"" (                 :
    '._               `"--...___...--"`              _.'
      \""--..__                              __..--""/
       '._     ""'----.....______.....----""''     _.'
          `""--..,,_____            _____,,..--""`
                        `""'----""'`                                                   
        """

        # Print the ascci-art big coffee.
        print(coffee_logo)

        # Return the string of the ascii-art big coffee.
        return coffee_logo


    @staticmethod
    def __printSmallCoffee():
        """(Private static method) Print a small cup of coffee in ascii art.

        Returns:
            str: smallCoffee_logo. The string of the ascii-art coffee.

        """

        # Define the string of the ascii-art small coffee.
        smallCoffee_logo = """ 
        ( (
         ) )
      .______.
      |      |]
      \      /
       `----'                     
        """

        # Print the ascci-art small coffee.
        print(smallCoffee_logo)

        # Return the string of the ascii-art big coffee.
        return smallCoffee_logo


    @staticmethod
    def __printAnswer():
        """(Private static method) Print the universal answer of the universe.

        Returns:
            str: answer_logo. The string of the ascii-art answer.

        """

         # Define the string of the ascii-art answer.
        answer_logo = """ 
        42.                    
        """

        # Print the ascci-art answer.
        print(answer_logo)

        # Return the string of the ascii-art answer.
        return answer_logo


    @staticmethod
    def __displaysetupiaenvImageLogo():
        """(Private static method) Display image of setupiaenv logo.

        """
 
        # Try to open the image of setupiaenv logo.
        try:
          # Define the local directory where are store images of the project.
          imagesDir = 'images'
          # Tell the name of the image to display.
          imageName = 'setupiaenvLogoFinal.png'
          # Form the pah where is located the image to display.
          pathOfImage = os.path.join(imagesDir, imageName)
          # Use Pillow to open the image with the default image Viewer.
          img = Image.open(pathOfImage)
          # Show image with default image Viewer.
          img.show()
        # If the image cannot been found at the define location, print a warning and exit.
        except IOError as e:
            # Input file doesn't exist. Print a warning and exit.
            CustomPrint.errorPrint("Error: the input file " + str(pathOfImage) + " doesn't exist.")
            CustomPrint.errorPrint(str(e))
            sys.exit(1)


    # see: https://github.com/jacky-ttt/CodingEveryday/blob/master/Day052-display%20image%20in%20full%20screen%20using%C2%A0python/DisplayImageFullScreen/main.py
    @staticmethod
    def __fit_center(pil_image):
        """(Private static method) Display an image (open with Pillow) in Full screen with tkinter.

        Args:
            pil_image (:obj: Image): An Pillow Image object.

        """

        # Define the main window with tkinter
        root = tkinter.Tk()
        # Define the title of the window.
        root.title("setupiaenv Logo")
        # Get width and height info of the device that run the script.
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        root.geometry("%dx%d+0+0" % (w, h))
        root.focus_set()
        # If user press escape, close the window.
        root.bind("<Escape>", lambda e: (e.widget.withdraw(), e.widget.quit()))
        # Construct a canvas with the size of the full screen window that will be inside the window and that will hold the image.
        canvas = tkinter.Canvas(root, width=w, height=h, highlightthickness=0)
        # Put the canvas in the window.
        canvas.pack()
        # Tell the the background of the canvas is black.
        canvas.configure(background='black')

        # Computation to resize the input image for the full screen.
        img_width, img_height = pil_image.size
        ratio = min(w / img_width, h / img_height)
        img_width = int(img_width * ratio)
        img_height = int(img_height * ratio)
        pil_image = pil_image.resize((img_width, img_height), Image.ANTIALIAS)

        # Put the image in tkinter window.
        image = ImageTk.PhotoImage(pil_image)
        imagesprite = canvas.create_image(w / 2, h / 2, image=image)
        root.mainloop()


    # see: https://github.com/jacky-ttt/CodingEveryday/blob/master/Day052-display%20image%20in%20full%20screen%20using%C2%A0python/DisplayImageFullScreen/main.py
    @staticmethod
    def __displaysetupiaenvImageLogoFullScreen():
        """(Private static method) Display image of setupiaenv logo in Full screen with tkinter.

        """
 
        # Try to open the image of setupiaenv logo.
        try:
          # Define the local directory where are store images of the project.
          imagesDir = 'images'
          # Tell the name of the image to display.
          imageName = 'setupiaenvLogoFinal.png'
          # Form the pah where is located the image to display.
          pathOfImage = os.path.join(imagesDir, imageName)
          # Use Pillow to open the image with the default image Viewer.
          img = Image.open(pathOfImage)
          # Show the image (open with Pillow) in Full screen with tkinter.
          CliManagementSetupIAEnv.__fit_center(img)
        # If the image cannot been found at the define location, print a warning and exit.
        except IOError as e:
            # Input file doesn't exist. Print a warning and exit.
            CustomPrint.errorPrint("Error: the input file " + str(pathOfImage) + " doesn't exist.")
            CustomPrint.errorPrint(str(e))
            sys.exit(1)
        



    @staticmethod
    def gen_cli_args(progName):
        """(Static method) Management of the parameters to give and given to the setupiaenv script.

        Args:
            progName (str): the name of the script that call gen_cli_args().

        Returns:
            argparse: args. Object from argparse that contains all the argument s given to the script.

        """
        
        # Retrieve meta-data of the script.
        (progName, progNameHard, progVersion, versionCodeName, versionText, progDescription, progExample_text, progMiscExample_text) = CliManagementSetupIAEnv.__meta_data_script(progName)
        
        # Define a parser to parse the arguments given to the program. Tell the parser to use formatter_class=argparse.RawDescriptionHelpFormatter to tell argparse to not modify our help layout.
        parser = argparse.ArgumentParser(prog=progName, description=progDescription, epilog=progExample_text, formatter_class=argparse.RawDescriptionHelpFormatter)
        

        """ A user must provide some arguments to the script (for instance: the input file to convert in .dot and in an output (default: .png) format, or a name for the output .dot and output (default: .png) files...)."""
        
        # [OPTIONAL] -v argument to show program's version number with codename verion and exit.
        parser.add_argument("-v", "--version", help="Show program's version number with codename verion and exit", dest='version', action='version', version=versionText)
     
        # Define groups to group the arguments options in graph subparser.
        group_Options = parser.add_argument_group('Options')
        group_Debug = parser.add_argument_group('Debug options')
     
        # When do setupiaenv graph [options], define what are the options.
        # group_Options group.
        group_Options.add_argument("-sys", "--installSystem", help="Install packages on system (not only within a virtualenv).", dest='installSystem', action='store_true')
        group_Options.add_argument("-b", "--batch", help="Run install in batch mode (without manual intervention). Automatically say yes when perform apt or pip3.", dest='batch', action='store_true')
        group_Options.add_argument("-f", "--force", help="Force the installation by ignoring all the warnings.", dest='force', action='store_true')
        group_Options.add_argument("-a", "--anaconda", help="Install Anaconda.", dest='anaconda', action='store_true')
        group_Options.add_argument("-envName", "--condaEnvName", help="Name of the Anaconda/conda virtual environment you will create.", dest='condaEnvName', action='store', type=str, default="iaenv")
        group_Options.add_argument("-gpu", "--gpuTensorflow", help="Install Tensorflow with gpu support.", dest='gpuTensorflow', action='store_true')
        # group_Options.add_argument("-ca", "--checkanacondasetup", help="Verify the hash of anaconda setup.", dest='checkanacondasetup', action='store_true')
        # group_Options.add_argument("-md5", "--md5anacondasetupexpected", help="The md5 that is expect for the anaconda setup.", dest='md5anacondasetupexpected', action='store', type=str, default="ec6a6bf96d75274c2176223e8584d2da")
        # group_Options.add_argument("-m", "--mask", help="Mask (base) environment after installation of Anaconda.", dest='mask', action='store_true')
        # group_Options.add_argument("-l", "--launchanaconda", help="lauchanaconda.", dest='launchanaconda', action='store_true')

        # Debug group.
        group_Debug.add_argument("-d", "--debug", help="Enter in debug mode. Level 1 usage: -d. Level 2 usage: -dd, etc...", dest='debug', action='count', default=0)
        group_Debug.add_argument("-arg", "--arguments", help="Only display the value of the arguments and check them.", dest='arguments', action='store_true')
        
        # Add a subparser to add additional commands.
        subparsers = parser.add_subparsers(title='sub-commands', description='available sub-commands', dest='sub_command_position1')

        # Create the parser for the "misc" command i.e. we can now do: setupiaenv misc [options]
        parser_misc = subparsers.add_parser('misc', help='Miscellaneous tools', description=progDescription, epilog=progMiscExample_text, formatter_class=argparse.RawDescriptionHelpFormatter)
        
        parser_misc.add_argument("-v", "--version", help="Show program's version number with codename verion and exit", dest='version', action='version', version=versionText)

        # Define groups to group the arguments options.
        group_Ascii_Art = parser_misc.add_argument_group('Ascii_Art options')
        group_Image = parser_misc.add_argument_group('Images options')

        # When do setupiaenv misc [options], define what are the options.
        # Ascii_Art group.
        group_Ascii_Art.add_argument("-l", "--logo", help="Display setupiaenv logo.", dest='logo', action='store_true')
        group_Ascii_Art.add_argument("-bc", "--bigcoffee", help="Make me a big coffee. (Because everyone deserves a big good coffee).", dest='bigcoffee', action='store_true')
        group_Ascii_Art.add_argument("-sc", "--smallcoffee", help="Make me a coffee. (Because everyone deserves a good coffee).", dest='smallcoffee', action='store_true')
        group_Ascii_Art.add_argument("-a", "--answer", help="Gives the Answer to the Ultimate Question of Life, the Universe, and Everything.", dest='answer', action='store_true')

        # Image group.
        group_Image.add_argument("-Il", "--Ilogo", help="Display image of setupiaenv logo with the default Image Viewer", dest='Ilogo', action='store_true')
        group_Image.add_argument("-FIl", "--FIlogo", help="Display image of setupiaenv logo in Full Screen. Press escape to exit.", dest='FIlogo', action='store_true')


        # Parse the arguments given to the program and store them in the object args.
        args = parser.parse_args()

        
        # Return the parsed arguments. To retrieve parsed arguments: args.param1, args.parmam2,...
        return args



    @staticmethod
    def checkIfMiscArguments(args):
        """(Static method) Sanity checks on the arguments given to the script.

        Args:
            args (argparse obj): the parsed arguments return by gen_cli_args() that contain all the arguments given to the program.

        """
        
        # Sanity checks on the arguments.
        # TODO: Implement sanity check in that case.

        # If the sub-command is misc.
        if(hasattr(args, 'sub_command_position1') and args.sub_command_position1 == 'misc'):
            # If the user provides the --logo option, print setupiaenv logo and exit.
            if(args.logo):
                CliManagementSetupIAEnv.__printsetupiaenvLogo()
                sys.exit(0)
            # If the user provides the --bigcoffee option, print big coffee ascii art and exit.
            if(args.bigcoffee):
                CliManagementSetupIAEnv.__printCoffee()
                sys.exit(0)
            # If the user provides the --smallcoffee option, print big coffee ascii art and exit.
            if(args.smallcoffee):
                CliManagementSetupIAEnv.__printSmallCoffee()
                sys.exit(0)
            # If the user provides the --answer option, print big coffee ascii art and exit.
            if(args.answer):
                CliManagementSetupIAEnv.__printAnswer()
                sys.exit(0)

            # If the user provides the --Illogo option, display setupiaenv logo image in default Image Viewer and exit.
            if(args.Ilogo):
                CliManagementSetupIAEnv.__displaysetupiaenvImageLogo()
                sys.exit(0)
            # If the user provides the --FIlogo option, display setupiaenv logo image in Full Screen in a Tkinter window and exit.
            if(args.FIlogo):
                CliManagementSetupIAEnv.__displaysetupiaenvImageLogoFullScreen()
                sys.exit(0)



    @staticmethod
    def checkAllArguments(args):
        """(Static method) Sanity checks on the arguments given to the script. To verify the arguments, the method need a dataframe that contain the data used to make a graph.

        Args:
            args (argparse obj): the parsed arguments return by gen_cli_args() that contain all the arguments given to the program.
            dataframe (pandas.DataFrame): the pandas dataframe representation of the data. Normally, this dataframe is obtain with the use of dataToDataframe() method.

        """
        
        """ Sanity checks on the arguments."""
        # ...

        # If the sub-command is misc.
        if(hasattr(args, 'sub_command_position1') and args.sub_command_position1 == 'misc'):
            # If the user provides the --logo option, print setupiaenv logo and exit.
            if(hasattr(args, 'logo') and args.logo):
                CliManagementSetupIAEnv.__printsetupiaenvLogo()
                sys.exit(0)
            # If the user provides the --bigcoffee option, print big coffee ascii art and exit.
            if(hasattr(args, 'bigcoffee') and args.bigcoffee):
                CliManagementSetupIAEnv.__printCoffee()
                sys.exit(0)
            # If the user provides the --smallcoffee option, print big coffee ascii art and exit.
            if(hasattr(args, 'smallcoffee') and args.smallcoffee):
                CliManagementSetupIAEnv.__printSmallCoffee()
                sys.exit(0)
            # If the user provides the --answer option, print big coffee ascii art and exit.
            if(hasattr(args, 'answer') and args.answer):
                CliManagementSetupIAEnv.__printAnswer()
                sys.exit(0)

            # If the user provides the --Illogo option, display setupiaenv logo image in default Image Viewer and exit.
            if(hasattr(args, 'Ilogo') and args.Ilogo):
                CliManagementSetupIAEnv.__displaysetupiaenvImageLogo()
                sys.exit(0)
            # If the user provides the --FIlogo option, display setupiaenv logo image in Full Screen in a Tkinter window and exit.
            if(hasattr(args, 'FIlogo') and args.FIlogo):
                CliManagementSetupIAEnv.__displaysetupiaenvImageLogoFullScreen()
                sys.exit(0)
        
        # Else...
        else: 
            # Check the cli arguments that hasen't been check yet (graph option arguments i.e.: -s, -dest, -ea, -isdir, -w and -l). 
            # To check these arguments, dataframe with info from input file should not be empty.
            print("OK")

        #     # Debug/arguments print.
        #     # If the debug level is greater or equal to 1 or if -a option is provided, print debug/arguments information on the argument given.
        #     if ((hasattr(args, 'debug') and hasattr(args, 'arguments')) and (args.debug or args.arguments)):
        #         # Print debug/arguments information.
        #         print("\n")
        #         print("Arguments: ")
        #         print("Value of level debug argument: " + str(args.debug))
        #     # If -i option is provided (normally always as it is mandatory), print info if in debug/arguments mode and check validity of this argument.
        #     if(hasattr(args, 'input') and str(args.input)!="None"):
        #         # If the debug level is greater or equal to 1 or if -a option is provided, print debug/arguments information.
        #         if ((hasattr(args, 'debug') and hasattr(args, 'arguments')) and (args.debug or args.arguments)):
        #             print("Value of input argument: " + str(args.input))
        #             print("Value of input argument leaf path: " + str(SysTools.path_leaf(args.input)))
        #         # Check validity of -i argument.
        #         # If the input file has not one of the following extension: 'atom', 'csv', 'json', 'json_rows', 'raw', 'xml', display a warning.
        #         extensionToCheck = ['atom', 'csv', 'json', 'json_rows', 'raw', 'xml']
        #         if not any(ext in str(SysTools.path_leaf(args.input)) for ext in extensionToCheck):
        #             CustomPrint.warningPrint("Warning: the input file " + str(SysTools.path_leaf(args.input)) + " has not a standard extension in: " + str(extensionToCheck) + ".")
        #         # If input file doesn't contain output/, display a warning (as normally input file are in the output/ directory).
        #         if ("output/" not in str(args.input)):
        #             CustomPrint.warningPrint("Warning: the input file " + str(args.input) + " doesn't contained output/. Normally input file is stored in the output/ folder.")
        #         # Check if the file specify in args.input exist. If not, print error and exit.
        #         SysTools.checkIfFileExist(str(args.input))
        #     # If -o option is provided (normally always as it is mandatory), print info if in debug/arguments mode and check validity of this argument.
        #     if(hasattr(args, 'output') and str(args.output)!="None"):
        #         # If the debug level is greater or equal to 1 or if -a option is provided, print debug/arguments information.
        #         if ((hasattr(args, 'debug') and hasattr(args, 'arguments')) and (args.debug or args.arguments)):
        #             print("Value of the output argument: " + str(args.output))
        #             print("Value of the output argument leaf path: " + str(SysTools.path_leaf(args.output)))
        #         # Check validity of -o argument.
        #         # If the output file name doesn't contain outputGraph/, display a warning.
        #         if ("outputGraph" not in str(args.output)):
        #             CustomPrint.warningPrint("Warning: the output files " + str(args.output) + " doesn't contained outputGraph/. Thus, the files will not be put in the outputGraph/ directory. Consider put the output files in the outputGraph/ directory.")
        #         # If the output file name contain "." (i.e. an extension), display a warning.
        #         if ("." in str(SysTools.path_leaf(args.output))):
        #             CustomPrint.warningPrint("Warning: the output file: " + str(args.output) + " has apparently an extension. Name of file in -o argument must not contain an extension. Consider delete the extension.")
        #         # Check if output directory exist at the given path args.output less path leaf (ie: outputGraph/testOutput -> is outputGraph/ exist?). If the folder doesn't exist, ask a confirmation to create the directory if the user want to.
        #         # Get path less path_leaf of args.output to obtain a directory (ie: outputGraph/testOutput -> outputGraph/).
        #         pathLessLeaf = SysTools.getPathLessPath_leaf(str(args.output))
        #         # Check if the path less path_leaf of args.output exist or not. If not, ask a confirmation to create the directory if the user want to.
        #         isPathLessLeaf = SysTools.checkIfDirExist(pathLessLeaf, True, True)
        #         # If the output directory still not exist, display an error and exit.
        #         if(not isPathLessLeaf):
        #             CustomPrint.errorPrint("Error: the output directory " + str(pathLessLeaf) + " doesn't exist.")
        #             sys.exit(1)
        #     # If the debug level is greater or equal to 1 or if -a option is provided, print debug/arguments information.
        #     if ((hasattr(args, 'debug') and hasattr(args, 'arguments')) and (args.debug or args.arguments)):
        #         # Print the value of -T argument (default: png)
        #         if(hasattr(args, 'format')):
        #             print("Value of the format argument: " + str(args.format))
        #         if(hasattr(args, 'openGraph')):
        #             print("Value of the openGraph argument: " + str(args.openGraph))

        #     # Check the cli arguments that hasen't been check yet (graph option arguments i.e.: -s, -dest, -ea, -isdir, -w and -l). 
        #     # To check these arguments, dataframe with info from input file should not be empty.
        #     if(not dataframe.empty):
        #         # If -sd is used, print the dataframe and exit.
        #         if(hasattr(args, 'showdata') and args.showdata):
        #             print("")
        #             print(dataframe)
        #             sys.exit(0)
        #         # If the debug level is greater or equal to 1 or if -a option is provided, print debug/arguments information.
        #         if ((hasattr(args, 'debug') and hasattr(args, 'arguments')) and (args.debug or args.arguments)):
        #             # Then, print the value of graph option arguments. These parameters cannot been check before because we must import the data to verify them.
        #             print("\nGraph arguments: ")
        #             if(hasattr(args, 'source')):
        #                 print("Value of the source argument: " + str(args.source))
        #         # Check validity of -s argument.
        #         # If args.source is not a column name, throw an error.
        #         if(hasattr(args, 'source') and (str(args.source) not in dataframe.columns)):
        #             CustomPrint.errorPrint("Error: source argument must be a column name.\nShould be one of the following: " + str(dataframe.columns))
        #             sys.exit(1)
        #         # If the debug level is greater or equal to 1 or if -a option is provided, print debug/arguments information.
        #         if ((hasattr(args, 'debug') and hasattr(args, 'arguments')) and (args.debug or args.arguments)):
        #             if(hasattr(args, 'destination')):
        #                 print("Value of the destination argument: " + str(args.destination))
        #         # Check validity of -dest argument.
        #         # If args.destination is not a column name, throw an error.
        #         if(hasattr(args, 'destination') and (str(args.destination) not in dataframe.columns)):
        #             CustomPrint.errorPrint("Error: destination argument must be a column name.\nShould be one of the following: " + str(dataframe.columns))
        #             sys.exit(1)
        #         # If column source and destination are the same, throw an error.
        #         if(hasattr(args, 'source') and hasattr(args, 'destination') and str(args.source) == str(args.destination)):
        #             CustomPrint.errorPrint("Error: source and destination argument must be different.")
        #             sys.exit(1)
        #         # If the debug level is greater or equal to 1 or if -a option is provided, print debug/arguments information.
        #         if ((hasattr(args, 'debug') and hasattr(args, 'arguments')) and (args.debug or args.arguments)):
        #             if(hasattr(args, 'edge_attributes')):
        #                 print("Value of the edge_attributes argument: " + str(args.edge_attributes))
        #         # Check validity of -ea argument.
        #         # If -ea is not empty.
        #         if(hasattr(args, 'edge_attributes') and args.edge_attributes):
        #             # If user has specify -ea all, do nothing special...
        #             if(len(args.edge_attributes)==1 and "all" in args.edge_attributes) :
        #                 # Do nothing
        #                 # If the debug level is greater or equal to 1 or if -a option is provided, print debug/arguments information.
        #                 if((hasattr(args, 'debug') and hasattr(args, 'arguments')) and (args.debug or args.arguments)):
        #                     print("Check -ea all: done!")
        #             # Check validity of -ea argument.
        #             # Check if dataframe.columns contains all elements of args.edge_attributes. If not, throw an error.
        #             elif(not all(elem in dataframe.columns for elem in args.edge_attributes)):
        #                 CustomPrint.errorPrint("Error: edge_attributes arguments must be column name.\nShould be one of the following: " + str(dataframe.columns))
        #                 sys.exit(1)
        #             # If source is in edge_attributes, display an error.
        #             elif(hasattr(args, 'source') and (str(args.source) in args.edge_attributes)):
        #                 CustomPrint.errorPrint("Error: edge_attributes arguments cannot contains the source.")
        #                 sys.exit(1)
        #             # If destination is in edge_attributes, display an error.
        #             elif(hasattr(args, 'destination') and (str(args.destination) in args.edge_attributes)):
        #                 CustomPrint.errorPrint("Error: edge_attributes arguments cannot contains the destination.")
        #                 sys.exit(1)
        #         # If args.edge_attributes is not specified, ie equal None, then initialize it to empty list.
        #         else:
        #             args.edge_attributes = []
        #         # If the debug level is greater or equal to 1 or if -a option is provided, print debug/arguments information.
        #         if ((hasattr(args, 'debug') and hasattr(args, 'arguments')) and (args.debug or args.arguments)):
        #             if(hasattr(args, 'isDirectional')):
        #                 print("Value of the isDirectional argument: " + str(args.isDirectional))
        #         # If the debug level is greater or equal to 1 or if -a option is provided, print debug/arguments information.
        #         if ((hasattr(args, 'debug') and hasattr(args, 'arguments')) and (args.debug or args.arguments)):
        #             if(hasattr(args, 'weight_colName')):
        #                 print("Value of the weight_colName argument: " + str(args.weight_colName))
        #         # Check validity of -w argument.
        #         # If the weight column is specified...
        #         if(hasattr(args, 'weight_colName') and str(args.weight_colName)!="None"):
        #             # Compute valid choice for the weight_colName (i.e. a column name that is numerical and no empty and that do not correspond to source or dest).

        #             if(hasattr(args, 'source')):
        #                 # Get a dataframe without the source_edges column.
        #                 df_WithoutSource_edges = dataframe.loc[:, dataframe.columns != str(args.source)].copy()
        #             if(hasattr(args, 'destination')):
        #                 # Get a dataframe without the source_edges and dest_edges column.
        #                 df_WithoutSource_edgesAndDest_edges = df_WithoutSource_edges.loc[:, df_WithoutSource_edges.columns != str(args.destination)].copy()
                    
        #             # On the df_WithoutSource_edgesAndDest_edges, compute the dataframe with only numerical and no empty column. 
        #             numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
        #             Numericaldf = df_WithoutSource_edgesAndDest_edges.select_dtypes(include=numerics).copy()
        #             # When all the value of a column are NaN, drop it.
        #             NumericaldfWithoutNaN = Numericaldf.dropna(axis='columns', how='all')

        #             # Dataframe with only valid column for weight_colName.
        #             #print(NumericaldfWithoutNaN)
        #             # Take the numerical and no empty column of df_WithoutSource_edgesAndDest_edges as valid choice of weight column.
        #             validChoiceFor_weight_colName = str(NumericaldfWithoutNaN.columns)
                    
        #             # Check validity of -w argument.
        #             # Check if weight column is a column name.
        #             if(hasattr(args, 'weight_colName') and (str(args.weight_colName) not in dataframe.columns)):
        #                 CustomPrint.errorPrint("Error: weight_colName argument must be a column name.\nShould be one of the following: " + str(validChoiceFor_weight_colName))
        #                 sys.exit(1)
        #             # If it is a column name, check if is not the same column than the source.    
        #             elif(hasattr(args, 'weight_colName') and hasattr(args, 'source') and str(args.weight_colName) == str(args.source)):
        #                 CustomPrint.errorPrint("Error: weight_colName argument must be a column name different from the source.\nShould be one of the following: " + str(validChoiceFor_weight_colName))
        #                 sys.exit(1)
        #             # If it is a column name and not the same column than the source, check if is not the same column than the destination.    
        #             elif(hasattr(args, 'weight_colName') and hasattr(args, 'destination') and str(args.weight_colName) == str(args.destination)):
        #                 CustomPrint.errorPrint("Error: weight_colName argument must be a column name different from the destination.\nShould be one of the following: " + str(validChoiceFor_weight_colName))
        #                 sys.exit(1)
        #             # Check if weight column is a numerical and no empty column.
        #             elif(hasattr(args, 'weight_colName') and (str(args.weight_colName) not in NumericaldfWithoutNaN)):
        #                 CustomPrint.errorPrint("Error: weight_colName argument must be a numerical column name.\nShould be one of the following: " + str(validChoiceFor_weight_colName))
        #                 sys.exit(1)

        #         # If the debug level is greater or equal to 1 or if -a option is provided, print debug/arguments information.
        #         if ((hasattr(args, 'debug') and hasattr(args, 'arguments')) and (args.debug or args.arguments)):
        #             if(hasattr(args, 'label_colName')):
        #                 print("Value of the label_colName argument: " + str(args.label_colName))
        #         # Check validity of -l argument.
        #         # If the label column is specified...
        #         if(hasattr(args, 'label_colName') and str(args.label_colName)!="None"):
        #             if(hasattr(args, 'source')):
        #                 # Compute valid choice for the label_colName (i.e. a column name that is not the source or the destination). 
        #                 # Get a dataframe without the source_edges column.
        #                 df_WithoutSource_edges = dataframe.loc[:, dataframe.columns != str(args.source)].copy()
        #             if(hasattr(args, 'destination')):
        #                 # Get a dataframe without the source_edges and dest_edges column.
        #                 df_WithoutSource_edgesAndDest_edges = df_WithoutSource_edges.loc[:, df_WithoutSource_edges.columns != str(args.destination)].copy()
        #             # Take df_WithoutSource_edgesAndDest_edges as valid choice of label.
        #             validChoiceFor_label_colName = str(df_WithoutSource_edgesAndDest_edges.columns)

        #             # Check validity of -l argument.
        #             # Check if label_colName is a column name.
        #             if(hasattr(args, 'label_colName') and (str(args.label_colName) not in dataframe.columns)):
        #                 CustomPrint.errorPrint("Error: label_colName argument must be a column name.\nShould be one of the following: " + str(validChoiceFor_label_colName))
        #                 sys.exit(1)
        #             # If it is a column name, check if is not the same column than the source.    
        #             elif(hasattr(args, 'label_colName') and hasattr(args, 'source') and str(args.label_colName) == str(args.source)):
        #                 CustomPrint.errorPrint("Error: label_colName argument must be a column name different from the source.\nShould be one of the following: " + str(validChoiceFor_label_colName))
        #                 sys.exit(1)
        #             # If it is a column name and not the same column than the source, check if is not the same column than the destination.    
        #             elif(hasattr(args, 'label_colName') and hasattr(args, 'destination') and str(args.label_colName) == str(args.destination)):
        #                 CustomPrint.errorPrint("Error: label_colName argument must be a column name different from the destination.\nShould be one of the following: " + str(validChoiceFor_label_colName))
        #                 sys.exit(1)
        #     # If dataframe is empty, throw an error.
        #     else:
        #         CustomPrint.errorPrint("The dataframe with information from input file is empty.")
        #         sys.exit(1)



        #     # ***Check the graph representation arguments.***

        #     # If the debug level is greater or equal to 1 or if -a option is provided, print debug/arguments information.
        #     if ((hasattr(args, 'debug') and hasattr(args, 'arguments')) and (args.debug or args.arguments)):
        #         print("\n")
        #     # If user specifies the -a option, then stop the program after display and check the value of arguments.
        #     if(hasattr(args, 'arguments') and args.arguments):
        #         sys.exit(0)


        # # If the sub-command is neither misc nor graph, print an error and exit.
        # else:
        #     CustomPrint.errorPrint("Error: sub-commands should be graph or misc.")
        #     sys.exit(1)


 
 
# ******Main******

# def main():
#     """Main entry point of the splunkQuery application.

#     """

#     # Get the name of the script.
#     progName = os.path.basename(__file__)

#     # Parse cli arguments.
#     args = CliManagementSetupIAEnv.gen_cli_args(str(progName))

#     # Check all the arguments.
#     CliManagementSetupIAEnv.checkAllArguments(args)

#     print("hello master")


# if __name__== "__main__":
#     # Call the main method to perform a splunk Query.
#     main()