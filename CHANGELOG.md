# Changelog

All notable changes to this project are documented in this file.

## [0.1.0] - 2026-05-14
- Initial public release (0.1.0).
- Introduced `jupiter_media` top-level package layout.
- Added custom exceptions (`jupiter_media/exceptions.py`).
- Added package-level logging configuration (`jupiter_media/__init__.py`).
- Improved `AudioExtractor` and `WhisperAdapter` with type hints, logging, and error handling.
- Improved `.srt` and `.lrc` exporters with validation and logging.
- Added example scripts in `examples/` and `RELEASE.md` instructions.
- Updated packaging metadata (`pyproject.toml`) and added `MANIFEST.in`.
- Built and validated distributions (`sdist` and `wheel`) with `twine check`.

For details, see the repository: https://github.com/Supan-Roy/Jupiter-Media-Pipeline
