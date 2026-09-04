from supabase import create_client, Client
from app.core.config import get_settings
from functools import lru_cache


@lru_cache()
def get_supabase() -> Client:
    """
    Client utama untuk backend (server terpercaya).
    Pakai service_role key supaya tidak diblokir RLS —
    backend sudah yang memvalidasi user_id, bukan Supabase Auth.
    """
    settings = get_settings()
    key = settings.supabase_service_key or settings.supabase_key
    return create_client(settings.supabase_url, key)


# Alias kompatibel — client admin sama dengan client utama
get_supabase_admin = get_supabase
