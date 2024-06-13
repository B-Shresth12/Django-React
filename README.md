# 📝 Note System using Django and React

## 👨‍💻 Developer: Bishal Shresha
- **Email**: [b.shresth12@gmail.com](mailto:b.shresth12@gmail.com)
- **LinkedIn**: [Bishal Shrestha](https://www.linkedin.com/in/bishal-shrestha-852a65262/)

---

## 🚀 Getting Started

### Prerequisites
Before you begin, ensure you have the following installed:

1. **Python 3.\***
2. **PIP 3.\*** (Package Installer for Python)
3. **`venv`** (Virtual Environment)
   - *Note: Installing venv can vary based on the OS.*
4. **Node.js 20.\*** (I am using v20.11.1)
5. **npm** (Node Package Manager)

### 🔧 Setup Instructions

#### Starting the Django Server

1. **Create a virtual environment:**
    ```bash
    python -m venv ./backend/venv
    ```

2. **Activate the virtual environment:**

    - **For Windows (CMD):**
        ```bash
        .\backend\venv\Scripts\activate.bat
        ```

    - **For Windows (PowerShell/Terminal):**
        ```bash
        .\backend\venv\Scripts\Activate.ps1
        ```

    - **For Linux/MacOS:**
        ```bash
        source ./backend/venv/bin/activate
        ```

3. **Install the required packages:**

    - **For Windows:**
        ```bash
        pip install -r requirements.txt
        ```

    - **For Linux/MacOS:**
        ```bash
        pip3 install -r requirements.txt
        ```

4. **Migrate the database:**

    - **For Windows:**
        ```bash
        python manage.py migrate
        ```

    - **For Linux/MacOS:**
        ```bash
        python3 manage.py migrate
        ```

5. **Run the Django server:**

    - **For Windows:**
        ```bash
        python manage.py runserver
        ```

    - **For Linux/MacOS:**
        ```bash
        python3 manage.py runserver
        ```

#### Running the React Project

1. **Navigate to the React project directory and install dependencies:**
    ```bash
    cd path/to/your/react/project
    npm install
    ```

2. **(Optional) Install Vite globally:**
    ```bash
    npm install -g vite
    ```

3. **Start the React development server:**

    - **If Vite is installed globally:**
        ```bash
        vite
        ```

    - **If Vite is not installed globally:**
        ```bash
        npm run dev
        ```

---

## 📚 Additional Information

- Ensure you have the correct version of Node.js and Python installed to avoid compatibility issues.
- Use virtual environments to manage your Python dependencies and keep them isolated from your global Python installation.
- For detailed guides on using Django and React, refer to their official documentation:
  - [Django Documentation](https://docs.djangoproject.com/)
  - [React Documentation](https://reactjs.org/docs/getting-started.html)
  - [Vite Documentation](https://vitejs.dev/guide/)

Feel free to reach out via email or LinkedIn if you have any questions or need further assistance. Happy coding! 🎉
