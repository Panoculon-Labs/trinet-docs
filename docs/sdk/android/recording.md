---
title: "Android: record and play back"
description: Record Trinet video, motion data and timestamps on Android with TrinetRecorder, and play back frame-accurately with TrinetPlayer.
---

# Android: record and play back

## Record

```kotlin
val recorder = TrinetRecorder(
    rootDir = context.filesDir,
    width = session.negotiatedWidth,
    height = session.negotiatedHeight,
    fps = 30,
    sampleRateHz = 400,            // the camera's IMU rate; written into the motion-data header
    device = TrinetRecorder.DeviceMeta(
        vendorId = device.info.vendorId,
        productId = device.info.productId,
        serial = device.info.serial,   // public per-unit ID
    ),
)

val handle = recorder.start()
val job = session.frames
    .onEach { f -> recorder.submitAccessUnit(f.annexB, f.ptsUs) }
    .flowOn(Dispatchers.IO)
    .launchIn(scope)

// … later
job.cancel()
handle.stop()      // finalizes the video and closes the data files
```

!!! warning "Don't hard-code the IMU rate"
    It is 400 Hz on current cameras and about 562 Hz on V1/V2. Use the rate the camera reports
    rather than a constant.

### The recording folder

| File | Contains |
|---|---|
| `video.mp4` | The video; on cameras with microphones, audio is added as a second track automatically. Also embeds the camera's identity and calibration. |
| `imu.bin` | Motion data |
| `frames.bin` | Frame timestamps |
| `meta.json` | Recording details (camera, firmware, stream layout, settings) |

`handle.state` is a `StateFlow` of the recording's state. These are the same formats as card
recordings, so the [Python toolkit](../../toolkit/index.md) reads them too.

### The camera's own card recordings

- `device.setVideoCodec(VideoCodec.H265)` / `getVideoCodec()` choose H.264 (default) or H.265 for
  recordings the camera writes to its card — from the next take, no restart. H.265 files are roughly
  40% smaller but slower to decode and less widely supported. Firmware 0.5.7+.
- To follow cameras recording to their cards, see [Wireless status](wireless-status.md).

## Play back

```kotlin
val folder = RecordingFolder(File(recordingsRoot, recordingId))
val player = TrinetPlayer(folder, surface)   // surface from a SurfaceView

player.play()
player.pause()
player.seekToFrame(120)          // frame-accurate; motion data follows

player.currentFrame              // StateFlow<Int>
player.currentSample             // StateFlow<ImuSample?> — motion aligned to the frame on screen
```

`RecordingFolder.listIn(...)` lists recordings for a library screen; `ImuFileReader` and
`VtsFileReader` read the data files directly.

More: [recording](https://github.com/Panoculon-Labs/Trinet-SDK/blob/main/docs/recording.md) and
[playback](https://github.com/Panoculon-Labs/Trinet-SDK/blob/main/docs/playback.md) guides on GitHub.
