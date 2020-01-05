#!/bin/bash
#
# NAME:  SetupIAEnv
# DESCRIPTION: Install all libraries useful for IA/Machine learning purposes.
# VER:   1.0.0
# PLAT:  linux-64
# LINES: ...
# MD5:   ...

if ! echo "$0" | grep '\.sh$' > /dev/null; then
    printf 'Please run using "bash" or "sh", but not "." or "source"\\n' >&2
    return 1
fi

# Determine RUNNING_SHELL; if SHELL is non-zero use that.
if [ -n "$SHELL" ]; then
    RUNNING_SHELL="$SHELL"
else
    if [ "$(uname)" = "Darwin" ]; then
        RUNNING_SHELL=/bin/bash
    else
        if [ -d /proc ] && [ -r /proc ] && [ -d /proc/$$ ] && [ -r /proc/$$ ] && [ -L /proc/$$/exe ] && [ -r /proc/$$/exe ]; then
            RUNNING_SHELL=$(readlink /proc/$$/exe)
        fi
        if [ -z "$RUNNING_SHELL" ] || [ ! -f "$RUNNING_SHELL" ]; then
            RUNNING_SHELL=$(ps -p $$ -o args= | sed 's|^-||')
            case "$RUNNING_SHELL" in
                */*)
                    ;;
                default)
                    RUNNING_SHELL=$(which "$RUNNING_SHELL")
                    ;;
            esac
        fi
    fi
fi

# Some final fallback locations
if [ -z "$RUNNING_SHELL" ] || [ ! -f "$RUNNING_SHELL" ]; then
    if [ -f /bin/bash ]; then
        RUNNING_SHELL=/bin/bash
    else
        if [ -f /bin/sh ]; then
            RUNNING_SHELL=/bin/sh
        fi
    fi
fi

if [ -z "$RUNNING_SHELL" ] || [ ! -f "$RUNNING_SHELL" ]; then
    printf 'Unable to determine your shell. Please set the SHELL env. var and re-run\\n' >&2
    exit 1
fi

# Suppose that the script is run at the following location: /home/auda/Documents/SetupIAEnv_Folder/setupiaenv/data/SetupIAEnv.sh

# Compute the directory where is run the script, ie /home/auda/Documents/SetupIAEnv_Folder/setupiaenv/data/.
THIS_DIR=$(DIRNAME=$(dirname "$0"); cd "$DIRNAME"; pwd)
# Compute the file that is running, ie SetupIAEnv.sh.
THIS_FILE=$(basename "$0")
# Compute the full path, ie /home/auda/Documents/SetupIAEnv_Folder/setupiaenv/data/SetupIAEnv.sh
THIS_PATH="$THIS_DIR/$THIS_FILE"
# Compute a prefix location where all libraries will be downloaded, ie /home/IAFolder
PREFIX=$HOME/IAFolder
# Variable to know if the script must be runnning install in batch mode (without manual intervention).
BATCH=0
# Variable to tell no error if install prefix (/home/IAFolder) already exists.
FORCE=0

SKIP_SCRIPTS=0
TEST=0
REINSTALL=0


# verify the size of the installer to see if the sh has not been corrupted.
# if ! wc -c "$THIS_PATH" | grep    9345 >/dev/null; then
#     printf "ERROR: size of %s should be    9345 bytes\\n" "$THIS_FILE" >&2
#     exit 1
# fi


# verify the MD5 sum of the begining of this file to detect modifications.
# MD5=$(md5sum "$THIS_PATH")

# MD5=$(head -n +275 "$THIS_PATH" | md5sum -)
# if ! echo "$MD5" | grep e4aa14a7a01a75c12d94ada9a9a506d8 >/dev/null; then
#     printf "WARNING: md5sum mismatch\\n" >&2
#     printf "expected: e4aa14a7a01a75c12d94ada9a9a506d8\\n" >&2
#     printf "     got: %s\\n" "$MD5" >&2
# fi

# extract the tarball appended to this header, this creates the *.tar.bz2 files
# for all the packages which get installed below
#cd "$PREFIX"


# Installing apt package from a requirements file.
# https://www.monolune.com/installing-apt-packages-from-a-requirements-file/
#sed 's/#.*//' my-requirements-file.txt | xargs sudo apt-get install

