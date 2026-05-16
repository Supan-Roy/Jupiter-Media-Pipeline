# Supan Roy (17 May, 2026)
# © 2026 Jupiter Sonic Labs. All Rights Reserved
import subprocess
from pathlib import Path

class PreviewGenerator:
    @staticmethod
    def generate(
        input_file: str,
        output_dir: str,
        interval: int = 10,
        width: int = 320
    ) -> dict[int, Path]:

        output_path = Path(output_dir)
        output_path.mkdir(
            parents=True,
            exist_ok=True
        )

        output_pattern = (
            output_path / "preview_%04d.jpg"
        )

        command = [
            "ffmpeg",
            "-y",
            "-i", input_file,
            "-vf",
            f"fps=1/{interval},scale={width}:-1",
            str(output_pattern)
        ]

        subprocess.run(
            command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True
        )

        previews = {}

        generated_files = sorted(
            output_path.glob("preview_*.jpg")
        )

        for index, file in enumerate(generated_files):
            timestamp = index * interval
            previews[timestamp] = file

        return previews