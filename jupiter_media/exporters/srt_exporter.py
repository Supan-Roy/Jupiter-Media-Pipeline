# Supan Roy (12 May, 2026)
# © 2026 Jupiter Sonic Labs. All Rights Reserved
from ..core.timeline import Timeline
import logging
from ..exceptions import ExportError

logger = logging.getLogger(__name__)

class SRTExporter:
    @staticmethod
    def format_timestamp(seconds: float) -> str:
        
        total_ms = int(round(seconds * 1000))

        hours = total_ms // 3600000
        remainder = total_ms % 3600000
        minutes = remainder // 60000
        remainder = remainder % 60000
        secs = remainder // 1000
        milliseconds = remainder % 1000

        return (
            f"{hours:02}:{minutes:02}:"
            f"{secs:02},{milliseconds:03}"
        )
    
    @classmethod
    def export(cls, timeline: Timeline) -> str:
        if not isinstance(timeline, Timeline):
            logger.error("SRT export received invalid timeline: %r", type(timeline))
            raise ExportError("Provided object is not a Timeline")

        lines = []

        timeline.sort()

        for index, segment in enumerate(timeline, start=1):
            start = cls.format_timestamp(segment.start)
            end = cls.format_timestamp(segment.end)

            lines.append(str(index))
            lines.append(f"{start} --> {end}")
            lines.append(segment.text)
            lines.append("")

        result = "\n".join(lines)
        logger.debug("Exported SRT with %d entries", len(timeline))
        return result