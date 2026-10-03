---
title: Metadata format (TMF)
description: The Trinet Metadata Format — what every Trinet MP4 carries besides video and audio (recording metadata, calibration, motion and timing data), and the recording-meta JSON sidecar.
---

# Metadata format (TMF)

Recordings from current firmware are **self-contained**. Besides video and audio, every `.mp4`
written by a Trinet camera carries the **Trinet Metadata Format (TMF)**:

| Where in the MP4 | What it holds |
|---|---|
| A timed metadata track (`tmfd`) | The motion data, per-frame timestamps and thermal telemetry, in about one-second chunks |
| `moov/udta/tmfm` | Recording metadata as JSON: camera, firmware, codec, sync state, frame-drop summary, temperature range |
| `moov/udta/tmfc` | The camera's calibration, as a binary blob |

Sharing just the `.mp4` is therefore enough: the `.imu`, `.vts` and `.tel` files can be rebuilt from
it byte for byte. Video players ignore the extra track; `ffprobe` lists it as a `data` stream.

!!! warning "Re-encoding removes TMF"
    Anything that re-encodes or re-muxes the file — video editors, many converters, some upload
    services — drops the metadata track and boxes. Keep the original files, or keep the `.imu`, `.vts`
    and `.tel` files the camera writes alongside the video; they hold the same data.

## Read it

With the [Python toolkit](../toolkit/index.md) installed:

```bash
python3 -m trinet_tools.tmf info take0001.mp4            # summary
python3 -m trinet_tools.tmf extract take0001.mp4 --out recovered/
```

`extract` rebuilds the `.imu`, `.vts` and `.tel` files plus the metadata JSON and the calibration
blob. From Python:

```python
from trinet_tools.tmf import read_tmf
from trinet_tools import calib_blob

rec = read_tmf("take0001.mp4")
print(rec.meta)                              # recording metadata (dict)
if rec.calib_blob:                           # absent if the camera had no calibration stored
    calib = calib_blob.unpack(rec.calib_blob)  # intrinsics, extrinsics, IMU model (dict)
```

## Recording metadata (`tmfm`)

UTF-8 JSON. Keys are omitted when unknown, and new keys may be added without changing the schema
number — read the keys you need and ignore the rest.

```json
{
  "tmf_schema": 2,
  "source": "sd",
  "device_id": "64ea7f5da17f71e411e8f1a8103a1558",
  "fw_version": "0.5.9",
  "hw_generation": "v6",
  "eye": "L",
  "pair_file": "take0004_R.mp4",
  "codec": "h264",
  "imu_version": 5,
  "imu_rate_hz": 400,
  "vts_version": 4,
  "sync": {"offset_ns": 0, "skew_ppb": 0, "quality_us": 0, "flags": 0},
  "drops": {"nominal_ms": 33.33, "expected": 3413, "recorded": 3413,
            "gap_count": 0, "gaps": []},
  "thermal": {"min_c": 38.7, "max_c": 52.3, "samples": 117}
}
```

| Key | Meaning |
|---|---|
| `tmf_schema` | Schema version of this JSON (current recordings: `2`) |
| `source` | Where the recording was made — `sd` for a recording to the camera's memory card |
| `generator` | The camera software component that wrote the metadata |
| `device_id` | The camera's public 32-hex [device ID](file-formats.md#device-id) |
| `fw_version`, `hw_generation` | Firmware version and hardware generation that made the recording |
| `eye`, `pair_file` | Stereo cameras only: `L` or `R`, and the file name of the other eye |
| `codec` | `h264` or `h265` |
| `imu_version`, `imu_rate_hz`, `vts_version` | Versions of the embedded motion and timestamp records, and the motion sample rate |
| `sync` | The multi-camera clock state for the take: offset to the kit's clock (ns), rate mismatch (ppb), estimated uncertainty (µs) and flags — the same values as the `.vts` header |
| `drops` | The camera's own frame-continuity check: nominal frame interval, frames expected and recorded, and up to 64 gaps found from the per-frame timestamps |
| `thermal` | Lowest and highest camera temperature during the take, and the number of readings |

## Calibration (`tmfc`)

