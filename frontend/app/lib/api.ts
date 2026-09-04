import axios from 'axios'

const BASE = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8002/api/v1'

const api = axios.create({
  baseURL: BASE,
  timeout: 60000, // longgar — serverless bisa cold start + panggilan AI
  headers: {
    'ngrok-skip-browser-warning': 'true',
  }
})

// Kompres foto struk di browser sebelum upload (host serverless membatasi body ~4.5MB,
// foto kamera HP bisa 3–8MB). Gagal kompres → kirim file asli.
export async function kompresGambar(file: File, maksSisi = 1600, kualitas = 0.8): Promise<File> {
  if (file.size <= 1_500_000) return file // sudah kecil, tidak perlu
  try {
    const bitmap = await createImageBitmap(file)
    const skala = Math.min(1, maksSisi / Math.max(bitmap.width, bitmap.height))
    const canvas = document.createElement('canvas')
    canvas.width = Math.round(bitmap.width * skala)
    canvas.height = Math.round(bitmap.height * skala)
    const ctx = canvas.getContext('2d')
    if (!ctx) return file
    ctx.drawImage(bitmap, 0, 0, canvas.width, canvas.height)
    const blob = await new Promise<Blob | null>(resolve => canvas.toBlob(resolve, 'image/jpeg', kualitas))
    if (!blob || blob.size >= file.size) return file
    return new File([blob], file.name.replace(/\.[^.]+$/, '') + '.jpg', { type: 'image/jpeg' })
  } catch {
    return file
  }
}

// ── Transaksi ────────────────────────────────────────────────

export async function kirimChat(teks: string, userId: string) {
  const res = await api.post('/transaksi/chat', { teks, user_id: userId })
  return res.data
}

export async function kirimSuara(audioBlob: Blob, userId: string) {
  const form = new FormData()
  form.append('audio', audioBlob, 'rekaman.webm')
  form.append('user_id', userId)
  const res = await api.post('/transaksi/suara', form, {
    headers: { 'Content-Type': 'multipart/form-data', 'ngrok-skip-browser-warning': 'true' },
  })
  return res.data
}

export async function kirimStruk(file: File, userId: string) {
  const foto = await kompresGambar(file)
  const form = new FormData()
  form.append('foto', foto)
  form.append('user_id', userId)
  const res = await api.post('/transaksi/scan-struk', form, {
    headers: { 'Content-Type': 'multipart/form-data', 'ngrok-skip-browser-warning': 'true' },
  })
  return res.data
}

export async function getTransaksi(userId: string, tanggal?: string, limit = 20) {
  const res = await api.get('/transaksi/list', {
    params: { user_id: userId, tanggal, limit },
  })
  return res.data
}

export async function getRingkasanHarian(userId: string, tanggal?: string) {
  const res = await api.get('/transaksi/ringkasan-harian', {
    params: { user_id: userId, tanggal },
  })
  return res.data
}

export async function getLaporan(userId: string, periode: 'harian' | 'mingguan' | 'bulanan') {
  const res = await api.get('/transaksi/laporan', {
    params: { user_id: userId, periode },
  })
  return res.data
}

export async function getPiutang(userId: string) {
  const res = await api.get('/transaksi/piutang', { params: { user_id: userId } })
  return res.data
}

export async function bayarPiutang(piutangId: string, jumlahBayar: number, userId: string) {
  const res = await api.post('/transaksi/piutang/bayar', {
    piutang_id: piutangId,
    jumlah_bayar: jumlahBayar,
  }, { params: { user_id: userId } })
  return res.data
}