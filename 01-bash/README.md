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
3. Masuk ke folder `playground` (buat dulu jika belum ada — lihat Exercise 3).
4. Kembali ke direktori sebelumnya.
5. Kembali ke home directory.

<details>
<summary>Solusi / Referensi Command</summary>

```bash
pwd
ls -la
cd playground
cd -
cd ~
```
</details>

## Exercise 2 — File Manipulation

Tujuan: bisa membuat, menyalin, memindahkan, dan menghapus file.

1. Buat file kosong bernama `catatan.txt`.
2. Tulis teks `"Halo Bash!"` ke dalam file tersebut (overwrite).
3. Tambahkan baris baru `"Baris kedua"` ke file yang sama (append, jangan overwrite).
4. Tampilkan isi file ke layar.
5. Copy `catatan.txt` menjadi `catatan-copy.txt`.
6. Rename `catatan-copy.txt` menjadi `catatan-backup.txt`.
7. Hapus `catatan-backup.txt`.

<details>
<summary>Solusi / Referensi Command</summary>

```bash
touch catatan.txt
echo "Halo Bash!" > catatan.txt
echo "Baris kedua" >> catatan.txt
cat catatan.txt
cp catatan.txt catatan-copy.txt
mv catatan-copy.txt catatan-backup.txt
rm catatan-backup.txt
```
</details>

## Exercise 3 — Directory Manipulation

Tujuan: bisa membuat, menyalin, memindahkan, dan menghapus folder.

1. Buat folder `playground`.
2. Di dalam `playground`, buat 2 subfolder sekaligus dalam satu perintah: `data` dan `logs`.
3. Copy `catatan.txt` (dari Exercise 2) ke dalam `playground/data`.
4. Pindahkan folder `playground/logs` menjadi `playground/archive`.
5. Hapus folder `playground` beserta seluruh isinya.

<details>
<summary>Solusi / Referensi Command</summary>

```bash
mkdir playground
mkdir -p playground/data playground/logs
cp catatan.txt playground/data/
mv playground/logs playground/archive
rm -rf playground
```
</details>

## Exercise 4 — File Permission

Tujuan: memahami `rwx` dan `chmod`.

1. Cek permission `catatan.txt` saat ini (`ls -l`).
2. Ubah permission `catatan.txt` supaya **owner** punya akses read+write+execute, **group** dan **others** hanya read (setara `744`).
3. Ubah lagi jadi read/write/execute untuk semua (setara `777`).
4. Jelaskan (tulis sebagai komentar/catatan) apa arti tiap digit pada `chmod 750`.

<details>
<summary>Solusi / Referensi Command</summary>

```bash
ls -l catatan.txt
chmod 744 catatan.txt
chmod 777 catatan.txt
# chmod 750  -> owner: rwx (7), group: r-x (5), others: --- (0)
```
</details>

## Exercise 5 — Bash Script

Tujuan: menulis script Bash sederhana yang interaktif (`read`), pakai variabel, dan menyimpan output ke file.

File `simple-script.sh` sudah disediakan di folder ini (isinya sama seperti contoh di slide).

1. Baca isi `simple-script.sh`, pahami alurnya: baca input `nama` & `umur`, cetak salam, lalu simpan ke `output.txt`.
2. Beri izin eksekusi ke script tersebut.
3. Jalankan scriptnya, isi input saat diminta.
4. Cek isi `output.txt` yang dihasilkan.

<details>
<summary>Solusi / Referensi Command</summary>

```bash
chmod +x simple-script.sh
./simple-script.sh
cat output.txt
```
</details>

### Tantangan tambahan (opsional)

Modifikasi `simple-script.sh` supaya:
- Validasi kalau `umur` yang diinput bukan angka, script mencetak pesan error dan berhenti.
- Menambahkan timestamp (`date`) di setiap baris yang ditulis ke `output.txt`.

---

Lanjut ke [02-docker-run](../02-docker-run/) setelah selesai.