The calibration the camera holds, embedded verbatim in every recording (absent if the camera had no
calibration stored when it recorded): a little-endian binary blob
starting with the magic `TBLC` and ending with a CRC-32. Two layouts exist:

- **Single camera (200 bytes):** image size, fisheye projection model, `fx fy cx cy` and up to five
  distortion coefficients, camera–IMU rotation and translation, camera–IMU time offset, IMU noise
  parameters, biases and calibration quality.
- **Stereo (300 bytes):** the same header, one block per eye (`cam0` = the scene-left `_L` eye), the
  camera–IMU transform, the stereo extrinsic `T_cam1_cam0` (its translation is the baseline) and a
  shared IMU block.

The time-offset convention is `t_imu = t_cam + timeshift_cam_imu_s`. `calib_blob.unpack()` returns the
same structure as a `calibration.json`. See [Calibration](../calibration/index.md).

## Embedded data track (`tmfd`)

Each sample of the metadata track covers about one second and is a key–length–value (KLV) structure,
little-endian throughout. It carries, as separate streams:

| Stream | Content | Rate |
|---|---|---|
| `TSNS` | Motion sample timestamps (ns, camera clock) | Motion rate |
| `ACCL`, `GYRO`, `MAGN` | Accelerometer (m/s², including gravity), gyroscope (rad/s), magnetometer (µT) | Motion rate |
| `TMPC` | Motion-sensor temperature (°C) | Motion rate |
| `TFRM` | Per-frame timestamp records — the `.vts` entries | Per frame |
| `TSOC` | Thermal telemetry records — the `.tel` entries | 1 Hz |

The first chunk also carries the original `.imu`, `.vts` and `.tel` file headers, which is what makes a
byte-identical rebuild possible. The complete byte-level layout is in the toolkit's
[data format reference ↗](https://github.com/Panoculon-Labs/Trinet-tools/blob/main/docs/data_formats.md#embedded-metadata-track-tmf).

## Recording-meta sidecar (`.json`)

A small, human-readable JSON file sits next to each recording. For [Wrist Kit](../products/wrist-kit.md)
takes it shows, at a glance, which take a file belongs to and how the camera relates to the others:

```json
{
  "format": "trinet-recording-meta/1",
  "session": 72593,
  "group": 48477,
  "role": "slave",
  "device_id": "64ea7f5da17f71e411e8f1a8103a1558",
  "device_tag": "64ea7f5d",
  "segment": 1,
  "synced": true,
  "master_clock_offset_ns": -4642873007,
  "clock_skew_ppb": 28617,
  "sync_quality_us": 610,
  "sync_flags": 1,
  "mode": "single",
  "basename": "grp72593_64ea7f5d_1",
  "created_unix": 79
}
```

| Field | Meaning |
|---|---|
| `session` | Recording-session ID — **shared by every camera in one synchronized take** (`0` = recorded on its own) |
| `group` | The kit the camera is paired into (`0` = unpaired) |
| `role` | `master` (the kit's clock reference), `slave` or `unpaired` |
| `device_id`, `device_tag` | The camera's ID, and its first 8 characters as used in file names |
| `segment` | Part number when a long take is split into several files (from `1`) |
| `synced`, `sync_flags` | Whether the offset to the master clock is valid (`sync_flags`: `1` synced, `2` master — so master = `3`) |
| `master_clock_offset_ns` | Add to this camera's frame timestamps to put them on the master's clock (`0` on the master) |
| `clock_skew_ppb` | Remaining clock-rate difference to the master, for drift correction on long takes |
| `sync_quality_us` | Estimated sync uncertainty, microseconds |
| `basename` | The shared base name of this camera's files, `grp<session>_<device-tag>_<segment>` |
| `created_unix` | Seconds since the camera powered on — not wall-clock time (the camera has no real-time clock; see [UTC for wireless recordings](../toolkit/wireless-utc.md)) |

The sync values are a convenience copy of the `.vts` header, which is what the toolkit uses:
`read_vts(path).global_sof_ns()` returns a camera's frame times already on the master's clock.

## Related

[File formats](file-formats.md) · [Timing and sync](sync.md) · [Calibration](../calibration/index.md) ·
[Sample data](sample-data.md) — every sample recording contains TMF.
