from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./users.db"
    API_URL: str = "https://jsonplaceholder.typicode.com/users"
    
    class Config:
        env_file = ".env"

settings = Settings()