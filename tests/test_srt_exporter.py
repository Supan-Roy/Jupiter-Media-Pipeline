from jupiter_media.core.timeline import Timeline
from jupiter_media.exporters.srt_exporter import SRTExporter

def test_srt_export():
    timeline = Timeline()

    timeline.add_segment(
        1.0,
        3.5,
        "Welcome to Cadence"
    )

    srt = SRTExporter.export(timeline)

    assert "Welcome to Cadence" in srt
    assert "00:00:01,000" in srt
    assert "00:00:03,500" in srt


def test_srt_multiple_segments():
    timeline = Timeline()

    timeline.add_segment(0.0, 1.0, "First")
    timeline.add_segment(2.0, 3.0, "Second")

    srt = SRTExporter.export(timeline)

    assert "First" in srt
    assert "Second" in srt
    assert "1" in srt
    assert "2" in srt


def test_srt_timestamp_hours():
    timeline = Timeline()

    timeline.add_segment(3661.234, 3662.0, "Hour test")

    srt = SRTExporter.export(timeline)

    assert "01:01:01,234" in srt
    assert "01:01:02,000" in srt


def test_empty_timeline_returns_empty_string():
    timeline = Timeline()

    srt = SRTExporter.export(timeline)

    assert srt == ""


def test_milliseconds_padding():
    timeline = Timeline()

    timeline.add_segment(0.0, 0.005, "Tiny")

    srt = SRTExporter.export(timeline)

    assert "00:00:00,005" in srt