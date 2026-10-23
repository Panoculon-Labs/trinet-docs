---
title: Visualize and check sync
description: Check Trinet recordings and kit takes for frame drops, frame rate and sync, render them with motion plots, and play kit cameras side by side on one timeline.
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

## Check a recording or kit take { #check-a-recording-or-kit-take }

`check_recording.py` prints a quality report for a single recording, a stereo take or a whole
[Wrist Kit](../products/wrist-kit.md) take:

```bash
# one recording (for a stereo camera, either eye — both are checked)
python scripts/check_recording.py path/to/recording1_1.mp4

# a kit: one folder per camera; takes are matched by their grp number
python scripts/check_recording.py my-session/head my-session/left my-session/right

# one take only, and the full report as JSON
python scripts/check_recording.py my-session/head my-session/left my-session/right \
    --take grp143024 --json report.json
```

For each video stream (each eye of a stereo camera):

| Figure | Means |
|---|---|
| Frames, dropped | Frames recorded, in the `.vts` and in the `.mp4`; frames missing inside the take. Timestamp steps in the first second of a kit take, while the camera joins the kit's clock, are listed separately as *start-up* and are not losses. |
| fps | Measured from the frame timestamps — 30 for a camera on its own, about 29.7 in a kit (see below) |
| Duration | First to last frame, and the `.mp4`'s own length |
| Bitrate, codec, audio | From the `.mp4` (needs `ffprobe`) |
| Data embedded in mp4 | Whether the motion data and timestamps are also inside the `.mp4` ([TMF](../data/metadata.md)) |
| Motion | `.imu` samples, rate and longest gap |

For a kit take it adds, per camera:

| Figure | Means |
|---|---|
| Synced | The camera's timestamps are on the kit's shared clock |
| Frame alignment | How far apart each frame was captured from the matching frame of the kit's master camera — median, 95th percentile and maximum, leaving out the first 2 seconds (`--skip`). Typically well under 1 ms. A larger value means frames were captured at slightly different instants; their timestamps still say exactly when, so data still lines up by time. |
| Left / right eyes | The same, between the two eyes of a stereo camera |

The report ends with **OK** or a list of **WARN** / **FAIL** lines, and the script exits with status
1 if anything was flagged, so it can gate a batch.

!!! note "Kit takes record at about 29.7 fps — on purpose"
    In a kit, every camera records at the same, slightly lower frame rate — about **29.7 fps**
    (a frame every 33.7 ms instead of 33.3 ms) — so each camera can hold its frames in step with the
    kit's master camera. This is intentional and the same on every camera of the kit. A camera
    recording on its own runs at 30 fps.

## Several cameras on one timeline

For a [Wrist Kit](../products/wrist-kit.md) take, `sync_view.py` renders every camera side by side,
with each frame placed on the kit's shared clock — the same instant lines up across panels, and the
header shows the live camera-to-camera offset.

!!! tip "Just recorded with a kit?"
    [View a kit take in sync](kit-takes.md) walks through it from the memory cards: matching takes by
    their `grp` number, telling cameras apart, and rendering a stereo head with two wrists.

```bash
python scripts/sync_view.py head.mp4 wristL.mp4 wristR.mp4 -o take_sync.mp4

# or let it group Mono cameras by take automatically (one folder, .json sidecars)
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
