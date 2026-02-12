from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ExtractionRequest:
    """Representa la intención de extraer audio de un archivo de video."""

    input_video: Path
    output_audio: Path
    output_format: str


@dataclass(frozen=True)
class ExtractionResult:
    """Resultado de una extracción de audio."""

    output_audio: Path
    ffmpeg_command: list[str]
