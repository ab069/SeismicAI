from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "SeismicAI"
    DATABASE_URL: str = "postgresql+asyncpg://seismicai:seismicai_secret@postgres:5432/seismicai"
    SECRET_KEY: str = "seismicai-super-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440

    class Config:
        env_file = ".env"


settings = Settings()
