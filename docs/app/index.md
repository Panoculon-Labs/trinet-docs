---
title: Trinet app
description: The Trinet app for Android — live preview and recording over USB, camera settings, firmware updates and wireless status for kits.
---

# Trinet app

The Trinet app for Android is the companion for every Trinet camera. Use it to:

- **preview and record** over USB, with motion data and audio;
- **review** recordings frame by frame with the motion data overlaid;
- **change camera settings** — picture, sound, video, recording codec and more;
- **update the camera's firmware**;
- **watch cameras and kits** recording to their own cards, over Bluetooth.

[:material-google-play: Get it on Google Play](https://play.google.com/store/apps/details?id=com.panoculonlabs.trinet){ .md-button .md-button--primary }

## Requirements

| | |
|---|---|
| Android | 9 or newer |
| Phone | USB-C with USB host (OTG) support |
| Bluetooth LE | Optional — only for [Wireless status](wireless-status.md) |
| Cameras | Every Trinet camera. Features that need newer camera firmware say so in the app. |

## First connection

<ol class="steps" markdown>
<li markdown>Put the camera in **USB webcam** mode: power it **without a memory card**. The light turns
<span class="led led-white"></span> white. (See [Recording modes](../get-started/modes.md).)</li>
<li markdown>Connect it to the phone with a USB-C cable. The app opens automatically when a Trinet camera
is plugged in.</li>
<li markdown>The home screen shows **Camera found – Tap to allow access**. Tap it and allow access in the
Android dialog. (Android asks for the camera permission too — USB video needs it.)</li>
<li markdown>The status changes to **Camera ready**.</li>
</ol>

## Home screen

| Tile | What it's for |
|---|---|
| **Record** | Live preview and recording — [Record and review](record-and-review.md) |
| **Library** | Your recordings on the phone |
| **Wireless status** | Cameras and kits recording to their cards nearby — [Wireless status](wireless-status.md) |
| **Camera settings** | Picture, sound, video and advanced settings — [Camera settings](camera-settings.md) |
| **Update firmware** | Check for and install camera firmware — [Firmware](../firmware/index.md) |

The app uses a dark interface on purpose, so you can judge the picture accurately.

!!! tip "Build your own app"
    Everything the app does is available to developers in the [Trinet SDK](../sdk/index.md), with a
    demo app you can build from source.
