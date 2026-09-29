---
title: Glossary
description: Terms used in the Trinet documentation.
---

# Glossary

Baseline
:   The distance between the two cameras of a stereo camera — 70 mm on Trinet Stereo and Stereo GS.

Calibration
:   Precise description of a camera's lens and of where the motion sensor sits relative to it, plus the
    small time offset between them. See [Calibration](../calibration/index.md).

Card recording
:   Recording to the camera's own memory card with the button — no phone or computer needed.

Device ID
:   A public 128-bit identifier unique to each camera, written into every recording.

exFAT
:   The memory-card format Trinet recommends; it allows files larger than 4 GB.

Field of view (FOV)
:   How wide an angle the camera sees, horizontally (HFOV), vertically (VFOV) or diagonally (DFOV).

Firmware
:   The software that runs on the camera. Updated from the [Trinet app](../firmware/index.md).

Global shutter
:   All rows of the image are exposed at the same instant — no skew with fast motion. Trinet Stereo GS.

IMU
:   Inertial measurement unit — the camera's accelerometer and gyroscope (and on newer cameras a
    magnetometer), recorded at a high rate alongside the video.

Kit / Wrist Kit
:   Several Trinet cameras paired to start, stop and keep time together. See
    [Trinet Wrist Kit](../products/wrist-kit.md).

Kit leader
:   The camera that pairing starts from and that the kit's shared clock follows.

MCAP
:   An open file format for robotics data used by Foxglove and ROS 2. See
    [Export to MCAP](../toolkit/mcap.md).

Mid-exposure timestamp
:   A frame time stamped at the middle of the frame's exposure — the instant that best represents it.

Rolling shutter
:   Image rows are exposed one after another; fast motion can skew the image. Trinet Mono and Stereo.

Take
:   One recording, from pressing record to pressing stop.

`timeshift_cam_imu`
:   The constant time offset between camera and IMU measured by calibration; add it to a frame time to
    place it on the IMU clock.

USB webcam mode
:   The camera appears as a standard USB video device to Android phones and computers.

iPhone mode
:   The camera appears as a USB network adapter so iPhone apps can stream from it (Trinet Mono).

Wireless status
:   Bluetooth broadcasts of each camera's recording state, read by the Trinet app without connecting.
