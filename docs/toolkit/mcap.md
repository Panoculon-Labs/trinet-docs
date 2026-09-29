---
title: Export to MCAP / ROS 2
description: Convert Trinet recordings to MCAP with video, IMU, magnetometer, calibration and frame timing for Foxglove and ROS 2.
---

# Export to MCAP / ROS 2

`to_mcap.py` converts any Trinet recording — single camera or stereo, rolling or global shutter,
H.264 or H.265 — into one `.mcap` file with video, motion data, magnetometer, calibration and
per-frame timing. Video frames are copied, not re-encoded.

```bash
python scripts/to_mcap.py /data/recording3_1.mp4         # -> recording3_1.mcap
python scripts/to_mcap.py /data/take0004_L.mp4           # stereo take -> take0004.mcap
```

| Option | Does |
|---|---|
| `-o PATH` | Output file |
| `--calibration FILE` | Use this calibration instead of the one embedded in the recording |
| `--apply-timeshift` | Shift camera timestamps by the calibrated camera–IMU time offset |
| `--local-clock` | Keep the camera's own clock instead of the kit's shared clock |
| `--compression {zstd,lz4,none}` | Chunk compression (default zstd) |

Open the file in [Foxglove](https://foxglove.dev) or use it with ROS 2 tooling. Video is published
as compressed video messages and motion data as standard IMU messages on one timeline.

Topic names, message types, timestamps and rolling-shutter row timing are listed in the toolkit's
[MCAP export reference](https://github.com/Panoculon-Labs/Trinet-tools/blob/main/docs/mcap_export.md).

!!! tip "Batch export"
    The [SD-card ingest](ingest.md) tool can write an MCAP per clip with `--mcap`.
