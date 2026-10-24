---
title: iOS SDK
description: The Trinet Swift package for iPhone — stream, preview and record Trinet Mono, Stereo and Stereo GS over USB, plus a demo app you can build and run on your own iPhone.
---

# iOS SDK

The iOS SDK is a Swift package in the [Trinet-SDK repository](https://github.com/Panoculon-Labs/Trinet-SDK/tree/main/ios)
for capturing video, motion data and audio from a Trinet camera connected to an iPhone over USB.

| | |
|---|---|
| Version | **0.3.5** (repository tag `v0.5.4`) |
| Minimum iOS | 17.0 |
| Language | Swift 5.9, no external dependencies |
| Cameras | Trinet Mono (V4), Trinet Stereo and Trinet Stereo GS, in **iPhone mode** |
| Camera firmware | Stereo and Stereo GS: [0.5.13](../firmware/release-notes.md#0513) or newer |

iPhones don't let apps use external USB webcams, so the camera connects in **iPhone mode**: it appears
as a USB network adapter and serves its stream over that link. The SDK keeps all traffic on that USB
link — never Wi-Fi or cellular. See [USB transports](transports.md).

## Get started

These steps take you from a camera in its box to a recording on your iPhone, using the **TrinetApp**
demo app from the repository. There is no App Store app: iOS apps must be signed for your own phone,
so you build the demo from source on a Mac. A free Apple ID is enough.

<ol class="steps" markdown>

<li markdown>**Put the camera in iPhone mode.** Create a text file on the camera's memory card at
`Trinet/trinet_mode.conf` containing the line `mode=ncm`, insert the card and power the camera on.
Alternatively, set *Boot mode → iPhone* in the [Trinet app](../app/camera-settings.md#advanced) on
Android, which applies when no card is inserted. The light turns
<span class="led led-cyan"></span> **cyan**. See [Recording modes](../get-started/modes.md).

Stereo and Stereo GS need camera firmware 0.5.13 or newer for iPhone mode. On older firmware they
start in USB webcam mode instead (light <span class="led led-white"></span> white). Update them
first: [Update the firmware](../get-started/update-firmware.md).</li>

<li markdown>**Install the tools on your Mac:** Xcode 16 or newer, and
[XcodeGen](https://github.com/yonomi/xcodegen) (`brew install xcodegen`).</li>

<li markdown>**Get the demo app and open it in Xcode:**

```bash
git clone https://github.com/Panoculon-Labs/Trinet-SDK.git
cd Trinet-SDK/ios/TrinetApp
xcodegen generate          # re-run after every git pull
open TrinetApp.xcodeproj
```
</li>

<li markdown>**Set your signing team** (once): select the **TrinetApp** target → **Signing &
Capabilities** → tick *Automatically manage signing* → choose your **Team**. A personal Apple ID
works.</li>

<li markdown>**Run it on your iPhone.** Connect the iPhone (iOS 17 or newer) to the Mac, trust the
computer, choose the iPhone as the run destination and press **▶ Run**. The first time, trust your
developer certificate on the phone under **Settings → General → VPN & Device Management**, then open
the app.

With a free Apple ID the app stops opening after **7 days**; run it from Xcode again to renew it. A
paid Apple Developer Program account removes the limit and adds TestFlight.</li>

<li markdown>**Connect the camera to the iPhone** with a USB-C cable. Within a few seconds a new
interface appears under **Settings → Ethernet**, and the app's Home tab shows the camera. Allow the
*Local Network* permission if iOS asks.</li>

<li markdown>**Record.** Open Record, check the preview — on a stereo camera choose the left eye,
right eye or both — and tap Record. Recordings continue if you lock the phone or switch apps. Files
are saved in the app's `Documents/Trinet/` folder: on a Mac, open the iPhone in **Finder → Files →
TrinetApp** to copy them off, or use *Share* in the app's Library.</li>

</ol>

The demo app also has a Library with full playback and a Controls tab with the camera's settings.

## Add the SDK to your app

```swift title="Package.swift"
dependencies: [
    .package(url: "https://github.com/Panoculon-Labs/Trinet-SDK", from: "0.5.4"),
],
targets: [
    .target(name: "MyApp", dependencies: [
        .product(name: "TrinetSDK", package: "Trinet-SDK"),
    ]),
]
```

In Xcode: **File → Add Package Dependencies…**, enter the repository URL, choose **Up to Next Major
0.5.4** and add the **TrinetSDK** product.

!!! note "Which version to pin"
    The repository ships the Android and iOS SDKs under one tag series. Tag `v0.5.4` carries iOS SDK
    0.3.5, so pin `from: "0.5.4"`. Older tags carry older iOS code — `v0.5.3` has iOS 0.2.1.

### Quick start

```swift
import TrinetSDK

// 1. Find the camera on the USB network link
let discovery = TrinetDiscovery()
guard let device = await discovery.scan(timeout: 2.0).first else { return }

// 2. Connect and open a live session
try await device.connect()
let session = await device.liveSession()
await session.start()

// 3. Preview in SwiftUI; on a stereo camera pick .left, .both or .right
//    LivePreviewView(stream: session.sampleStream, lens: .both)

// 4. Motion data, per frame
Task {
    for await batch in session.imuStream {
        // batch.samples: [ImuSample]
    }
}

// 5. Record: .mp4 (video, audio, motion data) + .imu + .vts
let handle = try await session.startRecording(in: outputDirectory)
// …
session.stopRecording()

// 6. Tear down
await session.stop()
await device.disconnect()
```

## Cameras and video

| Camera | Live video over USB |
|---|---|
| Trinet Mono (V4) | 1920×1080, 30 fps |
| Trinet Stereo | 3840×1080 side-by-side, 30 fps — left eye x 0–1919, right eye x 1920–3839 |
| Trinet Stereo GS | 3840×1080 side-by-side, 30 fps, global shutter |

On connect the SDK reads the camera model (`device.info`, `isStereo`, `model`). A stereo camera sends
both eyes in one frame, with one motion-data and audio stream for the pair; recordings keep the full
side-by-side frame.

There are two independent codec settings:

| Setting | SDK | Controls |
|---|---|---|
| Stream codec | `streamCodec()` / `setStreamCodec(_:)` | The live stream to the iPhone, H.264 or H.265. Changing it restarts the camera's stream (5–10 s); the session reconnects by itself. |
| Recording codec | `recordingCodec()` / `setRecordingCodec(_:)` | The camera's own memory-card recordings. |

The live session always follows the codec the camera actually streams. Cameras whose firmware has no
stream-codec setting stream H.264.

## Camera settings

`TrinetDevice` reads and sets the camera's settings, as the [Trinet app](../app/camera-settings.md)
does on Android: picture (brightness, contrast, saturation, sharpness, hue, gain, exposure, white
balance), sound, bitrate and rate control, keyframe interval, mains frequency, status light, wireless
broadcast, thermal limit, temporal noise reduction (Stereo GS), calibration read and upload, and the
boot mode.

| Setting | SDK |
|---|---|
| [Split recordings](../app/camera-settings.md#set-split-recordings-chunking) (chunking) | `setRecordingChunk(minutes:)` — 0 = one continuous file |
| Rotate the picture 180° | `setImageFlip(_:)` — the camera restarts |
| Uncompressed card audio | `setRecordingAudioFormat(_:)` — adds a `.wav` beside each card recording |

These three need camera firmware 0.5.13 or newer on Stereo and Stereo GS. Each setting is read on
connect; the demo app hides any the camera doesn't support. In your own code, treat a failed read as
"not available".

## Recording in the background

A recording on the iPhone keeps running when the app goes to the background or the phone locks. While
it records, the SDK's `BackgroundKeepAlive` keeps a silent audio session open, and the app declares
`UIBackgroundModes: audio`. The preview pauses in the background (iOS allows no video decoding there)
and resumes at the next keyframe. When not recording, the demo app closes the stream in the
background and reopens it on return.

!!! warning "App Store review"
    Silent background audio can be questioned in App Store review. TestFlight, ad-hoc and enterprise
    builds are unaffected.

## Troubleshooting

| Symptom | Fix |
|---|---|
| No camera in the app | Check the camera's light is <span class="led led-cyan"></span> cyan (iPhone mode) and that **Settings → Ethernet** lists it; wait a few seconds for it to get an address, then rescan. |
| A stereo camera's light is white, not cyan | Its firmware is older than 0.5.13 — [update it](../get-started/update-firmware.md). |
| The *Local Network* prompt appears again | iOS resets it when the app is reinstalled — allow it in Settings. |
| The app won't open after a week | Free Apple ID signing lasts 7 days — run it from Xcode again. |
| The Simulator can't see the camera | USB cameras only work on a real iPhone. |

## More

- [Full iOS guide on GitHub](https://github.com/Panoculon-Labs/Trinet-SDK/blob/main/ios/README.md) —
  every API, the SwiftUI helpers, diagnostics and the file formats.
- [iOS changelog](https://github.com/Panoculon-Labs/Trinet-SDK/blob/main/ios/CHANGELOG.md).
- [Network API reference](https://github.com/Panoculon-Labs/Trinet-SDK/blob/main/ios/docs/PROTOCOLS.md)
  — the camera's HTTP endpoints in iPhone mode.
- Recordings use the same [file formats](../data/file-formats.md) as Android, the camera's own card
  and the [Python toolkit](../toolkit/index.md).
