# Supan Roy (13 May, 2026)
# © 2026 Jupiter Sonic Labs. All Rights Reserved
import subprocess
from pathlib import Path
from typing import Union
import shutil
import logging

from ..exceptions import FFmpegNotFoundError, ExportError
logger = logging.getLogger(__name__)

class AudioExtractor:
    @staticmethod
    def extract(
        input_file: Union[str, Path],
        output_file: Union[str, Path],
        sample_rate: int = 16000
    ) -> Path:
        """Extract audio from a media file using ffmpeg.

        Args:
            input_file: Path or string to the input media file.
            output_file: Path or string where the extracted audio will be written.
            sample_rate: Output sample rate in Hz.

        Returns:
            Path to the written audio file.

        Raises:
            FFmpegNotFoundError: if `ffmpeg` is not available on PATH.
            ExportError: if ffmpeg fails to extract audio.
        """

        input_file = str(input_file)
        output_file = str(output_file)

        if shutil.which("ffmpeg") is None:
            logger.error("ffmpeg not found on PATH")
            raise FFmpegNotFoundError("ffmpeg binary not found; please install ffmpeg and ensure it's on PATH")

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

        logger.info("Running ffmpeg to extract audio: %s", " ".join(command))

        try:
            subprocess.run(
                command,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=True
            )
        except subprocess.CalledProcessError as exc:
            logger.exception("ffmpeg failed to extract audio")
            raise ExportError("ffmpeg failed during audio extraction") from exc

        return Path(output_file)