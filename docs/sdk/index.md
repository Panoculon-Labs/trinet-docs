---
title: Build apps
description: The Trinet SDK for Android and iOS — stream, record and play back Trinet video with synchronized motion data in your own app.
---

# Build apps with the Trinet SDK

The [Trinet SDK](https://github.com/Panoculon-Labs/Trinet-SDK) (MIT licence) lets your app use Trinet
cameras over USB: live video with the motion data embedded in every frame, recording with the same
files the camera writes, frame-accurate playback, camera settings, calibration and wireless status.

| Platform | Distribution | Version | Transport |
|---|---|---|---|
| **Android** | Prebuilt AAR (`com.panoculon:trinet-sdk:0.5.3`) + demo APK on [Releases](https://github.com/Panoculon-Labs/Trinet-SDK/releases) | 0.5.3 | USB webcam (UVC) |
| **iOS** | Swift source via Swift Package Manager | 0.2.1 | USB network (iPhone mode) |

## Camera compatibility

The SDK works with **every Trinet camera**. Newer capabilities are additive: where a camera or its
firmware can't do something, the SDK reports that (a `null`, `-1` or `false`) instead of failing.

| | V1/V2 (legacy) | V3 | V4 Mono | Stereo | Stereo GS |
|---|:---:|:---:|:---:|:---:|:---:|
| H.264 streaming, live preview, recording | ✓ | ✓ | ✓ | ✓ | ✓ |
| USB transfer mode chosen automatically | ✓ | ✓ | ✓ | ✓ | ✓ |
| Motion data in the stream (accel / gyro / temperature) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Hardware frame-sync delay per sample | ✓ | — | — | — | — |
| Live magnetometer | — | ✓ | ✓ | ✓ | ✓ |
| Embedded stereo audio | — | — | ✓ | ✓ | ✓ |
| Mid-exposure frame timing | — | — | ✓ | ✓ | ✓ |
| Rolling-shutter readout per frame | — | — | ✓ | ✓ | — (global shutter) |
| Both eyes in one side-by-side frame (3840×1080) | — | — | — | ✓ | ✓ |

Some controls depend on the camera's **firmware** rather than its generation — for example
`setVideoCodec` (firmware 0.5.7+) and `getWirelessBroadcast` (0.5.9+). **Feature-detect, don't
version-detect:** call the getter and check for `null`.

## Android in five minutes

```kotlin
// 1. Discover and open (suspends on the USB permission prompt).
val device = withContext(Dispatchers.IO) { DeviceDiscovery.openFirstAvailable(context) }
    ?: error("No Trinet camera attached")

// 2. Open a stream — wide frame for stereo cameras, 1080p fallback for mono.
val config = SessionConfig(width = 3840, height = 1080, fps = 30,
                           fallbackWidth = 1920, fallbackHeight = 1080)
val session = withContext(Dispatchers.IO) { device.open(config) }
check(session.start())

// 3. Preview (Jetpack Compose)
// LivePreview(frames = session.frames, width = session.negotiatedWidth, height = session.negotiatedHeight)

// 4. Record video + motion data + frame timestamps into a folder.
val recorder = TrinetRecorder(
    rootDir = context.filesDir,
    width = session.negotiatedWidth, height = session.negotiatedHeight, fps = 30,
    sampleRateHz = 400,   // the camera's IMU rate — read it from the stream or a recording
    device = TrinetRecorder.DeviceMeta(device.info.vendorId, device.info.productId, device.info.serial),
)
val handle = recorder.start()
val job = session.frames.onEach { f -> recorder.submitAccessUnit(f.annexB, f.ptsUs) }
    .flowOn(Dispatchers.IO).launchIn(scope)

// 5. Stop.
job.cancel(); handle.stop(); session.close(); device.close()
```

Step by step: [Get started](android/getting-started.md) · [Stream and preview](android/streaming.md) ·
[Record and play back](android/recording.md) · [IMU data](android/imu.md) ·
[Wireless status](android/wireless-status.md) · [API overview](android/api.md)

## Demo app

The demo APK on [GitHub Releases](https://github.com/Panoculon-Labs/Trinet-SDK/releases) exercises the
whole SDK — USB pairing, live preview, recording, a library with frame-accurate scrubbing, motion
overlays, stereo preview with a left/right switch, every camera setting, wireless status and firmware
update. The [Trinet app](../app/index.md) on Google Play is built on the same SDK.

## iOS

See [iOS SDK](ios.md). iPhones connect to Trinet Mono in iPhone mode; the two platforms carry the same
video and motion data and write the same files — see [USB transports](transports.md).