if [ "$5" = "True" ] # if -sys = True
then
    if [ "$1" = "batch" ] # interactive mode
    then

        printf "Run in batch mode."

        printf "\\n\\n    ###### UPDATE AND UPGDRADE ###### \\n"

        sudo apt-get -y update
        sudo apt-get -y upgrade

        printf "\\n\\n    ### INSTALL PIP3 AND PYTHON3 ### \\n"
        sudo apt-get -y install python3-pip python3-dev

        printf "\\n\\n    ###### INSTALL LIBRARIES VIA APT (Python Scientific Suite) ###### \\n"

        printf "\\n\\n    ### INSTALL USEFUL LIBRARIES (BUILD-ESSENTIAL, CMAKE, GIT, UNZIP, PKG-CONFIG) AND OPENBLAS LIBRARY ### \\n"
        sudo apt-get -y install build-essential cmake git unzip pkg-config libopenblas-dev liblapack-dev

        printf "\\n\\n    ### INSTALL THE PYTHON SCIENTIFIC SUITE (NUMPY, SCIPY, MATPLOTLIB, ...) ### \\n"
        sudo apt-get -y install python3-numpy python3-scipy python3-matplotlib python3-yaml

        printf "\\n\\n    ### INSTALL HDFS5 ### \\n"
        sudo apt-get -y install libhdf5-serial-dev python3-h5py

        printf "\\n\\n    ### INSTALL OPENCV ### \\n"
        sudo apt-get -y install python3-opencv

        printf "\\n\\n    ### INSTALL GRAPHVIZ ### \\n"
        sudo apt-get -y install graphviz

        printf "\\n\\n    ###### INSTALL LIBRARIES VIA PIP3 ###### \\n"

        printf "\\n\\n    ### INSTALL PYDOT ### \\n"
        yes | sudo pip3 install pydot-ng

        printf "\\n\\n    ### INSTALL PANDAS ### \\n"
        yes | sudo pip3 install pandas

        printf "\\n\\n    ### INSTALL PILLOW, LXML AND CYTHON ### \\n"
        yes | sudo pip3 install pillow lxml cython

        printf "\\n\\n    ### INSTALL PIPENV ### \\n"
        yes | sudo pip3 install pipenv

        printf "\\n\\n    ### INSTALL TENSORFLOW ### \\n"
        if [ "$4" = "False" ] # if -gpu = False, install tensorflow, else install tensorflow-gpu
        then
            yes | sudo pip3 install tensorflow
        else
            printf "\\n\\n    ### INSTALL TENSORFLOW-GPU ### \\n"
            yes | sudo pip3 install tensorflow-gpu
        fi

        printf "\\n\\n    ### INSTALL KERAS ### \\n"
        yes | sudo pip3 install keras

        printf "\\n\\n    ### INSTALL JUPYTER ### \\n"
        yes | sudo pip3 install jupyter

    else

        printf "Run in interactive mode."

        printf "\\n\\n    ###### UPDATE AND UPGDRADE ###### \\n"

        sudo apt-get update
        sudo apt-get upgrade

        printf "\\n\\n    ### INSTALL PIP3 AND PYTHON3 ### \\n"
        sudo apt-get install python3-pip python3-dev

        printf "\\n\\n    ###### INSTALL LIBRARIES VIA APT (Python Scientific Suite) ###### \\n"

        printf "\\n\\n    ### INSTALL USEFUL LIBRARIES (BUILD-ESSENTIAL, CMAKE, GIT, UNZIP, PKG-CONFIG) AND OPENBLAS LIBRARY ### \\n"
        sudo apt-get install build-essential cmake git unzip pkg-config libopenblas-dev liblapack-dev

        printf "\\n\\n    ### INSTALL THE PYTHON SCIENTIFIC SUITE (NUMPY, SCIPY, MATPLOTLIB, ...) ### \\n"
        sudo apt-get install python3-numpy python3-scipy python3-matplotlib python3-yaml

        printf "\\n\\n    ### INSTALL HDFS5 ### \\n"
        sudo apt-get install libhdf5-serial-dev python3-h5py

        printf "\\n\\n    ### INSTALL OPENCV ### \\n"
        sudo apt-get install python3-opencv

        printf "\\n\\n    ### INSTALL GRAPHVIZ ### \\n"
        sudo apt-get install graphviz

        printf "\\n\\n    ###### INSTALL LIBRARIES VIA PIP3 ###### \\n"

        printf "\\n\\n    ### INSTALL PYDOT ### \\n"
        sudo pip3 install pydot-ng

        printf "\\n\\n    ### INSTALL PANDAS ### \\n"
        sudo pip3 install pandas

        printf "\\n\\n    ### INSTALL PILLOW, LXML AND CYTHON ### \\n"
        sudo pip3 install pillow lxml cython

        printf "\\n\\n    ### INSTALL PIPENV ### \\n"
        sudo pip3 install pipenv

        printf "\\n\\n    ### INSTALL TENSORFLOW ### \\n"
        if [ "$4" = "False" ] # if -gpu = False, install tensorflow, else install tensorflow-gpu
        then
            sudo pip3 install tensorflow
        else
            printf "\\n\\n    ### INSTALL TENSORFLOW-GPU ### \\n"
            sudo pip3 install tensorflow-gpu
        fi

        printf "\\n\\n    ### INSTALL KERAS ### \\n"
        sudo pip3 install keras

        printf "\\n\\n    ### INSTALL JUPYTER ### \\n"
        sudo pip3 install jupyter

    fi
