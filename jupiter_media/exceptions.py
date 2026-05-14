"""
Custom exception types for Jupiter Media Pipeline.

Defines a small hierarchy of exceptions to make error handling
clearer for callers and example scripts.
"""
from __future__ import annotations

class JupiterMediaError(Exception):
    """Base exception for the package."""


class FFmpegNotFoundError(JupiterMediaError, FileNotFoundError):
    """Raised when the ffmpeg binary cannot be found on PATH."""


class TranscriptionError(JupiterMediaError):
    """Raised when a transcription adapter fails."""


class ExportError(JupiterMediaError):
    """Raised when exporting (SRT/LRC) or extraction fails."""
