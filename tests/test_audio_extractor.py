# Supan Roy (13 May, 2026)
# © 2026 Jupiter Sonic Labs. All Rights Reserved
from pathlib import Path
from jupiter_media.core.audio_extractor import AudioExtractor

def test_audio_extraction():
    input_file = "tests/assets/netflix-logo-animation-2019.mp4"
    input_path = Path(input_file)
    output_file = f"tests/output/{input_path.stem}.wav"

    Path("tests/output").mkdir(
        parents=True,
        exist_ok=True
    )

    extracted_file = AudioExtractor.extract(
        input_file=input_file,
        output_file=output_file
    )

    assert extracted_file.exists()
    assert extracted_file.suffix == ".wav"
    assert extracted_file.stem == input_path.stem