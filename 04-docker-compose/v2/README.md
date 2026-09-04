# 04 (v2) — Docker Compose: App + Postgres + Redis

Tujuan: latihan skenario yang lebih realistis — satu aplikasi Flask yang bergantung pada database (Postgres) dan cache (Redis), semua diorkestrasi lewat satu `docker-compose.yaml`.

File di folder ini:

- `app.py` — Flask app dengan 3 route:
  - `/` — halaman utama.
  - `/db` — mencoba connect ke Postgres dan menampilkan versinya.
  - `/redis` — mencoba connect ke Redis dan menghitung jumlah hit (`INCR`).
- `requirements.txt` — `Flask`, `psycopg2-binary`, `redis`.
- `Dockerfile` — build image untuk service `app`.
- `docker-compose.yaml` — 3 service: `app`, `db` (postgres:13), `redis` (redis:alpine), plus 1 named volume `postgres-data` supaya data Postgres tidak hilang saat container dihapus.

## Exercise 1 — Jalankan semua service

1. Dari folder ini, build & jalankan semua service di background.
2. Cek semua container berjalan (`docker ps -a`), harus ada 3 container.
3. Buka `http://localhost:5020` di browser.

<details>
<summary>Solusi / Referensi Command</summary>

```bash
cd ../v2
docker-compose up -d
docker ps -a
# http://localhost:5020
```
</details>

## Exercise 2 — Test koneksi ke Postgres & Redis

1. Buka `http://localhost:5020/db` — pastikan muncul pesan versi Postgres.
2. Buka `http://localhost:5020/redis` — refresh beberapa kali, pastikan angka hit bertambah.
3. Masuk ke container `db` dan cek database `mydb` lewat `psql`.

<details>
<summary>Solusi / Referensi Command</summary>

```bash
# http://localhost:5020/db
# http://localhost:5020/redis (refresh beberapa kali)

docker exec -it <container_name_db> psql -U postgres -d mydb
# di dalam psql:
\l
\q
```

Cari nama container `db` dengan `docker ps` (biasanya `v2-db-1` atau `v2_db_1` tergantung versi compose).
</details>

## Exercise 3 — Lihat log & stop

1. Lihat log semua service secara bersamaan (follow mode).
2. Hentikan semua service.
3. Hentikan dan hapus semua service + network, tapi **pertahankan** volume `postgres-data`.

<details>
<summary>Solusi / Referensi Command</summary>

```bash
docker-compose logs -f
docker-compose stop
docker-compose down          # volume tetap ada karena tidak pakai -v
```
</details>

---

Lanjut ke [05-makefile](../../05-makefile/) setelah selesai.
