# CatatAI — AI Financial Assistant untuk UMKM

> AI yang ngerti bahasa warung: "utang galon", "kulakan", "bon", "bayar separo"

## Struktur Proyek

```
catat-ai/
├── backend/                  # FastAPI Python
│   ├── app/
│   │   ├── api/              # Route endpoints
│   │   ├── core/             # Config, database, Groq client
│   │   ├── models/           # Pydantic models
│   │   ├── services/         # Business logic
│   │   └── prompts/          # AI prompt templates
│   ├── seed.py               # Insert user demo ke Supabase
│   ├── .env                  # Environment variables
│   └── requirements.txt
├── frontend/                 # Next.js React
│   ├── app/
│   │   ├── components/       # UI components
│   │   ├── lib/              # API client, utils
│   │   └── hooks/            # Custom React hooks
│   ├── .env.local
│   └── package.json
├── supabase/
│   └── schema.sql            # Database schema
└── docs/
    ├── SETUP.md
    └── STRUCTURE.md          # Struktur + daftar API endpoint
```

## Tech Stack

| Layer    | Teknologi                            |
|----------|--------------------------------------|
| Frontend | Next.js 14, Tailwind CSS, Recharts   |
| Backend  | FastAPI, Python 3.11                 |
| AI       | Groq — GPT-OSS 120B (parse & insight), Whisper large v3 (speech-to-text), Qwen 3.8 multimodal (scan struk) |
| Database | Supabase (PostgreSQL + Realtime)     |
| Auth     | Supabase Auth                        |

> Semua fitur AI jalan lewat satu API key Groq gratis — daftar di
> https://console.groq.com/keys

## Quick Start

1. **Clone & setup** — ikuti `docs/SETUP.md`
2. **Isi API key Groq** di `backend/.env` → `GROQ_API_KEY=...`
3. **Jalankan schema** `supabase/schema.sql` di SQL Editor Supabase
4. **Seed user demo** — `cd backend && python seed.py`
5. **Jalankan semuanya** — `bash run.sh` (atau jalankan backend & frontend terpisah)
6. **Buka** — http://localhost:3000

## Fitur MVP

- ✅ Input transaksi via chat (bahasa warung)
- ✅ Input suara (speech-to-text)
- ✅ Scan struk foto (vision AI)
- ✅ Dashboard pemasukan/pengeluaran/grafik
- ✅ Laporan harian, mingguan, bulanan
- ✅ AI insight & narasi keuangan otomatis
