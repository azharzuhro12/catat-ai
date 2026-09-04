# Entry point Vercel — semua request di-rewrite ke fungsi ini (lihat vercel.json)
import os
import sys

# Pastikan folder backend/ ada di sys.path supaya `app.*` bisa diimpor
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.main import app  # noqa: E402
