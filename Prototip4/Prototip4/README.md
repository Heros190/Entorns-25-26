# Prototip4 Authentication Service

This project is a Flask-based web service that provides user authentication functionality through a RESTful API. It includes a Data Access Object (DAO) for database interactions and various services to handle authentication logic.

## Project Structure

```
Prototip4
├── src
│   ├── app.py                # Entry point of the Flask application
│   ├── config.py             # Configuration settings for the application
│   ├── db.py                 # Database connection and setup
│   ├── dao
│   │   └── user_dao.py       # Data Access Object for user interactions
│   ├── models
│   │   └── user.py           # User model representing the user entity
│   ├── services
│   │   └── auth_service.py    # Service for handling authentication logic
│   ├── routes
│   │   └── auth.py           # Authentication routes including /login
│   ├── schemas
│   │   └── user_schema.py     # Schema for user data validation and serialization
│   └── utils
│       └── token.py          # Utility functions for token management
├── tests
│   └── test_auth.py          # Unit tests for authentication functionality
├── requirements.txt          # Project dependencies
├── .env                      # Environment variables for sensitive information
└── README.md                 # Project documentation
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd Prototip4
   ```

2. **Create a virtual environment**:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory and add your database credentials and secret keys.

5. **Run the application**:
   ```
   python src/app.py
   ```

## Usage

- The API provides a `/login` endpoint for user authentication.
- Send a POST request with `username` (or email) and `password` in the request body to authenticate users.

## Testing

Run the unit tests to ensure the authentication functionality works as expected:
```
python -m unittest discover -s tests
```

## License

This project is licensed under the MIT License.