# Cybersecuirty Suite for Forensic Analysis
UNR CS 425/426 Project

## Setting up the Virtual Environment on Linux
1. Install Python by following the instructions on [python.org](https://www.python.org/) if it's not already installed. Most Linux distributions come with Python pre-installed.
2. Open Terminal.
3. Navigate to the project directory:
    - `cd path/to/your/project/directory`
4. Create the virtual environment:
    - `python3 -m venv venv`
5. Activate the virtual environment:
    - `source venv/bin/activate`
6. Install the requirements in the virtual environment:
    - `pip install -r requirements.txt`
7. Once finished, leave the virtual environment:
    - `deactivate`

NOTE: Alongside the Python requirements, Java (JDK 21.0.1) will also need to be installed. Most Linux distributions come with a package manager that can be used to install Java easily. For example, on Ubuntu, you can use:
- `sudo apt update`
- `sudo apt install openjdk-21-jdk`

Please check your distribution's package manager and documentation for the appropriate commands.

### Running the program
To run the CSFA, you just need to run the `run.py` file:
- `python3 ./run.py`

## Setting up the Virtual Environment on Windows
1. Install Python from [python.org](https://www.python.org/) if you haven't already.
2. Open Command Prompt.
3. Navigate to the project directory:
    - `cd path\to\your\project\directory`
4. Create the virtual environment:
    - `python.exe -m venv venv`
5. Activate the virtual environment:
    - `.\venv\Scripts\activate`
6. Install the requirements in the virtual environment
    - `python.exe -m pip install -r requirements.txt`
7. Once finished, leave the virtual environment
    - `deactivate`

NOTE: Alongside the Python requirements, Java (JDK 21.0.1) will also need to be installed from [oracle.com](https://www.oracle.com/java/technologies/downloads/#jdk21-windows).

### Running the program on Windows
To run the CSFA, you just need to run the `run.py` file:
- `python.exe .\run.py`

# Contributing
## Notes
- This project follows the PEP8 Style guide for Python Code. Formatting can automatically be done using `black`

## TODO
- Using SQLite instead of a custom database solution
- Implement AI/ML techniques

## Contributors
- Alvin Leung
- Kameron Bettridge
- Raymond Pai
- Zachary Wilhite
