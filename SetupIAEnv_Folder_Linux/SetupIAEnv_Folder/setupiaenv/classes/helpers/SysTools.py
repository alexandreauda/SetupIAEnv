#!/usr/bin/python -u
# coding=utf-8

# Python 2
# Encoding: utf-8

""" Imports """
# General imports.
import sys
import os
import errno
import ntpath
import traceback

# Import to parse and execute commands.
import shlex, subprocess

""" Import all the custom classes."""
# Custom class to print errors, warnings, ...
from setupiaenv.classes.helpers.CustomPrint import CustomPrint

class SysTools:
    """Class that gather utility sys static functions.

    """

    # ******Static methods******

    # A custom function to ask confirmation of an action.
    @staticmethod
    def askConfirmation(question, default="yes"):
        """Ask a yes/no question via raw_input() and return their answer.

        Args:
            question (str): a string that is the question presented to the user.
            default (str, optional): the presumed answer if the user just hits <Enter>.
                It must be "yes" (the default), "no" or None (meaning an answer is requiered of the user).

        Returns:
            bool: True if user says "yes" or False for "no".

        Raises:
            ValueError: If default is different from None, yes or no.

        """
       
        # Valid answer from the user (yes, no , y, and n).
        valid = {"yes": True, "y": True, "no": False, "n": False}
        if(default is None):
            prompt = "    [y/n] "
        elif(default == "yes"):
            prompt = "    [Y/n] "
        elif(default == "no"):
            prompt = "    [y/N] "
        else:
            raise ValueError("Invalid default answer: '%s'" % default)

        # Ask the answer while a valid answer is not given.
        while True:
            # Print the question in yellow.
            CustomPrint.warningPrint(question + prompt)
            # Ask the question and retrieve the answer of user in choice variable.
            choice = input().lower()
            # If the user don't answer the question by typing Enter, and default is not None, the answer is the default choice.
            if(default is not None and choice == ''):
                return valid[default]
            # Else if the user type his answer, return the valid choice.
            elif(choice in valid):
                return valid[choice]
            # Else, print a warning that ask to enter a valid answer and print the question again.
            else:
                sys.stdout.write("Please respond with 'yes' or 'no' (or 'y' or 'n') \n")


    # see: https://stackoverflow.com/questions/8384737/extract-file-name-from-path-no-matter-what-the-os-path-format
    @staticmethod
    def path_leaf(path):
        """Return last part of a path.

        Args:
            path (str): a valid path (example: outputGraph/testOutput_Anon).

        Returns:
            str: The string that correspond to the leaf of the path (example: outputGraph/testOutput_Anon -> testOutput_Anon).

        Examples:
            Examples should be written in doctest format, and should illustrate how
            to use the function.

            >>> print(SysTools.path_leaf(outputGraph/testOutput_Anon))
            testOutput_Anon

            >>> print(SysTools.path_leaf(outputGraph/testOutput_Anon/))
            testOutput_Anon

        """
        head, tail = ntpath.split(path)
        return tail or ntpath.basename(head)


    # see: https://stackoverflow.com/questions/3663450/python-remove-substring-only-at-the-end-of-string
    # Ex: somestring='this is some string rec' => somestring = removeLastOccurenceOfSubString(somestring, ' rec') -> somestring='this is some string'
    @staticmethod
    def removeLastOccurenceOfSubString(thestring, ending):
        """Remove last occurence of subString in a string. Ex: somestring='this is some string rec' => somestring = removeLastOccurenceOfSubString(somestring, ' rec') -> somestring='this is some string'

        Args:
            thestring (str): The string where we want to remove the last occurence of the substring named ending.
            ending (str): The substring that we want to remove the last occurence in thestring.

        Returns:
            str: The string without the last occurence of ending.

        Examples:

            >>> print(SysTools.removeLastOccurenceOfSubString("this is some string rec", " rec"))
            this is some string

        """
        if thestring.endswith(ending):
            return thestring[:-len(ending)]
        return thestring


    # Ex: getPathLessPath_leaf("../../outputGraph/SimpleTestOutput") = "../../outputGraph/"
    @staticmethod
    def getPathLessPath_leaf(path):
        """Get leaf of path. Ex: getPathLessPath_leaf("../../outputGraph/SimpleTestOutput") = "../../outputGraph/"

        Args:
            path (str): The path we want to remove the leaf.

        Returns:
            str: The path without the leaf.

        Examples:

            >>> print(SysTools.getPathLessPath_leaf("../../outputGraph/SimpleTestOutput"))
            ../../outputGraph/

        """
        # Get leaf of path.
        path_leaf = SysTools.path_leaf(path)
        # Remove the leaf of path from the path.
        pathLessPath_leaf = SysTools.removeLastOccurenceOfSubString(path, path_leaf)
        # Return the path less the leaf of path.
        return pathLessPath_leaf

    
    # Check if file exist in the given path.
    @staticmethod
    def checkIfFileExist(pathOfFile):
        """Check if file exist in the given path. If not, print error and exit.

        Args:
            pathOfFile (str): The path of the file we want to test the existance.

        """
        # Check if the file exist at the given pathOfFile. If not, print error and exit.
        try:
            inputFile = open(str(pathOfFile), 'r')
            return True
        except EnvironmentError as e:      # OSError or IOError...
            # Input file doesn't exist. Print a warning and exit.
            CustomPrint.warningPrint("Warning: the input file " + str(pathOfFile) + " doesn't exist.")
            CustomPrint.warningPrint(os.strerror(e.errno))
            #sys.exit(1)
            return False


    # Check if file exist in the given path.
    @staticmethod
    def checkIfFileExistAndCreateItIfNotExist(pathOfFile):
        """Check if file exist in the given path. If not, create it.

        Args:
            pathOfFile (str): The path of the file we want to test the existance.

        """
        # Check if the file exist at the given pathOfFile. If not, print error and exit.
        try:
            inputFile = open(str(pathOfFile), 'r')
        except EnvironmentError as e:      # OSError or IOError...
            # Create the file.
            open(pathOfFile, 'w+')

    # Check if folder exist at the given path. If the folder doesn't exist, create it if the user want to.
    @staticmethod
    def checkIfDirExist(pathOfDir, createDirIfNotExist=False, askConfirmationBeforeCreateDir=True):
        """Check if folder exist at the given path. If the folder doesn't exist, create it if the user want to.

        Args:
            pathOfDir (str): The path of the directory we want to test the existance.
            createDirIfNotExist (bool, optional): Boolean to know if the function must create the folder in case the folder does not exist.
            askConfirmationBeforeCreateDir (bool, optional): Boolean to know if the function must ask a confirmation to create the folder in case the folder does not exist.

        Returns:
            bool: True if the directory exist, False otherwise.
                ...

        """
        # Check if the directory exist.
        isDirExist = os.path.isdir(pathOfDir)
        # If the directory not exist...
        if(not isDirExist):
            # If we want to create the directory if the directory not exist.
            if(createDirIfNotExist):
                # if the user doesn't want to be ask a confirmation before create the directory...
                if(not askConfirmationBeforeCreateDir):
                    # Create the directory.
                    os.mkdir(pathOfDir)
                    # Check if the directory exist after the creation.
                    isDirExist = os.path.isdir(pathOfDir)
                # Else, if the user want to be ask a confirmation before create the directory, ask the confirmation before create the directory.
                else:
                    confirmationString = "The path: " + str(pathOfDir) + " don't exist and you are about to create it. Are you sure you want to create the directory " + str(pathOfDir) + "?"
                    # If the user say yes to create the directory, create the directory.
                    if(SysTools.askConfirmation(confirmationString, "no")):
                        # Create the directory.
                        os.mkdir(pathOfDir)
                        # Check if the directory exist after the creation.
                        isDirExist = os.path.isdir(pathOfDir)

        # Return the boolean to tell if the directory exist or not.
        return isDirExist


    @staticmethod
    def removeAllFileAndSubFolderInDirectory(pathOfDir, createDirIfNotExist=False, askConfirmationBeforeCreateDir=True):
        # Check if Directory exist or not.
        isDirExist = SysTools.checkIfDirExist(pathOfDir, createDirIfNotExist, askConfirmationBeforeCreateDir)
        # If folder pathOfDir exist, rm all files and subfolder in this directory
        if(isDirExist):
            # rm all files and subfolder in html/ directory.
            # see: https://stackoverflow.com/questions/185936/how-to-delete-the-contents-of-a-folder-in-python
            for the_file in os.listdir(pathOfDir):
                file_path = os.path.join(pathOfDir, the_file)
                try:
                    # rm file in pathOfDir directory.
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                    # rm subfolder in pathOfDir directory.
                    elif os.path.isdir(file_path): shutil.rmtree(file_path) 
                except Exception as e:
                    print(e)

        return isDirExist



    @staticmethod
    def removeFileIfExist(filePath):
    
        # Python 2.x: define [FileNotFoundError] exception if it doesn't exist 
        try:
            FileNotFoundError
        except NameError:
            FileNotFoundError = IOError

        # Handle errors while calling os.remove()
        try:
            # As file at filePath is deleted now, so we should check if file exists or not before deleting them
            if os.path.exists(filePath):
                # Remove a file
                os.remove(filePath)
            else:
                CustomPrint.warningPrint("Can not delete the file " + str(filePath) + " as it doesn't exists")
        except:
            CustomPrint.errorPrint("Error while deleting file " + str(filePath))
            traceback.print_exc()
     
       

    # A custom function to execute an external command and get its exitcode, stdout (output of the command) and stderr (error of the command).
    @staticmethod
    def execute_command(cmd):
        """Execute the external command and get its exitcode, stdout (output of the command) and stderr (error of the command).

        Args:
            cmd (str): The command line command the user want to execute (ls, cd , ...).
        
        Returns:
            bool: exit code, output and errors of the command.

        """
        # Split the command (shlex.split() determining the correct tokenization for command args, especially in complex cases).
        args = shlex.split(cmd)

        # Execute the command (asynchronously i.e. doesn't freeze the program.
        # Command injection is prevented because shell=False in Popen (implicitly).
        proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        # Print output of shell in real time.
        while True:
            output = proc.stdout.readline()
            if(str(output, 'utf-8') == "" and proc.poll() is not None):
                break
            if output:
                print(str(output.strip(), 'utf-8'))

        rc = proc.poll()

        # Retrieve eventual output of the command in stdout and the eventual errors of the command in stderr.
        stdout,stderr = proc.communicate()

        # Retrieve the exit code of the command. Return 0 if OK.
        exitcode = proc.returncode

        # Return exit code, output and errors of the command.
        return (exitcode, stdout, stderr, rc)


    @staticmethod
    def openWithBrowser(url):
        """Open an url in the default web browser.

        Args:
            url (str): The url we want to open in web browser.

        Returns:
            bool: True if successful, False otherwise.

        """
        # Open the url in a web browser.
        try:
            webbrowser.open(str(url))
            return True
        # If exection is raise, exit.
        except:
            sys.exit(1)
            return False


    @staticmethod
    def get_class( kls ):
        """Construct an object from the name of the class in argument.
        https://stackoverflow.com/questions/452969/does-python-have-an-equivalent-to-java-class-forname

        Args:
            kls (str): String with the full name of the class to instanciate (example: beholder.classes.graphRepresentation.strategyNodes.ColorStrategy.ColorNodeStrategy4).

        Returns:
            bool: An object instance from the class name specify in parameter.

        """
        # Example of parameter kls: beholder.classes.graphRepresentation.strategyNodes.ColorStrategy.ColorNodeStrategy4
        # We split kls with the "." separator to obtain parts = [beholder, classes, graphRepresentation, strategyNodes, ColorStrategy, ColorNodeStrategy4]
        parts = kls.split('.')
        # Compute the module. For that, select all elements of parts except the last one. So: module = beholder.classes.graphRepresentation.strategyNodes.ColorStrategy
        module = ".".join(parts[:-1])
        try:
            # Import the module previously computed. So import beholder.classes.graphRepresentation.strategyNodes.ColorStrategy module.
            m = __import__( module )
        except Exception:
            CustomPrint.errorPrint("Error in " + str(sys._getframe().f_code.co_name))
            traceback.print_exc()
            sys.exit(1)
        # For all the elements of parts except the first one (ie for all the following elements: [classes, graphRepresentation, strategyNodes, ColorStrategy, ColorNodeStrategy4])
        for comp in parts[1:]:
            # Construct the module during the loop. Ie, at first loop, construct module classes, then module classes.graphRepresentation, then ..., and finaly <class 'beholder.classes.graphRepresentation.strategyNodes.ColorStrategy.ColorNodeStrategy4'>.
            m = getattr(m, comp)        
        
        # Return object. Example return object of type <class 'beholder.classes.graphRepresentation.strategyNodes.ColorStrategy.ColorNodeStrategy4'>.
        return m()


