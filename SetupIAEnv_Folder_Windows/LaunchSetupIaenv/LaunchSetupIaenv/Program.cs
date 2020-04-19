using CSRNET_GUI;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LaunchSetupIaenv
{
    class Program
    {
        static void Main(string[] args)
        {
            IShellProcess Shell = new CMDShell();
            // Get location of the current process (ie the GUI .exe) and find from here the location of the scripts bat and ps1 that are the connectors between GUI and CLI.
            string currentProcessPath = Path.GetDirectoryName(Process.GetCurrentProcess().MainModule.FileName);
            string directoryName = string.Empty;
            // Perform 6 times the GetDirectoryName() method.
            for (int i = 0; i < 6; i++)
            {
                directoryName = Path.GetDirectoryName(currentProcessPath);
                currentProcessPath = directoryName;
                if (i == 1)
                {
                    currentProcessPath = directoryName + @"\";  // This will preserve the previous path.
                }
            }

        
            // Check if the full path exists or not. If not, throw an error.
            if (!System.IO.Directory.Exists(directoryName))
            {
                throw new DirectoryNotFoundException();
            }
            Shell.executeCommand(directoryName, "SetupIAEnv.bat");
        }
    }
}
