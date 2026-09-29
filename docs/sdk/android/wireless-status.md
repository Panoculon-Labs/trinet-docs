---
title: "Android: wireless status"
description: Follow Trinet cameras recording to their own cards over Bluetooth LE with WirelessCameraMonitor — live state, UTC start/stop events, history and export.
---

# Android: wireless status

`WirelessCameraMonitor` listens to the Bluetooth LE status broadcasts of cameras recording to their
own memory cards. The phone **only listens** — it never connects — so any number of phones can follow
any number of cameras. This is what powers the app's [Wireless status](../../app/wireless-status.md).

**Requirements:** camera firmware 0.5.9+, SDK 0.5.3+, a phone with Bluetooth LE. The broadcast is on by
default; switch it with `device.setWirelessBroadcast(enabled)` (applies from the camera's next start).

## Permissions

The SDK declares no Bluetooth permissions itself. Add:

```xml
<uses-feature android:name="android.hardware.bluetooth_le" android:required="false" />
<uses-permission android:name="android.permission.BLUETOOTH_SCAN"
    android:usesPermissionFlags="neverForLocation" />
<uses-permission android:name="android.permission.BLUETOOTH" android:maxSdkVersion="30" />
<uses-permission android:name="android.permission.BLUETOOTH_ADMIN" android:maxSdkVersion="30" />
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" android:maxSdkVersion="30" />
```

and request `WirelessCameraMonitor.requiredPermissions()` at runtime.

## Follow cameras

```kotlin
val monitor = WirelessCameraMonitor(context)
monitor.start()

scope.launch {
    monitor.cameras.collect { cameras ->
        for (cam in cameras) {
            val status = when {
                cam.recording  -> "recording take ${cam.takeNumber}"
                cam.finalizing -> "finalizing"
                else           -> "idle"
            }
            show(cam.unitId, status, if (cam.sdOk) "card OK" else "no card", cam.rssiAvg)
        }
    }
}

scope.launch {
    monitor.events.collect { e ->
        when (e) {
            is WirelessEvent.Started      -> log("${e.unitId} started take ${e.takeNumber} at ${e.utcMillis}")
            is WirelessEvent.Stopped      -> log("${e.unitId} stopped at ${e.utcMillis}")
            is WirelessEvent.AbnormalStop -> alert("${e.unitId} stopped unexpectedly")
        }
    }
}
// monitor.stop() when done
```

Each camera reports its unit ID, recording / finalizing / card state, take number, number of
recordings on the card, kit ID and role, signal strength, and its model and firmware.

## History and export

The monitor keeps a history on the phone (`WirelessHistory`) and can export it; the toolkit's
[wireless UTC tool](../../toolkit/wireless-utc.md) uses the export to put card recordings on UTC.

Full reference, including scan modes and background logging:
[wireless-status guide on GitHub](https://github.com/Panoculon-Labs/Trinet-SDK/blob/main/docs/wireless-status.md).
