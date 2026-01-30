from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "ptp-b2b-platform"
    VERSION: str = "0.1.0"
    ENV: str = "dev"
    DEBUG: bool = True

    API_V1_STR: str = "/api/v1"

    class Config:
        env_file = ".env"


settings = Settings()

