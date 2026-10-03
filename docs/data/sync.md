---
title: Timing and sync
description: How Trinet aligns motion data and video to sub-millisecond accuracy, how cameras in a kit share time, and how to use the timestamps correctly.
---

# Timing and sync

## At a glance

| | Typical |
|---|---|
| Motion data to video, within one camera | **Sub-millisecond**, hardware-timestamped |
| Frame timestamp precision (jitter) | About 10 µs |
| Camera to camera in a [Wrist Kit](../products/wrist-kit.md) | **Under 1 ms** |

## Within one camera

**One shared clock.** Motion samples are timestamped at the moment they are measured, and video
frames at the **middle of their exposure** — the instant that best represents a frame, whatever the
exposure time. Both use the same camera clock, so aligning motion to a frame is a direct timestamp
comparison.

**Why middle of exposure?** A frame is exposed over a window that changes with lighting — from a
fraction of a millisecond to tens of milliseconds. Stamping the start of the frame would introduce an
offset that varies with brightness. Stamping the middle removes it, so alignment is stable indoors and
outdoors. (Current cameras. On some earlier Mono versions the timestamp refers to the start of the
frame; each timestamp file has a flag that says which — see [File formats](file-formats.md).)

**Rolling vs global shutter.** On rolling-shutter cameras (Mono, Stereo) rows are exposed one after
another; the frame timestamp refers to the **centre row**, and each frame records the readout time so
you can compute every row's time. On Trinet Stereo GS all rows are exposed together.

**The calibration time offset.** Even with one clock, the image path and the motion sensor have small,
fixed internal delays. Calibration measures the remaining constant offset between camera and IMU —
`timeshift_cam_imu` — and it is included with every camera's calibration. Apply it:

```text
t_on_imu_timeline = t_frame + timeshift_cam_imu
```

### Using the timestamps

```text
for each video frame f:
    t = f.frame_timestamp + timeshift_cam_imu     # mid-exposure, camera clock
    samples = IMU samples with timestamps around t
    use / interpolate samples at t
```

1. Use the **frame timestamps** from the `.vts` file (or the SDK), never the video container's
   playback timestamps or the computer's clock.
2. Apply the calibration **time offset** when you have it.
3. **Stay on the camera clock** for motion–video work; convert to other clocks only at the end.

The [Python toolkit](../toolkit/visualize.md) can draw motion data over the video and check the
alignment visually and numerically.

## Across cameras (Wrist Kit)

Cameras in a kit share a clock over a short-range radio link:

- Every frame's timestamp can be placed on the kit's **shared timeline** — the per-frame offset is
  recorded in the timestamp file — so frames from different cameras line up directly, not by frame
  index.
- While recording, cameras stay within **1 ms** of each other.
- For the first one to two seconds after a take starts, a camera that is still locking on can be less
  accurate. Trim the first seconds when you need the tightest alignment.
- If the radio link drops, each camera keeps recording and carries its timing forward; it re-aligns
  when the link returns.

## On UTC time

Cameras don't have a real-time clock. To put card recordings on UTC — to line them up with other
sensors, video or logs — use the Trinet app's [Wireless status](../app/wireless-status.md) export with
the toolkit's [wireless UTC tool](../toolkit/wireless-utc.md).

## Quoting accuracy

When describing Trinet timing to others, the accurate summary is: **sub-millisecond,
hardware-timestamped motion–video alignment, and under 1 ms between cameras in a kit.**
