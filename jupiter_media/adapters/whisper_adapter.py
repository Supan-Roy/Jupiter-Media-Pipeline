# Supan Roy (14 May, 2026)
# © 2026 Jupiter Sonic Labs. All Rights Reserved
from faster_whisper import WhisperModel
from ..core.timeline import Timeline
from pathlib import Path
from typing import Union
import logging

from ..exceptions import TranscriptionError

logger = logging.getLogger(__name__)

class WhisperAdapter:
    # Speech Transcription using Faster-Whisper

    def __init__(self, model_size: str = "base"):
        self.model = WhisperModel(
            model_size,
            compute_type="int8"
        )

    def transcribe(
            self,
            audio_file: Union[str, Path]
    ) -> Timeline:
        """Transcribe an audio file and return a `Timeline` of segments.

        Args:
            audio_file: Path or string to audio file to transcribe.

        Returns:
            `Timeline` containing the transcription segments.

        Raises:
            TranscriptionError: on underlying model failures.
        """

        audio_file = str(audio_file)

        try:
            segments, info = self.model.transcribe(audio_file)
        except Exception as exc:
            logger.exception("Transcription failed for %s", audio_file)
            raise TranscriptionError("Transcription failed") from exc
        timeline = Timeline()

        segs = list(segments)

        if len(segs) == 0:
            segments2, info2 = self.model.transcribe(audio_file, suppress_blank=False)
            segs = list(segments2)

        if len(segs) == 0:
            # No segments produced; add an empty placeholder segment
            duration = getattr(info, "duration", 0.0)
            timeline.add_segment(start=0.0, end=duration or 0.0, text="")
            return timeline

        for segment in segs:
            timeline.add_segment(
                start=segment.start,
                end=segment.end,
                text=segment.text.strip()
            )

        logger.info("Transcription produced %d segments", len(timeline))

        return timeline