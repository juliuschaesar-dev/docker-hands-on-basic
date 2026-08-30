# Docker & Bash Practice

Materi latihan (hands-on) **"Docker & Bash"**.

Repo ini berisi contoh kode dan **langkah-langkah exercise** yang mengikuti urutan materi di slide:

| # | Folder | Topik | Slide |
|---|--------|-------|-------|
| 1 | [01-bash](01-bash/) | Introduction to Bash (navigation, file/directory manipulation, permission, scripting) | Lesson 1 & 2 |
| 2 | [02-docker-run](02-docker-run/) | Docker Run — hello-world, simple-web, clean up | Lesson 4 (Demo: Docker - Run) |
| 3 | [03-docker-containerization](03-docker-containerization/) | Bikin Dockerfile & build image sendiri (Flask app) | Demo: Docker - Containerization |
| 4 | [04-docker-compose](04-docker-compose/) | Docker Compose v1 (multi image, satu app) & v2 (app + postgres + redis) | Demo: Docker - Compose |
| 5 | [05-makefile](05-makefile/) | Makefile untuk otomasi task | Lesson 5 |

## Prasyarat

Install dan pastikan berjalan sebelum sesi:

- **Git Bash / WSL / Bash shell** — untuk latihan bagian Bash. Windows user disarankan pakai Git Bash atau WSL.
- **Docker Desktop** — https://www.docker.com/products/docker-desktop/ (pastikan Docker Engine & Docker Compose sudah aktif, cek dengan `docker --version` dan `docker compose version`)
- **make** (opsional untuk bagian 05) — di Windows bisa lewat WSL, Git Bash (`choco install make`), atau Chocolatey.
- Text editor (VS Code direkomendasikan).

## Cara pakai

1. Clone/buka repo ini.
2. Ikuti folder secara berurutan (01 → 05), tiap folder punya `README.md` sendiri berisi penjelasan singkat + langkah-langkah exercise.
3. Kerjakan exercise di masing-masing folder sebelum lanjut ke topik berikutnya.

## Referensi Belajar

- https://www.gnu.org/software/bash/manual/bash.html
- https://www.w3schools.com/bash/
- https://docs.docker.com/get-started/
- https://makefiletutorial.com/
- https://docker-handbook.farhan.dev/
