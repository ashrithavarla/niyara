from pydantic_settings import BaseSettings


# Equivalent to application.properties
class Settings(BaseSettings):
    APP_NAME: str = "tissues"
    SERVER_PORT: int = 1818

    # Email Configuration
    MAIL_HOST: str = "smtp.gmail.com"
    MAIL_PORT: int = 587
    MAIL_USERNAME: str = "your-email@gmail.com"
    MAIL_PASSWORD: str = "your-app-password"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
