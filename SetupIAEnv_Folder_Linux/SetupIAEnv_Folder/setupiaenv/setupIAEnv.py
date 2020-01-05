#!/usr/bin/python -u
# coding=utf-8

# Python 2
# Encoding: utf-8

""" Import for error handling. """
from __future__ import print_function

""" Import all the general packages useful. """
# General packages.
import os.path

import sys

""" Import all the custom classes."""
# Custom class to manage cli parsers.
from setupiaenv.cli import CliManagementSetupIAEnv

# Custom class to print errors, warnings, ...
from setupiaenv.classes.helpers.CustomPrint import CustomPrint

# Custom class that provide various sys static functions.
from setupiaenv.classes.helpers.SysTools import SysTools


""" Implementation of custom functions."""


def main():
    """Main entry point of the splunkQuery application.

    """

    # ***********************************************************************************************************************************************************************************************************
    # Meta-data of the script. 
    
    # Get the name of the script.
    progName = os.path.basename(__file__) 
    THIS_PATH = os.path.realpath(__file__)
    THIS_DIR = SysTools.getPathLessPath_leaf(THIS_PATH)

    # print(THIS_PATH)
    # print(THIS_DIR)
    # print(progName)

    machine_type = os.uname().machine
    # print(machine_type)

    sysname = os.uname().sysname
    # print(sysname)

    # Constant variables.
    # When start a task, add [*] icon in blue.
    information_icon = CustomPrint.highlight('[*]', 'blue')
    # When finished a task, add [+] icon in green.
    success_icon = CustomPrint.highlight('[+]', 'green')

    # ***********************************************************************************************************************************************************************************************************
    # Management of the parameters to give and given to the script. 
    
    # Parse cli arguments.
    args = CliManagementSetupIAEnv.gen_cli_args(str(progName))

    # Check if misc [option] is used. If it is the case, perform the operation and exit.
    CliManagementSetupIAEnv.checkIfMiscArguments(args)

    # ***********************************************************************************************************************************************************************************************************

    # If not force, allows to print warnings.
    if(not args.force):
        # Check if the script is executed on a 64-bits system. 
        if(machine_type!="x86_64"):
            CustomPrint.warningPrint("WARNING:\n")
            CustomPrint.warningPrint("    Your operating system appears not to be 64-bit, but you are trying to\n")
            CustomPrint.warningPrint("    install a 64-bit version of SetupIAEnv.\n")
            answer1 = SysTools.askConfirmation("    Are sure you want to continue the installation? \n", default="no")
            if(not answer1):
                CustomPrint.warningPrint("Aborting installation\n")
                sys.exit(0)

        # Check if the script is executed on a 64-bits system. 
        if(sysname!="Linux"):
            CustomPrint.warningPrint("WARNING:\n")
            CustomPrint.warningPrint("    Your operating system does not appear to be Linux, \n")
            CustomPrint.warningPrint("    but you are trying to install a Linux version of SetupIAEnv.\n")
            answer2 = SysTools.askConfirmation("    Are sure you want to continue the installation? \n", default="no")
            if(not answer2):
                CustomPrint.warningPrint("Aborting installation\n")
                sys.exit(0)


        print("\n")
        print("Welcome to SetupIAEnv 1.0.0\n")

    # Give execution rights to the installation script.
    (exitcode0, stdout0, stderr0, rc0) = SysTools.execute_command("chmod +x data/SetupIAEnv.sh")

    # If in batch mode, pass the batch argument to the script.
    if(args.batch):
        # If we want to install Anaconda, pass the anaconda argument to the script.
        if(args.anaconda):
            # Run with bash -i because of this issue: https://stackoverflow.com/questions/55507519/python-activate-conda-env-through-shell-script
            (exitcode1, stdout1, stderr1, rc1) = SysTools.execute_command("bash -i data/SetupIAEnv.sh batch anaconda " + str(args.condaEnvName) + " " + str(args.gpuTensorflow) + " " + str(args.installSystem))
        # If we doesn't want to install Anaconda, pass the noAnaconda argument to the script.
        else:
            # Run with bash -i because of this issue: https://stackoverflow.com/questions/55507519/python-activate-conda-env-through-shell-script
            (exitcode1, stdout1, stderr1, rc1) = SysTools.execute_command("bash -i data/SetupIAEnv.sh batch NoAnaconda" + str(args.condaEnvName) + " " + str(args.gpuTensorflow) + " " + str(args.installSystem))
    # If not in batch mode, pass the noBatch argument to the script.
    else:
        # If we want to install Anaconda, pass the anaconda argument to the script.
        if(args.anaconda):
            # Run with bash -i because of this issue: https://stackoverflow.com/questions/55507519/python-activate-conda-env-through-shell-script
            (exitcode1, stdout1, stderr1, rc1) = SysTools.execute_command("bash -i data/SetupIAEnv.sh noBatch anaconda" + str(args.condaEnvName) + " " + str(args.gpuTensorflow) + " " + str(args.installSystem))
        # If we doesn't want to install Anaconda, pass the noAnaconda argument to the script.
        else:
            # Run with bash -i because of this issue: https://stackoverflow.com/questions/55507519/python-activate-conda-env-through-shell-script
            (exitcode1, stdout1, stderr1, rc1) = SysTools.execute_command("bash -i data/SetupIAEnv.sh noBatch NoAnaconda" + str(args.condaEnvName) + " " + str(args.gpuTensorflow) + " " + str(args.installSystem))






if __name__== "__main__":
    # Call the main method.
    main()

