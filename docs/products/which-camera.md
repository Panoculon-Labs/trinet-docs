---
title: Which camera do I have?
description: Identify your Trinet camera model and hardware version (V1–V6), and how the app, SDK and calibration files refer to it.
---

# Which camera do I have?

Trinet cameras have a product name and a **hardware version** (V1–V6). The app, SDK, toolkit and
calibration files sometimes use the hardware version or a generation code, so this table maps
between them.

| Product | Hardware version | Generation code (app / SDK) | Recognise it by |
|---|---|---|---|
| Trinet Mono (original) | V1, V2 | `v2` (legacy) | One camera; motion data at about 560–570 Hz; no audio |
| Trinet Mono | V3 | `v3` | One camera; 400 Hz motion data with magnetometer; no audio |
| Trinet Mono | V4 | `v4` | One camera; stereo audio in recordings |
| Trinet Stereo | V5 | `v5` | Two lenses; recordings marked rolling shutter |
| Trinet Stereo GS | V6 | `v6` | Two lenses; recordings marked global shutter |

## How to check

=== "Trinet app"

    - **Firmware version:** connect the camera and open **Update firmware** in the
      [Trinet app](../app/index.md) — it shows the installed version.
    - **Model and firmware of every camera nearby:** with camera firmware 0.5.9 or newer, the
      [Wireless status](../app/wireless-status.md) screen shows each camera's model and firmware
      without connecting.
    - Recordings made in the app store the camera's generation and firmware in their `meta.json`.

=== "From a recording"

    Recordings carry the camera's identity and calibration, and stereo recordings are marked
    rolling or global shutter. The [toolkit's inspect command](../toolkit/inspect-and-repair.md)
    shows what a recording contains, including its file-format versions
    ([what they mean](../data/file-formats.md)).

=== "SDK"

    `TrinetDevice.getGeneration()` returns the generation code (`null` means `v2`). For stereo
    cameras, the stream shape is the most robust signal: a camera that streams a 3840×1080
    side-by-side frame is a Stereo or Stereo GS. See [Build apps](../sdk/index.md).

## Calibration files

Each hardware version has its own [reference calibration](../calibration/reference-calibrations.md);
calibrations of different versions are **not interchangeable**. Stereo and Stereo GS units also
carry their own per-unit factory calibration.
