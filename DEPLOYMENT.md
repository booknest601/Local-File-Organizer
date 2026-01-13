# Deployment Guide

## Docker Deployment

### Quick Start with Docker Compose

1. **Build and run the container:**
   ```bash
   docker-compose up --build
   ```

2. **Place your files** in the `./data` directory

3. **Organized files** will appear in the `./output` directory

### Manual Docker Build

1. **Build the image:**
   ```bash
   docker build -t local-file-organizer .
   ```

2. **Run the container:**
   ```bash
   docker run -it \
     -v $(pwd)/data:/app/data \
     -v $(pwd)/output:/app/output \
     local-file-organizer
   ```

## GitHub Container Registry

The Docker image is automatically published to GitHub Container Registry (GHCR) on every push to main.

### Pull from GHCR:
```bash
docker pull ghcr.io/booknest601/local-file-organizer:main
```

### Run from GHCR:
```bash
docker run -it \
  -v $(pwd)/data:/app/data \
  -v $(pwd)/output:/app/output \
  ghcr.io/booknest601/local-file-organizer:main
```

## Local Python Installation

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   # or
   conda env update --file environment.yml
   ```

2. **Run the application:**
   ```bash
   python main.py
   ```

## Environment Variables

- `PYTHONUNBUFFERED=1` - Enable unbuffered Python output for better logging

## Volume Mounts

- `/app/data` - Input directory for files to organize
- `/app/output` - Output directory for organized files

## System Requirements

- Docker 20.10+ or Python 3.10+
- Minimum 4GB RAM (AI models require memory)
- Tesseract OCR (included in Docker image)

## Notes

- First run will download AI models (Llama3.2 and Llava)
- Processing time depends on file count and types
- Privacy-first: All processing happens locally