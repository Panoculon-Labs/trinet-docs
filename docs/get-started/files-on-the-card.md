---
title: Files on the card
description: Where Trinet recordings are saved on the memory card, what each file contains, and how takes are named.
---

# Files on the card

All recordings go in the `Trinet` folder on the memory card. A recording is a **set of files** —
keep them together.

| File | Contains |
|---|---|
| `.mp4` | The video (and audio on cameras with microphones). It also carries the camera's identity, calibration and a copy of the motion and timing data. |
| `.imu` | Motion data: accelerometer, gyroscope and magnetometer samples with timestamps. |
| `.vts` | One timestamp per video frame, on the same clock as the motion data. |
| `.json` | A small, human-readable summary of the recording: session and kit IDs, this camera's role and device ID. |

The `.imu` and `.vts` files are binary — open them with the [Python toolkit](../toolkit/index.md) or
the [SDK](../sdk/index.md). Their layout is documented in [File formats](../data/file-formats.md).

## Trinet Mono

```text
Trinet/
├── recording1_1.mp4
├── recording1_1.imu
├── recording1_1.vts
├── recording2_1.mp4
└── …
```

Files are named `recording<session>_<part>`. The session number increases with every take. A take
normally has one part; a new part is started when recording resumes after a
[cooling pause](../power-and-care/thermal.md) (`recording3_2`, `recording3_3`, …).

## Trinet Stereo and Stereo GS

```text
Trinet/recording/
├── take0001_L.mp4     left eye
├── take0001_R.mp4     right eye
├── take0001_L.vts     left-eye frame timestamps
├── take0001_R.vts     right-eye frame timestamps
├── take0001.imu       motion data
└── …
```

Left and right are as seen by the wearer.

## Kit recordings

Takes recorded in a [Wrist Kit](../products/wrist-kit.md) start with a shared kit prefix,
`grp<session>_<camera>_…`, so the files from each camera that belong to the same take are easy to
match.

## Other files

You may also see a few small files the camera uses for bookkeeping — for example a log written
after a cooling pause or an automatic shutdown, a timing-telemetry file (`.tel`) next to stereo
takes, or a temporary marker while a take is in progress. Leave them in place; the toolkit can use
them.

!!! tip "Copy the whole folder"
    When you back up or share recordings, copy the complete `Trinet` folder (or at least every file
    with the same name) so video, motion data and timestamps stay together.
