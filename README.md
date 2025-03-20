## BASIC FASTAPI MODEL

This is basic setting up a basic FastAPI API project in Python with ORACLE database

### Installation

1. **Clone the repository:**

   Open your terminal or command prompt and run:

   ```bash
   git clone <repository-link>
   cd basicFastapi-model
   pip install -r requirements.txt
   ```

2. **Create your .env:**

   ```bash
    JWT_SECRET_KEY=your-secret-key
    JWT_ALGORITHM=HS256
    ORACLE_HOST=localhost
    ORACLE_PORT=1521
    ORACLE_SERVICE_NAME=ORCLCDB
    ORACLE_USER=SYS
    ORACLE_PASSWORD=your-password
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    ADMIN_USERNAME=admin
    ADMIN_PASSWORD=password
   ```
3. **Run the application:**

   ```bash
   uvicorn main:app --reload   
   ```

