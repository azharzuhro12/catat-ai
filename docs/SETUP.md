# Setup Guide — CatatAI

## Yang Perlu Disiapkan

### Akun & API Keys (semua gratis tier tersedia)

1. **Groq** (wajib — dipakai untuk semua fitur AI) → https://console.groq.com/keys
   - Satu key untuk: parse transaksi & insight (GPT-OSS 120B), speech-to-text (Whisper v3), scan struk (Qwen 3.8 multimodal)
   - Gratis, cukup untuk development

2. **Supabase** (wajib) → https://supabase.com
   - Buat project baru
   - Ambil: Project URL, anon key, service_role key

> Gemini / OpenAI key **tidak diperlukan** — semua fitur AI sudah jalan lewat Groq.

---

## Langkah 1 — Install Prerequisites

### macOS
```bash
# Install Homebrew (jika belum)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python 3.11
brew install python@3.11

# Install Node.js 18+
brew install node

# Verifikasi
python3 --version   # Python 3.11.x
node --version      # v18.x.x atau lebih
npm --version       # 9.x.x atau lebih
```

### Windows (PowerShell sebagai Admin)
```powershell
# Install Chocolatey
Set-ExecutionPolicy Bypass -Scope Process -Force
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Install Python dan Node
choco install python311 nodejs -y

# Verifikasi
python --version
node --version
```

### Linux/Ubuntu
```bash
sudo apt update
sudo apt install python3.11 python3.11-venv python3-pip nodejs npm -y
```

---

## Langkah 2 — Setup Backend (FastAPI)

```bash
cd catat-ai/backend

# Buat virtual environment
python3.11 -m venv venv

# Aktifkan virtual environment
# macOS/Linux:
source venv/bin/activate
# Windows:
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Buat file .env
cp .env.example .env
# Edit .env dengan API keys kamu
```

### Isi file `.env` backend:
```env
GROQ_API_KEY=gsk_...             # WAJIB — dari console.groq.com/keys
SUPABASE_URL=https://xxx.supabase.co
SUPABASE_KEY=eyJ...             # anon key
SUPABASE_SERVICE_KEY=eyJ...     # service_role key (dipakai backend, bypass RLS)
SECRET_KEY=buat-string-random-panjang-di-sini
```

---

## Langkah 3 — Setup Database (Supabase)

1. Buka Supabase dashboard → SQL Editor
2. Copy-paste isi file `supabase/schema.sql`
3. Klik **Run**
4. Seed user demo (dipakai frontend saat development):
   - Kalau `schema.sql` versi terbaru dijalankan, user demo sudah otomatis ikut.
   - Kalau tidak, jalankan isi `supabase/seed-demo.sql` di SQL Editor juga.

---

## Langkah 4 — Setup Frontend (Next.js)

```bash
cd catat-ai/frontend

# Install dependencies
npm install

# Buat file .env.local
cp .env.local.example .env.local
# Edit dengan URL backend dan Supabase kamu
```

### Isi file `.env.local` frontend:
```env
NEXT_PUBLIC_API_URL=http://localhost:8002/api/v1
NEXT_PUBLIC_SUPABASE_URL=https://xxx.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJ...
```

---

## Langkah 5 — Jalankan Aplikasi

Cara cepat (backend + frontend sekaligus):
```bash
bash run.sh
```

Atau terpisah:

### Terminal 1 — Backend
```bash
cd catat-ai/backend
source venv/bin/activate        # aktifkan venv
uvicorn app.main:app --reload --port 8002
```
Buka http://localhost:8002/docs untuk lihat API documentation.
Cek http://localhost:8002/health → `"groq_api_key": true` berarti key sudah terbaca.

### Terminal 2 — Frontend
```bash
cd catat-ai/frontend
npm run dev
```
Buka http://localhost:3000

---

## Troubleshooting

**Error: `ModuleNotFoundError`**
→ Pastikan virtual environment aktif (`source venv/bin/activate`)

**Error: `CORS error` di browser**
→ Pastikan backend berjalan di port 8002

**Error: Supabase connection failed**
→ Cek URL dan key di file `.env`

**Pesan "GROQ_API_KEY belum diisi"**
→ Isi `GROQ_API_KEY` di `backend/.env`, lalu restart backend

**Groq API error 429 (rate limit)**
→ Tunggu sebentar (limit gratis reset cepat), atau cek usage di console.groq.com

**Insert ke Supabase ditolak / data tidak muncul**
→ Pastikan `SUPABASE_SERVICE_KEY` terisi (backend butuh service_role key), dan `python seed.py` sudah dijalankan
