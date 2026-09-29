---
title: Trinet Mono
description: Trinet Mono — a single ultra-wide wearable camera with synchronized motion data and audio. Specifications and capabilities.
---

# Trinet Mono

Trinet Mono is a single ultra-wide camera that records 1080p video, motion data and stereo audio
on one shared clock. It records on its own to a memory card, streams live over USB to an Android
phone, a computer or an iPhone, and can join other Trinet cameras in a synchronized kit.

## Specifications

These values are for the current Trinet Mono (hardware version V4) with current firmware. Earlier
versions are listed [below](#earlier-versions).

<div class="spec-table" markdown>

| | |
|---|---|
| Video | 1920×1080, 30 fps |
| Codec | H.264 (default) or H.265 for card recordings; live USB stream is H.264 |
| Card bitrate | Variable, about 15 Mbps by default; adjustable in the [Trinet app](../app/camera-settings.md) |
| Storage | About 7 GB per hour at default settings |
| Lens | Ultra-wide fisheye; effective field of view about 139° horizontal × 73° vertical (from calibration) |
| Frame timing | Every frame timestamped at the middle of its exposure, on the camera clock |
| Motion sensing | 3-axis accelerometer (±8 g), 3-axis gyroscope (±2000 °/s) at 400 Hz; 3-axis magnetometer at about 100 Hz |
| Audio | Stereo microphones, AAC, 48 kHz by default (16, 44.1 or 48 kHz selectable) |
| IMU–video alignment | Sub-millisecond, hardware-timestamped |
| Recording to card | One button; up to 8 hours per take (the take is then saved automatically) |
| Live streaming | USB webcam mode (Android, computer) and iPhone mode |
| Wireless | Multi-camera sync; recording-status broadcast readable by the Trinet app |
| Calibration | Reference (batch) calibration for the model; per-unit calibration available as a service |
| Power | USB-C, 5 V |

</div>

## What you get in a recording

A card recording is a set of files that belong together: the video (`.mp4`), the motion data
(`.imu`) and the per-frame timestamps (`.vts`). The video file also carries the camera's identity
and calibration. See [Files on the card](../get-started/files-on-the-card.md) and
[File formats](../data/file-formats.md).

## Heat

During long recordings in warm conditions the camera may reach its temperature limit. It then saves
the current take and pauses; the light stays blue. Once it has cooled, recording resumes by itself
as the next part of the same session. See [Heat and thermal protection](../power-and-care/thermal.md).

## Earlier versions

| Version | What's different |
|---|---|
| V1, V2 | Original Trinet. ~180° lens. Motion data at about 560–570 Hz, no magnetometer data, no audio. |
| V3 | Adds a live magnetometer and 400 Hz motion data. Shipped with a ~180° or a ~150° lens. No audio. |
| V4 (current) | Adds stereo audio and mid-exposure frame timing. ~150° class lens. |

All versions work with the current [Trinet app](../app/index.md), [SDK](../sdk/index.md) and
[Python toolkit](../toolkit/index.md); features a camera doesn't have are simply not offered. To
find your version, see [Which camera do I have?](which-camera.md)
