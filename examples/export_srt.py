"""Example: transcribe an audio file and print SRT to stdout.

Usage:
    python examples/export_srt.py audio.wav
"""
import argparse
import logging
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

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
