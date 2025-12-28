#!/usr/bin/env python3
"""Optional helper: export timezone band boundaries.

This project doesn't require Python to run.
This script is just a convenience if you want to:
- generate a GeoJSON file of timezone bands,
- or reuse the math elsewhere.

Usage:
  python3 tools/generate_bands.py > timezone_bands.geojson
"""

import json

def bands():
  features = []
  for off in range(-12, 15):
    start = off * 15 - 7.5
    end = off * 15 + 7.5
    start = max(-180.0, start)
    end = min(180.0, end)
    # polygon as a rectangle covering most latitudes
    coords = [
      [start, -85.0],
      [end, -85.0],
      [end, 85.0],
      [start, 85.0],
      [start, -85.0],
    ]
    features.append({
      "type": "Feature",
      "properties": {"utc_offset": off},
      "geometry": {"type": "Polygon", "coordinates": [coords]},
    })
  return {"type": "FeatureCollection", "features": features}

print(json.dumps(bands(), ensure_ascii=False))
