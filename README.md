# django-valorantlineups
Valorant Lineups is a webapp aimed at providing strategies to players of Valorant by Riot Games.
Using Django as a web backend, users can submit various lineups for other players to view. 

This application is my honours project for 2022 and a short demo of the application can be seen here:
https://youtu.be/97zBjWDTky8

To build the project follow these steps below:

1. Ensure you have a working install of Python 3.9.

2. Install Pip (Python Installs Packages).
```
       > python3 -m pip install --user --upgrade pip
       > python3 -m pip --version
       ~ pip 21.1.3 from $HOME/.local/lib/python3.9/site-packages (python 3.9)
```
       
3. Install pip-env via Python Pip (Python Installs Packages).
```
       > python3 -m pip install --user virtualenv
```
4. Clone the repository to the directory of your choosing. 

5. Create a virtual-environment within the root directory 'django-valorantlineups'.
```
       > python3 -m venv /django-valorantlineups/.venv/
       > source /.venv/bin/activate
       > which python
       ~ ../.venv/bin/python
 ```
6. Install the dependencies into the local virutal-environemnt now setup. 
```
       > python3 -m pip install -r requirements.txt
```
7. Once dependencies are installed, navigate to the /django-valorantlineups/valorantlineups/ folder. 
8. From here you can now run Django's testing sever on your local host address.
```
       > python3 manage.py runserver
       ~ Watching for file changes with StatReloader
         Performing system checks...

         System check identified no issues (0 silenced).
         March 25, 2022 - 19:11:32
         Django version 4.0.1, using settings 'valorantlineups.settings'
         Starting development server at http://127.0.0.1:8000/
         Quit the server with CONTROL-C.
```
