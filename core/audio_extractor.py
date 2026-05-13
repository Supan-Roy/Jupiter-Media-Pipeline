# Supan Roy (13 May, 2026)
# © 2026 Jupiter Sonic Labs. All Rights Reserved
import subprocess
from pathlib import Path

class AudioExtractor:
    @staticmethod
    def extract(
        input_file: str,
        output_file: str,
        sample_rate: int = 16000
    ) -> Path:
        command = [
            "ffmpeg",
            "-y",
            "-i", input_file,
            "-vn",
            "-acodec", "pcm_s16le",
            "-ar", str(sample_rate),
            "-ac", "1",
            output_file
        ]

        subprocess.run(
            command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True
        )

        return Path(output_file)