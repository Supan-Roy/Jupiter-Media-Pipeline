# Supan Roy (13 May, 2026)
# © 2026 Jupiter Sonic Labs. All Rights Reserved
from core.timeline import Timeline

class LRCExporter:
    @staticmethod
    def format_timestamp(seconds: float) -> str:
        minutes = int(seconds // 60)
        secs = int(seconds % 60)
        centiseconds = int((seconds - int(seconds)) * 100)

        return f"{minutes:02}:{secs:02}.{centiseconds:02}"
    
    
    @classmethod
    def export(cls, timeline: Timeline) -> str:
        timeline.sort()

        lines = []

        for segment in timeline:
            timestamp = cls.format_timestamp(segment.start)

            lines.append(
                f"[{timestamp}]{segment.text}"
            )

        return "\n".join(lines)