from pydantic_settings import BaseSettings, SettingsConfigDict

# Settings class used for loading environment variables from .env file
class Settings(BaseSettings):

    # Reads values from .env file and ignores extra variables
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # Database connection URL
    DB_CONNECTION: str

    # Secret key used for JWT token generation and validation
    SERECT_KEY : str

    # JWT algorithm like HS256
    ALGORITHM : str

    # Token expiration time
    EXP_TIME : int


# Creates settings object for accessing environment variables globally
settings = Settings()