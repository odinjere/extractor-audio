# Extractor de audio en Python

Este proyecto implementa un extractor de audio desde videos (`mp4`, `avi`, `mkv`, etc.) con salida en:

- `mp3`
- `mp4` **solo audio** (codec AAC)

## Arquitectura (Clean Architecture)

Separamos el código en capas para que sea fácil de probar y extender:

- **domain/**: modelos y puertos (contratos).
- **application/**: caso de uso principal (`ExtractAudioUseCase`).
- **infrastructure/**: implementación concreta con `ffmpeg`.
- **presentation/**: CLI.

Patrón clave aplicado:

- **Ports and Adapters (Hexagonal)**: el caso de uso depende de un puerto (`AudioExtractionPort`), no de `ffmpeg` directamente.

## Requisitos

- Python 3.10+
- `ffmpeg` instalado y accesible en PATH.

## Instalación

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Uso

```bash
audio-extractor input_video.avi salida.mp3 --format mp3
audio-extractor input_video.mkv salida.mp4 --format mp4
```

## Siguientes pasos sugeridos

1. Soportar extracción por lotes.
2. Añadir presets de calidad.
3. Soportar una interfaz web o desktop sin tocar la capa de dominio.
