
# Heart Disease Prediction App

This application uses a **Python backend** with a machine learning model to predict heart disease and a **Ruby on Rails frontend** to upload data and view the results.

## Prerequisites

### General
- **Git**: You must have Git installed to clone the repository.
- **Ruby**: Ensure Ruby is installed (check the required version in the Gemfile).
- **Rails**: Install Rails globally using `gem install rails`.
- **Python**: Python 3.6+ is required. You'll also need to create and activate a virtual environment.

### System-Specific Dependencies
- **For Windows**: You may need to install build tools (like MSYS2) to compile certain gems and Python libraries.

## Cloning the Project

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. The project consists of two main parts:
   - `frontend/`: The Ruby on Rails app.
   - `backend/`: The Python backend for running the AI model.

---

## Backend Setup (Python)

1. **Navigate to the backend directory**:
   ```bash
   cd backend
   ```

2. **Create a Python virtual environment**:
   - On Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     python -m venv venv
     source venv/bin/activate
     ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Running the backend**:
   Start the Python Flask backend:
   ```bash
   python app.py
   ```

   This will start the backend server on `http://localhost:5000`.

---

## Frontend Setup (Ruby on Rails)

1. **Navigate to the frontend directory**:
   ```bash
   cd ../frontend
   ```

2. **Install Ruby dependencies**:
   Install the necessary gems for the Rails app:
   ```bash
   bundle install
   ```

3. **Setup the database**:
   If you're using SQLite (or another database), you'll need to create and migrate the database:
   ```bash
   rails db:create
   rails db:migrate
   ```

4. **Running the Rails server**:
   Start the Rails frontend server:
   ```bash
   rails server
   ```

   This will start the Rails server on `http://localhost:3000`.

---

## Environment Setup

The `.gitignore` file excludes certain files that should not be tracked by Git, such as:

- `backend/venv/`: Your Python virtual environment (must be created on each machine).
- `frontend/log/`, `frontend/tmp/`: Temporary and log files generated during development.
- `frontend/public/assets`: Compiled frontend assets.

Ensure that you **create and activate the Python virtual environment** and install the necessary dependencies (`pip install -r requirements.txt`) as outlined in the backend setup.

### Ignored Files
The following files and directories are intentionally excluded from Git:
- **Python virtual environment** (`backend/venv/`): You will need to create this locally using `python -m venv venv`.
- **Logs and temporary files** for both the frontend and backend.
- **Node.js dependencies** (`frontend/node_modules/`): If you use Node.js in the frontend, you'll need to install these dependencies using `npm install`.

---

## Common Issues

1. **Virtual environment not working**:
   If the Python backend fails due to missing libraries, ensure you've created and activated the virtual environment (`venv`) and run `pip install -r requirements.txt`.

2. **Database issues**:
   If Rails cannot find the database, make sure you've run `rails db:create` and `rails db:migrate`.

3. **File permissions**:
   Ensure proper permissions for files, especially when working with Rails credentials or if you're using Docker.

4. **Line ending issues**:
   If you encounter warnings related to line endings (LF vs CRLF), the project has a `.gitattributes` file to ensure consistent handling of line endings across different platforms.

---

## Running the Full Application

1. **Start the Python backend**:
   ```bash
   cd backend
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   python app.py
   ```

2. **Start the Rails frontend**:
   ```bash
   cd ../frontend
   rails server
   ```

3. **Access the app in your browser**:
   - **Frontend**: `http://localhost:3000`
   - **Backend**: `http://localhost:5000` (API for model predictions)

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## `.gitignore` File

Here is an overview of the `.gitignore` contents:

- **backend/venv/**: The Python virtual environment.
- **frontend/log/** and **frontend/tmp/**: Logs and temporary files.
- **frontend/public/assets**: Compiled frontend assets.
- **config/master.key**: The Rails master key for decrypting credentials (if applicable).
- **db/*.sqlite3**: SQLite database files, if used.

---

By following these steps, you'll have both the backend and frontend set up and running locally.
