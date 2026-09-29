---
title: Python toolkit
description: Trinet-tools — open-source Python tools to parse, repair, visualize, sync-check and export Trinet recordings.
---

# Python toolkit (Trinet-tools)

[Trinet-tools](https://github.com/Panoculon-Labs/Trinet-tools) is the open-source (MIT) Python
toolkit for Trinet recordings. It can:

- **parse** `.imu` and `.vts` files into NumPy arrays;
- **repair** recordings that some players or uploaders show as only a second long;
- **extract** motion data and timestamps from a video captured over USB;
- **visualize** a recording as video with live motion plots, and several kit cameras side by side on
  one timeline;
- **export** to [MCAP](mcap.md) for Foxglove and ROS 2;
- put card recordings on **[UTC time](wireless-utc.md)**;
- **package** SD cards into upload-ready data deliveries;
- run **stereo depth**, motion HUDs and stereo-inertial odometry on stereo takes.

## Install

```bash
git clone https://github.com/Panoculon-Labs/Trinet-tools.git
cd Trinet-tools
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

- Python 3 on Windows, macOS or Linux.
- `ffmpeg` and `ffprobe` must be on your `PATH` for extraction and visualization (most package
  managers install both together).
- The repair and SD-card ingest scripts need only the Python standard library.

Run the tests with `pip install -r requirements-dev.txt && python3 -m pytest -q`.

## Quick start

```python
from trinet_tools.reader import read_imu, read_vts, interpolate_imu_to_frames

imu = read_imu("recording1_1.imu")
vts = read_vts("recording1_1.vts")

print(f"{imu.num_samples} samples over {imu.duration_s:.1f} s at {imu.actual_rate_hz:.1f} Hz")
per_frame = interpolate_imu_to_frames(imu, vts)   # motion data aligned to each video frame
print(per_frame[0]["frame_number"], per_frame[0]["accel"], per_frame[0]["gyro"])
```

Or start with the notebook
[`examples/tmf_metadata_and_calibration.ipynb`](https://github.com/Panoculon-Labs/Trinet-tools/blob/main/examples/tmf_metadata_and_calibration.ipynb):
it reads the metadata, motion data and calibration embedded in a real stereo recording shipped with
the repository and undistorts a frame.

## Guides

<div class="grid cards" markdown>

- [:material-magnify: **Inspect and repair**](inspect-and-repair.md) — read, check and fix recordings
- [:material-chart-line: **Visualize and check sync**](visualize.md) — motion plots over video, kits side by side
- [:material-database-export: **Export to MCAP / ROS 2**](mcap.md) — one file for Foxglove and ROS 2
- [:material-clock-outline: **Put recordings on UTC**](wireless-utc.md) — using the app's wireless log
- [:material-package-variant: **Ingest SD cards**](ingest.md) — upload-ready deliveries with metadata
- [:material-cube-outline: **Stereo and 3D**](stereo-and-3d.md) — depth, motion HUD, VIO

</div>

## Help and issues

Found a bug or a recording the toolkit can't read? Open an issue on
[GitHub](https://github.com/Panoculon-Labs/Trinet-tools/issues).
