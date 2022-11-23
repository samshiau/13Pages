# User-Interface
***NOTE: Please make sure you have internet connectivity to run the application!***\
\
To run this project, please make sure you have Django 4.1 and Python 3.9+ installed.\
\
To install Python, please click this ***[LINK](https://www.python.org/downloads/)***\
To install Django, please refer this ***[LINK](https://docs.djangoproject.com/en/4.1/topics/install/#installing-official-release)***\
To install the picture display package, please run `pip install Pillow` in the terminal and refer to this ***[LINK](https://pypi.org/project/Pillow/)***\
If you do not have SQLite installed, please refer ***[LINK](https://www.sqlite.org/index.html)***\
\
To verify everything is installed, please test these in your terminal, you should have a similar result
```
  ~ python3 --version
  Python 3.10.8
  
  ~ pip --version
  pip 22.3.1 from .../python3.10/site-packages/pip (python 3.10)
  
  ~ pip list
  // you should see Django, Pillow, and other packages after entering pip list
  
  ~ sqlite3 --version
  // you should see version number here
```
\
Next, change to correct directory (under "mysite" floder)\
Run `ls` and you should see a file called **`manage.py`** means you are in the correct place.\
To start the server, run `python3 manage.py runserver` in the terminal.\
Then you should see something like this:
```
  Watching for file changes with StatReloader
  Performing system checks...

  System check identified no issues (0 silenced).
  November 22, 2022 - 22:31:31
  Django version 4.1.1, using settings 'mysite.settings'
  Starting development server at http://127.0.0.1:8000/
  Quit the server with CONTROL-C.
```
Finally, open your browser and go to `http://127.0.0.1:8000` (might be different), you should be able to see the website

***If you have problem with running the project, please email Samuel.Shiau@my.utsa.edu for more information.***
