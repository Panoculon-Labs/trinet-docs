---
title: "Android: stream and preview"
description: Open a Trinet video session on Android, consume the frame flow, show a live preview, and handle stereo cameras.
---

# Android: stream and preview

## Open a session

```kotlin
val config = SessionConfig(width = 1920, height = 1080, fps = 30)
val session = withContext(Dispatchers.IO) { device.open(config) }
if (!session.start()) {
    // the camera didn't offer a matching format
}
```

The camera chooses the USB transfer mode (bulk or isochronous) itself; there's nothing to
configure.

## The frame flow

`session.frames` is a Kotlin `Flow` of H.264 access units — each with the video, the motion samples
captured since the previous frame and (on cameras with microphones) audio embedded. Any number of
consumers can collect it at once — for example a preview and a recorder.

```kotlin
session.frames
    .onEach { frame ->
        // frame.annexB: one H.264 access unit; frame.ptsUs: microseconds
    }
    .launchIn(scope)
```

A 1 Hz **stream health** flow reports measured frame rates, dropped or corrupt frames, the
transfer mode and stalls.

## Live preview (Jetpack Compose)

```kotlin
LivePreview(
    frames = session.frames,
    width = session.negotiatedWidth,
    height = session.negotiatedHeight,
)
```

`LiveAudio` plays the embedded audio during preview on cameras with microphones.

## Stereo cameras { #stereo-cameras }

Trinet Stereo and Stereo GS send **both eyes side by side in one frame** (3840×1080; the left half is
the left eye). Ask for the wide frame with a mono fallback and the same code opens any camera:

```kotlin
val config = SessionConfig(
    width = 3840, height = 1080, fps = 30,
    fallbackWidth = 1920, fallbackHeight = 1080,
)
val session = withContext(Dispatchers.IO) { device.open(config) }
check(session.start())

session.layout         // StreamLayout.SIDE_BY_SIDE or StreamLayout.MONO
session.isSideBySide   // true on a stereo camera
```

- **Detect stereo from the stream shape**, not the USB product ID — stereo and mono cameras can
  share a product ID.
- **Preview one eye:** pass `cropEye = 0` (left) or `1` (right) to `LivePreview`.
- **Record** with the negotiated size; recordings keep both eyes and are marked side-by-side.
- **Calibration:** `device.getCalibrationAny()` returns a mono or a two-eye stereo calibration.
- **Global shutter:** Stereo GS behaves the same; its frames report a readout time of zero and the
  shutter type is reported as global. A rolling-shutter calibration isn't valid on a global-shutter
  camera.

Some phones' hardware decoders reject 3840-wide video; `LivePreview` falls back to software decoding
automatically.

## Stop

Cancel your collectors, then `session.close()` and `device.close()`.

More: [streaming guide on GitHub](https://github.com/Panoculon-Labs/Trinet-SDK/blob/main/docs/streaming.md).
