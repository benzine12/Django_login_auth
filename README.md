# Django JWT Authentication

A Django REST framework implementation demonstrating JWT (JSON Web Token) authentication with public and protected routes.

## Features

- JWT Authentication using `djangorestframework-simplejwt`
- Public and protected API endpoints
- Custom token claims
- User authentication endpoints

## Default Credentials

```
Username: admin
Password: admin
```

## Prerequisites

- Python 3.8+
- Django 4.0+
- Django REST Framework
- djangorestframework-simplejwt

## Installation

1. Clone the repository:
```bash
git clone https://github.com/benzine12/Django_login_auth.git
cd Django_login_auth
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install django djangorestframework djangorestframework-simplejwt
```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser (or use default credentials):
```bash
python manage.py createsuperuser
# Or use the default credentials:
# username: admin
# password: admin
```

## API Endpoints

### Authentication Endpoints

- `POST /api/login/`: Obtain JWT token pair
  - Request body:
    ```json
    {
        "username": "admin",
        "password": "admin"
    }
    ```
  - Response:
    ```json
    {
        "access": "access_token",
        "refresh": "refresh_token"
    }
    ```

### Test Endpoints

- `GET /api/public/`: Public endpoint (no authentication required)
- `GET /api/private/`: Protected endpoint (requires valid JWT token)

## Usage

1. Start the development server:
```bash
python manage.py runserver
```

2. Get authentication token:
```bash
curl -X POST http://localhost:8000/api/login/ -d "username=admin&password=admin"
```

3. Access protected endpoint:
```bash
curl -H "Authorization: Bearer your_access_token" http://localhost:8000/api/private/
```

## Configuration

The JWT settings can be configured in `settings.py`:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}
```

## Custom Token Claims

The project includes a custom token serializer that adds the username to the token claims:

```python
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token
```

## Security Considerations

- Keep your `SECRET_KEY` secure and never commit it to version control
- Use HTTPS in production
- Configure appropriate token lifetimes
- Implement proper error handling
- Add rate limiting for login attempts
- Change default credentials in production environment

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is open-source and available under the MIT License.

## Contact

Your Name - [@benzine12](https://github.com/benzine12)

Project Link: [https://github.com/benzine12/Django_login_auth](https://github.com/benzine12/Django_login_auth)