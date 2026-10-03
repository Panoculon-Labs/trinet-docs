---
title: "Spec note: Stereo + Wrist Kit"
description: One-page specification for synchronized stereo head plus wrist-camera collection with Trinet — configuration, per-camera specs, timing, storage, power and outputs.
---

# Spec note: Stereo + Wrist Kit

Synchronized egocentric collection with a **stereo head camera and a camera on each wrist**: depth
from the head, close-up views of both hands, and motion data from all three — every frame and sample
on one shared timeline.

<figure>
  <video class="sample-clip" autoplay muted loop playsinline preload="metadata" poster="../../assets/video/wristkit-sample-poster.jpg">
    <source src="../../assets/video/wristkit-sample.mp4" type="video/mp4">
  </video>
  <figcaption>A real kit recording: Stereo GS head camera (top) and two Mono wrist cameras (bottom).
  Depth and point cloud computed afterwards on a computer. Download it from
  <a href="../../data/sample-data/">Sample data</a>.</figcaption>
</figure>

## Configuration

| Position | Camera | Notes |
|---|---|---|
| Head | [Trinet Stereo](stereo.md) **or** [Trinet Stereo GS](stereo-gs.md) | Two cameras, 70 mm baseline; GS = global shutter for fast motion |
| Left wrist | [Trinet Mono](mono.md) | One ultra-wide camera |
| Right wrist | [Trinet Mono](mono.md) | One ultra-wide camera |

Every camera needs a **radio-beacon adapter** for wireless sync — beacons are sold separately. Kits
are paired at the factory; more cameras can join the same kit. See [Wrist Kit](wrist-kit.md).

## Kit at a glance

| | |
|---|---|
| Cameras | 3 (head + two wrists) — 4 video streams (2 head eyes + 2 wrists) |
| Motion data | 3 IMUs — one per camera, each at 400 Hz with a magnetometer at about 100 Hz |
| Audio | Stereo microphones in every camera, each with a hardware [mute switch](../get-started/mute-switch.md) |
| Start / stop | Press the button on **any** camera — the whole kit starts and stops together |
| Recording | Each camera records to its **own** microSD card; no phone, computer or cables between cameras |
| Field monitoring | [Trinet app → Wireless status](../app/wireless-status.md) shows every camera's state over Bluetooth (firmware 0.5.9+) |

## Timing and sync

| Measure | Typical |
|---|---|
| Motion data to video, within each camera | **Sub-millisecond**, hardware-timestamped |
| Frame timestamp precision (jitter) | About 10 µs |
| Head stereo, left eye to right eye | Both eyes triggered from a single clock |
| Camera to camera within the kit | **Under 1 ms** — measured typically about 50 µs ([validation report](../data/sync-validation.md)) |

- Frames are timestamped at **mid-exposure**; motion samples at the moment they're measured — all on
  the camera clock, and across the kit on the shared kit clock.
- If the radio link drops mid-take, every camera keeps recording and re-aligns when the link returns.
- For the first one to two seconds of a take, cameras still locking on can be less accurate — trim
  them when you need the tightest alignment.

Method and details: [Timing and sync](../data/sync.md).

## Per-camera specifications

| | Head: Trinet Stereo | Head: Trinet Stereo GS | Wrists: Trinet Mono |
|---|---|---|---|
| Sensors | 2 × 3 MP rolling shutter | 2 × 2.3 MP **global shutter** | 1, rolling shutter |
| Video | 1920×1080 per eye, 30 fps | 1920×1080 per eye, 30 fps | 1920×1080, 30 fps |
| Effective field of view (from calibration) | ≈158° H × 94° V per eye | ≈160° H × 96° V per eye | ≈139° H × 73° V |
| Codec on card | H.264 (default) or H.265 | H.264 (default) or H.265 | H.264 (default) or H.265 |
| Card bitrate | 10 Mbps constant, per eye | 10 Mbps constant, per eye | ≈15 Mbps variable (adjustable) |
| Frame timing | Mid-exposure of the centre row; per-frame readout time | Whole frame at once | Mid-exposure |
| Motion | Accel ±8 g + gyro ±2000 °/s at 400 Hz; magnetometer ≈100 Hz | same | same |
| Audio | Stereo, AAC 44.1 kHz | Stereo, AAC 44.1 kHz | Stereo, AAC 48 kHz (default) |
| Calibration | Per-unit factory calibration, embedded in every recording | same | Reference (batch) calibration for the model; per-unit calibration available as a service |
| Storage | ≈10 GB per hour | ≈10 GB per hour | ≈7 GB per hour |

Full details: [Stereo](stereo.md) · [Stereo GS](stereo-gs.md) · [Mono](mono.md).

## Storage and power

| | Head (Stereo / GS) | Each wrist (Mono) | Whole kit |
|---|---|---|---|
| Data per hour | ≈10 GB | ≈7 GB | ≈24 GB |
| Recommended card | 128 GB or more, **V30** | 64 GB or more, **V30** | — |
| Hours per card | ≈12 h on 128 GB | ≈9 h on 64 GB | — |
| Power | USB-C, 5 V, 1 A or more | USB-C, 5 V | One power bank per camera (or a multi-port bank) |

See [Memory cards](../power-and-care/memory-cards.md) and
[Tested power banks](../power-and-care/power-banks.md).

## Outputs

Each camera writes its own files; takes recorded together share a kit prefix (`grp…`) so matching
files group easily.

| Camera | Files per take |
|---|---|
| Head (stereo) | `_L.mp4`, `_R.mp4` (video + audio + calibration), `_L.vts`, `_R.vts` (frame timestamps), `.imu` (motion) |
| Each wrist | `.mp4` (video + audio + calibration), `.vts`, `.imu` |

The [Python toolkit](../toolkit/index.md) reads every file, plays kit takes side by side, checks sync,
exports to [MCAP / ROS 2](../toolkit/mcap.md) and places every take on
[UTC](../toolkit/wireless-utc.md). Formats: [File formats](../data/file-formats.md).

## Heat

If any camera in the kit needs to cool down, the **whole kit pauses** and resumes together, so takes
stay matched. If one camera's card fills up or is removed, the kit stops together. See
[Heat and thermal protection](../power-and-care/thermal.md).

## Try it and order

- **Sample recordings** from this exact setup (Stereo GS head + two Mono wrists):
  [Sample data](../data/sample-data.md).
- **Setup guide and video:** [Set up a Wrist Kit](../get-started/wrist-kit-setup.md).
- **Pricing, beacons and custom configurations:** [contact us](../support/index.md).

<small>Specifications for current hardware and firmware 0.5.9; typical values, not guarantees.
Subject to change — see the [firmware release notes](../firmware/release-notes.md).</small>
