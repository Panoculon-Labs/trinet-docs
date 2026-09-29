---
title: Inspect and repair recordings
description: Read Trinet recordings in Python, print a summary, fix MP4s that show as one second long, extract data from USB captures and record from a computer.
---

# Inspect and repair recordings

All commands run from the [Trinet-tools](index.md) folder with its virtual environment active.

## Summary of a recording

```bash
python examples/inspect_recording.py path/to/recording1_1.imu
```

Prints the format version and camera generation, device ID, sample count, duration, measured
sample rate and sensor ranges.

## Read the data in Python

```python
from trinet_tools.reader import read_imu, read_vts

imu = read_imu("recording1_1.imu")
print(imu.header.sample_rate_hz, imu.header.device_id_hex, imu.header.generation)
print(imu.timestamps_ns[:5], imu.accel[:5], imu.gyro[:5])   # ns, m/s², rad/s

vts = read_vts("recording1_1.vts")
print(vts.frame_numbers[:5], vts.sof_timestamps_ns[:5])      # mid-exposure frame times
```

Read the embedded metadata and calibration straight from a video file:

```python
from trinet_tools.tmf import read_tmf
from trinet_tools import calib_blob

rec = read_tmf("take0002_L.mp4")
print(rec.meta)                              # recording details
calib = calib_blob.unpack(rec.calib_blob)    # intrinsics, extrinsics, IMU noise
```

## Recording shows only one second? Repair it

Some players, web uploaders and editors show a Trinet MP4 as about one second long, or reject it,
even though it plays fine in VLC or QuickTime. `repair_recordings.py` rebuilds the file index into a
standard MP4 — no re-encoding, lossless, audio preserved, safe to re-run.

```bash
python3 scripts/repair_recordings.py /path/to/recordings            # in place
python3 scripts/repair_recordings.py /path/to/recordings -r --backup  # subfolders, keep .bak copies
python3 scripts/repair_recordings.py /path/to/recordings --dry-run    # show what would change
```

Standard-library Python only; no `ffmpeg` needed.

!!! note "Repairing after power loss is automatic"
    Takes interrupted by a power loss are repaired **by the camera** the next time it starts with
    that card. This script is for player and uploader compatibility.

## Data from a USB capture

Videos captured over USB carry the motion data inside the video stream. Extract it into the usual
files:

```bash
python -m trinet_tools.extract_sei input.mp4 --out my_recording/
# -> my_recording/video.mp4, video.imu, video.vts
```

## Record from a computer { #record-from-a-computer }

With the camera in [USB webcam mode](../get-started/modes.md), record video plus embedded motion
data directly on a computer:

```bash
python scripts/record_uvc.py --list                       # find the camera
python scripts/record_uvc.py -o captures/ -d 60           # record 60 seconds
```

Options include `--device`, `--width`, `--height` and `--fps`. Stereo cameras record both eyes.
