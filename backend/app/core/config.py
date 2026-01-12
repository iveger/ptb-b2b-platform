from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "ptb-b2b-platform"
    environment: str = "local"

settings = Settings()
