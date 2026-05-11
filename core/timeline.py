# Supan Roy (12 May, 2026)
# © 2026 Jupiter Sonic Labs. All Rights Reserved
from dataclasses import dataclass, field
from typing import List
import json

@dataclass
class TimelineSegment:
    """
    Represents a single timed text segment.

    Example:
        [00:01.20 - 00:03.50] Hello world
    """

    start: float
    end: float
    text: str

    def duration(self) -> float:
        return self.end - self.start

    def to_dict(self) -> dict:
        return {
            "start": self.start,
            "end": self.end,
            "text": self.text
        }

@dataclass
class Timeline:
    """
    Stores and manages multiple timed segments.
    Used for:
    - subtitles
    - lyrics
    - captions
    - dubbing alignment
    """

    segments: List[TimelineSegment] = field(default_factory=list)

    def add_segment(self, start: float, end: float, text: str):
        self.segments.append(
            TimelineSegment(start, end, text)
        )

    def sort(self):
        self.segments.sort(key=lambda s: s.start)

    def total_duration(self) -> float:
        if not self.segments:
            return 0.0

        return max(segment.end for segment in self.segments)

    def to_dict(self) -> List[dict]:
        return [segment.to_dict() for segment in self.segments]

    def to_json(self, indent: int = 4) -> str:
        return json.dumps(self.to_dict(), indent=indent)

    def __len__(self):
        return len(self.segments)

    def __iter__(self):
        return iter(self.segments)