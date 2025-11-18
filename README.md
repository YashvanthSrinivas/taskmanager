# Task Management System API  
A simple and secure Task Management System built using **Django REST Framework** with **Token Authentication**.

This project allows users to create, view, update, and delete their own tasks.  
Superusers can view **all users' tasks**, while normal users can only access their own.

---

## Features

### User & Authentication
- Token-based authentication (DRF TokenAuth)
- Each user can only access their own tasks
- Superuser can access **all tasks** in the system

### Task Management
- Create new tasks
- List all tasks
- Retrieve a single task
- Update a task
- Delete a task
- Auto-assign task owner based on logged-in user

---

## API Endpoints

### Auth
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/login` | Authenticate user & generate token/session |

---

## Task APIs
| Method | Endpoint | Description | Access |
|--------|----------|-------------|--------|
| GET | `/tasks` | Get all tasks | USER, ADMIN |
| GET | `/tasks/{id}` | Get task by ID | USER, ADMIN |
| POST | `/tasks` | Create a new task | ADMIN |
| PUT | `/tasks/{id}` | Update an existing task | ADMIN |
| DELETE | `/tasks/{id}` | Delete a task | ADMIN |
| PATCH | `/tasks/{id}/status` | Update only the task status | ADMIN |

---

## User APIs
| Method | Endpoint | Description | Access |
|--------|----------|-------------|--------|
| POST | `/users` | Create a new user | ADMIN |
| GET | `/users` | Get all users | ADMIN |
| GET | `/users/{id}` | Get user by ID | ADMIN |


### Authentication
| Method | Endpoint | Description |
|--------|-----------|--------------|
| POST | `/api-token-auth/` | Get token using username & password |

Request body:
```json
{
  "username": "your_username",
  "password": "your_password"
}
