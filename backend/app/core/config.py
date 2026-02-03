from pydantic import Field, AliasChoices
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Базовые настройки проекта
    PROJECT_NAME: str = Field(
        default="ptp-b2b-platform",
        validation_alias=AliasChoices("PROJECT_NAME", "project_name", "APP_NAME", "app_name"),
    )
    VERSION: str = Field(
        default="0.1.0",
        validation_alias=AliasChoices("VERSION", "version"),
    )
    ENV: str = Field(
        default="dev",
        validation_alias=AliasChoices("ENV", "env"),
    )
    DEBUG: bool = Field(
        default=True,
        validation_alias=AliasChoices("DEBUG", "debug"),
    )

    # API
    API_V1_STR: str = Field(
        default="/api/v1",
        validation_alias=AliasChoices("API_V1_STR", "api_v1_str", "api_v1"),
    )

    # Сервер (чтобы твои host/port из .env не ломали запуск и могли использоваться)
    HOST: str = Field(
        default="127.0.0.1",
        validation_alias=AliasChoices("HOST", "host"),
    )
    PORT: int = Field(
        default=8000,
        validation_alias=AliasChoices("PORT", "port"),
    )

    # Секреты (оставляем дефолт для локальной разработки, но лучше задать в .env)
    SECRET_KEY: str = Field(
        default="local-dev-secret-123456",
        validation_alias=AliasChoices("SECRET_KEY", "secret_key"),
    )

    # Pydantic v2 настройка чтения окружения
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",  # ключевой момент: лишние переменные в .env НЕ валят приложение
    )


settings = Settings()

