---
title: "Android: IMU data"
description: Read Trinet motion samples live from the video stream on Android, compute orientation with Madgwick fusion, and show IMU widgets.
---

# Android: IMU data

## The sample

Each motion sample carries:

| Field | Unit |
|---|---|
| `timestampNs` | Nanoseconds on the camera clock (the same clock as the frame timestamps) |
| `accel` | m/s², x/y/z, gravity included |
| `gyro` | rad/s, x/y/z |
| `mag` | µT, x/y/z — live on cameras with a magnetometer |
| `tempC` | Sensor temperature, °C |

The trailing per-sample value means different things by generation (a frame-sync delay on V1/V2, the
magnetometer reading's age on newer cameras); use `SeiImuParser.deriveSofNs(sample, version)` rather
than interpreting it yourself.

## Rate

400 Hz on current cameras, about 562 Hz on V1/V2. Each video frame carries the samples captured since
the previous frame — about 13 per frame at 400 Hz. Read the rate from the data rather than assuming it.

## Live samples from the stream

```kotlin
session.frames
    .onEach { frame ->
        for (payload in SeiImuParser.parse(frame.annexB)) {
            // payload.header: version, sample count, sensor ranges
            for (sample in payload.samples) {
                // sample.timestampNs, sample.accel, sample.gyro, sample.mag, …
            }
        }
    }
    .launchIn(scope)
```

## Orientation (Madgwick fusion)

```kotlin
val madgwick = Madgwick(beta = 0.1f)
var lastNs = 0L

fun onSample(s: ImuSample) {
    if (lastNs == 0L) {
        madgwick.seedFromAccel(s.accel[0], s.accel[1], s.accel[2])
    } else {
        val dt = (s.timestampNs - lastNs).coerceAtLeast(0L) / 1e9f
        madgwick.updateIMU(s.gyro[0], s.gyro[1], s.gyro[2], s.accel[0], s.accel[1], s.accel[2], dt)
    }
    lastNs = s.timestampNs
    val quatXyzw = madgwick.asXyzw()
}
```

## UI widgets (Compose)

`ImuOverlayPanel` (live values), `OrientationCube` (quaternion-driven 3D cube) and
`TimeSeriesPlot` / `TripleAxisPlot` (scrolling plots).

For aligning samples to frames, see [Timing and sync](../../data/sync.md). More:
[IMU guide on GitHub](https://github.com/Panoculon-Labs/Trinet-SDK/blob/main/docs/imu.md).
