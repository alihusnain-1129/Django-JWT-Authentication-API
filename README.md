# 🔐 Django JWT Authentication API

A secure User Authentication System built using Django REST Framework and JSON Web Tokens (JWT).

This project demonstrates a production-ready authentication flow including:

- User Registration (Signup)
- Login with Access & Refresh Tokens
- Protected Routes
- Token Refresh
- Logout (Token Blacklisting)
- Token Expiry Handling
- Session Timeout Control

---

## 🚀 Tech Stack

- Python
- Django
- Django REST Framework
- Simple JWT

---

## 📌 Features

### ✅ User Registration
Users can create a new account using username, email, and password.

### ✅ Login
Returns:
- Access Token (short-lived)
- Refresh Token (long-lived)

### ✅ Protected Routes
Only accessible using a valid Access Token.

### ✅ Token Refresh
Generate new access token using refresh token.

### ✅ Logout
Refresh token is blacklisted to prevent reuse.

### ✅ Token Expiry
- Access Token expires in 5 minutes
- Refresh Token expires in 1 day

### ✅ Change Password
Authenticated users can update their password securely by providing the old password.

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/django-jwt-authentication-api.git
cd django-jwt-authentication-api
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations

```bash
python manage.py migrate
```

### 5️⃣ Run Server

```bash
python manage.py runserver
```

Server will start at:
```
http://127.0.0.1:8000/
```

---

## 🔗 API Endpoints

| Method | Endpoint | Description |
|--------|----------|------------|
| POST | /api/register/ | Register new user |
| POST | /api/login/ | Get access & refresh token |
| POST | /api/refresh/ | Refresh access token |
| POST | /api/logout/ | Blacklist refresh token |
| GET | /api/protected/ | Access protected route |
| POST | /api/change-password/ | Change user password |

---

## 🔐 How Authentication Works

1. User logs in
2. Server returns:
   - Access Token (5 min expiry)
   - Refresh Token (1 day expiry)
3. Access token is sent in headers:

```
Authorization: Bearer <access_token>
```

4. When access token expires:
   - Use refresh token to get new one
5. On logout:
   - Refresh token is blacklisted

---

### 🔐 Change Password Example

**Headers:**
Authorization: Bearer <access_token>

**Body:**
{
  "old_password": "oldpassword",
  "new_password": "newpassword123"
}

---

## 🧠 Learning Outcomes

This project demonstrates:

- Stateless Authentication
- JWT Security Concepts
- Token Rotation
- Blacklisting Mechanism
- REST API Security
- Backend API Development Best Practices

---

## 📈 Future Improvements

- Custom User Model
- Email Verification
- Password Reset via Email
- Rate Limiting
- HttpOnly Cookie Authentication
- Docker Deployment
- CI/CD Integration
