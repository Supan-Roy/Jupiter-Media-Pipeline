Jupiter Media Pipeline

A reusable Python framework for building AI-powered media processing systems.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

---

This repository provides `jupiter_media`, a small toolkit for timed-text workflows (subtitles, lyrics) including:

- core timeline models (`jupiter_media.core`)
- exporters for `.srt` and `.lrc`
- an adapter for Whisper-style transcription (via `faster-whisper`)
- audio extraction helper and example scripts

The project ships as the `jupiter-media` Python package (package name: `jupiter-media`).

---

## Installation

Install from PyPI (when published):

```bash
pip install jupiter-media
```

For local development, build and install from source:

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
python -m pip install --upgrade pip
python -m pip install --upgrade build twine
python -m build
python -m pip install dist/jupiter_media-0.1.0-py3-none-any.whl
```

Notes:
- `ffmpeg` is required on PATH for audio extraction.
- Optional/extra dependencies for different adapters may be documented in the README or package metadata.

---

## Usage (example)

Extract audio, transcribe, and export SRT:

```python
from jupiter_media.core.audio_extractor import AudioExtractor
from jupiter_media.adapters.whisper_adapter import WhisperAdapter
from jupiter_media.exporters.srt_exporter import SRTExporter

AudioExtractor.extract("movie.mp4", "audio.wav")
adapter = WhisperAdapter()
timeline = adapter.transcribe("audio.wav")
srt = SRTExporter.export(timeline)
print(srt)
```

There are runnable examples in the `examples/` folder:
- [examples/transcribe_video.py](examples/transcribe_video.py)
- [examples/export_srt.py](examples/export_srt.py)

---

## Testing

Run the test suite locally (tests are not included in distributions):

```bash
pytest
```

---

## Packaging & Release

See [RELEASE.md](RELEASE.md) for the release process. GitHub Actions handles pull-request checks and tagged publishes, so future updates can be shipped from GitHub with a version bump, tag, and release.

## GitHub Workflow

1. Create a feature branch and open a pull request.
2. Merge to `main` after CI passes.
3. For a release, update the version in `pyproject.toml` and the changelog, then create and push a tag such as `v0.1.1`.
4. The tagged push publishes the package to PyPI and creates a GitHub release.

---

## Links

- Repository: https://github.com/Supan-Roy/Jupiter-Media-Pipeline
- Homepage: https://supanroy.com
- Changelog: [CHANGELOG.md](CHANGELOG.md)

---

## License

This project is licensed under the **MIT License**.

© 2026 Jupiter Sonic Labs — Author: Supan Roy ([contact@supanroy.com](mailto:contact@supanroy.com))
