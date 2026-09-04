"""
Insert user demo ke tabel profiles (dipakai frontend sebagai DEMO_USER_ID).
Jalankan sekali setelah schema.sql dijalankan di Supabase:

    cd backend
    source venv/bin/activate
    python seed.py
"""
from app.core.database import get_supabase

DEMO_USER_ID = "00000000-0000-0000-0000-000000000001"


def main():
    db = get_supabase()

    existing = db.table("profiles").select("id").eq("id", DEMO_USER_ID).execute()
    if existing.data:
        print(f"✅ User demo sudah ada: {DEMO_USER_ID}")
        return

    db.table("profiles").insert({
        "id": DEMO_USER_ID,
        "nama_toko": "Toko Pak Demo",
        "jenis_usaha": "warung",
    }).execute()
    print(f"✅ User demo dibuat: {DEMO_USER_ID} (Toko Pak Demo)")


if __name__ == "__main__":
    main()
