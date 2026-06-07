
from fastapi import HTTPException, status, Request
from src.user.dtos import UserSchema, LoginSchema
from sqlalchemy.orm import Session
from src.user.models import UserModel
from pwdlib import PasswordHash
import jwt
from src.utils.settings import settings
from datetime import datetime, timedelta
from jwt.exceptions import InvalidTokenError

# table primary key is remove and start with 1, 2, : TRUNCATE TABLE user_tasks RESTART IDENTITY;

password_hash = PasswordHash.recommended()

def get_password_hash(password):
    return password_hash.hash(password)

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)


def register(body:UserSchema, db: Session):
    ## username validation
    is_user = db.query(UserModel).filter(UserModel.userName == body.userName).first()
    if is_user:
        raise HTTPException(status.HTTP_400_BAD_REQUEST,detail="Username already exists..")

    ## email validation
    is_email = db.query(UserModel).filter(UserModel.email == body.email).first()

    if is_email:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Email Address already exists..")
    
    ## password hasing here 
    hash_password = get_password_hash(body.password)

    new_user = UserModel(
        name = body.name,
        userName = body.userName,
        hash_password = hash_password,
        email = body.email
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def login_user(body:LoginSchema, db=Session):
    user = db.query(UserModel).filter(UserModel.userName == body.userName).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You Entered wrong username!")
    
    if not verify_password(body.password, user.hash_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You Entered wrong password!")
    
    exp_time = datetime.now() + timedelta(minutes=settings.EXP_TIME)

    token = jwt.encode({"_id":user.id, "exp":exp_time.timestamp()},settings.SERECT_KEY,settings.ALGORITHM)

    return {"token":token}

## token validation here 
def is_authenticated(request: Request, db : Session):
    try:    
        token = request.headers.get("authorization")
        if not token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are unauthorized.")

        token = token.split(" ")[-1]
        data = jwt.decode(token, settings.SERECT_KEY, settings.ALGORITHM)

        user_id = data.get("_id")
        
        user = db.query(UserModel).filter(UserModel.id == user_id).first()

        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are unauthorized.")

        return user
    
    except InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are unauthorized.")

    
        

