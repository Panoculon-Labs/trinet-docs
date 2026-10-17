---
title: Motion data axes
description: The axis convention of Trinet motion data (accelerometer, gyroscope, magnetometer) for every camera — Mono V1–V4, Stereo and Stereo GS — and how to rotate it into the camera frame.
---

# Motion data axes

Trinet cameras record motion data in the **motion sensor's own frame**, exactly as the sensor measures
it. The camera does not rotate or re-map the axes. Because the sensor sits differently on each
camera's board, the direction of x, y and z relative to the lens **depends on the camera model**. The
calibration's camera–IMU rotation is what links the two frames, and this page lists it for every
model.

## Conventions

| | |
|---|---|
| Frame | Right-handed |
| Accelerometer | m/s², **gravity included**. At rest, the axis pointing **up** reads about **+9.81** |
| Gyroscope | rad/s. Positive is counter-clockwise about the axis, seen from its tip (right-hand rule) |
| Magnetometer | µT, in its own frame (see [below](#magnetometer)) |
| Same frame for | `.imu` files, the motion data inside the video file, the live USB stream, the SDK and the [MCAP](../toolkit/mcap.md) `/imu` topic |

**Camera frame**, used in the table below: as seen from behind the camera, looking where the lens
looks, **x points right, y down and z forward** out of the lens. It's the image frame: x along the
image rows, y down the image. On stereo cameras it is the left eye (`_L`, `cam0`).

## Axes per camera

Where each motion-sensor axis points, in camera terms:

| Camera | Hardware version | IMU +x | IMU +y | IMU +z | Lens up, at rest |
|---|---|---|---|---|---|
| Trinet Mono (original) | V1, V2 | up | left | **backward** | z ≈ −9.8 |
| Trinet Mono | V3 | left | up | forward | z ≈ +9.8 |
| Trinet Mono | V4 | up | right | forward | z ≈ +9.8 |
| Trinet Stereo | V5 | down | left | forward | z ≈ +9.8 |
| Trinet Stereo GS | V6 | right | down | forward | z ≈ +9.8 |

The same as rotation matrices, `R_cam_imu`, which maps a vector from the IMU frame into the camera
frame (`v_cam = R_cam_imu · v_imu`):

| Camera | `R_cam_imu` (rounded) |
|---|---|
| Mono V1, V2 | `[[0,-1,0], [-1,0,0], [0,0,-1]]` |
| Mono V3 | `[[-1,0,0], [0,-1,0], [0,0,1]]` |
| Mono V4 | `[[0,1,0], [-1,0,0], [0,0,1]]` |
| Stereo V5 | `[[0,-1,0], [1,0,0], [0,0,1]]` |
| Stereo GS V6 | `[[1,0,0], [0,1,0], [0,0,1]]` |

These are the rounded rotations of the [reference calibrations](../calibration/reference-calibrations.md).
The true mounting is within a few degrees of them. For exact work, use the rotation from the
calibration itself. Stereo and Stereo GS cameras carry their own per-unit calibration; see
[Get your camera's calibration](../calibration/get-calibration.md). Not sure which hardware version
you have? See [Which camera do I have?](../products/which-camera.md)

!!! tip "Quick check"
    Record a few seconds with the camera on a table, lens pointing at the ceiling, and read the
    accelerometer with the [toolkit](../toolkit/inspect-and-repair.md). z reads about +9.8 m/s² on
    V3–V6, and about −9.8 on V1/V2.

## Rotate motion data into the camera frame

With the exact rotation from the camera's calibration:

```python
import json
import numpy as np
from trinet_tools.reader import read_imu

calib = json.load(open("calibration.json"))
T = (calib.get("T_cam0_imu")                                 # stereo
     or calib.get("T_cam_imu")                               # mono, reference file
     or calib["extrinsics"]["T_cam_imu"])                    # mono, read from the camera
R_cam_imu = np.asarray(T)[:3, :3]

imu = read_imu("take0004.imu")
accel_cam = np.asarray(imu.accel) @ R_cam_imu.T              # m/s², camera frame
gyro_cam  = np.asarray(imu.gyro)  @ R_cam_imu.T              # rad/s, camera frame
```

The calibration also gives the lever arm — where the motion sensor sits relative to the camera —
and the small camera–IMU time offset. See [Use a calibration](../calibration/use-a-calibration.md#conventions).
VIO and SLAM tools such as OpenVINS, Kalibr, VINS-Fusion and Basalt take the IMU data in the IMU
frame together with this transform, so you normally pass both unchanged
([export](../calibration/use-a-calibration.md#export-to-kalibr-openvins-vins-fusion-basalt)).

## Magnetometer

The magnetometer (Mono V3 and later, Stereo and Stereo GS) is a separate sensor, recorded in **its own
frame**. That frame differs from the accelerometer/gyroscope frame, and its readings are reported
with the **opposite sign** to the field direction. To bring it into the IMU frame, apply
`m_imu = R_imu_mag · m`:

| Camera | `R_imu_mag` | In words |
|---|---|---|
| Mono V4 | `[[0,1,0], [-1,0,0], [0,0,-1]]` | x = +m_y, y = −m_x, z = −m_z |
| Stereo V5 | `[[0,-1,0], [-1,0,0], [0,0,1]]` | x = −m_y, y = −m_x, z = +m_z |
| Stereo GS V6 | `[[-1,0,0], [0,-1,0], [0,0,-1]]` | x = −m_x, y = −m_y, z = −m_z |

These mappings were **measured from recordings**: the gyroscope's rotation was matched against the
change in the magnetic field, over several units and recordings per model, and the sign was set by
Earth's field direction. They are reliable for V4 and V5. Treat V6 as provisional: the fit there is
weaker. Mono V3 is not yet measured. Mono V1/V2 have no live magnetometer, so the field reads zero.

The magnetometer is **not calibrated for hard- and soft-iron effects**, so readings include fixed
offsets from the camera's own electronics. Calibrate them out, for example with a sphere or
ellipsoid fit over a recording that turns the camera through many orientations, before you use the
data for heading.

Related: [File formats](file-formats.md#imu-motion-data) · [Timing and sync](sync.md) ·
[Use a calibration](../calibration/use-a-calibration.md)
