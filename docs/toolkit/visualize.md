---
title: Visualize and check sync
description: Render Trinet recordings with motion plots, play kit cameras side by side on one timeline, and verify motion–video alignment.
---

# Visualize and check sync

## One recording with motion plots

```bash
python scripts/visualize.py path/to/recording1_1.mp4
# -> path/to/recording1_1_viz.mp4
```

Renders the video with live plots of the motion data underneath. Choose plots with `--plots` (for
example `orientation,accel,gyro`), a time range with `--start` / `--end`, and the plot window with
`--window`.

## Several cameras on one timeline

For a [Wrist Kit](../products/wrist-kit.md) take, `sync_view.py` renders every camera side by side,
with each frame placed on the kit's shared clock — the same instant lines up across panels, and the
header shows the live camera-to-camera offset.

```bash
python scripts/sync_view.py head.mp4 wristL.mp4 wristR.mp4 -o take_sync.mp4

# or let it group cameras by take automatically
python scripts/sync_view.py --auto path/to/recordings -o take_sync.mp4

# preview in a window instead of writing a file
python scripts/sync_view.py head.mp4 wristL.mp4 --show
```

| Option | Does |
|---|---|
| `--imu` | Draws each camera's accelerometer and gyroscope under its panel, on the same timeline |
| `--audio master` | Adds a soundtrack (`none`, `master`, `mix`, or a panel number) |
| `--rotate180 0,2` | Flips panels for cameras mounted upside down (common on wrists) |
| `--imu-h`, `--imu-window` | Plot height and visible time span |

To also draw **each camera's orientation**, use `sync_view_imu.py` with a calibration file:

```bash
python scripts/sync_view_imu.py head.mp4 wristL.mp4 wristR.mp4 --calib calibration.json -o take_oriented.mp4
```

!!! tip "Audio is for listening, not for sync"
    The soundtrack follows the video file's own audio alignment. For timing, the frame timestamps are
    the reference.

## Checking motion–video alignment yourself

A common mistake is to measure alignment against the video's playback timestamps or the arrival time
at a computer — that can appear to show tens of milliseconds of "latency" that isn't in the data.
Always compare against the recorded frame timestamps. The toolkit's
[IMU–video sync guide](https://github.com/Panoculon-Labs/Trinet-tools/blob/main/docs/imu_video_sync.md)
explains the pitfalls and includes a verification script you can run on your own clips. Background:
[Timing and sync](../data/sync.md).
