# 04 (v1) — Docker Compose: Multiple Services, Satu Aplikasi

Tujuan: memahami bahwa Docker Compose bisa menjalankan beberapa service sekaligus dengan satu perintah, dan bedanya `build:` vs `image:` di `docker-compose.yaml`.

File di folder ini:

- `app.py`, `requirements.txt`, `Dockerfile` — sama seperti di [03-docker-containerization](../../03-docker-containerization/).
- `docker-compose.yaml` — mendefinisikan 2 service dari aplikasi yang sama:
  - `my-app-dockerfile` → di-**build** langsung dari `Dockerfile` di folder ini, expose di port `5051`.
  - `my-app-image` → pakai **image jadi** bernama `docker-app` (yang kamu build di exercise 03), expose di port `5052`.

## Persiapan

Pastikan image `docker-app` sudah ada (dari exercise 03). Kalau belum:

```bash
docker build -t docker-app ../../03-docker-containerization
```

## Exercise 1 — Jalankan dengan Docker Compose

1. Dari folder ini, jalankan semua service sekaligus di background.
2. Cek semua container yang berjalan (harus ada 2 container).
3. Buka `http://localhost:5051` → harus muncul `Hello, my-app-dockerfile!`.
4. Buka `http://localhost:5052` → harus muncul `Hello, my-app-image!`.
5. Stop semua service dengan satu perintah.

<details>
<summary>Solusi / Referensi Command</summary>

```bash
cd 04-docker-compose/v1
docker-compose up -d
docker ps -a
# http://localhost:5051
# http://localhost:5052
docker-compose stop
```
</details>

## Exercise 2 — Bersihkan

1. Hentikan dan hapus container + network yang dibuat compose (bukan cuma stop).
2. Pastikan `docker ps -a` sudah bersih dari kedua service ini.

<details>
<summary>Solusi / Referensi Command</summary>

```bash
docker-compose down
```
</details>

---

Lanjut ke [v2](../v2/) untuk latihan multi-service dengan database & cache.
