---
title: Trinet Stereo
description: Trinet Stereo — a 70 mm stereo wearable camera with rolling-shutter sensors, synchronized motion data and per-unit factory calibration.
---

# Trinet Stereo

Trinet Stereo has two ultra-wide cameras 70 mm apart, recording both eyes together with motion
data and audio on one clock. Every unit is calibrated individually at the factory, so recordings are
ready for stereo depth, 3D reconstruction and stereo visual-inertial odometry.

<figure markdown>
  ![Trinet Stereo worn on a head strap](../assets/images/stereo-gs-head-mount.webp){ width="360" loading=lazy }
  <figcaption>A Trinet stereo camera on the head strap.</figcaption>
</figure>

## Specifications

<div class="spec-table" markdown>

| | |
|---|---|
| Cameras | 2, baseline 70 mm |
| Sensors | 3 MP rolling shutter, recorded at 1920×1080 per eye |
| Frame rate | 30 fps (nominal) |
| Codec | H.264 (default) or H.265 for card recordings (firmware 0.5.7 or newer); live USB stream is H.264 |
| Card bitrate | Constant 10 Mbps per eye |
| Storage | About 10 GB per hour (both eyes, audio and motion data) |
| Lens | Ultra-wide fisheye; effective field of view about 158° horizontal × 94° vertical per eye (from calibration) |
| Frame timing | Timestamped at mid-exposure of the centre image row; rolling-shutter readout about 32 ms, reported per frame |
| Motion sensing | 3-axis accelerometer (±8 g), 3-axis gyroscope (±2000 °/s) at 400 Hz; 3-axis magnetometer at about 100 Hz |
| Audio | Stereo microphones, AAC, 44.1 kHz on card recordings |
| IMU–video alignment | Sub-millisecond, hardware-timestamped |
| Recording to card | One button; no limit on take length |
| Live streaming | USB webcam mode: one 3840×1080 side-by-side stream (both eyes) to Android or a computer |
| Wireless | Multi-camera sync; recording-status broadcast readable by the Trinet app |
| Calibration | Every unit calibrated at the factory; stored on the camera and embedded in every recording |
| Weight | About 51 g |
| Power | USB-C, 5 V; a supply of 1 A or more is recommended |

</div>

## Recordings

Each take is saved as two video files — one per eye — plus timestamps for each eye and one motion
data file:

```text
Trinet/recording/take0001_L.mp4    left eye
Trinet/recording/take0001_R.mp4    right eye
Trinet/recording/take0001_L.vts    left-eye frame timestamps
Trinet/recording/take0001_R.vts    right-eye frame timestamps
Trinet/recording/take0001.imu      motion data
```

Both video files carry the camera's identity and its factory calibration. See
[Files on the card](../get-started/files-on-the-card.md).

## Heat

Trinet Stereo does not pause for heat when used on its own. If it reaches its critical temperature
it saves both eyes, the light shows solid red for about two seconds, and the camera switches off.
Reconnect power to start again. In a [Wrist Kit](wrist-kit.md), a kit-wide cooling pause is used
instead. See [Heat and thermal protection](../power-and-care/thermal.md).

!!! info "iPhone"
    Trinet Stereo streams in USB webcam mode only. iPhone streaming is available on Trinet Mono.
