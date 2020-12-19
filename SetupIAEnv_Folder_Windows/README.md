# SetupIAEnv_Folder_Windows

This project aims to install all packages required to perform machine learning and artificial intelligence on Windows.

To do this, go in the folder you want to put the project, and clone the project (for instance in \MachineLearningProject).

Then run the `InstallAnaconda.bat` by double clicking on the .bat file in the folder. 

This will check if Anaconda is installed. If not, this bat will downloaded the Anaconda installer (if not already present) and will let you install Anaconda3. This will also change your path to be able to run conda from command-line.

Then open Anaconda:

![alt text](https://github.com/alexandreauda/SetupIAEnv/blob/master/SetupIAEnv_Folder_Windows/ImageForReadme/ImageForReadme_1.png)

Click on the "Environment" tab on the left panel:

![alt text](https://github.com/alexandreauda/SetupIAEnv/blob/master/SetupIAEnv_Folder_Windows/ImageForReadme/ImageForReadme_2.PNG)

![alt text](https://github.com/alexandreauda/SetupIAEnv/blob/master/SetupIAEnv_Folder_Windows/ImageForReadme/ImageForReadme_3.PNG)

Now left click on the green arrow next to the `Base (Root)` environment and left click on the `Open Terminal` tab:

![alt text](https://github.com/alexandreauda/SetupIAEnv/blob/master/SetupIAEnv_Folder_Windows/ImageForReadme/ImageForReadme_4.PNG)

![alt text](https://github.com/alexandreauda/SetupIAEnv/blob/master/SetupIAEnv_Folder_Windows/ImageForReadme/ImageForReadme_5.PNG)

A console terminal should then open:

![alt text](https://github.com/alexandreauda/SetupIAEnv/blob/master/SetupIAEnv_Folder_Windows/ImageForReadme/ImageForReadme_6.png)

Now, navigate to the folder where the .bat files are located in SetupIAEnv:

![alt text](https://github.com/alexandreauda/SetupIAEnv/blob/master/SetupIAEnv_Folder_Windows/ImageForReadme/ImageForReadme_7.png)

Finally, execute the .bat you want (with or without gpu support): `SetupIAEnv.bat` (for only CPU Support on Tensorflow) or `SetupIAEnv_gpu.bat` (for GPU Support on Tensorflow).

For `SetupIAEnv.bat` (with only CPU Support on Tensorflow):

![alt text](https://github.com/alexandreauda/SetupIAEnv/blob/master/SetupIAEnv_Folder_Windows/ImageForReadme/ImageForReadme_8.png)

For `SetupIAEnv_gpu.bat` (with GPU Support on Tensorflow):

![alt text](https://github.com/alexandreauda/SetupIAEnv/blob/master/SetupIAEnv_Folder_Windows/ImageForReadme/ImageForReadme_9.png)


The script will create the virtual env `iaenv` or `iaenv_gpu` in Anaconda3 with all the packages useful for the machine learning and artificial intelligence.

![alt text](https://github.com/alexandreauda/SetupIAEnv/blob/master/SetupIAEnv_Folder_Windows/ImageForReadme/ImageForReadme_10.png)



