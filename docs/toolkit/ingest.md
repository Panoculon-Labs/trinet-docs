---
title: Ingest SD cards
description: Turn a Trinet SD card into upload-ready ZIPs, one per clip, with video, motion data and collection metadata.
---

# Ingest SD cards

`ingest_sd_card.py` turns a memory card straight into upload-ready ZIP files — one per clip — each
with the video, its motion data and timestamps, and a `metadata.json` describing where and how the
footage was collected. It's built for data-collection programmes that require per-video metadata and
quality thresholds.

```bash
# Windows: card in E:, deliveries to D:\deliveries
python scripts\ingest_sd_card.py --drive E: --collector alice01 ^
    --country US --environment residential/laundry --capture-date 2026-07-20 ^
    --calibration cal\unit-aa3d26ba.json --out D:\deliveries

# macOS / Linux: a card mounted as a folder
python3 scripts/ingest_sd_card.py --folder /media/TRINET --collector alice01 \
    --country US --environment residential/laundry --out deliveries/
```

Each ZIP contains:

```text
alice01_20260720_aa3d26ba_recording3_1.zip
    recording3_1.{mp4,imu,vts,json}
    metadata.json     collection details + calibration + video and IMU specs
    README.md         how to read the files
```

## What it does

- **Reads the card only** — never writes to it. It finds the card by itself and mounts it read-only
  if needed.
- Handles solo recordings and [Wrist Kit](../products/wrist-kit.md) takes.
- Fills `metadata.json` with your collection details (environment, country, collector, session), the
  device ID, the video's technical properties (codec, resolution, frame rate, bitrate, keyframe
  interval), the motion-data details and — with `--calibration` — intrinsics, extrinsics and a
  correctly computed fisheye field of view.
- **Repairs** the MP4 index by default (lossless) so strict uploaders accept it; `--no-repair` copies
  files verbatim.

## Common options

| Option | Does |
|---|---|
| `--mcap` | Also write a Foxglove-ready [MCAP](mcap.md) per clip |
| `--reencode` / `--reencode-mbps N` | Transcode to a compliant H.264 bitrate (needs `ffmpeg`, uses hardware acceleration when available) |
| `--gate` | Skip clips that would be refused (too short, no motion data, truncated video); see `--min-duration`, `--require-imu`, `--require-valid-video` |
| `--task`, `--participant-id`, `--session-id`, `--region`, `--env-note` | More collection metadata |
| `-j N` | Process clips in parallel |
| `--dry-run` | Show what would be produced |

To add missing metadata to ZIPs you already delivered, use `scripts/backfill_metadata.py`. The full
guide, including the metadata field mapping and batch-versus-unit calibration, is the toolkit's
[data collection packaging guide](https://github.com/Panoculon-Labs/Trinet-tools/blob/main/docs/data_collection_packaging.md).
