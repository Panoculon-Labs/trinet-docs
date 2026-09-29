---
title: Calibration
description: Trinet camera and IMU calibration — per-unit factory calibration, reference calibrations, and how to get and use them.
---

# Calibration

A calibration describes a camera precisely: its lens (focal length, optical centre and fisheye
distortion), where the motion sensor sits relative to the camera, and the small fixed time offset
between camera and motion sensor. It is what turns pixels and motion samples into metric
measurements — for undistortion, stereo depth and visual-inertial odometry.

## What your camera comes with

| Camera | Calibration |
|---|---|
| **Trinet Stereo, Stereo GS** | **Calibrated individually at the factory.** The calibration is stored on the camera and embedded in every recording. |
| **Trinet Mono** | Use the [reference calibration](reference-calibrations.md) for your hardware version. A per-unit calibration is available as an add-on **calibration service** — [contact us](../support/index.md). |

## Where to find a unit's calibration

- **In every recording.** Recordings carry the camera's stored calibration inside the video file,
  so a clip is usable for undistortion even on its own. The [toolkit](../toolkit/inspect-and-repair.md)
  reads it.
- **From the camera.** The [Trinet app](../app/camera-settings.md#advanced) can read the stored
  calibration (*Calibration → Read*), and apps can use the SDK's `getCalibration`.
- **As a file.** Where we hold your units' calibrations as files, they use the same JSON format as the
  reference calibrations, keyed by device ID.

Cameras can also store a calibration you provide: *Calibration → Upload from file* in the app, with
*Lock calibration* to prevent it being overwritten.

## Reference vs per-unit calibration

The [reference (batch) calibration](reference-calibrations.md) is a representative calibration for
each hardware version. Focal length, distortion, stereo baseline, camera–IMU rotation, lever arm and
time offset are very similar from unit to unit; the **optical centre** and, on stereo cameras, the
small **rotation between the two eyes** vary per unit.

| Use the reference calibration for | Use a per-unit calibration for |
|---|---|
| Mono units without the calibration service | Metric stereo depth |
| Quick starts, prototyping, simulation, dataset tooling | Visual-inertial odometry / SLAM at full accuracy |
| Initial values for online refinement | Anything needing sub-pixel accuracy |

Next: [Reference calibrations](reference-calibrations.md) · [Use a calibration](use-a-calibration.md)
