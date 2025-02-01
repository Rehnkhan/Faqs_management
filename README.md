# FAQ Management System

A Django-based FAQ management system with multilingual support and a REST API.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Running Tests](#running-tests)
- [Docker Setup](#docker-setup)
- [Contribution Guidelines](#contribution-guidelines)
- [License](#license)

## Installation

Follow these steps to set up the project on your local machine.

### Prerequisites

- Python 3.8+
- Django 5.1+
- Redis
- Docker (optional, for containerization)
- pip

### Steps

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/faq-management.git
    cd faq-management
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up Redis:**

    Ensure Redis is installed and running on your machine. You can download it from [here](https://redis.io/download).

5. **Run migrations:**

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Create a superuser:**

    ```sh
    python manage.py createsuperuser
    ```

7. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

8. **Access the admin panel:**

    Open your browser and go to `http://127.0.0.1:8000/admin` and log in with the superuser credentials.

## Usage

### API Endpoints

- **List FAQs:** `GET /api/faqs/`
- **Create FAQ:** `POST /api/faqs/`
- **Retrieve FAQ:** `GET /api/faqs/{id}/`
- **Update FAQ:** `PUT /api/faqs/{id}/`
- **Delete FAQ:** `DELETE /api/faqs/{id}/`

### Examples

#### List FAQs

```sh
curl -X GET "http://127.0.0.1:8000/api/faqs/"