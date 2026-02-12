import argparse
from pathlib import Path

from audio_extractor.application.use_cases import ExtractAudioUseCase
from audio_extractor.infrastructure.ffmpeg_extractor import FFmpegAudioExtractor


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Extrae audio desde archivos de video.")
    parser.add_argument("input_video", type=Path, help="Ruta al video de entrada (mp4, avi, mkv, etc.)")
    parser.add_argument("output_audio", type=Path, help="Ruta del audio de salida")
    parser.add_argument(
        "--format",
        required=True,
        choices=["mp3", "mp4"],
        help="Formato de salida: mp3 o mp4 (audio-only)",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    use_case = ExtractAudioUseCase(extractor=FFmpegAudioExtractor())
    result = use_case.execute(
        input_video=args.input_video,
        output_audio=args.output_audio,
        output_format=args.format,
    )
    print(f"✅ Audio extraído: {result.output_audio}")
    print(f"Comando usado: {' '.join(result.ffmpeg_command)}")


if __name__ == "__main__":
    main()
