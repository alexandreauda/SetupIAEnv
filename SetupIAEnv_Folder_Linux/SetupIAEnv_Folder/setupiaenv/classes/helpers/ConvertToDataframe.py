#!/usr/bin/python -u
# coding=utf-8

# Python 2
# Encoding: utf-8

""" Imports """
# General imports.
import sys
import os
import errno
import traceback

# Load the Pandas libraries with alias 'pd' 
import pandas as pd 

import json
from pandas.io.json import json_normalize

# Custom class to print errors, warnings, ...
from setupiaenv.classes.helpers.CustomPrint import CustomPrint
# Custom class that provide various sys static functions.
from setupiaenv.classes.helpers.SysTools import SysTools

class ConvertToDataframe:
    """Class to convert data in various format (json, csv, ...) in pandas dataframe.
    
    """

    # ******Static methods******

    # Read a file in json and convert it to a pandas dataframe.
    @staticmethod
    def jsonToDataframe(jsonFileNameToRead, DebugLevel=0):
        """Read a file in json and convert it to a pandas dataframe.

        Args:
            jsonFileNameToRead (str): The json file that contain the data to convert in dataframe.
            DebugLevel (int): The Debug Level.

        Returns:
            Pandas dataframe: The dataframe representation of the json data.

        """
        # Check if the jsonFileNameToRead exist. If not, print error and exit.
        SysTools.checkIfFileExist(jsonFileNameToRead)
        # Declare an empty dataframe.
        df_json = pd.DataFrame()
        # Open the json file.
        with open(str(jsonFileNameToRead)) as f :
            if(DebugLevel):
                print("\nReading the json: " + str(jsonFileNameToRead) + "...")
            # Load the json data (but that data is not normalize that is can contain nested list and so on).
            data = json.load(f)
            if(DebugLevel):
                print("\nNo json_normalization: " + str(data) + "\n\n")
            # Normalize the data to delete nested list in data and so on.
            data_normalized = json_normalize(data['results'])
            if(DebugLevel):
                print("json_normalization: \n" + str(data_normalized))
            # Initialize the dataframe with the normalize data from the json file.
            df_json = pd.DataFrame(data_normalized)
            # Close the json file.
            f.close()
        # Return the dataframe that contain the json data.
        return df_json


    # Read a file in csv and convert it to a pandas dataframe.
    @staticmethod
    def csvToDataframe(csvFileNameToRead, DebugLevel=0):
        """Read a file in csv and convert it to a pandas dataframe.

        Args:
            csvFileNameToRead (str): The csv file that contain the data to convert in dataframe.
            DebugLevel (int): The Debug Level.

        Returns:
            Pandas dataframe: The dataframe representation of the csv data.

        """
        # Check if the csvFileNameToRead exist. If not, print error and exit.
        SysTools.checkIfFileExist(csvFileNameToRead)
        if(DebugLevel):
            print("\nReading the csv: " + str(csvFileNameToRead) + "...")
        # Use the read_csv() method from Panda to put the csv in a dataframe.
        df = pd.read_csv(csvFileNameToRead)
        if(DebugLevel):
            print("Convert csv to dataframe: Done!")
        # Return the dataframe that contain the csv data.
        return df


    # Read a file in universal format and convert it to a pandas dataframe.
    @staticmethod
    def dataToDataframe(args, information_icon = CustomPrint.highlight('[*]', 'blue'), success_icon = CustomPrint.highlight('[+]', 'green')):
        """Read a file in universal format and convert it to a pandas dataframe.

        Args:
            args (argparse object): The argparse object that contains all the arguments given by the user in the Cli.
            DebugLevel (int): The Debug Level.

        Returns:
            Pandas dataframe: The dataframe representation of the data.

        """
        # ******If the input file is a .json file, we convert the data of that json in a dataframe with jsonToDataframe() function.******
        if(hasattr(args, 'input') and hasattr(args, 'debug')):
            # If the input file is a json file...
            if(".json" in str(SysTools.path_leaf(args.input))):
                if(args.debug) :
                    print("\n***********************JSON TO DATAFRAME***********************")
                if(args.debug) :
                    print("\n" + information_icon + " Convert json to dataframe...")
                # Convert json (contained in the input file) to dataframe.
                df = ConvertToDataframe.jsonToDataframe(str(args.input))

                # Check all graph arguments (i.e.: -s, -dest, -ea, -isdir, -w and -l).
                #CliManagementBeholder.checkGraphArguments(args, df) 
                
                if(args.debug) :
                    print(success_icon + " Convert json to dataframe: done!\n")
                if(args.debug) :
                    print("Print the dataframe (from normalized json):")
                    print(df)

                return df

            # ******If the input file is a .csv file, we convert the data of that json in a dataframe with csvToDataframe() function.******
            # If the input file is a csv file...
            elif(".csv" in str(SysTools.path_leaf(args.input))):
                if(args.debug) :
                    print("\n***********************CSV TO DATAFRAME***********************")
                if(args.debug) :
                    print("\n" + information_icon + " Convert csv to dataframe...")
                # Convert csv to dataframe
                df = ConvertToDataframe.csvToDataframe(str(args.input))

                # Check all graph arguments (i.e.: -s, -dest, -ea, -isdir, -w and -l).
                #CliManagementBeholder.checkGraphArguments(args, df)
                
                if(args.debug) :
                    print(success_icon + " Convert csv to dataframe: done!\n")
                if(args.debug) :
                    print("Print the dataframe:")
                    print(df)
                return df
            # If the input file is none of the previous type, throw an error and exit.
            else:
                CustomPrint.errorPrint("Error: the support format for the input string are: 'atom', 'csv', 'json', 'json_rows', 'raw' and 'xml'. Therefore the file extension of the input file should be one of these.")
                sys.exit(1)
        else:
            CustomPrint.errorPrint("Error: the parameter args in " + str(sys._getframe().f_code.co_name) + " must have input and debug as attributes.")
            #traceback.print_exc()
            sys.exit(1)



    @staticmethod
    def cleanDataframe(dataframe, args, information_icon = CustomPrint.highlight('[*]', 'blue'), success_icon = CustomPrint.highlight('[+]', 'green')):
        """Remove rows with null value in the source and destination columns.

        Args:
            dataframe (Pandas dataframe): the pandas dataframe to clean.
            args (argparse object): argparse object.
            information_icon (str, optional): string to mark the begining of a task.
            success_icon (str, optional): string to mark the success of a task.

        Returns:
            Pandas dataframe: The cleaned dataframe.

        """
        if(hasattr(args, 'source') and hasattr(args, 'debug') and hasattr(args, 'arguments') and hasattr(args, 'destination')):
            # Check validity of -s argument.
            # If args.source is not a column name, throw an error.
            if(str(args.source) not in dataframe.columns):
                CustomPrint.errorPrint("Error: source argument must be a column name.\nShould be one of the following: " + str(dataframe.columns))
                sys.exit(1)
            # If the debug level is greater or equal to 1 or if -a option is provided, print debug/arguments information.
            if (args.debug or args.arguments):
                print("Value of the destination argument: " + str(args.destination))
            # Check validity of -dest argument.
            # If args.destination is not a column name, throw an error.
            if(str(args.destination) not in dataframe.columns):
                CustomPrint.errorPrint("Error: destination argument must be a column name.\nShould be one of the following: " + str(dataframe.columns))
                sys.exit(1)
            # If column source and destination are the same, throw an error.
            if(str(args.source) == str(args.destination)):
                CustomPrint.errorPrint("Error: source and destination argument must be different.")
                sys.exit(1)

            # Copy the dataframe because we don't want to modify the original dataframe.
            df = dataframe.copy()

            if(args.debug) :
                    print("\n" + information_icon + " Cleaning dataframe: Remove rows with null value in the source and destination columns...")

            # Remove rows with null value in the source column.
            df = df[pd.notnull(df[str(args.source)])]
            # Remove rows with null value in the destination column.
            df = df[pd.notnull(df[str(args.destination)])]

            if(args.debug) :
                    print(success_icon + " Cleaning dataframe: Remove rows with null value in the source and destination columns: done!\n")

            # Return the cleaned dataframe.
            return df
        else:
            CustomPrint.errorPrint("Error: the parameter args in " + str(sys._getframe().f_code.co_name) + " must have source, debug, arguments and destination as attributes.")
            #traceback.print_exc()
            sys.exit(1)

