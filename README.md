# Jupiter Media Pipeline

> A reusable Python framework for building AI-powered media processing systems.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Tests](https://img.shields.io/badge/Tests-passing-brightgreen)
![Status](https://img.shields.io/badge/Status-Early%20Development-orange)

---

Jupiter Media Pipeline provides a modular, extensible architecture for timed text handling, subtitle generation, lyrics synchronization, media transcription, and future AI dubbing workflows.

It is designed to serve as a shared foundation for media applications such as:

- **Jupiter Player** — a full-featured media player
- **Cadence Music Player** — a music-focused playback application

---

## Features

- **Timeline-based segment system** — precise `start`/`end` timed text segments
- **Reusable data structures** — shared subtitle and lyrics models
- **Extensible adapter architecture** — plug in new AI/transcription backends easily
- **Export support** — built-in exporters for `.srt`, `.lrc`, and more
- **Testable & scalable** — clean project layout ready for CI/CD

---

## Planned Features

| Feature | Status |
|---|---|
| Audio extraction pipeline | Planned |
| Whisper transcription adapter | Planned |
| Subtitle exporters (`.srt`, `.vtt`) | Planned |
| Lyrics synchronization (`.lrc`) | Planned |
| Translation pipeline | Planned |
| AI dubbing support | Planned |
| Offline AI processing | Planned |

---

## Project Structure

```text
jupiter_media_pipeline/
│
├── core/           # Core data models (Timeline, TimelineSegment, ...)
├── adapters/       # AI/transcription backend adapters
├── exporters/      # Format exporters (.srt, .lrc, .vtt, ...)
├── utils/          # Shared utility functions
├── tests/          # Pytest test suite
├── examples/       # Usage examples and demos
└── conftest.py     # Pytest root configuration
```

---

## Installation

```bash
# Clone the repository
git clone https://github.com/your-org/jupiter-media-pipeline.git
cd jupiter-media-pipeline

# Create and activate a virtual environment
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS / Linux

# Install dependencies
pip install -r requirements.txt
```

---

## Running Tests

```bash
pytest
```

For verbose output:

```bash
pytest -v
```

---

## Quick Example

```python
from core.timeline import Timeline

timeline = Timeline()
timeline.add_segment(0.0, 2.5, "Hello, world!")
timeline.add_segment(3.0, 6.0, "Welcome to Jupiter.")

print(timeline.to_json())
```

---

## License

This project is licensed under the **MIT License**.

&copy; 2026 Jupiter Sonic Labs. All Rights Reserved.  
Author: Supan Roy
