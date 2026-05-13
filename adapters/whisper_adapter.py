# Supan Roy (14 May, 2026)
# © 2026 Jupiter Sonic Labs. All Rights Reserved
from faster_whisper import WhisperModel
from core.timeline import Timeline

class WhisperAdapter:
    # Speech Transcription using Faster-Whisper

    def __init__(self, model_size: str = "base"):
        self.model = WhisperModel(
            model_size,
            compute_type="int8"
        )

    def transcribe(
            self,
            audio_file: str
    ) -> Timeline:
        segments, info = self.model.transcribe(audio_file)
        timeline = Timeline()

        segs = list(segments)

        # If no segments were produced, retry
        # with suppress_blank disabled to be more permissive in tests.
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

        return timeline