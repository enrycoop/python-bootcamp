# Python Bootcamp - 100 days of Code
100 Days of Code: the complete python pro bootcamp for 2023

# Installing requirements
Some project require to install some dependencies. In that case there is a requirements.txt file.
In order to install that dependencies into a virtual environment run the following command:
```commandline
python3 -m venv .venv
source .venv/bin/activate 
```
To ensure that the python interpreter is not the system one run the following command:
```commandline
which python
```
f you want to switch projects or leave your virtual environment, deactivate the environment:
```commandline
deactivate
```
# Prepare pip
In order to install all dependencies, run the following command inside the project, after create/activate the venv:
```commandline
python3 -m pip install --upgrade pip

python3 -m pip install -r requirements.txt
```

If you want to generate the requirements.txt you can run:
```commandline
python3 -m pip freeze
```