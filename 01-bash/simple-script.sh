#!/bin/bash
# Read input from the user
echo "Masukkan nama Anda:"
read nama
echo "Masukkan umur Anda:"
read umur

# Print Result
echo "Hello, $nama! Anda berumur $umur tahun."

# Save the output to a file
echo "Script ini telah dijalankan oleh $nama yang berumur $umur tahun" > output.txt