fi

#     printf "\\n\\n    Do you want to install Anaconda? [yes|no]\\n"
#             printf "[no] >>> "
#             read -r ans
#             if [ "$ans" != "yes" ] && [ "$ans" != "Yes" ] && [ "$ans" != "YES" ] && \
#                [ "$ans" != "y" ]   && [ "$ans" != "Y" ]
#             then
#                 printf "Aborting installation of anaconda.\\n"
#                 exit 2
#             fi

if [ "$2" = "anaconda" ] # install anaconda
then
    # Setup Anaconda.
    ANACONDAFILE="$THIS_DIR/Anaconda3-2019.07-Linux-x86_64.sh"
    # If the installeur of Anaconda doesn't already exist in directory, then download it.
    if [ ! -f "$ANACONDAFILE" ]; then
        printf "\\n\\n    ### DOWNLOAD ANACONDA SETUP ### \\n"
        # Get the installateur Anaconda of Linux. 
        wget -P data/ https://repo.anaconda.com/archive/Anaconda3-2019.07-Linux-x86_64.sh
    fi

    printf "\\n\\n    ### CHECK MD5 OF THE ANACONDA INSTALLEUR ### \\n"

    # verify the MD5 sum of the the file to detect modifications. We do not want to run a malicious file nammed: Anaconda3-2019.07-Linux-x86_64.sh.
    MD5ANACONDA=$(md5sum "$ANACONDAFILE")
    if ! echo "$MD5ANACONDA" | grep ec6a6bf96d75274c2176223e8584d2da >/dev/null; then
        printf "ERROR: md5sum mismatch\\n" >&2
        printf "expected: ec6a6bf96d75274c2176223e8584d2da\\n" >&2
        printf "     got: %s\\n" "$MD5ANACONDA" >&2
        exit 2
    fi
    printf "Done!"

    printf "\\n\\n    ### GIVE EXECUTION RIGHT TO THE ANACONDA INSTALLEUR ### \\n"
    # Give execution right to the installateur.
    chmod +x "$ANACONDAFILE"
    printf "Done!"

    printf "\\n\\n    ### EXECUTE ANACONDA INSTALLEUR ### \\n"
    # Execute installateur of Anaconda.
    "$ANACONDAFILE"
    printf "Installation of Anaconda done!\\n\\n"

    # Conda Documentation:
    # https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/

    # Check if Anaconda is well installed by listing available virtual env.
    # https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#determining-your-current-environment
    printf "\\n\\n    [+] Determining your current Conda environment: \\n"
    conda info --envs

    # Check if Anaconda is well installed by listing packages in Anaconda environment.
    #conda list
    
    # Hide (base) environment.
    # https://askubuntu.com/questions/1026383/why-does-base-appear-in-front-of-my-terminal-prompt
    # conda config --set changeps1 False
    # Activate display of (base) environment.
    # conda config --set changeps1 True

    printf "\\n\\n    Anaconda has been installed successfully. You can launch Anaconda by executing the following command: \\n"
    printf "    anaconda-navigator\\n"

    # Update conda.
    printf "\\n\\n    [+] Update conda: \\n"
    conda update -n base -c defaults conda -y

    # Initialize all shell to be able to run conda in it.
    printf "\\n\\n    [+] Initialize all shell to be able to run conda in them: \\n"
    conda init --all

    # https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#determining-your-current-environment
    printf "\\n\\n    [+] Determining your current Conda environment: \\n"
    conda info --envs

    # https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands
    printf "\\n\\n    [+] Creation of Anaconda virtual environment $3: \\n"
    conda create --name iaenv -y

    # https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activating-an-environment
    printf "\\n\\n    [+] Activation of Anaconda virtual environment $3: \\n"
    conda activate "$3"
    printf "Done! \\n"

    # https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#determining-your-current-environment
    printf "\\n\\n    [+] Determining your current Conda environment: \\n"
    conda info --envs

    printf "\\n\\n    [+] ###### INSTALL ALL LIBRARIES IN VIRTUAL ENV VIA CONDA ###### \\n"

    conda install nb_conda -y
    conda install matplotlib -y
    conda install scipy -y
    conda install pandas -y
    conda install pillow -y
    conda install opencv -y
    conda install lxml -y
    conda install cython -y
    conda install graphviz -y
    conda install h5py -y
    conda install scikit-learn -y
    conda install scikit-image -y
    conda install tqdm -y
    conda install imagesize -y
    conda install spyder -y
    conda install pydot -y
    if [ "$4" = "False" ] # if -gpu = False, install tensorflow, else install tensorflow-gpu
    then
        conda install tensorflow -y
    else
        conda install tensorflow-gpu -y
    fi
    conda install tensorflow-hub -y
    conda install tensorflow-datasets -y
    conda install keras -y
    conda install seaborn -y 

    # List packages in the conda virtual env.
    printf "\\n\\n    [+] List packages in the conda virtual env $3: \\n"
    conda list


    # # ******REMOVE THESE LINES IN PRODUCTION******
    # # Deactivate virtual env.
    # printf "\\n\\n    [+] Deactivate virtual env $3: \\n"
    # conda deactivate
    # printf "Done! \\n"
    # # Remove virtual env.
    # printf "\\n\\n    [+] Remove virtual env $3: \\n"
    # conda env remove -n "$3" -y
    # printf "Done! \\n"




    printf "\\n\\n    Do you want to launch Anaconda Navigator now? [yes|no]\\n"
            printf "[no] >>> "
            read -r ans
            if [ "$ans" != "yes" ] && [ "$ans" != "Yes" ] && [ "$ans" != "YES" ] && \
               [ "$ans" != "y" ]   && [ "$ans" != "Y" ]
            then
                printf "Exiting.\\n"
                exit 2
            fi

    anaconda-navigator

fi

exit 0