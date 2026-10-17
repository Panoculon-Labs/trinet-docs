---
title: Get your camera's calibration
description: Get the calibration stored on your Trinet camera as calibration.json — from any recording (MP4), over USB in webcam mode (UVC), or over USB networking in iPhone mode (NCM).
---

# Get your camera's calibration

Every Trinet camera keeps its calibration on board, so you can get it back at any time as a
`calibration.json`. That file works with every [toolkit](../toolkit/index.md) command that takes
`--calibration`, and with the steps in [Use a calibration](use-a-calibration.md).

There are three ways to read it. Pick the one that matches what you have:

| You have | Method | Works on |
|---|---|---|
| A recording from the camera | [From an MP4](#from-a-recording-mp4) | Windows, macOS, Linux |
| The camera, in USB webcam mode | [Over USB (UVC)](#over-usb-webcam-mode-uvc) | Linux |
| A Trinet Mono, in iPhone mode | [Over USB networking (NCM)](#over-usb-networking-iphone-mode-ncm) | Windows, macOS, Linux |

All three give the same calibration. The camera embeds exactly what it has stored into every
recording it makes.

!!! note "Trinet Mono"
    Trinet Stereo and Stereo GS are calibrated individually at the factory. A Trinet Mono has a stored
    calibration only if it came with the per-unit **calibration service**. If yours didn't, the tool
    reports *no calibration stored*. Use the [reference calibration](reference-calibrations.md) for
    your hardware version instead.

## Set up

Install the [Python toolkit](../toolkit/index.md#install) once, then run the commands below from its
folder.

## From a recording (MP4)

Point the tool at any recording the camera made, either from the memory card or from the app. For
a stereo take, use either eye's file.

```bash
python3 scripts/get_calibration.py --mp4 take0004_L.mp4
# stereo calibration (300 bytes) from take0004_L.mp4 -> calibration.json
```

This is the simplest method and needs no camera. It needs the **original** file. A video that has
been re-encoded or edited, or a rendered visualization, no longer carries the calibration.

## Over USB, webcam mode (UVC)

1. Put the camera in **USB webcam** mode: power it on **without a memory card**. The light turns
   <span class="led led-white"></span> white. See [Recording modes](../get-started/modes.md).
2. Connect it to a Linux computer with a USB-C cable, then run:

```bash
python3 scripts/get_calibration.py --uvc
# or name the camera's video device: --uvc /dev/video2
```

The tool finds the Trinet camera by itself. It can read the calibration while another app is
streaming from the camera. If you get *permission denied*, add yourself to the `video` group
(`sudo usermod -aG video $USER`, then log out and back in).

On Windows or macOS, use the MP4 method, or the [Trinet app](#from-the-app-or-your-own-software)
on Android.

## Over USB networking, iPhone mode (NCM)

For **Trinet Mono** in **iPhone** mode. The light turns <span class="led led-cyan"></span> cyan.
To switch the camera to this mode, see [Recording modes](../get-started/modes.md).

1. Connect the camera to the computer with a USB-C cable. The computer sees a new wired network
   connection and gets an address of the form `172.32.X.71` from the camera.
2. Run:

```bash
python3 scripts/get_calibration.py --ncm
# or give the camera's address: --ncm 172.32.18.70
```

The tool finds the camera's address by itself; the camera is always at `172.32.X.70`, on the same
`X` as the computer. If you'd rather not use the toolkit, the camera serves the raw calibration
over HTTP:

```bash
curl -o calibration.bin http://172.32.X.70:8081/api/calibration    # 404 = none stored
python3 -m trinet_tools.calib_blob unpack calibration.bin > calibration.json
```

## Options

| Option | What it does |
|---|---|
| `-o PATH` | Where to write the JSON (default `calibration.json`) |
| `--bin PATH` | Also save the calibration exactly as stored on the camera: 200 bytes for a single camera, 300 for stereo |

The command finishes with one of three exit codes, so scripts can check the result: `0` means the
calibration was written, `1` means none is stored, and `2` means an error, such as no camera found.
The binary format is described in the toolkit's
[file-format reference](https://github.com/Panoculon-Labs/Trinet-tools/blob/main/docs/data_formats.md#calibration-blob-tblc).

## From the app or your own software

- **Trinet app (Android):** *Camera settings → Advanced → Calibration → Read* shows the stored
  calibration. See [Camera settings](../app/camera-settings.md#advanced).
- **Android SDK:** `getCalibrationAny()` returns the stored calibration, mono or stereo.
- **iOS SDK:** `getCalibrationAny()` does the same over USB networking.
- **Python:** `trinet_tools.device_calibration` offers `from_mp4()`, `read_uvc()` and `read_ncm()`,
  plus `to_calibration_json()`.

Next: [Use a calibration](use-a-calibration.md) · [Check your calibration in the field](use-a-calibration.md#check-your-calibration-in-the-field)
