from jupiter_media.core.timeline import Timeline

def test_add_segment():
    timeline = Timeline()

    timeline.add_segment(
        start=0.0,
        end=2.5,
        text="Hello world"
    )

    assert len(timeline) == 1
    assert timeline.segments[0].text == "Hello world"


def test_total_duration():
    timeline = Timeline()

    timeline.add_segment(0.0, 2.0, "First")
    timeline.add_segment(3.0, 7.5, "Second")

    assert timeline.total_duration() == 7.5


def test_sort_segments():
    timeline = Timeline()

    timeline.add_segment(10.0, 12.0, "Late")
    timeline.add_segment(1.0, 3.0, "Early")

    timeline.sort()

    assert timeline.segments[0].text == "Early"


def test_to_dict():
    timeline = Timeline()

    timeline.add_segment(0.0, 1.0, "Test")

    data = timeline.to_dict()

    assert isinstance(data, list)
    assert data[0]["text"] == "Test"