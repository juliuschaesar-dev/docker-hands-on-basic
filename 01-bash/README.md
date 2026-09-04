# 01 — Introduction to Bash

Bash (Bourne Again Shell) adalah command-line interpreter & scripting language untuk berinteraksi dengan OS lewat teks, tanpa perlu klik-klik GUI.

Buka terminal Bash (Git Bash / WSL / Terminal) di folder ini sebelum mulai:

```bash
cd 01-bash
```

## Exercise 1 — Navigation

Tujuan: terbiasa berpindah dan melihat isi direktori.

1. Cek posisi direktori saat ini.
2. Lihat isi direktori saat ini (termasuk file/folder tersembunyi).
3. Buat folder baru bernama `playground` di sini (akan dipakai lagi di Exercise 3).
4. Masuk ke folder `playground`.
5. Cek lagi posisi direktori saat ini, pastikan sudah pindah ke dalam `playground`.
6. Kembali ke direktori sebelumnya (folder `01-bash`).
7. Pindah ke home directory, lalu kembali lagi ke direktori sebelumnya (folder `01-bash`) — pastikan kamu berakhir di `01-bash` sebelum lanjut ke Exercise 2.

<details>
<summary>Solusi / Referensi Command</summary>

```bash
pwd
ls -la
mkdir playground
cd playground
pwd
cd -
cd ~
cd ..
```
</details>

## Exercise 2 — File Manipulation

Tujuan: bisa membuat, menyalin, memindahkan, dan menghapus file.

Kita kerjakan di dalam folder `playground` (dibuat di Exercise 1).

1. Masuk ke folder `playground`.
2. Buat file kosong bernama `catatan.txt`.
3. Tulis teks `"Halo Bash!"` ke dalam file tersebut (overwrite).
4. Tambahkan baris baru `"Baris kedua"` ke file yang sama (append, jangan overwrite).
5. Tampilkan isi file ke layar, pastikan ada 2 baris.
6. Copy `catatan.txt` menjadi `catatan-copy.txt`.
7. Rename `catatan-copy.txt` menjadi `catatan-backup.txt`.
8. Hapus `catatan-backup.txt` (biarkan `catatan.txt` tetap ada, dipakai di Exercise 3).
9. Kembali ke folder `01-bash`.

<details>
<summary>Solusi / Referensi Command</summary>

```bash
cd playground
touch catatan.txt
echo "Halo Bash!" > catatan.txt
echo "Baris kedua" >> catatan.txt
cat catatan.txt
cp catatan.txt catatan-copy.txt
mv catatan-copy.txt catatan-backup.txt
rm catatan-backup.txt
cd ..
```
</details>

## Exercise 3 — Directory Manipulation

Tujuan: bisa membuat, menyalin, memindahkan, dan menghapus folder.

Folder `playground` sudah dibuat di Exercise 1 dan berisi `catatan.txt` dari Exercise 2 — sekarang masuk ke dalamnya untuk mengisi dan mengelola isinya.

1. Masuk ke folder `playground`.
2. Buat 2 subfolder sekaligus dalam satu perintah: `data` dan `logs`.
3. Copy `catatan.txt` (yang sudah ada di dalam `playground`, dari Exercise 2) ke dalam `data`.
4. Pindahkan folder `logs` menjadi `archive`.
5. Cek isi folder saat ini (harus ada `catatan.txt`, `data/`, dan `archive/`, tidak ada `logs/` lagi).
6. Hapus folder `archive`.

<details>
<summary>Solusi / Referensi Command</summary>

```bash
cd playground
mkdir -p data logs
cp catatan.txt data/
mv logs archive
ls -la
rm -rf archive
```
</details>

## Exercise 4 — File Permission

Tujuan: memahami `rwx` dan `chmod`.

Kamu masih berada di dalam folder `playground` dari Exercise 3, tempat `catatan.txt` berada.

1. Cek permission `catatan.txt` saat ini (`ls -l`).
2. Ubah permission `catatan.txt` supaya **owner** punya akses read+write+execute, **group** dan **others** hanya read (setara `744`).
3. Cek lagi dengan `ls -l`, pastikan permission-nya berubah jadi `-rwxr--r--`.
4. Ubah lagi jadi read/write/execute untuk semua (setara `777`).
5. Jelaskan (tulis sebagai komentar/catatan) apa arti tiap digit pada `chmod 750`.

<details>
<summary>Solusi / Referensi Command</summary>

```bash
ls -l catatan.txt
chmod 744 catatan.txt
ls -l catatan.txt
chmod 777 catatan.txt
# chmod 750  -> owner: rwx (7), group: r-x (5), others: --- (0)
```
</details>

---

Lanjut ke [02-docker-run](../02-docker-run/) setelah selesai.
