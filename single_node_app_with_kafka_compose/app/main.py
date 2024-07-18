#creating an authentication system which verifies the user by password and usernames
#step 1 : verify if user has entered the correct email 
#step 2 : verify if user has entered the correct password
#step 3: generate token


from fastapi import FastAPI, Depends, HTTPException
from jose import jwt, JWTError
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from typing import Annotated, Any
from fakedb import fake_db


ALGORITHM: str = "HS256"
SECCRET_KEY:str = "my secret key"

# creating access token
def create_access_token(subject: str, expires_delta: timedelta)-> str:

    expire = datetime.utcnow() + expires_delta

    to_encode = {"exp": expire, "sub": str(subject)}

    encoded_jwt = jwt.encode(to_encode, SECCRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt



app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

#creating login route 
@app.post("/login")

def login_request(user_data: Annotated[Any, Depends(OAuth2PasswordRequestForm)]): # depends calls the OAuth2PasswordRequestForm class


    user_in_db = fake_db.get(user_data.username)
    if user_in_db is None:
        raise HTTPException(status_code=401, detail="Incorrect Username")

    if user_in_db["password"] != user_data.password:
        raise HTTPException(status_code=401, detail="Incorrect Password")


    access_token_expiry_minutes= timedelta(minutes=15)

    generated_token = create_access_token(
        subject=user_data.username,
        expires_delta=access_token_expiry_minutes
    )

    return{"username": user_data.username, "access_token": generated_token}


@app.get("/all-user")
def get_all_users(token: Annotated[str, Depends(oauth2_scheme)]):
    return fake_db

@app.get("/special-endpoint")
def specia_endpoint(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"user details": "Authorized User", "token":token}

    
@app.get("/get-token")
def get_token(name:str):
    access_token_expiry_minutes= timedelta(minutes=15)

    generated_token = create_access_token(
        subject=name,
        expires_delta=access_token_expiry_minutes
    )

    return {"access_token": generated_token}

def decode_access_token(acess_token:str):
    decoded_jwt = jwt.decode(acess_token, SECCRET_KEY, algorithms=[ALGORITHM])
    
    return decoded_jwt



@app.get("/decoded token")
def decoding_token(access_token:str):
    try:
        decoded_jwt = decode_access_token(access_token)
        return{"decoded_token": decoded_jwt}
    except JWTError:
        return {"error": "Invalid token"}

#Multi microservice architecture OAuth

#step 1 # creating a wrapper endpoint that will call the login endpoint and return the access token

#step 2 # importing oAuth2PasswordBearer - token 