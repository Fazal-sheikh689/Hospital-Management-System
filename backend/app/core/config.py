from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_SERVER: str
    DB_DATABASE: str
    DB_DRIVER: str

    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    @property
    def DATABASE_URL(self):
        return (
            f"mssql+pyodbc://@{self.DB_SERVER}/{self.DB_DATABASE}"
            f"?driver={self.DB_DRIVER}"
            "&trusted_connection=yes"
        )

    class Config:
        env_file = ".env"


settings = Settings()