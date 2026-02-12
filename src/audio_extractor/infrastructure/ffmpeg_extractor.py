from pathlib import Path
import subprocess

from audio_extractor.domain.models import ExtractionRequest, ExtractionResult


class FFmpegAudioExtractor:
    """Adaptador de infraestructura basado en ffmpeg."""

    def extract(self, request: ExtractionRequest) -> ExtractionResult:
        self._validate_input(request.input_video)
        request.output_audio.parent.mkdir(parents=True, exist_ok=True)

        command = self._build_command(request)
        subprocess.run(command, check=True)

        return ExtractionResult(output_audio=request.output_audio, ffmpeg_command=command)

    @staticmethod
    def _validate_input(input_video: Path) -> None:
        if not input_video.exists():
            raise FileNotFoundError(f"No existe el archivo de entrada: {input_video}")

    @staticmethod
    def _build_command(request: ExtractionRequest) -> list[str]:
        base_command = ["ffmpeg", "-y", "-i", str(request.input_video), "-vn"]

        if request.output_format == "mp3":
            return [*base_command, "-codec:a", "libmp3lame", "-q:a", "2", str(request.output_audio)]

        # Audio-only MP4: usamos AAC dentro de contenedor mp4.
        return [*base_command, "-codec:a", "aac", "-b:a", "192k", str(request.output_audio)]
