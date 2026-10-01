---
title: Sample data
description: Download real Trinet recordings — Stereo, Stereo GS and a Wrist Kit — with video, motion data, per-frame timestamps and calibration, straight from the camera.
---

# Sample data

Real recordings from Trinet cameras, exactly as the camera wrote them to its memory card — so you
can try your pipeline before you have a camera. Every sample includes the video for each eye, the
motion data (`.imu`), the per-frame timestamps (`.vts`) and the camera's calibration.

<figure>
  <video class="sample-clip" autoplay muted loop playsinline preload="metadata" poster="../../assets/video/wristkit-sample-poster.jpg">
    <source src="../../assets/video/wristkit-sample.mp4" type="video/mp4">
  </video>
  <figcaption>Wrist Kit sample: a Trinet Stereo GS head camera (top: rectified left and right eyes) and
  two Trinet Mono wrist cameras (bottom left and centre), all on one timeline. Depth and the point
  cloud were computed afterwards on a computer — the camera itself does not output depth.</figcaption>
</figure>

## Download

All samples are in one public Google Drive folder:
**[Trinet sample data ↗](https://drive.google.com/drive/folders/1ov4ORRtFXlk5liHmQoorvy957q_AnexZ)**.
Each sample folder has a README with a quick start.

### Trinet Stereo GS (global shutter)

| Sample | What's in it | Length (min:s) |
|---|---|---|
| [Sample 1 — with wrists ↗](https://drive.google.com/drive/folders/1OYBGV_ZUmXnRciRyUehjHx_uJLSfc32O) | Wrist Kit: Stereo GS head camera plus left and right Mono wrist cameras, one folder each | 2:23 |
| [Sample 2 — with wrists ↗](https://drive.google.com/drive/folders/1_-ICq36UDDlZElKlGw96gzk1RKtC1lZQ) | Wrist Kit: Stereo GS head camera plus left and right Mono wrist cameras | 1:57 |
| [Sample 3 — stereo only ↗](https://drive.google.com/drive/folders/10vYXm1nYR6xmvYiieAnkrRKDiQ3EKkw7) | Stereo GS head camera, H.264, with extracted `calibration.json` | 1:54 |
| [Sample 4 — stereo only, H.265 ↗](https://drive.google.com/drive/folders/13b5Yx6_JwX1jj0QfJEnlpXrqwS6NPnSV) | Stereo GS head camera, H.265, plus an **MCAP** file for Foxglove / ROS 2 | 0:47 |

### Trinet Stereo (rolling shutter)

| Sample | What's in it | Length (min:s) |
|---|---|---|
| [Sample 1 ↗](https://drive.google.com/drive/folders/1SxEgG_ZWfVt9zQsPwvQ6se9q9DwOaacg) | Stereo head camera, H.265 | 1:45 |
| [Sample 2 ↗](https://drive.google.com/drive/folders/1V1xRaBkef56A07VI2NTGJ1utRnpeJOFV) | Stereo head camera | 3:27 |
| [Sample 3 ↗](https://drive.google.com/drive/folders/195yswJrobe-gebEnyIXMjyD1iuwH5bSf) | Stereo head camera | 1:32 |
| [Sample 4 ↗](https://drive.google.com/drive/folders/1P1MJKwRJJXepkitoCYJiyZ6fvdobCGdY) | Stereo head camera, plus a rendered stereo-depth and motion video | 2:01 |

Most samples also include a rendered `visualization` video — the same kind of overview as above —
so you can see what was recorded before you download the raw files.

## What's raw and what isn't

The camera writes only the per-eye `.mp4` files, the `.vts` timestamps, the `.imu` motion data and a
small `.tel` telemetry file. Everything else in a sample folder — visualization videos, depth,
`calibration.json` (the calibration is also embedded in each `.mp4`) and MCAP files — was produced
afterwards on a computer with the [Python toolkit](../toolkit/index.md).

## Open a sample

1. Install the [Python toolkit](../toolkit/index.md).
2. [Inspect a recording](../toolkit/inspect-and-repair.md) to see its camera, timing and calibration.
3. [Visualize it and check sync](../toolkit/visualize.md), or
   [export it to MCAP / ROS 2](../toolkit/mcap.md).

For the file layouts, see [File formats](file-formats.md); for how the clocks line up, see
[Timing and sync](sync.md).

!!! note "Sample names"
    Folder READMEs may call the Stereo GS camera "Trinet Pro Stereo GS" — that's the same camera.
    Samples were recorded on firmware from July to September 2026 and read with current tools.
