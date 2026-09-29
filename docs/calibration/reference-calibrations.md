---
title: Reference calibrations
description: Reference (batch) camera and IMU calibrations for every Trinet hardware version, V1–V6, and their JSON format.
---

# Reference calibrations

The public [Trinet-BatchCalibrations](https://github.com/Panoculon-Labs/Trinet-BatchCalibrations)
repository has one reference calibration per hardware version (two for V3, one per lens).

| Version | Product | Camera | File |
|---|---|---|---|
| V1 | Trinet Mono (original) | mono, ~180° lens | `mono/V1/trinet_V1_batch_calibration.json` |
| V2 | Trinet Mono (original) | mono, ~180° lens | `mono/V2/trinet_V2_batch_calibration.json` |
| V3 | Trinet Mono | mono, ~180° lens | `mono/V3/trinet_V3_180deg_batch_calibration.json` |
| V3 | Trinet Mono | mono, ~150° lens | `mono/V3/trinet_V3_150deg_batch_calibration.json` |
| V4 | Trinet Mono | mono, ~150° lens | `mono/V4/trinet_pro_mono_V4_batch_calibration.json` |
| V5 | Trinet Stereo | stereo, rolling shutter | `stereo-rs/V5/trinet_pro_stereo_V5_batch_calibration.json` |
| V6 | Trinet Stereo GS | stereo, global shutter | `stereo-gs/V6/trinet_pro_stereo_gs_V6_batch_calibration.json` |

!!! warning "Use the file for your version"
    Calibrations of different versions are **not interchangeable** — in particular the camera–IMU
    time offset differs between versions, and Stereo (V5) and Stereo GS (V6) calibrations differ even
    though both have a 70 mm baseline. See [Which camera do I have?](../products/which-camera.md)

## Typical unit-to-unit spread

| Version | Focal length (1 SD) | Optical centre (1 SD) | Relative rotation between eyes (median / 95th pct) | Baseline (1 SD) |
|---|---|---|---|---|
| V3 (~180°) | ±3 px | ±10–17 px | — | — |
| V5 | ±2 px | ±30–40 px | 0.45° / 1.2° | ±0.4 mm |
| V6 | ±4 px | ±30–65 px | 0.7° / 1.6° | ±0.8 mm |

For stereo, 0.1° of relative rotation shifts the image by about 1 pixel — so for metric depth,
rectify with the unit's own factory calibration.

## File format

All files are JSON. Units: **pixels** for intrinsics, **metres** for translations, **seconds** for
time offsets. Every file repeats its conventions in a `conventions` block.

=== "Mono (`trinet-mono-calibration/1`)"

    ```jsonc
    {
      "format": "trinet-mono-calibration/1",
      "hardware": "Trinet Pro Mono",
      "hardware_version": "V4",
      "calibration_type": "batch",
      "lens": "~150° fisheye",
      "shutter": "rolling",
      "calibration_date": "2026-09-26",
      "conventions": { ... },
      "intrinsics": {
        "image_size": [1920, 1080],
        "model": "equidistant",
        "fx": 871.03, "fy": 872.44, "cx": 965.76, "cy": 551.46,
        "distortion": [k1, k2, k3, k4]
      },
      "T_cam_imu": [[...4x4...]],
      "timeshift_cam_imu_s": 0.00647,
      "imu": { "rate_hz": 400.25, "gyro_noise_density": ..., "gyro_random_walk": ...,
               "accel_noise_density": ..., "accel_random_walk": ... }
    }
    ```

=== "Stereo (`trinet-stereo-calibration/1`)"

    ```jsonc
    {
      "format": "trinet-stereo-calibration/1",
      "hardware": "Trinet Pro Stereo",
      "hardware_version": "V5",
      "calibration_type": "batch",
      "shutter": "rolling",
      "cameras": [
        { "intrinsics": { ...left eye, as mono... }, "timeshift_cam_imu_s": 0.0035 },
        { "intrinsics": { ...right eye... },         "timeshift_cam_imu_s": 0.0035 }
      ],
      "T_cam1_cam0": [[...4x4...]],
      "T_cam0_imu":  [[...4x4...]],
      "imu": { ... },
      "rolling_shutter": {                      // Stereo (V5) only
        "readout_time_s": 0.0318,
        "line_delay_s": 2.94e-05,
        "timestamp_reference": "centre image row, mid-exposure"
      }
    }
    ```

    Stereo GS (V6) has no `rolling_shutter` block; its `timestamp_reference` is `mid-exposure`.

The `hardware` field uses the internal model names: *Trinet Pro Mono* = Trinet Mono V4, *Trinet Pro
Stereo* = Trinet Stereo, *Trinet Pro Stereo GS* = Trinet Stereo GS.

Calibrations are for **1920×1080 per camera** (per eye on stereo). Conventions and tools:
[Use a calibration](use-a-calibration.md).

## Versioning

Files are updated in place when a version's calibration is revised; every revision is recorded in
the repository's changelog, and each file's `calibration_date` gives the date of its current revision.
