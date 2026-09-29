---
title: iOS SDK
description: The Trinet Swift package for iPhone — discover, stream, preview and record a Trinet camera over USB, plus a demo app you can build.
---

# iOS SDK

The iOS SDK is a Swift package in the [Trinet-SDK repository](https://github.com/Panoculon-Labs/Trinet-SDK/tree/main/ios)
for capturing video and motion data from a Trinet camera connected to an iPhone over USB.

| | |
|---|---|
| Minimum iOS | 17.0 |
| Language | Swift 5.9, no external dependencies |
| Cameras | Trinet Mono in **iPhone mode** |
| Version | 0.2.1 |

iPhones don't let apps use external USB webcams, so the camera connects in **iPhone mode**: it appears
as a USB network adapter and serves its stream over that link. Put the camera in this mode with a
[mode file](../get-started/modes.md#the-mode-file) (`mode=ncm`) or the app's Boot mode setting; the
light turns <span class="led led-cyan"></span> cyan. See [USB transports](transports.md).

## Install

```swift title="Package.swift"
dependencies: [
    .package(url: "https://github.com/Panoculon-Labs/Trinet-SDK", from: "0.2.1"),
],
targets: [
    .target(name: "MyApp", dependencies: [
        .product(name: "TrinetSDK", package: "Trinet-SDK"),
    ]),
]
```

In Xcode: **File → Add Package Dependencies…**, enter the repository URL and add the **TrinetSDK**
product.

## Quick start

```swift
import TrinetSDK

let discovery = TrinetDiscovery()
guard let device = await discovery.scan(timeout: 2.0).first else { return }

try await device.connect()
let session = await device.liveSession()
await session.start()

// Live preview in SwiftUI:  LivePreviewView(stream: session.sampleStream)

Task {
    for await batch in session.imuStream {
        // batch.samples: [ImuSample]
    }
}

let handle = try await session.startRecording(in: outputDirectory)   // .mp4 + .imu + .vts
// …
session.stopRecording()
await session.stop()
await device.disconnect()
```

SwiftUI helpers include a live preview, motion plots, an orientation cube and a playback motion track;
`MadgwickAHRS` computes orientation.

## Demo app

The repository includes **TrinetApp**, a complete SwiftUI demo — device list, live preview with motion
plots, recording and playback. To run it you need a Mac with Xcode 16+, an Apple ID and
[XcodeGen](https://github.com/yonomi/xcodegen); the
[iOS guide](https://github.com/Panoculon-Labs/Trinet-SDK/blob/main/ios/README.md) walks through
clone → Xcode → iPhone.
