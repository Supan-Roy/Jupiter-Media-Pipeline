"""Example: transcribe an audio file and print SRT to stdout.

Usage:
    python examples/export_srt.py audio.wav
"""
import argparse
import logging
from pathlib import Path

from jupiter_media.adapters.whisper_adapter import WhisperAdapter
from jupiter_media.exporters.srt_exporter import SRTExporter


def main():
    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser(description="Transcribe audio and print SRT")
    parser.add_argument("input", help="Input audio file")
    args = parser.parse_args()

    input_path = Path(args.input)

    adapter = WhisperAdapter()
    timeline = adapter.transcribe(input_path)

    srt = SRTExporter.export(timeline)
    print(srt)


if __name__ == "__main__":
    main()
