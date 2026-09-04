import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ENV_FILE = os.path.join(BASE_DIR, ".env")


class Settings(BaseSettings):
    gemini_api_key: str = ""      # tidak dipakai lagi (opsional)
    groq_api_key: str = ""
    supabase_url: str = ""
    supabase_key: str = ""
    supabase_service_key: str = ""
    openai_api_key: str = ""      # tidak dipakai lagi (opsional)
    secret_key: str = "dev-secret-key"
    environment: str = "development"

    model_config = SettingsConfigDict(env_file=ENV_FILE)


@lru_cache()
def get_settings() -> Settings:
    return Settings()
