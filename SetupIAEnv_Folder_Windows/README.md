# SetupIAEnv_Folder_Windows

This project aims to install all packages required to perform machine learning and artificial intelligence on Windows.

To do this, go in the folder you want to put the project, and clone the project (for instance in \MachineLearningProject).

Then run the `InstallAnaconda.bat` by double clicking on the .bat file in the folder. 

This will check if Anaconda is installed. If not, this bat will downloaded the Anaconda installer (if not already present) and will let you install Anaconda3. This will also change your path to be able to run conda from command-line.

Then open Anaconda:

![alt text](https://github.com/alexandreauda/SetupIAEnv/blob/master/SetupIAEnv_Folder_Windows/ImageForReadme/ImageForReadme_1.png)

Click on the "Environment" tab on the left panel:

![alt text](https://github.com/alexandreauda/SetupIAEnv/blob/master/SetupIAEnv_Folder_Windows/ImageForReadme/ImageForReadme_2.PNG)

Finally, execute the .bat you want (with or without gpu support): `SetupIAEnv.bat` (for only CPU Support on Tensorflow) or `SetupIAEnv_gpu.bat` (for GPU Support on Tensorflow).

The script will create the virtual env iaenv in Anaconda3 with all the packages useful for the machine learning and artificial intelligence.



