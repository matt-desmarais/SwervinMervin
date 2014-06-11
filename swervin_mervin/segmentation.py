# Helper functions for generating / finding segments.

import settings as s

def build_segments():
    """Builds an array of segments, pre-populating each with a Z position
       and alternating colour palette"""
    segments = []

    for n in range(500):
        palette = "dark" if (n / s.RUMBLE_LENGTH) % 2 == 0 else "light"

        segments.append({
          "index":  n,
          "top":    {"world": {"z": ((n + 1) * s.SEGMENT_HEIGHT)},
                     "camera": {},
                     "screen": {}},
          "bottom": {"world": {"z": (n * s.SEGMENT_HEIGHT)},
                     "camera": {},
                     "screen": {}},
          "colour": s.COLOURS[palette]})

    return segments

def find_segment(z, segments):
    """Finds the correct segment for any given Z position"""
    i = int(round((z / s.SEGMENT_HEIGHT) % len(segments)))

    if i == len(segments):
        i = 0

    return segments[i]


