#
# Single Node App with Kafka and FastAPI Authentication

This project demonstrates a single node application using FastAPI for user authentication and Apache Kafka for messaging, orchestrated with Docker Compose. The application verifies user credentials and generates JWT tokens for secure access to endpoints.

## Features
**User Authentication**: Verifies user credentials using a mock database and generates JWT tokens for secure access.

**Token Generation and Validation**: Provides endpoints to create and decode JWT tokens.

**Kafka Integration**: Uses Apache Kafka for messaging, with a Kafka UI for easy management.

**OAuth2 Support**: Implements OAuth2 password flow for secure user login

## Components
**FastAPI**: Handles HTTP requests for authentication and token management.

**Apache Kafka**: Manages messaging between services.

**Kafka UI**: Provides a user interface to manage Kafka.

**Docker Compose**: Orchestrates the deployment of FastAPI and Kafka services.

## Endpoints
**POST /login**: Authenticates users and returns a JWT token.

**GET /all-user**: Retrieves all users from the mock database.

**GET /special-endpoint**: Returns details for authorized users.

**GET /get-token**: Generates a JWT token for a given username.

**GET /decoded token**: Decodes a provided JWT token.

## Setup 
 ### Clone the Repository
```
git clonehttps://github.com/Muhammad-Saad-2/Kafka-with-Docker/tree/main/single_node_app_with_kafka_compose 
```

 ### Navigate to the Repository
```
cd <repository-directory>
```
### Run the application using Docker Compose
```
Docker compose up
```
### Access the Application:

FastAPI: http://localhost:8000

Kafka UI: http://localhost:8080

## Configuration

### JWT Settings
Configurable in main.py:
```
ALGORITHM = "HS256"
SECRET_KEY = "my secret key"
```

## Mock Database
Defined in fakedb.py with sample users:
```
fake_db = {
    "Rose Marry": {
        "username": "Rose Marry",
        "password": "my_password",
        "email": "rosemarry@example.com"
    },
    "Alice Benjamin": {
        "username": "Alice Benjamin",
        "password": "your_password",
        "email": "alice@example.com"
    }
}
```
## Usage
### To interact with the API endpoints, use the OpenAPI docs provided by FastAPI:

* Navigate to the OpenAPI Documentation:
Open your browser and go to http://localhost:8000/docs.

* Authenticate User:

Use the POST /login endpoint to authenticate users and obtain a JWT token.

* Retrieve All Users:

Use the GET /all-user endpoint to get a list of all users from the mock database.

* Access Special Endpoint:

Use the GET /special-endpoint endpoint to access protected information.

* Generate Token:

Use the GET /get-token endpoint to generate a JWT token for a given username.

* Decode Token:

Use the GET /decoded token endpoint to decode a provided JWT token.
