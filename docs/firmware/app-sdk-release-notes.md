---
title: App, SDK and toolkit release notes
description: What's new in the Trinet Android app and SDK, the iOS SDK, the Python toolkit and the reference calibrations.
---

# App, SDK and toolkit release notes

## Trinet app and Android SDK

The Trinet app, the Android SDK and the SDK demo app share one version number. Get the app from
[Google Play](https://play.google.com/store/apps/details?id=com.panoculonlabs.trinet); the SDK and demo
APK are on [GitHub Releases](https://github.com/Panoculon-Labs/Trinet-SDK/releases).

### 0.5.3 — 28 September 2026 { #053 }

- New **[Wireless status](../app/wireless-status.md)**: see every nearby camera and kit recording to
  its card, sorted by distance, with take times in UTC, model and firmware, and alerts for unexpected
  stops or a missing card. Background logging and history export for the
  [wireless UTC tool](../toolkit/wireless-utc.md).
- New wireless broadcast switch in Camera settings.
- Needs camera firmware 0.5.9 or newer for wireless features.

### 0.5.2 — 24 September 2026 { #052 }

- Support for **Trinet Stereo GS**: preview, recording and stereo calibration. Recordings note
  whether the shutter is global or rolling.

### 0.5.1 — 14 September 2026 { #051 }

- Choose **H.264 or H.265** for the camera's card recordings (needs camera firmware 0.5.7).
- Updated for Android 16.

### 0.5.0 — 8 September 2026 { #050 }

- **Trinet Stereo** support: left/right lens switch in the preview, recordings keep both eyes, and
  stereo calibration can be read and uploaded. (Released to Google Play as part of 0.5.1.)

### 0.4.3 — 23 August 2026 { #043 }

- Stability fix.

### 0.4.2 — August 2026 { #042 }

- Shorter minimum exposure (0.05 ms).
- Reliable automatic reconnect when the camera is plugged back in.

### 0.4.1 — 21 August 2026 { #041 }

- Recordings carry the camera's identity and calibration inside the video file.
- Settings are confirmed with the camera; new *Restore defaults*.
- Redesigned dark interface, library thumbnails, and a bitrate slider with presets.
- The update screen checks for firmware automatically.

### 0.4.0 { #040 }

- Works with firmware that uses the newer USB transfer mode; live stream-health indicator; more
  robust decoding on more phones. (Not released to Google Play.)

### 0.3.0 — 13 July 2026 { #030 }

- Microphone audio in recordings, with gain, mute, automatic gain and sample-rate controls.
- Live image adjustments.
- Keyframe interval, IMU stream and calibration-lock settings.
- Reliable reconnect.

### 0.2.2 — 29 June 2026 { #022 }

- Exposure range and Location (50/60 Hz mains) settings to remove flicker.

### 0.2.1 — 23 June 2026 { #021 }

- Card-recording option in Boot mode, with plain-language explanations of each mode.

### 0.2.0 — 23 June 2026 { #020 }

- Upload a `calibration.json` to the camera.
- Automatic pause and resume while the camera cools.
- Bitrate and CBR/AVBR control.
- The library handles large recordings.

### 0.1.5 — 28 May 2026 { #015 }

- Fixed recordings that started mid-stream.
- Playback seek bar and orientation cube stay locked to the frame shown.

### 0.1.4 — 24 May 2026 { #014 }

- In-app firmware update.

## iOS SDK

The iOS SDK is at **0.2.1** (23 June 2026). See [iOS SDK](../sdk/ios.md).

## Python toolkit (Trinet-tools)

[Trinet-tools](https://github.com/Panoculon-Labs/Trinet-tools) is updated continuously on its `main`
branch.

- **September 2026** — New [wireless UTC tool](../toolkit/wireless-utc.md): combines the app's
  wireless status export with card recordings and gives every take, and optionally every frame, a UTC
  time with an error estimate; corrects for an inaccurate phone clock (in a field check, three
  cameras agreed within 0.32 ms). Shows each camera's model and firmware. Adds a reader for a
  recording's embedded metadata. Stereo recording over USB for Stereo and Stereo GS, and
  [MCAP export](../toolkit/mcap.md) for stereo and single-camera recordings.
- **August 2026** — [SD-card ingest](../toolkit/ingest.md) to upload-ready packages; support for the
  newer timestamp file version; sturdier orientation fusion.

## Reference calibrations (Trinet-BatchCalibrations)

- **26 September 2026** — Initial release: [reference calibrations](../calibration/reference-calibrations.md)
  for every hardware version, V1–V6 (two for V3, one per lens), with Kalibr / OpenVINS export and
  undistort / rectify examples.
