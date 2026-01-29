from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "ptp-b2b-backend"
    VERSION: str = "0.1.0"
    ENV: str = "dev"
    DEBUG: bool = True


settings = Settings()
