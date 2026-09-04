-- ============================================================
-- CatatAI — Seed User Demo (DEVELOPMENT ONLY!)
-- Jalankan di Supabase SQL Editor SETELAH schema.sql
--
-- Membuat akun demo di auth.users + profile "Toko Pak Demo"
-- yang dipakai frontend sebagai DEMO_USER_ID.
-- HAPUS/BYPASS ini saat production!
-- ============================================================

-- 1. Akun demo di Supabase Auth
--    (trigger on_auth_user_created otomatis bikin row profiles-nya)
INSERT INTO auth.users (
  instance_id, id, aud, role, email, encrypted_password,
  email_confirmed_at, raw_app_meta_data, raw_user_meta_data,
  created_at, updated_at
) VALUES (
  '00000000-0000-0000-0000-000000000000',
  '00000000-0000-0000-0000-000000000001',
  'authenticated',
  'authenticated',
  'demo@catatai.local',
  crypt('demo12345', gen_salt('bf')),
  now(),
  '{"provider":"email","providers":["email"]}'::jsonb,
  '{"nama_toko":"Toko Pak Demo"}'::jsonb,
  now(),
  now()
) ON CONFLICT (id) DO NOTHING;

-- 2. Fallback kalau trigger belum ada / gagal
INSERT INTO public.profiles (id, nama_toko, jenis_usaha)
VALUES (
  '00000000-0000-0000-0000-000000000001',
  'Toko Pak Demo',
  'warung'
) ON CONFLICT (id) DO NOTHING;

-- Verifikasi: harus 1 row
SELECT id, nama_toko FROM public.profiles WHERE id = '00000000-0000-0000-0000-000000000001';
