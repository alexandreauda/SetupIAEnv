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
            for (int i = 0; i < 4; i++)
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
            // Run the bat that download and install Anaconda if not present.
            Shell.executeCommand(Path.Combine(directoryName,"Ressources"), "InstallAnaconda.bat");
            // Ajout de Anaconda au path pour pouvoir utiliser conda dans un cmd/PowerShell, s'il n'est pas déjà présent.
            // Il peut en effet être déjà présent car une autre solution pour ajouter Anaconda au path est de le spécifier dans l'installation (ne pas faire attention au warning).
            Shell.executeCommand(directoryName, "echo Add Anaconda to PATH... & path|find /i \";%USERPROFILE%\\anaconda3;%USERPROFILE%\\anaconda3\\Library\\mingw - w64\\bin;%USERPROFILE%\\anaconda3\\Library\\usr\\bin;%USERPROFILE%\\anaconda3\\Library\\bin;%USERPROFILE%\\anaconda3\\Scripts;\">nul || setx path \"%path%;%USERPROFILE%\\anaconda3;%USERPROFILE%\\anaconda3\\Library\\mingw - w64\\bin;%USERPROFILE%\\anaconda3\\Library\\usr\\bin;%USERPROFILE%\\anaconda3\\Library\\bin;%USERPROFILE%\\anaconda3\\Scripts;\"");
            //Shell.executeCommand(directoryName, "SetupIAEnv.bat");
        }
    }
}
