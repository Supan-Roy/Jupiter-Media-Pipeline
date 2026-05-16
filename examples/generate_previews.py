import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from jupiter_media.processing.preview_generator import (
    PreviewGenerator
)


def resolve_input_path(raw_input: str) -> Path:
    input_path = Path(raw_input)
    if input_path.exists():
        return input_path

    script_relative_path = Path(__file__).resolve().parent / input_path
    if script_relative_path.exists():
        return script_relative_path

    return input_path


previews = PreviewGenerator.generate(
    input_file=resolve_input_path("Silicon-Valley-Test.mp4"),
    output_dir=Path(__file__).resolve().parent / "previews",
    interval=5
)

print("\nGenerated previews:\n")

for timestamp, path in previews.items():
    print(
        f"{timestamp}s -> {path}"
    )