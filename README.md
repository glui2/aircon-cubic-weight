# aircon-cubic-weight

## Description

This code demonstrates the usage of an API provided by Kogan which returns a list of objects with different categories and dimensions in Python, and calculates the average cubic weight of all product listed under the "Air Conditioners" category.

### SETUP INSTRUCTIONS FOR WINDOWS

After downloading the zip file and unzipping it in your desired location:

1. Ensure that Python 3.7+ is downloaded and installed on your machine. Installation details can be found at https://www.python.org/downloads/
2. Open a command prompt in the root of this project (/aircon-cubic-weight) and create a new Python Virtual Environment by running the command  
    `python -m venv aircon-cubic-weight-env`
   (or `python3 -m venv aircon-cubic-weight-env` if the above command defaults to python 2)
   which will create a new environment called aircon-cubic-weight-env. Further details can be found at https://docs.python.org/3/tutorial/venv.html
3. Activate the environment by running the command  
   `.\aircon-cubic-weight-env\Scripts\activate`
4. Install the required packages within your environment by running
   `pip install -r requirements.txt`
   (or `pip3 install -r requirements.txt` if the above command defaults to python 2's pip)
5. Wait for the package to install and you're ready to go!

### SETUP INSTRUCTIONS FOR MAC

After downloading the zip file and unzipping it in your desired location:

1. Ensure that Python 3.7+ is downloaded and installed on your machine. Installation details can be found at https://www.python.org/downloads/
2. Open a command prompt in the root of this project (/aircon-cubic-weight) and create a new Python Virtual Environment by running the command  
    `python -m virtualenv aircon-cubic-weight-env`
   (or `python3 run_simulation.py` if the above command defaults to python 2)
   which will create a new environment called aircon-cubic-weight-env. Further details can be found at https://docs.python.org/3/tutorial/venv.html
3. Make the activate file executable by running the command
   `chmod +x ./aircon-cubic-weight-env/bin/activate`
4. Activate the environment by running the command  
   `source ./aircon-cubic-weight-env/bin/activate`
5. Install the required packages within your environment by running
   `pip install -r requirements.txt`
   (or `pip3 install -r requirements.txt` if the above command defaults to python 2's pip)
6. Wait for the package to install and you're ready to go!

### RUNNING THE SIMULATION

1. To run the simulation, simply run
   `python aircon_cubic_weight.py`
   (or `python3 aircon_cubic_weight.py` if the above command defaults to python 2)
