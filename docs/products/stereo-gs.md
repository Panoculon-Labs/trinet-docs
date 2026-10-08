---
title: Trinet Stereo GS
description: Trinet Stereo GS — the 70 mm stereo wearable camera with global-shutter sensors, for fast motion without skew.
---

# Trinet Stereo GS

Trinet Stereo GS is the global-shutter version of [Trinet Stereo](stereo.md). Every row of the
image is exposed at the same instant, so fast hand, tool and head motion is captured without the
skew and wobble of a rolling shutter. Everything else — two eyes 70 mm apart, motion data, audio,
factory calibration, the app and the SDK — works exactly like Trinet Stereo.

<figure markdown>
  ![Trinet stereo camera, front view](../assets/images/product/stereo-front.webp){ .product-shot width="420" loading=lazy }
  <figcaption>Trinet Stereo GS shares the Trinet Stereo form factor: two lenses, 70 mm apart.</figcaption>
</figure>

## Specifications

<div class="spec-table" markdown>

| | |
|---|---|
| Cameras | 2, baseline 70 mm |
| Sensors | 2.3 MP **global shutter**, recorded at 1920×1080 per eye |
| Frame rate | 30 fps |
| Codec | H.264 (default) or H.265 for card recordings; live USB stream is H.264 |
| Card bitrate | Constant 10 Mbps per eye |
| Storage | About 10 GB per hour (both eyes, audio and motion data) |
| Lens | Ultra-wide fisheye; effective field of view about 180° horizontal × 96° vertical per eye (from calibration) |
| Frame timing | Whole frame exposed at once; timestamped at mid-exposure |
| Motion sensing | 3-axis accelerometer (±8 g), 3-axis gyroscope (±2000 °/s) at 400 Hz; 3-axis magnetometer at about 100 Hz |
| Audio | Stereo microphones, AAC, 44.1 kHz on card recordings; [hardware mute switch](../get-started/mute-switch.md) |
| IMU–video alignment | Sub-millisecond, hardware-timestamped |
| Recording to card | One button; no limit on take length |
| Live streaming | USB webcam mode: one 3840×1080 side-by-side stream (both eyes) to Android or a computer |
| Wireless | Multi-camera sync; recording-status broadcast readable by the Trinet app |
| Calibration | Every unit calibrated at the factory; stored on the camera and embedded in every recording |
| Weight | About 51 g |
| Power | USB-C, 5 V; a supply of 1 A or more is recommended |

</div>

## How to tell it apart

In software, recordings from a Stereo GS are marked as global shutter, and their per-frame timing
reports a rolling-shutter readout time of zero. The Trinet app's camera information and the SDK show
the camera model. See [Which camera do I have?](which-camera.md)

## Recordings, heat and everything else

Recording files, button, lights, heat behaviour and kit use are the same as
[Trinet Stereo](stereo.md). Keep the firmware current: Stereo GS firmware
[0.5.8 and later](../firmware/release-notes.md) include important image-quality and reliability
improvements.
