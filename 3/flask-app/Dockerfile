# Gunakan image Python sebagai base image
FROM python:3.9-slim

# Set environment variable untuk memastikan log Flask keluar langsung ke console
ENV PYTHONUNBUFFERED=1

# Buat direktori kerja di dalam container
WORKDIR /app

# Salin file requirements.txt ke direktori kerja
COPY requirements.txt /app/

# Install dependencies yang terdaftar di requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Salin semua file dari direktori lokal ke direktori kerja di dalam container
COPY . /app

EXPOSE 5000

# Tentukan command untuk menjalankan aplikasi Flask
CMD ["python", "app.py"]
