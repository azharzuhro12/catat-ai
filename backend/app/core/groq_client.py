from groq import AsyncGroq
from app.core.config import get_settings

_groq: AsyncGroq | None = None


def get_groq() -> AsyncGroq:
    """
    Client Groq lazy-init — baru dibuat saat pertama kali dipakai,
    jadi aplikasi tetap bisa start walau GROQ_API_KEY belum diisi.
    """
    global _groq
    if _groq is None:
        key = get_settings().groq_api_key
        if not key:
            raise RuntimeError(
                "GROQ_API_KEY belum diisi. Ambil gratis di https://console.groq.com/keys "
                "lalu isi di backend/.env"
            )
        _groq = AsyncGroq(api_key=key)
    return _groq
