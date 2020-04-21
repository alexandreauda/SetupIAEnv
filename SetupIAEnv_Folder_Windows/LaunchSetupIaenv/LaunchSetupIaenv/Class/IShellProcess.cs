using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CSRNET_GUI
{
    interface IShellProcess
    {
        #region ATTRIBUTES
        /****************** ATTRIBUTES ******************/
        string WorkingDirectory { get; set; }
        string Command { get; set; }
        bool UseOSShell { get; set; }
        bool CreateNoWindow { get; set; }
        bool CloseShellAfterExecuted { get; set; }
        bool FullScreen { get; set; }
        #endregion

        #region METHODS
        /****************** METHODS ******************/
        void executeCommand();
        void executeCommand(string command);
        void executeCommand(string workingDirectory, string command);
        #endregion
    }
}
