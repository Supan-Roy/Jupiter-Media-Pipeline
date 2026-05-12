# Supan Roy (12 May, 2026)
# © 2026 Jupiter Sonic Labs. All Rights Reserved
from core.timeline import Timeline

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
        lines = []

        timeline.sort()

        for index, segment in enumerate(timeline, start=1):
            start = cls.format_timestamp(segment.start)
            end = cls.format_timestamp(segment.end)

            lines.append(str(index))
            lines.append(f"{start} --> {end}")
            lines.append(segment.text)
            lines.append("")
        
        return "\n".join(lines)