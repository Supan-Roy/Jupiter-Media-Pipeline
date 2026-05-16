import logging

logging.getLogger(__name__).addHandler(logging.NullHandler())

from .core import (
    Timeline,
    TimelineSegment,
    AudioExtractor,
)

from .exporters import (
    SRTExporter,
    LRCExporter,
)

from .processing import PreviewGenerator

try:
    from .adapters import WhisperAdapter
except ModuleNotFoundError as exc:
    if exc.name != "faster_whisper":
        raise