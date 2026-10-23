---
title: Camera settings
description: Every Trinet camera setting in the app — picture, sound, video bitrate and codec, wireless broadcast, boot mode, calibration and restore defaults.
---

# Camera settings

Settings are stored **on the camera**, so they stay with it whichever phone or computer you use. On
Trinet Mono they apply to card recordings as well as USB streaming. Settings a camera's firmware
doesn't support yet are shown with *Update the camera firmware to enable them*.

## Picture

Brightness, contrast, saturation, sharpness, gain, white balance (automatic or a colour
temperature), manual exposure, and the status light.

## Sound

On cameras with microphones: mute, automatic gain, gain level and sample rate (16, 44.1 or 48 kHz). The camera also has a [hardware mute switch](../get-started/mute-switch.md).

## Video

| Setting | What it does |
|---|---|
| **Bitrate** | 1–20 Mbps (0.5 Mbps steps), with constant (CBR) or variable (AVBR) rate control. The camera restarts to apply it. Stereo card recordings always use 10 Mbps per eye. |
| **Recording codec** | **H.264** or **H.265** for recordings the camera writes to its own card. Applies from the next take, no restart. The live USB stream is always H.264. Needs camera firmware 0.5.7 or newer on stereo cameras (0.5.9 on Mono). |
| **Exposure range** | Minimum and maximum exposure time. |
| **Split recordings** | Off, 5, 10, 15, 30 or 60 minutes — also called **chunking**. Cameras ordered that way are set at the factory, with lengths up to 240 minutes. A long recording is saved as a series of takes of that length instead of one very large file, so a problem costs you one take rather than everything. Applies from the next recording, no restart. Expect a pause of 10–20 seconds between takes. [How to set it](#set-split-recordings-chunking). |
| **Location** | Mains frequency, 50 or 60 Hz, to avoid flicker under artificial light. Choose your country's mains frequency. |

!!! tip "H.264 or H.265?"
    H.264 plays everywhere and decodes fastest — the best default for data pipelines. H.265 gives
    smaller files at the same quality if your tools support it.

### Set split recordings (chunking) { #set-split-recordings-chunking }

You need Trinet app 0.5.5 or newer. On Trinet Stereo and Stereo GS, use camera firmware
[0.5.13](../firmware/release-notes.md#0513) or newer, which starts and ends each take cleanly.

<ol class="steps" markdown>

<li markdown>**Connect the camera to the phone** in USB webcam mode: no memory card, light
<span class="led led-white"></span> **white**. The home screen shows *Camera ready*. Then tap
**Camera settings**.

<div class="photo-row"><figure><img class="app-shot" src="../../assets/images/app/app-home.webp" alt="Trinet app home screen with Camera ready and the Camera settings button" loading="lazy"><figcaption>Tap <em>Camera settings</em>.</figcaption></figure><figure><img class="app-shot" src="../../assets/images/app/settings-top.webp" alt="Camera settings screen, showing the camera as Connected" loading="lazy"><figcaption>The camera shows as <em>Connected</em>.</figcaption></figure></div>
</li>

<li markdown>**Scroll down to Video → Split recordings.** The card shows the camera's current
setting, for example *Current: off — one continuous file*. A camera set to split at the factory
shows its length here. Tap **Read from camera** to refresh it.

<div class="photo-row"><figure><img class="app-shot card" src="../../assets/images/app/split-recordings-off.webp" alt="Split recordings card: Current off, with buttons Off, 5, 10, 15, 30 and 60 min and Read from camera" loading="lazy"><figcaption>The <em>Split recordings</em> card, set to <em>Off</em>.</figcaption></figure></div>
</li>

<li markdown>**Tap a length**: 5, 10, 15, 30 or 60 min, or **Off** for one continuous file. The
button fills in, and the app confirms *Recordings will be split every … min — applies to the next
recording*.

<div class="photo-row"><figure><img class="app-shot card" src="../../assets/images/app/split-recordings-30.webp" alt="Split recordings card with 30 min selected and the confirmation message" loading="lazy"><figcaption>Set to 30 minutes.</figcaption></figure></div>
</li>

<li markdown>**Record as usual.** The setting is saved on the camera and applies from the next
recording to its memory card. There's no restart, and a recording already running isn't changed.
Unplug the camera, insert the card and start recording with the button.</li>

</ol>

On Stereo and Stereo GS with firmware 0.5.13, each part is saved as **its own numbered take**
(`take0001`, `take0002`, …) directly in `Trinet/recording/`. That replaces the folder of parts the
app's description mentions. See [Split recordings](../get-started/files-on-the-card.md#split-recordings)
for what a split session looks like on the card.

If the card says *Not available on this camera's firmware*, [update the camera
firmware](../get-started/update-firmware.md) first.

## Wireless

**Broadcast recording status** — lets phones follow the camera's recording status over Bluetooth
while it records to its card (see [Wireless status](wireless-status.md)). On by default with
firmware 0.5.9 or newer; the camera applies a change from its next start.

## Advanced

| Setting | What it does |
|---|---|
| **Keyframe interval (GOP)** | 1–600 frames; default 30 (one keyframe per second). The camera restarts to apply it. |
| **Embed IMU samples** | Carry motion data inside the video stream (on by default; needed by the app and SDK). |
| **Calibration** | *Read* the calibration stored on the camera, *Upload from file* (a `calibration.json`), or *Lock calibration* so it can't be overwritten. |
| **Boot mode** | The mode the camera starts in when **no card** is inserted: USB webcam, iPhone or card recording. The camera restarts. See [Recording modes](../get-started/modes.md). |
| **Restore defaults** | Returns picture, sound and video settings to the factory defaults. Keeps the boot mode, calibration and kit pairing. |
