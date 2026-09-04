import io
from app.core.groq_client import get_groq


async def transcribe_audio(audio_bytes: bytes, filename: str = "audio.webm") -> str:
    """Transkripsi audio pakai Groq Whisper — gratis!"""
    audio_file = (filename, io.BytesIO(audio_bytes), "audio/webm")

    try:
        response = await get_groq().audio.transcriptions.create(
            file=audio_file,
            model="whisper-large-v3-turbo",
            language="id",
            prompt="Transaksi warung UMKM Indonesia: jual, beli, kulakan, bon, utang, ribu, rb.",
        )
        return response.text.strip()
    except Exception as e:
        raise RuntimeError(f"Gagal transcribe: {str(e)}")