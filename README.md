# Task Management API

A RESTful API for managing tasks built with Django REST Framework. The API includes JWT authentication and provides endpoints for creating, reading, updating, and deleting tasks.

## Features

- JWT Authentication
- CRUD operations for tasks
- Task completion endpoint
- Input validation
- Unit tests
- User-specific task management

## Prerequisites

- Python 3.8+
- pip (Python package installer)
- virtualenv (recommended)

## Installation & Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd task-management
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the root directory and add:
```
DJANGO_SECRET_KEY=your-secret-key-here
```

5. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create a superuser (admin):
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

## API Endpoints

### Authentication
- POST `/api/token/`: Obtain JWT token pair
- POST `/api/token/refresh/`: Refresh JWT token

### Tasks
- GET `/api/tasks/`: List all tasks
- POST `/api/tasks/`: Create a new task
- GET `/api/tasks/{id}/`: Retrieve a specific task
- PUT `/api/tasks/{id}/`: Update a specific task
- DELETE `/api/tasks/{id}/`: Delete a specific task
- PATCH `/api/tasks/{id}/complete/`: Mark a task as complete

## Testing

Run the tests using pytest:
```bash
pytest
```

## Design Decisions & Assumptions

1. Authentication:
   - Used JWT for stateless authentication
   - Tokens expire after 5 hours (configurable)
   - Refresh tokens valid for 1 day

2. Task Model:
   - Tasks are user-specific
   - Status choices limited to: pending, in_progress, completed
   - Due date is required
   - Description is optional

3. Security:
   - Users can only access their own tasks
   - All endpoints (except token generation) require authentication
   - CORS middleware included for potential frontend integration

4. Database:
   - Using SQLite for development (can be changed for production)
   - Implemented soft deadlines (due_date) without strict enforcement

## API Usage Examples

1. Obtain JWT Token:
```bash
curl -X POST http://localhost:8000/api/token/ \
     -H "Content-Type: application/json" \
     -d '{"username": "your_username", "password": "your_password"}'
```

2. Create Task:
```bash
curl -X POST http://localhost:8000/api/tasks/ \
     -H "Authorization: Bearer your_jwt_token" \
     -H "Content-Type: application/json" \
     -d '{
           "title": "Sample Task",
           "description": "Task description",
           "due_date": "2024-12-31"
         }'
```

3. List Tasks:
```bash
curl -X GET http://localhost:8000/api/tasks/ \
     -H "Authorization: Bearer your_jwt_token"
```

## Production Considerations

1. Security:
   - Use strong SECRET_KEY
   - Enable HTTPS
   - Configure CORS properly
   - Set DEBUG=False

2. Database:
   - Switch to PostgreSQL or similar
   - Configure database connection pooling

3. Performance:
   - Add caching if needed
   - Consider pagination for large datasets

4. Monitoring:
   - Add logging
   - Implement health checks
   - Set up monitoring tools

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request
