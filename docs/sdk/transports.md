---
title: USB transports
description: How Trinet cameras connect over USB — webcam mode for Android and computers, network mode for iPhone — and what is identical across both.
---

# USB transports

Trinet cameras connect over USB in one of two ways, depending on what the host allows.

| | **USB webcam mode** | **iPhone mode** |
|---|---|---|
| Used by | Android (Trinet app, Android SDK), computers | iPhone (iOS SDK) |
| Cameras | All | Trinet Mono |
| Appears as | A standard USB video device | A USB network adapter (Settings → Ethernet on iPhone) |
| Video | H.264, pulled by the app | H.264, over the USB network link |
| Camera settings | Through the SDK | Through the SDK |
| Light when ready | <span class="led led-white"></span> White | <span class="led led-cyan"></span> Cyan |

On Android the SDK chooses the USB transfer mode (bulk or isochronous) from what the camera reports —
nothing to configure, and cameras on older firmware keep working. On iPhone, traffic stays on the USB
link and never goes over Wi-Fi or cellular.

## What's identical

The transport differs; everything above it is shared, so recordings and tools work across platforms:

- **Video:** H.264 (the live stream) with parameter sets sent up front.
- **Motion data** travels inside the video stream with every frame, with the frame's timestamp on the
  same camera clock — no separate sync channel.
- **On disk:** `.mp4` + `.imu` + `.vts`, byte-for-byte the same formats on Android, iOS, the camera's
  own card and the Python toolkit.
- **Orientation:** Madgwick 6-axis fusion in both SDKs.

Choosing the mode on the camera: [Recording modes](../get-started/modes.md). Technical details:
[transport guide on GitHub](https://github.com/Panoculon-Labs/Trinet-SDK/blob/main/docs/TRANSPORT.md).
