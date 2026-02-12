from typing import Protocol

from audio_extractor.domain.models import ExtractionRequest, ExtractionResult


class AudioExtractionPort(Protocol):
    """Puerto de salida para ejecutar la extracción en infraestructura."""

    def extract(self, request: ExtractionRequest) -> ExtractionResult:
        ...
