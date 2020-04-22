# SetupIAEnv_Folder_Linux

This project aims to install all packages required to perform machine learning and artificial intelligence on linux.

We recommand to install pipenv: 

-https://pipenv-fork.readthedocs.io/en/latest/install.html#installing-pipenv

-https://geniesducode.com/articles/comment-installer-pipenv/

You must install tkinter with the following commands:

`sudo apt-get install python3-tk`

Then, run the following commands:

`cd SetupIAEnv_Folder/`

`pipenv shell`

`pipenv install`

`python setup.py install`

`pipenv update`

`pipenv graph`

`pipenv check`

`cd setupiaenv/`

`setupIAEnv -h`

If conda is not recognized, you must close all terminals and run it again as conda will be recognized only after closing all terminals (after the update of the path).
