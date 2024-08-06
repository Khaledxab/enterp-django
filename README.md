# Enterprise Website

This is a Django-based enterprise website project. It includes user authentication, reservations, and other features.

## Prerequisites

- Python 3.10 or higher
- Django 3.2 or higher
- Virtualenv

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/enterprise_website.git
    cd enterprise_website
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

## Usage

### Accessing the Admin Panel

1. Open your web browser and go to `http://127.0.0.1:8000/admin`.
2. Log in with the superuser credentials you created earlier.

### API Endpoints

#### User Signup

- **URL:** `/api/accounts/signup/`
- **Method:** `POST`
- **Payload:**
    ```json
    {
        "username": "yourusername",
        "password": "yourpassword",
        "email": "youremail@example.com"
    }
    ```

#### User Login

- **URL:** `/api/accounts/login/`
- **Method:** `POST`
- **Payload:**
    ```json
    {
        "username": "yourusername",
        "password": "yourpassword"
    }
    ```

#### Reservations

- **URL:** `/api/reservations/`
- **Method:** `GET`, `POST`
- **Payload for POST:**
    ```json
    {
    "description": "string",
    "date": "YYYY-MM-DD",
    "time": "10:30"
    }
    ```

## Project Structure

- `accounts/`: Contains user authentication-related code.
- `reservations/`: Contains reservation-related code.
- `enterprise_website/`: Main project directory.
- `manage.py`: Django's command-line utility for administrative tasks.

