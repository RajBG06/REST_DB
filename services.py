import requests
from sqlalchemy.orm import Session
from config import settings
import models
import schemas

class UserService:
    @staticmethod
    def fetch_users():
        response = requests.get(settings.API_URL)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def save_user(db: Session, user_data: dict):
        user = models.User(
            name=user_data["name"],
            email=user_data["email"],
            username=user_data["username"],
            phone=user_data.get("phone"),
            website=user_data.get("website")
        )
        
        # Check for existing user
        existing_user = db.query(models.User).filter(
            models.User.email == user_data["email"]
        ).first()
        
        if existing_user:
            existing_user.name = user_data["name"]
            existing_user.username = user_data["username"]
            existing_user.phone = user_data.get("phone")
            existing_user.website = user_data.get("website")
            db.commit()
            db.refresh(existing_user)
            return existing_user
            
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def get_all_users(db: Session):
        return db.query(models.User).all()