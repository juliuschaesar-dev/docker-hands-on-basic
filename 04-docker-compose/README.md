# 04 — Docker Compose

Docker Compose dipakai untuk menjalankan **beberapa container sekaligus** (multi-service) dengan satu file konfigurasi (`docker-compose.yaml`) dan satu perintah, alih-alih menjalankan `docker run` satu-satu secara manual.

Latihan dibagi 2 skenario, kerjakan berurutan:

1. **[v1](v1/)** — dua service dari aplikasi yang sama, satu di-`build` dari Dockerfile, satu lagi pakai `image` jadi. Fokus: memahami struktur dasar `docker-compose.yaml`.
2. **[v2](v2/)** — satu aplikasi Flask yang bergantung pada Postgres dan Redis. Fokus: `depends_on`, `volumes`, environment variable antar-service, dan koneksi antar-container lewat nama service.

Basic command yang akan dipakai di kedua skenario:

```bash
docker-compose up -d      # jalankan semua service di background
docker ps -a               # cek container yang berjalan
docker-compose logs -f     # lihat log semua service
docker-compose stop        # hentikan semua service
docker-compose down        # hentikan & hapus container + network
docker-compose down -v     # sama seperti down, plus hapus volume
```

> Catatan: `docker-compose` (Compose V1, standalone) dan `docker compose` (Compose V2, plugin bawaan Docker Desktop terbaru) fungsinya setara — pakai yang tersedia di sistemmu.
