import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # API Configuration
    gemini_api_key: str = "YOUR_GEMINI_API_KEY"
    instagram_app_secret: str = "YOUR_INSTAGRAM_APP_SECRET"
    instagram_access_token: str = "YOUR_INSTAGRAM_ACCESS_TOKEN"
    webhook_verify_token: str = "YOUR_WEBHOOK_VERIFY_TOKEN"

    # Database
    database_url: str = "sqlite:///./hotel_booking.db"
    database_pool_size: int = 10

    # Application
    environment: str = "development"
    debug: bool = True

    # Rate Limiting
    rate_limit_per_user: int = 10
    rate_limit_global: int = 100

    # Security
    session_timeout: int = 3600  # seconds

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
