---
title: Record and review
description: Record Trinet video, motion data and audio to your phone with the Trinet app, and review, share and manage recordings.
---

# Record and review

## Record

Open **Record** with the camera connected in USB webcam mode.

- The **live preview** shows the camera image with the measured frame rate. While recording, a
  **REC** timer runs.
- On **Trinet Stereo** and **Stereo GS**, the **LENS L / R** switch chooses which eye the preview
  shows. It only changes the display — recordings always keep both eyes.
- Image adjustments made during preview apply immediately.
- If the camera gets too warm, a **Camera cooling down** banner appears: recording pauses and
  resumes automatically when the camera has cooled.

Tap the record button to start and stop. Recordings are saved on the phone.

### What a phone recording contains

Each recording is a folder:

| File | Contains |
|---|---|
| `video.mp4` | Video (both eyes side by side on stereo cameras) and, on cameras with microphones, audio. Also carries the camera's identity and calibration. |
| `imu.bin` | Motion data |
| `frames.bin` | One timestamp per frame |
| `meta.json` | Recording details: camera, firmware, settings |

These use the same formats as card recordings; the [Python toolkit](../toolkit/index.md) and the
[SDK](../sdk/index.md) read both.

## Library

**Library** lists your recordings with thumbnails. Select one or several to delete, or open a
recording to **share**, **rename** or **delete** it.

## Review

Opening a recording starts the **player**:

- frame-accurate scrubbing — step through the video frame by frame;
- the **motion data overlay** shows the samples for the frame on screen;
- **Info** shows the recording's details;
- turn the phone to landscape for a larger view.
