using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CSRNET_GUI
{
    class PowerShellShell : IShellProcess
    {
        #region ATTRIBUTES
        /****************** ATTRIBUTES + GETTERS & SETTERS ******************/
        // Define where the commands will be run (in which directory).
        private string workingDirectory;
        // Specify the commands we want to execute in PowerShell.
        public string Command { get; set; }
        // Use the OS shell or the shell from C#. As we need to launch bat/ps1 files and use OS command like conda, we will use the OS shell. Important! See: https://stackoverflow.com/questions/5255086/when-do-we-need-to-set-useshellexecute-to-true
        public bool UseOSShell { get; set; }
        // Tell if we show the PowerShell window or not.
        public bool CreateNoWindow { get; set; }
        // Specify if we want to close PowerShell window after the execution of the commands.
        public bool CloseShellAfterExecuted { get; set; }
        // Define constants that represent PowerShell options to close PowerShell window after the execution of the commands or not.
        private const string PowerShellOptionKeepPowerShellOpenAfterExecution = "-noexit";
        private const string PowerShellOptionClosePowerShellAfterExecution = "";
        // Specify if we want to launch cmd window in full screen or not.
        public bool FullScreen { get; set; }

        // Readonly attribute to specify the path of the processToLaunch ie powershell.exe.
        private readonly string processToLaunch;

        #endregion

        #region CONSTRUCTORS
        /****************** CONSTRUCTORS ******************/
        #region PARAMETERS_CONSTRUCTORS
        public PowerShellShell(string workingDirectory, string command, bool useOSShell = true, bool fullScreen = true, bool createNoWindow = false, bool closePowerShellAfterExecuted = false)
        {
            // Define the path of the process to launch. In our case, it is the path of powershell.exe.
            this.processToLaunch = "powershell.exe";
            // Define where the commands will be run (in which directory). Assign the specify working directory only if it is an existing directory. Else, throw an exeption.
            if (System.IO.Directory.Exists(workingDirectory))
            {
                this.workingDirectory = workingDirectory;
            }
            else
            {
                throw new DirectoryNotFoundException();
            }
            // Assign other parameters.
            // Specify the commands we want to execute in PowerShell.
            this.Command = command;
            // Use the OS shell or the shell from C#. As we need to launch bat/ps1 files and use OS command like conda, we will use the OS shell. Important! See: https://stackoverflow.com/questions/5255086/when-do-we-need-to-set-useshellexecute-to-true
            this.UseOSShell = useOSShell;
            // Specify if we launch the PowerShell window in full screen or not.
            this.FullScreen = fullScreen;
            // Tell if we show the PowerShell window that will run the commands or not.
            this.CreateNoWindow = createNoWindow;
            // Tell if we want to close the PowerShell window after the execution of all the commands or not.
            this.CloseShellAfterExecuted = closePowerShellAfterExecuted;
        }
        #endregion

        #region DEFAULT_CONSTRUCTORS
        // Use parameters constructors to create default constructor.
        public PowerShellShell() : this(Environment.GetFolderPath(Environment.SpecialFolder.UserProfile), "")
        {
        }
        #endregion

        #endregion



        #region GETTERS_SETTERS
        /****************** GETTER & SETTERS******************/
        //Get and Set the attribute workingDirectory.
        public string WorkingDirectory
        {
            // Getter.
            get
            {
                return workingDirectory;
            }
            // Setter.
            set
            {
                // Set directory where the commands will be run (in which directory). Assign the specify working directory only if it is an existing directory. Else, throw an exeption.
                if (System.IO.Directory.Exists(value))
                {
                    workingDirectory = value;
                }
                else
                {
                    throw new DirectoryNotFoundException();
                }
            }
        }

        #endregion


        #region METHODS
        /****************** METHODS ******************/

        public void executeCommand()
        {
            // Method to launch the cmd.exe process and execute a command in it.
            executeCommand(workingDirectory, Command);
        }

        public void executeCommand(string p_command)
        {
            // Method to launch the cmd.exe process and execute a command in it.
            executeCommand(workingDirectory, p_command);
        }

        public void executeCommand(string p_workingDirectory, string p_command)
        {
            // Method to launch the powershell.exe process and execute a command in it.

            // Don't close the PowerShell after execution.
            string powershellOption = PowerShellOptionKeepPowerShellOpenAfterExecution;
            // If we want to close the PowerShell after execution...
            if (CloseShellAfterExecuted)
            {
                // Close the cmd after execution.
                powershellOption = PowerShellOptionClosePowerShellAfterExecution;
            }

            // Create a ProcessStartInfo to specify the options of our process.
            ProcessStartInfo startInfo = new ProcessStartInfo();
            // Define where the commands will be run (in which directory).
            startInfo.WorkingDirectory = p_workingDirectory;
            // Define the filename of the process we want to launch. In our case, it is powershell.exe.
            startInfo.FileName = processToLaunch;
            // Specify the commands we want to execute in PowerShell with the options.
            startInfo.Arguments = powershellOption + " " + p_command;
            // Tell if we show the PowerShell window or not.
            startInfo.CreateNoWindow = CreateNoWindow;
            // Use the OS shell or the shell from C#. As we need to launch bat/ps1 files and use OS command like conda, we will use the OS shell. Important! See: https://stackoverflow.com/questions/5255086/when-do-we-need-to-set-useshellexecute-to-true
            startInfo.UseShellExecute = UseOSShell;
            // If we want the PowerShell in full screen...
            if (FullScreen)
            {
                // Put the PowerShell window in full screen.
                startInfo.WindowStyle = ProcessWindowStyle.Maximized;
            }

            // Define a process.
            Process process = new Process();
            // Pass to the process our options.
            process.StartInfo = startInfo;

            // Start the process.
            process.Start();

            // Wait for exit to have time to print exit code.
            process.WaitForExit();
            //Console.WriteLine("ExitCode: {0}", process.ExitCode);

            // Close the process.
            process.Close();
        }
        #endregion
    }
}
