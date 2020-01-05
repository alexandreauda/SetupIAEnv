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