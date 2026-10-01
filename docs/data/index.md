---
title: Your data
description: What a Trinet recording contains — video, motion data and per-frame timestamps on one shared clock — and how to use it.
---

# Your data

Every Trinet recording is a **synchronized set** of three streams, all timestamped on the same
camera clock:

| Stream | What it is | Rate |
|---|---|---|
| **Video** | H.264 or H.265, 1920×1080 per camera (per eye on stereo) | 30 fps |
| **Motion (IMU)** | Accelerometer, gyroscope, magnetometer, sensor temperature | 400 Hz (about 560–570 Hz on V1/V2) |
| **Frame timestamps** | One timestamp per video frame, at the middle of its exposure | One per frame |

Plus **audio** on cameras with microphones, and the camera's **identity and calibration** inside
the video file.

## One clock

The camera keeps one steadily increasing clock and stamps everything against it: each motion sample
at the moment it was measured, and each video frame at the middle of its exposure. Lining up motion
with video is therefore just comparing timestamps — no separate sync signal to decode. See
[Timing and sync](sync.md).

!!! warning "Don't align with video playback times"
    Use the frame timestamps the camera records, not the video container's playback timestamps or
    your computer's clock — those carry buffering and transport jitter of milliseconds.

## Where recordings come from

| How you recorded | What you get |
|---|---|
| **Card recording** (button) | `.mp4` + `.imu` + `.vts` in the `Trinet` folder — see [Files on the card](../get-started/files-on-the-card.md) |
| **Trinet app** / SDK over USB | A folder with `video.mp4`, `imu.bin`, `frames.bin`, `meta.json` — see [Record and review](../app/record-and-review.md) |
| **Computer** (toolkit USB recorder) | The same set of files, reconstructed from the live stream |

Over USB, the motion data travels inside the video stream; the app, SDK and toolkit separate it back
into the same set of files, so every tool reads every recording the same way.

## Self-describing

- Every file states its **format version** in its header, and readers handle every version — so
  recordings from older cameras and firmware keep working.
- The video file carries the camera's **device ID** and **calibration**, so a clip is usable even if
  it gets separated from its folder.
- The motion data file records its own **sample rate** — always read it from there rather than
  assuming a value.

## Working with your data

No camera yet? Download real recordings from the [sample data](sample-data.md) page.

- [Python toolkit](../toolkit/index.md) — inspect, repair, visualize, export to MCAP / ROS 2.
- [Calibration](../calibration/index.md) — intrinsics, camera–IMU extrinsics and time offset.
- [File formats](file-formats.md) — layouts, versions and the full byte-level specifications.
