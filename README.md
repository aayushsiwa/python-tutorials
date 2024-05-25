## Project Title

Python Tutorials

## Description

This is a Django web application that allows users to browse python tutorials categorized into various series. Users can register, log in, and manage their accounts. The project is connected to a PostgreSQL database hosted on [render](Render.com).

## Features

- User authentication (registration, login, logout)
- Browse tutorials by categories and series
- Detailed tutorial pages
- User account management
- Error handling pages

## Technologies Used

- Python 3.7+
- Django
- PostgreSQL
- [Render](render.com) for hosting
- HTML, CSS for front-end

## Prerequisites

- Python 3.7+
- PostgreSQL
- Pip (Python package installer)

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/senaditya/python-tutorials.git
    cd yourproject
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database**:
    Ensure you have PostgreSQL installed and create a new database. Update your `DATABASE_URL` environment variable with your database details in the format:
    ```text
    postgres://USER:PASSWORD@HOST:PORT/DBNAME
    ```

5. **Run database migrations**:
    ```bash
    python manage.py migrate
    ```

6. **Create a superuser**:
    ```bash
    python manage.py createsuperuser
    ```

7. **Collect static files**:
    ```bash
    python manage.py collectstatic
    ```

## Running the Application

1. **Start the development server**:
    ```bash
    python manage.py runserver
    ```

2. Open your browser and go to `http://127.0.0.1:8000` to see the application running.

## Deployment

To deploy this project to Render.com:

1. **Create a new web service** on Render.com and connect your GitHub repository.

2. **Add environment variables** in the Render.com dashboard:
    - `DATABASE_URL`: Your PostgreSQL database URL
    - Any other necessary environment variables

3. **Specify the build and start commands** in the Render.com settings:
    - Build Command: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
    - Start Command: `gunicorn yourproject.wsgi:application`

4. **Deploy the service** and Render.com will automatically build and start your application.

## Usage

- Visit the homepage to see a list of tutorial categories.
- Click on a category to see the series within it.
- Click on a series to view the tutorials in that series.
- Register or log in to manage your account.
- Log out when you are done.

## Contributing

1. **Fork the repository**.
2. **Create a new branch**.
    ```bash
    git checkout -b feature/your-feature
    ```
3. **Make your changes**.
4. **Commit your changes**.
    ```bash
    git commit -m "Add your feature"
    ```
5. **Push to the branch**.
    ```bash
    git push origin feature/your-feature
    ```
6. **Open a pull request**.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

For any questions or feedback, please reach out to [me](aditya.sen1hl@gmail.com) or create an issue on GitHub.

---

Feel free to customize the above template according to your project's specific details and requirements.

<img src="./screenshot.png">