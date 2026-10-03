---
title: Sync validation report
description: Validation of Trinet wireless camera-to-camera synchronization using an LED reference — methods, results, specification and limitations.
---

# Wireless synchronization of Trinet cameras — validation report

<p class="report-meta">Panoculon Labs · Report version 1.1, October 2026</p>

## Summary

Trinet cameras in a [Wrist Kit](../products/wrist-kit.md) have no cables between them; each keeps
time with its own oscillator, and a short-range radio link brings all of them onto one shared clock.
This report measures how closely the resulting timestamps agree, using an LED filmed by the cameras
as the reference.

| Result | Experiment | Value |
|---|---|---|
| Timestamp offset, wrist camera vs stereo head camera | Light-matched frames, 7,200 frames | **+56 µs** median |
| Timestamp offset between two wrist cameras | LED row-edge method, 27 sessions | **+49 ± 8 µs** (mean ± standard error) |
| Session-to-session scatter, wrist cameras | Same 27 sessions | **≤ 43 µs** (1 SD, upper bound) |
| Drift over one continuous hour | Two wrist cameras, frame pairing | **−1.0 ± 0.7 µs per hour** — below 12 µs per hour (2σ) |
| Stereo head camera, left vs right eye | One recording, 7,649 frames | **0.0 µs** median, 0.82 µs SD |

**Sign convention:** a positive offset means the first-named camera's timestamp is later than the
second's for the same moment (for example, wrist later than head).

All measured offsets are a small fraction of the 33.3 ms frame interval at 30 fps. We specify
camera-to-camera agreement conservatively as **under 1 ms**.

## 1. Test setup

| | |
|---|---|
| Head camera | One **Trinet Stereo** (rolling shutter) |
| Wrist cameras | Three Trinet wrist camera units, used two at a time and swapped between positions |
| Link | The cameras' built-in radio link, operating live during recording |
| Recording | 1920 × 1080 at 30 fps to each camera's own memory card (about 29.7 fps in the one-hour test) |
| Firmware | Late-August 2026 builds; the one-hour test (Section 3.4) used an earlier build from 26 August |
| Reference | The status LED of a Trinet unit, switched at randomized times, in view of all cameras |
| Environment | Indoor bench, cameras close together; exposure locked at 1/120 s for the one-hour test (dark room) |
| Calibration | No per-device timing calibration was applied to any camera |

## 2. Methods

Three complementary methods were used. Each result in this report names the method it comes from.

**A. LED row-edge method (wrist camera vs wrist camera).** A rolling-shutter sensor reads out its rows
one after another (a few tens of microseconds per row). When the LED switches while a frame
is being read out, part of the image shows the LED on and part shows it off; where that transition
falls in the rows gives the moment the LED switched, measured in each camera's own timeline.
Comparing the same physical event across cameras gives their timestamp offset without relying on any
clock being tested. A single event is noisy (around 0.8 ms); averaging the hundreds of events in each
session gives a session mean with a standard error of about 20–30 µs.

**B. Light-matched frames (wrist camera vs stereo head camera).** The LED's on/off pattern, as seen by
each camera, is cross-correlated to establish which frame in one camera corresponds to which frame in
the other — using the light, not the clocks. Because the cameras' shutters are phase-locked to the
shared clock, matched frames are captured at the same moment, and the difference between their
timestamps is the timestamp offset. This method reaches timestamp precision on every frame. It relies on
the shutter phase lock, and it cannot detect an error that is identical in both cameras' timestamps
and shutter timing; method A, which does not share that assumption, was used for the wrist-camera
pairs.

**C. Frame pairing (one-hour stability).** Frames from two cameras are paired by their timestamps
(precision about 8 µs) to measure frame-to-frame variation and long-term drift. It measures variation
and drift, not the absolute offset.

![The LED reference as recorded by Trinet cameras: off, switching during the frame, and on](../assets/reports/sync-2026-08/fig1-led-photos.jpg)

<p class="report-caption"><strong>Figure 1.</strong> The LED reference as recorded by Trinet cameras
during the experiments — top: the strobe unit; bottom: close-ups of the LED. In the centre frames the
LED switched while the frame was being read out, so only part of the light is captured. Original
camera frames, cropped but not retouched.</p>

**Exclusions.** The first second of each recording, while a camera locks onto the shared clock, is
shown shaded in Figure 2 and excluded from the percentages quoted for it. Where other exclusions
apply, the result says so.

## 3. Results

### 3.1 Wrist camera vs stereo head camera (method B)

![Per-frame timestamp offset between a wrist camera and the stereo head camera over four minutes](../assets/reports/sync-2026-08/fig1-per-frame-offset.svg)

