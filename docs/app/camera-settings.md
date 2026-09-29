---
title: Camera settings
description: Every Trinet camera setting in the app — picture, sound, video bitrate and codec, wireless broadcast, boot mode, calibration and restore defaults.
---

# Camera settings

Settings are stored **on the camera**, so they stay with it whichever phone or computer you use. On
Trinet Mono they apply to card recordings as well as USB streaming. Settings a camera's firmware
doesn't support yet are shown with *Update the camera firmware to enable them*.

## Picture

Brightness, contrast, saturation, sharpness, gain, white balance (automatic or a colour
temperature), manual exposure, and the status light.

## Sound

On cameras with microphones: mute, automatic gain, gain level and sample rate (16, 44.1 or 48 kHz).

## Video

| Setting | What it does |
|---|---|
| **Bitrate** | 1–20 Mbps (0.5 Mbps steps), with constant (CBR) or variable (AVBR) rate control. The camera restarts to apply it. Stereo card recordings always use 10 Mbps per eye. |
| **Recording codec** | **H.264** or **H.265** for recordings the camera writes to its own card. Applies from the next take, no restart. The live USB stream is always H.264. Needs camera firmware 0.5.7 or newer on stereo cameras (0.5.9 on Mono). |
| **Exposure range** | Minimum and maximum exposure time. |
| **Location** | Mains frequency, 50 or 60 Hz, to avoid flicker under artificial light. Choose your country's mains frequency. |

!!! tip "H.264 or H.265?"
    H.264 plays everywhere and decodes fastest — the best default for data pipelines. H.265 gives
    smaller files at the same quality if your tools support it.

## Wireless

**Broadcast recording status** — lets phones follow the camera's recording status over Bluetooth
while it records to its card (see [Wireless status](wireless-status.md)). On by default with
firmware 0.5.9 or newer; the camera applies a change from its next start.

## Advanced

| Setting | What it does |
|---|---|
| **Keyframe interval (GOP)** | 1–600 frames; default 30 (one keyframe per second). The camera restarts to apply it. |
| **Embed IMU samples** | Carry motion data inside the video stream (on by default; needed by the app and SDK). |
| **Calibration** | *Read* the calibration stored on the camera, *Upload from file* (a `calibration.json`), or *Lock calibration* so it can't be overwritten. |
| **Boot mode** | The mode the camera starts in when **no card** is inserted: USB webcam, iPhone or card recording. The camera restarts. See [Recording modes](../get-started/modes.md). |
| **Restore defaults** | Returns picture, sound and video settings to the factory defaults. Keeps the boot mode, calibration and kit pairing. |
