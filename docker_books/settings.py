#  host – за замовчуванням 0.0.0.0
# ● port – за замовчуванням 8080
# ● max_books – за замовчуванням None
# ● data_file_path – за замовчуванням ./books.json

from pydantic_settings import BaseSettings,SettingsConfigDict
class Settings(BaseSettings):

    host: str = 'localhost'
    port: int = 8080
    max_books: int | None = None
    data_file_path: str = './books.json'

    model_config = SettingsConfigDict(
    env_file=".env",
    env_file_encoding="utf-8"
    )


settings = Settings()