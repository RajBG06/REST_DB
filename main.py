from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import engine, get_db
from services import UserService

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="User Data API")

@app.post("/api/sync-users", response_model=dict)
async def sync_users(db: Session = Depends(get_db)):
    try:
        users = UserService.fetch_users()
        saved_users = []
        for user_data in users:
            saved_user = UserService.save_user(db, user_data)
            saved_users.append(saved_user)
        return {"message": "Users synced successfully", "count": len(saved_users)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/users", response_model=List[schemas.User])
async def get_users(db: Session = Depends(get_db)):
    try:
        return UserService.get_all_users(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# To run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)