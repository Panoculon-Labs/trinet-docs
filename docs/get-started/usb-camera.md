---
title: Use as a USB camera
description: Stream a Trinet camera live over USB to the Trinet Android app, a computer or an iPhone.
---

# Use as a USB camera

Over USB, the camera streams video with the motion data and audio embedded, and the phone or
computer records it.

=== "Android (Trinet app)"

    <ol class="steps" markdown>
    <li markdown>**Install the [Trinet app](../app/index.md)** from Google Play (Android 9 or newer, with
    USB-C host support).</li>
    <li markdown>**Remove the memory card** from the camera (or use a [mode file](modes.md#the-mode-file)
    with `mode=uvc`).</li>
    <li markdown>**Connect the camera to the phone** with a USB-C cable. The light turns
    <span class="led led-white"></span> **white** when the camera is ready.</li>
    <li markdown>**Open the app and allow access** when Android asks for permission to use the camera
    (this can take a few seconds to appear). The app shows *Camera ready*.</li>
    <li markdown>**Tap Record.** You'll see the live preview; tap record to save to the phone. See
    [Record and review](../app/record-and-review.md).</li>
    </ol>

=== "Computer"

    In USB webcam mode the camera is a standard USB video device. Use the
    [Python toolkit's USB recorder](../toolkit/inspect-and-repair.md#record-from-a-computer) to save
    video with the embedded motion data, or any webcam software to view it.

    Trinet Stereo and Stereo GS stream both eyes as one 3840×1080 side-by-side image.

=== "iPhone (Trinet Mono)"

    iPhones connect to Trinet Mono in **iPhone mode**:

    1. Put a card in the camera with `Trinet/trinet_mode.conf` containing `mode=ncm`
       ([details](modes.md#the-mode-file)), or choose iPhone in the app's Boot mode.
    2. Power the camera; the light turns <span class="led led-cyan"></span> **cyan**.
    3. Connect it to the iPhone and open an app built with the [iOS SDK](../sdk/ios.md). The SDK
       includes a demo app you can build and run.

## Good to know

- The live stream is always **H.264**, 30 fps.
- Settings you change in the app are stored on the camera. On Trinet Mono they apply to card
  recordings too; Trinet Stereo and Stereo GS card recordings always use 10 Mbps per eye, whatever
  the bitrate setting (the recording codec setting does apply).
- In USB modes the camera's button does nothing — record from the app.
- Some USB hubs and very long or worn cables cause disconnects. Use a good-quality USB-C cable.
