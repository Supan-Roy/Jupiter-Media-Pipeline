# Supan Roy (13 May, 2026)
# © 2026 Jupiter Sonic Labs. All Rights Reserved
from jupiter_media.core.timeline import Timeline
from jupiter_media.exporters.lrc_exporter import LRCExporter

def test_lrc_export():
    timeline = Timeline()

    timeline.add_segment(
        1.25,
        3.50,
        "Hello Cadence"
    )

    lrc = LRCExporter.export(timeline)

    assert "[00:01.25]" in lrc
    assert "Hello Cadence" in lrc


def test_lrc_multiple_segments():
    timeline = Timeline()

    timeline.add_segment(0.0, 1.0, "First line")
    timeline.add_segment(2.5, 3.5, "Second line")
    timeline.add_segment(5.0, 6.0, "Third line")

    lrc = LRCExporter.export(timeline)

    assert "[00:00.00]First line" in lrc
    assert "[00:02.50]Second line" in lrc
    assert "[00:05.00]Third line" in lrc


def test_lrc_centisecond_precision():
    timeline = Timeline()

    timeline.add_segment(0.007, 1.0, "Tiny")
    timeline.add_segment(1.999, 2.0, "Close")

    lrc = LRCExporter.export(timeline)

    assert "[00:00.00]Tiny" in lrc
    assert "[00:01.99]Close" in lrc


def test_lrc_empty_timeline():
    timeline = Timeline()

    lrc = LRCExporter.export(timeline)

    assert lrc == ""


def test_lrc_sorts_segments():
    timeline = Timeline()

    timeline.add_segment(5.0, 6.0, "Last")
    timeline.add_segment(1.0, 2.0, "First")
    timeline.add_segment(3.0, 4.0, "Middle")

    lrc = LRCExporter.export(timeline)

    lines = lrc.split("\n")
    assert lines[0] == "[00:01.00]First"
    assert lines[1] == "[00:03.00]Middle"
    assert lines[2] == "[00:05.00]Last"