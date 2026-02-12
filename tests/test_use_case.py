from pathlib import Path

import pytest

from audio_extractor.application.use_cases import ExtractAudioUseCase
from audio_extractor.domain.models import ExtractionResult


class FakeExtractor:
    def __init__(self) -> None:
        self.called = False

    def extract(self, request):
        self.called = True
        return ExtractionResult(output_audio=request.output_audio, ffmpeg_command=["ffmpeg"])


def test_extract_audio_use_case_validates_supported_format() -> None:
    use_case = ExtractAudioUseCase(extractor=FakeExtractor())

    with pytest.raises(ValueError):
        use_case.execute(Path("in.mp4"), Path("out.wav"), "wav")


def test_extract_audio_use_case_calls_port() -> None:
    extractor = FakeExtractor()
    use_case = ExtractAudioUseCase(extractor=extractor)

    result = use_case.execute(Path("in.mp4"), Path("out.mp3"), "mp3")

    assert extractor.called is True
    assert result.output_audio == Path("out.mp3")
