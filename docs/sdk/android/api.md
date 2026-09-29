---
title: "Android: API overview"
description: The main classes of the Trinet Android SDK, by package, with links to the full API reference.
---

# Android: API overview

The full per-class reference is on GitHub:
**[Android API reference](https://github.com/Panoculon-Labs/Trinet-SDK/blob/main/docs/api-reference.md)**.

| Area | Main types | What they do |
|---|---|---|
| Discovery | `DeviceDiscovery`, `DeviceInfo` | Find attached cameras, request USB permission, open a camera |
| Device | `TrinetDevice`, `DeviceControls` | Open sessions; camera settings (bitrate, GOP, image, audio, LED, codec, wireless broadcast); calibration; generation and firmware; `resetSettings()` |
| Session | `SessionConfig`, `TrinetSession`, `StreamLayout` | Negotiate and run the video stream; frame flow; stream health; mono vs side-by-side |
| Recording | `TrinetRecorder`, `RecordingHandle` | Record video + motion data + frame timestamps + metadata to a folder |
| Playback | `RecordingFolder`, `TrinetPlayer` | Browse recordings; frame-accurate playback with aligned motion data |
| Files | `ImuFileReader`, `VtsFileReader` | Read motion-data and frame-timestamp files |
| In-stream data | `SeiImuParser`, `SeiAudioParser`, `AudioPlayer` | Extract motion samples and audio from the live stream |
| Model | `TrinetGeneration`, `VideoCodec`, `ShutterType`, `Calibration`, `StereoCalibrationData` | Camera generation, codec, shutter type, mono and stereo calibration |
| Fusion | `Madgwick` | Orientation from accelerometer and gyroscope |
| Wireless | `WirelessCameraMonitor`, `WirelessCamera`, `WirelessIdentity`, `WirelessAdvert`, `WirelessHistory`, `DeviceClockFit` | Follow cameras over Bluetooth LE; UTC timing; history and export |
| UI (Compose) | `LivePreview`, `LiveAudio`, `ImuOverlayPanel`, `OrientationCube`, `TimeSeriesPlot`, `TripleAxisPlot` | Ready-made preview and motion widgets |

## Design notes

- **Kotlin-first,** built on coroutines, `Flow` and `StateFlow`. Do USB I/O off the main thread.
- **Never throws for missing features:** firmware-dependent getters return `null`, `-1` or `false`
  on cameras that lack them. Feature-detect.
- **Forward and backward compatible files:** readers parse every format version; see
  [File formats](../../data/file-formats.md).
