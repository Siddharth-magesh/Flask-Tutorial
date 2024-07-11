# Flask-Tutorial

## Introduction
Welcome to the Flask Stack tutorial on full-stack development using Python. This tutorial is designed to help you build a lightweight and quick responsive API. Flask's simple implementation and abundant online documentation make it an ideal choice for web development. 

**Video Tutorial** : (https://www.anaconda.com/download)

The architecture is divided into three parts:
1. **Front-end:** Consists of HTML, CSS, and JavaScript.
2. **Core:** Runs on Python and includes two key modules: Flask and MySQL Connector.
3. **Backend:** Utilizes MySQL for database management.

The tutorial begins with the HTML form tag, which collects user input and sends it to a Python local variable via Flask. This temporary data is then injected into a predefined MySQL database using the MySQL Connector module. To retrieve data from MySQL, the SQL module is used to store the data in a temporary Python variable. Finally, Flask renders the template with the retrieved data.

![[Architecture](https://github.com/Siddharth-magesh/Flask-Tutorial/tree/main/materials)
](https://github.com/Siddharth-magesh/Flask-Tutorial/blob/main/materials/Architecture.jpg)

## Installation and Running
1. Download anaconda in your local system from the given link (https://www.anaconda.com/download) and MySQL.
    if you have already downloaded it, move to the next step.

2. Clone the repository from GitHub:
    ```bash
    git clone https://github.com/Siddharth-magesh/Flask-Tutorial.git
    ```
    This command creates a local copy of the AgriHub project on your machine.

3. Create a new conda environment with Python 3.10:
    ```bash
    conda create project python=3.10
    ```
    This sets up a new environment named `project` with Python version 3.10, isolating dependencies.

4. Navigate to the project directory:
    ```bash
    cd Flask-Tutorial
    ```
    This command changes the current directory to the Agri-Hub project folder. Navigate to the cloned directory.

5. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
    This installs all the necessary libraries and dependencies listed in the `requirements.txt` file.

6. Activate your Mysql:
   ```bash
   MySQL -u root -p
   ```
   After Running this command, Enter your Mysql Password.

7. Setup your database;
   ```bash
   source database.sql
   ```
   Make Sure that the database and table name are the same in MySQL and app.py

8. Run the main application:
    ```bash
    python main.py
    ```
    This command starts the Flask application.
