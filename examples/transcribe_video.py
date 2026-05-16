"""Example: extract audio from a video, transcribe, and export SRT.

Usage:
    python examples/transcribe_video.py input_video.mp4 [output.srt]
"""
import argparse
import logging
import tempfile
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


def resolve_input_path(raw_input: str) -> Path:
    input_path = Path(raw_input)
    if input_path.exists():
        return input_path

    script_relative_path = Path(__file__).resolve().parent / input_path
    if script_relative_path.exists():
        return script_relative_path

    return input_path

from jupiter_media.core.audio_extractor import AudioExtractor
from jupiter_media.adapters.whisper_adapter import WhisperAdapter
from jupiter_media.exporters.srt_exporter import SRTExporter


def main():
    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser(description="Transcribe video and export SRT")
    parser.add_argument("input", help="Input video file")
    parser.add_argument("output", nargs="?", help="Output SRT file")
    args = parser.parse_args()

    input_path = resolve_input_path(args.input)
    output_path = Path(args.output) if args.output else input_path.with_suffix(".srt")

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
        audio_path = Path(tmp.name)

    try:
        AudioExtractor.extract(input_path, audio_path)

        adapter = WhisperAdapter()
        timeline = adapter.transcribe(audio_path)

        srt = SRTExporter.export(timeline)
        output_path.write_text(srt, encoding="utf-8")

        print(f"Wrote SRT to: {output_path}")
    finally:
        try:
            audio_path.unlink()
        except Exception:
            pass


if __name__ == "__main__":
    main()
