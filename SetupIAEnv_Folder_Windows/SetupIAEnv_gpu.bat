@echo off
REM @echo off if you don't want to see the commands executed.
REM https://superuser.com/questions/175466/determine-if-command-is-recognized-in-a-batch-file
CALL conda -V >nul 2>&1 && (set "isCondaCommandRecognized=true" ) || (set "isCondaCommandRecognized=false" )
IF "%isCondaCommandRecognized%" == "true" (
    echo conda command recognized. Continue...
) ELSE  (
    echo conda command not recognized. Launch the installation of Anaconda...
    echo Check if running on 32 bits or 64 bits OS:
    if %PROCESSOR_ARCHITECTURE%==x86 (
        echo This is a 32 bits operating system.
    	REM If Anaconda installer not exist, download it.
        IF NOT EXIST "Anaconda3-2020.02-Windows-x86.exe" (
            echo Download the Anaconda Windows Installer for 64 bits:
            REM Download Anaconda Windows installeur. Warning: curl only installed on latest Windows 10.
            REM curl "https://repo.anaconda.com/archive/Anaconda3-2020.02-Windows-x86.exe" --output Anaconda3-2020.02-Windows-x86.exe
            CALL powershell -command "wget https://repo.anaconda.com/archive/Anaconda3-2020.02-Windows-x86.exe -OutFile Anaconda3-2020.02-Windows-x86.exe"
        )
        REM Convert cmd in PowerShell temporarily to compute the hash of the download installer. If check succeeds, continue. Else, exit.
        CALL powershell -command "$compHash = (Get-FileHash Anaconda3-2020.02-Windows-x86.exe -Algorithm SHA256).hash; Write-Host 'Computed hash of downloaded installer is:' $compHash; $realHash='D13381D6145C47755B198662AF8A5F412836ADECDB68627BC297BE6738A3BDAC'; Write-Host 'Good hash for installer is: D13381D6145C47755B198662AF8A5F412836ADECDB68627BC297BE6738A3BDAC'; if($compHash -eq $realHash){Write-Host 'Installer integrity check has succeeded. Continue.'}else{Write-Host 'Installer integrity check has failed. Common causes include incomplete download and damaged media. Please download a new copy. Exiting...'; if (Test-Path Anaconda3-2020.02-Windows-x86.exe) {Remove-Item Anaconda3-2020.02-Windows-x86.exe}; Read-Host -Prompt 'Press Enter to continue'; Stop-Process -Name 'cmd'}"
        REM Execute the Anaconda Installeur, if hash check has succeeded.
        Anaconda3-2020.02-Windows-x86.exe
    ) else (
        echo This is a 64 bits operating system.
        REM If Anaconda installer not exist, download it.
        IF NOT EXIST "Anaconda3-2020.02-Windows-x86_64.exe" (
            echo Download the Anaconda Windows Installer for 64 bits:
            REM Download Anaconda Windows installeur. Warning: curl only installed on latest Windows 10.
            REM curl "https://repo.anaconda.com/archive/Anaconda3-2020.02-Windows-x86_64.exe" --output Anaconda3-2020.02-Windows-x86_64.exe
            CALL powershell -command "wget https://repo.anaconda.com/archive/Anaconda3-2020.02-Windows-x86_64.exe -OutFile Anaconda3-2020.02-Windows-x86_64.exe"
        )
        REM Convert cmd in PowerShell temporarily to compute the hash of the download installer. If check succeeds, continue. Else, exit.
        CALL powershell -command "$compHash = (Get-FileHash Anaconda3-2020.02-Windows-x86_64.exe -Algorithm SHA256).hash; Write-Host 'Computed hash of downloaded installer is:' $compHash; $realHash='83C2F53C7174253ADCC2DE7D1293A7408C37B295ABBBB8FECA32CB8428A26158'; Write-Host 'Good hash for installer is: 83C2F53C7174253ADCC2DE7D1293A7408C37B295ABBBB8FECA32CB8428A26158'; if($compHash -eq $realHash){Write-Host 'Installer integrity check has succeeded. Continue.'}else{Write-Host 'Installer integrity check has failed. Common causes include incomplete download and damaged media. Please download a new copy. Exiting...'; if (Test-Path Anaconda3-2020.02-Windows-x86_64.exe) {Remove-Item Anaconda3-2020.02-Windows-x86_64.exe}; Read-Host -Prompt 'Press Enter to continue'; Stop-Process -Name 'cmd'}"
        REM Execute the Anaconda Installeur, if hash check has succeeded.
        Anaconda3-2020.02-Windows-x86_64.exe
    )
)
REM @echo off if you want to see the commands executed.
@echo on
REM Update conda.
REM printf "\\n\\n    [+] Update conda: \\n"
CALL conda update -n base -c defaults conda -y
REM Initialize all shell to be able to run conda in it.
REM printf "\\n\\n    [+] Initialize all shell to be able to run conda in them: \\n"
REM conda init --all
REM https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#determining-your-current-environment
REM printf "\\n\\n    [+] Determining your current Conda environment: \\n"
CALL conda info --envs
REM https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands
REM printf "\\n\\n    [+] Creation of Anaconda virtual environment $3: \\n"
CALL conda create --name iaenv_gpu -y
REM https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activating-an-environment
REM printf "\\n\\n    [+] Activation of Anaconda virtual environment $3: \\n"
CALL conda activate iaenv_gpu
REM printf "Done! \\n"
REM https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#determining-your-current-environment
REM printf "\\n\\n    [+] Determining your current Conda environment: \\n"
CALL conda info --envs
REM printf "\\n\\n    [+] ###### INSTALL ALL LIBRARIES IN VIRTUAL ENV VIA CONDA ###### \\n"
CALL conda install nb_conda -y
CALL conda install matplotlib -y
CALL conda install scipy -y
CALL conda install pandas -y
CALL conda install pillow -y
CALL conda install opencv -y
CALL conda install lxml -y
CALL conda install cython -y
CALL conda install graphviz -y
CALL conda install h5py -y
CALL conda install scikit-learn -y
CALL conda install scikit-image -y
CALL conda install tqdm -y
CALL conda install imagesize -y
CALL conda install spyder -y
CALL conda install pydot -y
CALL conda install tensorflow-gpu -y
CALL conda install tensorflow-hub -y
CALL conda install tensorflow-datasets -y
CALL conda install keras -y
CALL conda install seaborn -y 
REM List packages in the conda virtual env.
REM printf "\\n\\n    [+] List packages in the conda virtual env $3: \\n"
CALL conda list
REM # # ******REMOVE THESE LINES IN PRODUCTION******
REM # # Deactivate virtual env.
REM # printf "\\n\\n    [+] Deactivate virtual env $3: \\n"
REM CALL conda deactivate
REM # printf "Done! \\n"
REM # # Remove virtual env.
REM # printf "\\n\\n    [+] Remove virtual env $3: \\n"
REM CALL conda env remove -n iaenv_gpu -y
REM # printf "Done! \\n"
