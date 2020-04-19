using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CSRNET_GUI
{
    class CMDShell : IShellProcess
    {
        #region ATTRIBUTES
        /****************** ATTRIBUTES + GETTERS & SETTERS ******************/
        // Define where the commands will be run (in which directory).
        private string workingDirectory;
        // Specify the commands we want to execute in cmd.
        public string Command { get; set; }
        // Use the OS shell or the shell from C#. As we need to launch bat/ps1 files and use OS command like conda, we will use the OS shell. Important! See: https://stackoverflow.com/questions/5255086/when-do-we-need-to-set-useshellexecute-to-true
        public bool UseOSShell { get; set; }
        // Tell if we show the cmd window or not.
        public bool CreateNoWindow { get; set; }
        // Specify if we want to close cmd window after the execution of the commands.
        public bool CloseShellAfterExecuted { get; set; }
        // Define constants that represent cmd options to close cmd window after the execution of the commands or not.
        private const string cmdOptionKeepCMDOpenAfterExecution = "/k";
        private const string cmdOptionCloseCMDAfterExecution = "/c";
        // Specify if we want to launch cmd window in full screen or not.
        public bool FullScreen { get; set; }
        
        // Readonly attribute to specify the path of the processToLaunch ie cmd.exe.
        private readonly string processToLaunch;

        #endregion

        #region CONSTRUCTORS
        /****************** CONSTRUCTORS ******************/
        #region PARAMETERS_CONSTRUCTORS
        public CMDShell(string workingDirectory, string command, bool useOSShell = true, bool fullScreen = true, bool createNoWindow = false, bool closeCMDAfterExecuted = false)
        {
            // Define the path of the process to launch. In our case, it is the path of cmd.exe.
            this.processToLaunch = Path.Combine(Environment.SystemDirectory, "cmd.exe");
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
            // Specify the commands we want to execute in cmd.
            this.Command = command;
            // Use the OS shell or the shell from C#. As we need to launch bat/ps1 files and use OS command like conda, we will use the OS shell. Important! See: https://stackoverflow.com/questions/5255086/when-do-we-need-to-set-useshellexecute-to-true
            this.UseOSShell = useOSShell;
            // Specify if we launch the cmd window in full screen or not.
            this.FullScreen = fullScreen;
            // Tell if we show the cmd window that will run the commands or not.
            this.CreateNoWindow = createNoWindow;
            // Tell if we want to close the cmd window after the execution of all the commands or not.
            this.CloseShellAfterExecuted = closeCMDAfterExecuted;
        }
        #endregion


        #region DEFAULT_CONSTRUCTORS
        // Use parameters constructors to create default constructor.
        public CMDShell() : this(Environment.GetFolderPath(Environment.SpecialFolder.UserProfile), "")
        {
        }
        #endregion

        #endregion



        #region GETTERS_SETTERS
        /****************** GETTER & SETTERS ******************/
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
            // Method to launch the cmd.exe process and execute a command in it.

            // Don't close the cmd after execution.
            string cmdOption = cmdOptionKeepCMDOpenAfterExecution;
            // If we want to close the cmd after execution...
            if (CloseShellAfterExecuted)
            {
                // Close the cmd after execution.
                cmdOption = cmdOptionCloseCMDAfterExecution;
            }

            // Create a ProcessStartInfo to specify the options of our process.
            ProcessStartInfo startInfo = new ProcessStartInfo();
            // Define where the commands will be run (in which directory).
            startInfo.WorkingDirectory = p_workingDirectory;
            // Define the filename of the process we want to launch. In our case, it is cmd.exe.
            startInfo.FileName = processToLaunch;
            // Specify the commands we want to execute in cmd.
            startInfo.Arguments = cmdOption + " " + p_command;
            // Tell if we show the cmd window or not.
            startInfo.CreateNoWindow = CreateNoWindow;
            // Use the OS shell or the shell from C#. As we need to launch bat/ps1 files and use OS command like conda, we will use the OS shell. Important! See: https://stackoverflow.com/questions/5255086/when-do-we-need-to-set-useshellexecute-to-true
            startInfo.UseShellExecute = UseOSShell;
            // If we want the cmd in full screen...
            if (FullScreen)
            {
                // Put the cmd window in full screen.
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
