# SetupIAEnv_Folder_Windows

This project aims to install all packages required to perform machine learning and artificial intelligence on Windows.

To do this, go in the folder you want to put the project, and clone the project (for instance in \MachineLearningProject).

Then run the `InstallAnaconda.bat`. 

This will check if Anaconda is installed. If not, this bat will downloaded the Anaconda installer (if not already present) and will let you install Anaconda3. This will also change your path to be able to run conda from command-line.

Finally, execute the .bat you want (with or without gpu support): `SetupIAEnv_gpu.bat` or `SetupIAEnv_gpu.bat`.

The script will create the virtual env iaenv in Anaconda3 with all the packages useful for the machine learning and artificial intelligence.


