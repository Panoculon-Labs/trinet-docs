---
title: Use a calibration
description: Conventions of Trinet calibrations, exporting to Kalibr / OpenVINS / VINS-Fusion / Basalt, undistorting and rectifying with OpenCV, and refining online.
---

# Use a calibration

## Conventions

- **Camera model:** pinhole projection with **equidistant (Kannala-Brandt) fisheye distortion**,
  `distortion = [k1, k2, k3, k4]` — OpenCV's `cv2.fisheye` model and Kalibr's `pinhole-equi`.
- **Camera frame:** x right, y down, z forward (along the optical axis).
- **`T_cam_imu` / `T_cam0_imu`:** 4×4 transform mapping a point from the IMU frame into the camera
  frame, `p_cam = T_cam_imu · p_imu`. Its translation column is the IMU origin in the camera frame.
- **`T_cam1_cam0`:** maps a point from the left eye (cam0) into the right eye (cam1). Its translation is
  about (−0.070, 0, 0) m: the right eye sits 70 mm to the right.
- **Stereo eyes:** cam0 = the wearer's **left** eye = the left half of a side-by-side frame
  (x = 0…1919); cam1 = the right eye = the right half (x = 1920…3839). On card recordings the eyes
  are separate `_L` and `_R` files.
- **Time offset:** `t_imu = t_cam + timeshift_cam_imu_s` — add the time shift to put a camera
  timestamp on the IMU clock. Same sign convention as Kalibr's `timeshift_cam_imu`.
- **Frame timestamps:** Stereo (V5) timestamps refer to the **centre image row at mid-exposure**;
  row `r` of a frame was exposed at `t_frame + (r − 540) · line_delay_s`. Stereo GS (V6) exposes all
  rows together; timestamps are mid-exposure.
- **IMU noise:** continuous-time noise densities and random walks (Kalibr / OpenVINS convention),
  conservative defaults suited to VIO.
- **Resolution:** all values are for 1920×1080 per camera. If you scale images, scale `fx, fy, cx, cy`
  by the same factor; distortion coefficients are unchanged.

## Export to Kalibr / OpenVINS / VINS-Fusion / Basalt

From the [Trinet-BatchCalibrations](https://github.com/Panoculon-Labs/Trinet-BatchCalibrations)
repository (Python 3):

```bash
python3 tools/to_kalibr_yaml.py stereo-rs/V5/trinet_pro_stereo_V5_batch_calibration.json out/
# -> out/camchain-imucam.yaml  out/imu.yaml

python3 tools/to_kalibr_yaml.py mono/V4/trinet_pro_mono_V4_batch_calibration.json out/ \
    --cam-topics /cam0/image_raw --imu-topic /imu0
```

## Undistort (mono) or rectify (stereo) with OpenCV

Needs `numpy` and `opencv-python`:

```bash
python3 tools/undistort_example.py mono/V4/trinet_pro_mono_V4_batch_calibration.json frame.png undistorted.png
python3 tools/undistort_example.py stereo-gs/V6/trinet_pro_stereo_gs_V6_batch_calibration.json sbs.png rectified.png
```

The stereo example splits a side-by-side frame, rectifies both eyes with
`cv2.fisheye.stereoRectify`, draws horizontal check lines and prints the `Q` matrix for
disparity-to-depth. Options `--balance` and `--fov-scale` control how much of the fisheye image is
kept.

## Refine online

The quantities that vary per unit are cheap to refine while running:

- **Stereo relative rotation:** pitch and roll between the eyes are observable from the vertical
  disparity of matched features in any scene; yaw from distant features, or from a VIO with online
  camera–IMU extrinsic refinement (for example OpenVINS or Basalt). Keep intrinsics and baseline fixed.
- **Optical centre:** refine together with the camera–IMU extrinsics in your VIO, or use a per-unit
  calibration.

## With the toolkit

The [Python toolkit](../toolkit/index.md) reads the calibration embedded in recordings, uses it for
[MCAP export](../toolkit/mcap.md) and [OpenVINS configuration](../toolkit/stereo-and-3d.md), and its
[SD-card ingest](../toolkit/ingest.md) folds a calibration file into delivery metadata.