<p class="report-caption"><strong>Figure 2.</strong> Timestamp offset, wrist minus head, for
light-matched frames over a four-minute recording (7,200 frames, plotted at 5 Hz). Median +56 µs
(split halves +56.8 and +56.2 µs); standard deviation over all 7,200 frames 71 µs, including the
first second. After the first second, 99% of plotted samples lie within 150 µs of zero. One brief
radio-degraded episode, about 2 s long, reached −561 µs before the link recovered. A second wrist
unit measured against the same head gave +59 µs, with a larger spread (standard deviation 273 µs).</p>

### 3.2 Wrist camera vs wrist camera across cold restarts (method A)

![Mean wrist-to-wrist camera offset in 27 sessions, each after a cold restart](../assets/reports/sync-2026-08/fig2-cold-restarts.svg)

<p class="report-caption"><strong>Figure 3.</strong> Mean offset between two wrist cameras in each of 27
sessions of about four minutes (≈1 h 50 min of recording, spread over about six hours), with the
recording software of every camera restarted from cold before each session. Mean +49 ± 8 µs
(standard error); standard deviation 43 µs, range −22 to +134 µs. The standard deviation includes
each session's own measurement noise (about 20–30 µs), so the true session-to-session scatter is
smaller, about 35 µs. No significant trend across sessions (−1.1 ± 1.1 µs per session).</p>

The constant follows **camera position rather than the device**: a different wrist unit placed in the
same position measured +28 ± 9 µs against the same partner. No per-device calibration is needed.

### 3.3 Stereo head camera: left vs right eye

![Histogram of the left minus right eye timestamp difference per frame](../assets/reports/sync-2026-08/fig3-stereo-eyes.svg){ style="max-width:42rem" }

<p class="report-caption"><strong>Figure 4.</strong> Per-frame timestamp difference between the two
eyes of the stereo head camera over one recording (7,649 frames; logarithmic scale). Median 0.0 µs,
standard deviation 0.82 µs; 99.1% of frames within ±2 µs. Both eyes are triggered from a single
line and share one clock, so this bounds the uncorrelated per-eye timestamp jitter at under a
microsecond; errors common to both eyes are not visible in this comparison.</p>

### 3.4 Long-duration stability (method C, earlier firmware build)

![Per-minute median deviation between two cameras over one continuous hour](../assets/reports/sync-2026-08/fig4-one-hour.svg)

<p class="report-caption"><strong>Figure 5.</strong> Per-minute median deviation between two wrist
cameras over one continuous hour (107,107 frame pairs), re-centred on its own average. Linear trend
+0.3 ± 5.5 µs per hour across the minute medians; per-frame trend −1.0 ± 0.7 µs per hour. Over the same
hour the cameras' raw clocks drifted apart by 14.4 ms; with per-frame timestamp correction, the net
trend over the hour is about 1 µs. Dark room, exposure locked at 1/120 s, no link-loss events; camera
temperatures rose from 44.0 to 52.9 °C and from 42.2 to 50.5 °C and levelled off.</p>

| Absolute frame-to-frame deviation from the mean, one hour | Value |
|---|---|
| Median (p50) | 33.7 µs |
| 90th percentile | 86.6 µs |
| 99th percentile | 230 µs |
| Standard deviation | 66 µs |

These statistics exclude the first 30 s of the hour (about 890 frames, covering the initial lock);
all later frames are included, flagged or not. The largest steady-state deviation was 1.03 ms.

## 4. Specification

| Parameter | Typical value | Basis |
|---|---|---|
| Wrist camera vs stereo head camera | ≈ +56 µs | Figure 2 (method B) |
| Wrist camera vs wrist camera | ≈ +49 µs | Figure 3 (method A) |
| Session-to-session scatter | ≤ 43 µs (1 SD) | Figure 3 |
| Frame-to-frame deviation, 99th percentile | ≈ 230 µs | Section 3.4 |
| Drift | Below 12 µs per hour (2σ) | Figure 5 |
| Stereo left vs right eye, per-eye jitter | < 1 µs | Figure 4 |
| **Product specification, camera to camera** | **Under 1 ms** | All of the above, with headroom |

## 5. Limitations

- **Lock acquisition.** During the first one to two seconds of a recording, while a camera locks onto
  the shared clock, timestamps can be much less accurate — up to about 11 ms in the one-hour test,
  with 28 of the 29 affected frames marked by the per-frame quality flag. Trim this period, or use the
  flag, where the tightest alignment matters.
- **Radio-degraded episodes.** Brief interruptions of the radio link degrade agreement temporarily:
  −561 µs at worst in the four-minute test. In the one-hour test, three brief mid-recording re-lock
  episodes (about 0.5 s each) stayed below about 1 ms; one short episode of six unflagged frames
  peaked at 1.03 ms.
- **Position-dependent constant.** The camera-to-camera constant varies by a few tens of
  microseconds with camera placement (Section 3.2).
- **Conditions.** Indoor bench tests with two or three cameras close together; the one-hour test
  used an earlier firmware build. Results in the field depend on the environment and radio
  conditions.

## Related reading

[Timing and sync](sync.md) · [Wrist Kit](../products/wrist-kit.md) · [Sample data](sample-data.md)
