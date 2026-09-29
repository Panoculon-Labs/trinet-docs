---
title: Products
description: The Trinet camera family — Mono, Stereo, Stereo GS and the Wrist Kit — compared side by side.
---

# Trinet cameras

Trinet cameras are small wearable cameras that record video together with high-rate motion
(IMU) data and audio, all timestamped on one shared clock. They are built for egocentric
("first-person") data collection: robot learning from human demonstration, visual-inertial
odometry and SLAM, and research on how people move and use their hands.

Every Trinet camera can:

- record on its own to a memory card with one button — no phone or computer needed;
- stream live over USB to an Android phone, a computer or (Mono) an iPhone;
- join other Trinet cameras in a wirelessly synchronized kit.

## Compare

| | Trinet Mono | Trinet Stereo | Trinet Stereo GS | Trinet Wrist Kit |
|---|---|---|---|---|
| Cameras | 1 | 2, 70 mm apart | 2, 70 mm apart | 3 (head + both wrists) |
| Shutter | Rolling | Rolling | **Global** | Per camera |
| Recording | 1920×1080, 30 fps | 1920×1080 per eye, 30 fps | 1920×1080 per eye, 30 fps | Per camera |
| Lens | Ultra-wide fisheye | Ultra-wide fisheye | Ultra-wide fisheye | Per camera |
| Motion sensing | Accelerometer, gyroscope, magnetometer | Accelerometer, gyroscope, magnetometer | Accelerometer, gyroscope, magnetometer | On every camera |
| Audio | Stereo microphones | Stereo microphones | Stereo microphones | Per camera |
| Card storage (default settings) | ≈7 GB per hour | ≈10 GB per hour | ≈10 GB per hour | Per camera |
| Factory calibration | Reference calibration; per-unit on request | Every unit | Every unit | Per camera |
| USB live stream | Android, computer, iPhone | Android, computer | Android, computer | Per camera |
| Multi-camera sync | ✓ | ✓ | ✓ | Built in |

Details for each product:

<div class="grid cards" markdown>

- [:material-camera-iris: **Trinet Mono**](mono.md) — single camera
- [:material-camera-burst: **Trinet Stereo**](stereo.md) — stereo, rolling shutter
- [:material-camera-control: **Trinet Stereo GS**](stereo-gs.md) — stereo, global shutter
- [:material-hand-back-right: **Trinet Wrist Kit**](wrist-kit.md) — three synchronized cameras

</div>

!!! tip "Which one should I choose?"
    - **Monocular data, lowest storage per hour:** Trinet Mono.
    - **Depth, 3D reconstruction or stereo SLAM:** Trinet Stereo.
    - **Fast motion close to the camera** — hands, tools, quick head turns — where rolling-shutter
      skew matters: Trinet Stereo GS.
    - **Bimanual manipulation data** with views of both hands: the Trinet Wrist Kit.

    For purchasing and availability, see [panoculonlabs.com/trinet](https://www.panoculonlabs.com/trinet)
    or email [innovate@panoculonlabs.com](mailto:innovate@panoculonlabs.com).
