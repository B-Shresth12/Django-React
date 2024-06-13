# Note System using Django and React

## Developer: Bishal Shresha
- **Email**: [b.shresth12@gmail.com](mailto:b.shresth12@gmail.com)
- **LinkedIn**: [Bishal Shrestha](https://www.linkedin.com/in/bishal-shrestha-852a65262/)

## To Run this Project

### Prerequisites
User **must** install:
1. Python 3.*
2. PIP 3.* (Package Installer for Python)
3. `venv` (Virtual Environment. PS: Installing venv can vary based on the OS used)
4. Node 20.* (I am using v20.11.1)
5. npm

### Setup Instructions

#### Starting the Django Server

1. Create a virtual environment:
    ```bash
    python -m venv ./backend/venv
    ```

2. Activate the virtual environment:

    - For Windows (CMD):
        ```bash
        venv\Scripts\activate.bat
        ```

    - For Windows (PowerShell/Terminal):
        ```bash
        venv\Scripts\Activate.ps1
        ```

    - For Linux:
        ```bash
        source venv/bin/activate
        ```

3. Install the required packages:

    - For Windows:
        ```bash
        pip install -r requirements.txt
        ```

    - For Linux:
        ```bash
        pip3 install -r requirements.txt
        ```

4. Migrate the database:

    - For Windows:
        ```bash
        python manage.py migrate
        ```

    - For Linux:
        ```bash
        python3 manage.py migrate
        ```

5. Run the Django server:

    - For Windows:
        ```bash
        python manage.py runserver
        ```

    - For Linux:
        ```bash
        python3 manage.py runserver
        ```

#### Running the React Project

1. Navigate to the React project directory and install dependencies:
    ```bash
    npm install
    ```

2. (Optional) Install Vite globally:
    ```bash
    npm install -g vite
    ```

3. Start the React development server:

    - If Vite is installed globally:
        ```bash
        vite
        ```

    - If Vite is not installed globally:
        ```bash
        npm run dev
        ```
