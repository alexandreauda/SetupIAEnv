#!/bin/bash
# since Bash v4

# Go in the parent folder.
cd ..
# "Compile" with the following command to take into account the last change of code.
python setup.py install
# Go back in setupIAEnv folder.
cd setupiaenv