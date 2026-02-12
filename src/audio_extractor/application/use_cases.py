from pathlib import Path

from audio_extractor.domain.models import ExtractionRequest, ExtractionResult
from audio_extractor.domain.ports import AudioExtractionPort


class ExtractAudioUseCase:
    """Caso de uso principal para extraer audio."""

    SUPPORTED_OUTPUT_FORMATS = {"mp3", "mp4"}

    def __init__(self, extractor: AudioExtractionPort) -> None:
        self._extractor = extractor

    def execute(self, input_video: Path, output_audio: Path, output_format: str) -> ExtractionResult:
        normalized_format = output_format.lower().strip()
        if normalized_format not in self.SUPPORTED_OUTPUT_FORMATS:
            raise ValueError(
                f"Formato de salida no soportado: {output_format}. "
                f"Usa uno de {sorted(self.SUPPORTED_OUTPUT_FORMATS)}"
            )

        request = ExtractionRequest(
            input_video=input_video,
            output_audio=output_audio,
            output_format=normalized_format,
        )
        return self._extractor.extract(request)
