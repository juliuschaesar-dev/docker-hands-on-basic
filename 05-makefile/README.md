# 05 — Makefile

Makefile adalah blueprint untuk mengotomasi task berulang (build, run, clean, dsb) supaya perintah panjang cukup dipanggil lewat 1 kata pendek, misalnya `make run-script`.


File di folder ini:

- `simple-script.sh` — script Bash yang sama seperti di [01-bash](../01-bash/).
- `Makefile` — berisi target `all`, `run-script`, `docker-build`, `clean`, `help`.

## Exercise 1 — Jalankan target

1. Jalankan `make` tanpa argumen apa pun, baca pesan bantuan yang muncul.
2. Jalankan `make run-script`, isi input nama & umur seperti biasa.
3. Cek `output.txt` sudah terbuat.
4. Jalankan `make clean`, pastikan `output.txt` terhapus.

<details>
<summary>Solusi / Referensi Command</summary>

```bash
cd ../../05-makefile
make
make run-script
cat output.txt
make clean
ls output.txt   # harus "No such file or directory"
```
</details>

## Exercise 2 — Gabungkan dengan Docker

Target `docker-build` di Makefile ini akan build image dari folder [03-docker-containerization](../03-docker-containerization/).

1. Jalankan `make docker-build`.
2. Cek image sudah muncul dengan `docker images`.

<details>
<summary>Solusi / Referensi Command</summary>

```bash
make docker-build
docker images | grep docker-app
```
</details>

