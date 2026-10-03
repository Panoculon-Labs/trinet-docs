---
title: Sync validation report
description: How we measured Trinet's wireless camera-to-camera sync with an independent LED strobe — about 50 µs between cameras, sub-microsecond between stereo eyes, stable across 27 cold restarts.
---

# Sync validation report

We measured Trinet's synchronization **from outside the system**: an LED with randomized switching
times was filmed by every camera at once, and its edges — read through the rolling shutter, row by
row — give the true moment each frame was captured, independent of any clock being tested.

<div class="grid cards" markdown>

-   **~50 µs**

    ---

    Typical camera-to-camera agreement over the wireless link — about 1/700th of a frame at 30 fps.

-   **0.8 µs**

    ---

    Spread between the two eyes of a stereo head camera, per frame.

-   **27 cold restarts**

    ---

    Mean +49 ± 8 µs between cameras, every device fully restarted between sessions.

-   **0 calibration steps**

    ---

    No per-unit timing calibration: every constant comes from the sensor's own geometry.

</div>

[:material-file-chart: Read the full report](../assets/reports/trinet-wireless-sync-2026-08.html){ .md-button .md-button--primary target=_blank }

## What was measured

| Test | Result |
|---|---|
| Wrist camera vs stereo head camera, 4 minutes (~7,000 frames), live wireless link | Median +56 µs, standard deviation 71 µs; no drift, steps or warm-up transient |
| 27 sessions, every device cold-restarted in between, ~4-minute recordings | Mean +49 ± 8 µs; all sessions within a ±42 µs band, no trend over six hours |
| Left vs right eye of a stereo head camera, 7,650 frames | Median 0.0 µs, standard deviation 0.82 µs |

**Stated as a specification:** cross-camera timestamp agreement is typically **≤ 50 µs**, with
session-to-session variation of ±42 µs, bounded at about 150 µs; the stereo pair is sub-microsecond.
Every frame carries a quality flag, and the rare radio-degraded frames (under 1%) are marked. We quote
**under 1 ms** between cameras as the conservative product figure.

## Good to know

- Measurements were made on 27–28 August 2026 with production firmware, using a stereo head camera
  and wrist cameras in a [Wrist Kit](../products/wrist-kit.md).
- For the first one to two seconds of a take, a camera that is still locking on can be less accurate
  — see [Timing and sync](sync.md).
- Want the methodology or raw data? [Contact us](../support/index.md).
