---
title: File formats
description: Overview of the Trinet recording formats — .imu motion data, .vts frame timestamps, embedded metadata and calibration — with links to the full specifications.
---

# File formats

Trinet formats are open, versioned and fully documented. This page is an overview; the complete
byte-level specification is maintained with the Python toolkit:
**[Trinet recording data formats](https://github.com/Panoculon-Labs/Trinet-tools/blob/main/docs/data_formats.md)**.

## Compatibility promise

Every file begins with a short text identifier and a **format version**. Newer versions only use
bytes that were previously zero, so:

- current readers parse every version ever written;
- older readers can still read newer files (they see the new fields as zeros).

## `.imu` — motion data

A 64-byte header followed by one fixed-size record per motion sample.

| Header gives you | |
|---|---|
| Format version | 1–6 (6 on current cameras) |
| **Sample rate** | Nominal rate of this recording — **always read it from here** |
| Accelerometer and gyroscope ranges | e.g. ±8 g, ±2000 °/s |
| Start times | First sample and first video frame, on the camera clock |
| Device ID | The camera's public 128-bit identifier |

Each sample holds its **timestamp** (nanoseconds, camera clock), **acceleration** (m/s², gravity
included), **angular rate** (rad/s), **magnetic field** (µT, on cameras with a live magnetometer),
**sensor temperature**, and the age of the magnetometer reading.

| Version | Cameras | What changed |
|---|---|---|
| 1–2 | Early firmware | Shorter samples |
| 3–4 | V1/V2 | Current 80-byte sample; device ID in the header |
| 5 | V3 | Live magnetometer |
| 6 | V4, Stereo, Stereo GS | Mid-exposure frame timing (the change is in the `.vts`; the `.imu` layout is the same) |

## `.vts` — frame timestamps

One entry per encoded video frame.

| Version | What each entry adds |
|---|---|
| 1 | Frame number and frame timestamp |
| 2–3 | Link to the encoded video packet; multi-camera clock information in the header |
| 4 | Exposure time, rolling-shutter readout time and flags; the timestamp is **mid-exposure** (centre row on rolling-shutter cameras) |
| 5 | The frame's offset to the kit's shared clock (multi-camera takes) and a flag for frames recorded before the kit had locked |

Global-shutter cameras report a readout time of zero.

## Inside the video file

The `.mp4` carries:

- the video (H.264 or H.265) and, on cameras with microphones, an AAC audio track;
- an **embedded metadata track** with the device ID, firmware and camera generation, calibration,
  and the motion and timing data — so a clip remains usable on its own.

Streams sent over USB also carry the motion data inside the video, one packet per frame; the app, SDK
and toolkit turn it back into `.imu` and `.vts` files.

## Calibration

Calibration comes as JSON (`calibration.json` or the
[reference calibration files](../calibration/reference-calibrations.md)): intrinsics with an
equidistant (Kannala-Brandt) fisheye model, camera–IMU rotation and position, and the camera–IMU
time offset. See [Calibration](../calibration/index.md).

## Device ID

Every camera has a public 128-bit identifier, written into every recording. The first eight
characters are used as the camera's short ID in the app (for example in
[Wireless status](../app/wireless-status.md)).

## Reading the files

- **Python:** `trinet_tools.reader` in the [toolkit](../toolkit/index.md) reads every version.
- **Android / iOS:** the [SDK](../sdk/index.md) includes readers for the same files.
