# Supan Roy (14 May, 2026)
# © 2026 Jupiter Sonic Labs. All Rights Reserved
from adapters.whisper_adapter import WhisperAdapter
from core.timeline import Timeline

def test_whisper_transcription():
    adapter = WhisperAdapter(
        model_size="tiny"
    )

    timeline = adapter.transcribe(
        "tests/output/netflix-logo-animation-2019.wav"
    )

    assert isinstance(timeline, Timeline)
    assert len(timeline) > 0

    first_segment = timeline.segments[0]

    assert isinstance(first_segment.text, str)
    assert first_segment.start >= 0