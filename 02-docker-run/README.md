# 02 — Docker Run

Sebelum mulai, pastikan Docker Desktop sudah jalan:

```bash
docker --version
docker ps
```

## Exercise 1 — Hello World

Tujuan: menjalankan container pertamamu.

1. Pull image `hello-world`.
2. Jalankan image `hello-world`.
3. Baca pesan yang muncul di terminal — pahami alur yang dijelaskan Docker (pull → create container → run → output → exit).

<details>
<summary>Solusi / Referensi Command</summary>

```bash
docker pull hello-world
docker run hello-world
```
</details>

## Exercise 2 — Simple Web

Tujuan: menjalankan web server di background dengan port mapping dan nama container custom.

1. Pull image `yeasy/simple-web`.
2. Jalankan image `yeasy/simple-web`:
   - sebagai **background process** (detached)
   - **port mapping**: port `9111` di host diarahkan ke port `80` di container
   - beri nama container **`simpleweb`**
3. Buka `http://localhost:9111` di browser, pastikan web-nya muncul.
4. Masuk (exec) ke dalam container `simpleweb` lewat `/bin/bash`, lalu cek isi source code web-nya (biasanya di `/usr/share/nginx/html` atau sesuai isi image).
5. Keluar dari container tanpa mematikannya.

<details>
<summary>Solusi / Referensi Command</summary>

```bash
docker pull yeasy/simple-web
docker run -d -p 9111:80 --name simpleweb yeasy/simple-web

# buka browser ke http://localhost:9111

docker exec -it simpleweb /bin/bash
# di dalam container:
ls /usr/share/nginx/html
exit
```
</details>

## Exercise 3 — Clean Up Everything

Tujuan: terbiasa membersihkan resource Docker (container & image) yang sudah tidak dipakai.

1. Cek semua container yang sedang berjalan.
2. Cek semua container (termasuk yang sudah berhenti).
3. Cek semua image yang ada di local.
4. Stop container `simpleweb`.
5. Hapus **semua** container (yang sudah stop).
6. Hapus **semua** image yang ada.

<details>
<summary>Solusi / Referensi Command</summary>

```bash
# container yang running
docker ps

# semua container (termasuk stopped)
docker ps -a

# semua image
docker images

# stop 1 container
docker stop simpleweb

# hapus semua container yang sudah stop
docker rm $(docker ps -aq)

# hapus semua image
docker rmi $(docker images -q)
```

> Catatan: `docker rm $(docker ps -aq)` akan error kalau ada container yang masih running — stop dulu semua container, atau pakai `docker rm -f $(docker ps -aq)` untuk force remove (hati-hati, ini menghentikan paksa container yang masih jalan).
</details>

### Referensi command tambahan (dari slide)

```bash
docker pull <image-name>
docker volume create <volume-name>
docker run -d -p 8000:8000 -p 9000:9000 -p 9443:9443 --name portainer --restart=always -v portainer_data:/data portainer/portainer-ce:latest
docker exec -it <container-name> /bin/bash
```

---

Lanjut ke [03-docker-containerization](../03-docker-containerization/) setelah selesai.
