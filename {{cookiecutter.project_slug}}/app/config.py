from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str
    DEBUG: bool = False


settings = Settings()
