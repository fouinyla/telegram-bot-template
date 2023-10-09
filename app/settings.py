from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


class ApplicationSettings(BaseSettings):
    DEBUG: bool = False
    RELOAD: bool = False
    APP_HOSTNAME: str
    APP_EXPOSE_PORT: int = 80
    OPENAPI_URL: str = '/openapi.json'
    DOCS_URL: str = '/docs'
    REDOC_URL: str = '/redoc'


application_settings = ApplicationSettings()


class BotSettings(BaseSettings):
    TOKEN: str = Field(validation_alias="BOT_TOKEN")

bot_settings = BotSettings()


class DatabaseSettings(BaseSettings):
    DATABASE_DRIVER: str
    DATABASE_USERNAME: str
    DATABASE_PASSWORD: str
    DATABASE_HOSTNAME: str
    DATABASE_PORT: int
    DATABASE_NAME: str
    DATABASE_PORT_EXPOSE: int

    @property
    def url(self) -> str:
        driver, user, password, host, port, name = (
            self.DATABASE_DRIVER,
            self.DATABASE_USERNAME,
            self.DATABASE_PASSWORD,
            self.DATABASE_HOSTNAME,
            self.DATABASE_PORT,
            self.DATABASE_NAME,
        )

        return f"{driver}://{user}:{password}@{host}:{port}/{name}"


database_settings = DatabaseSettings()


class RedisSettings(BaseSettings):
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_COMMANDER_PORT: int
    REDIS_COMMANDER_USER: str
    REDIS_COMMANDER_PASSWORD: str

    @property
    def url(self) -> str:
        host, port = (
            self.REDIS_HOST,
            self.REDIS_PORT,
        )

        return f'redis://{host}:{port}/0'

redis_settings = RedisSettings()
