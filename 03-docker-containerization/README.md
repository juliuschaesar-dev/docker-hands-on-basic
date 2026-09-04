# 03 — Docker Containerization

Sekarang kita bikin image sendiri dari sebuah aplikasi Python (Flask), bukan cuma pakai image orang lain.

File yang sudah disiapkan di folder ini:

- `app.py` — aplikasi Flask sederhana, membaca environment variable `CUSTOM_NAME` dan menampilkannya di halaman web.
- `requirements.txt` — dependency Python (`Flask`).
- `Dockerfile` — resep untuk build image dari `app.py`.

## Exercise 1 — Build image

1. Dari dalam folder `03-docker-containerization`, build image dengan nama `docker-app`.
2. Cek image sudah muncul di `docker images`.

<details>
<summary>Solusi / Referensi Command</summary>

```bash
cd 03-docker-containerization
docker build -t docker-app .
docker images
```
</details>

## Exercise 2 — Run container dari image sendiri

1. Jalankan container dari image `docker-app`:
   - detached (`-d`)
   - beri nama container `my-app`
   - override environment variable `CUSTOM_NAME` menjadi nama kamu sendiri
   - port mapping: host `9100` → container `8080`
2. Buka `http://localhost:9100` di browser, pastikan muncul `Hello, <nama-kamu>!`.
3. Cek log container-nya.

<details>
<summary>Solusi / Referensi Command</summary>

```bash
docker run -d --name my-app -e CUSTOM_NAME=InsertNameHere -p 9100:8080 docker-app
# buka http://localhost:9100
docker logs my-app
```
</details>

## Exercise 3 — Ubah kode, rebuild

1. Ubah default value `CUSTOM_NAME` di `app.py` menjadi nama kelas kamu, misalnya `'docker-app-v2'`.
2. Stop & hapus container `my-app` lama.
3. Build ulang image (pakai tag versi baru, misalnya `docker-app:v2`).
4. Jalankan container baru dari image `:v2` tanpa override `CUSTOM_NAME`, pastikan default value baru muncul di browser.

<details>
<summary>Solusi / Referensi Command</summary>

```bash
docker stop my-app && docker rm my-app
docker build -t docker-app:v2 .
docker run -d --name my-app-v2 -p 9100:8080 docker-app:v2
```
</details>

---

Lanjut ke [04-docker-compose](../04-docker-compose/) setelah selesai.
