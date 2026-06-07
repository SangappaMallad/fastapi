
from fastapi import HTTPException, status, Request, Depends
from sqlalchemy.orm import Session
from src.utils.settings import settings
from src.user.models import UserModel
from src.utils.db import get_db
import jwt
from jwt.exceptions import InvalidTokenError

# Authentication dependency function used for validating JWT token
def is_authenticated(request: Request, db : Session = Depends(get_db)):
    try:    
        # Gets authorization token from request headers
        token = request.headers.get("authorization")
        # Checks whether token is missing
        if not token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are unauthorized.")

        # Extracts actual JWT token from 'Bearer <token>'
        token = token.split(" ")[-1]

        # Decodes and validates JWT token using secret key and algorithm
        data = jwt.decode(token, settings.SERECT_KEY, settings.ALGORITHM)

        # Gets user id from JWT payload
        user_id = data.get("_id")
        
        # Fetches user from database using token user id
        user = db.query(UserModel).filter(UserModel.id == user_id).first()

        # Checks whether user exists or not
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are unauthorized.")

        # Returns authenticated user object
        return user
    
    # Handles invalid or expired JWT token errors
    except InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are unauthorized.")
