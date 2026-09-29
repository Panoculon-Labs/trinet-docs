---
title: "Android: get started"
description: Add the Trinet SDK to an Android project, set up the manifest and USB permissions, and open a camera.
---

# Android: get started

## Requirements

| | |
|---|---|
| Min SDK | 28 (Android 9) |
| Native ABIs | `arm64-v8a`, `armeabi-v7a`, `x86_64` |
| Hardware | USB host (USB-C OTG); Bluetooth LE only for [wireless status](wireless-status.md) |
| Language | Kotlin (coroutines and `Flow` throughout; Java interop works) |

## Install

Download `trinet-sdk-0.5.3.aar` from the [SDK repository](https://github.com/Panoculon-Labs/Trinet-SDK/tree/main/aar)
and add it as a flat-dir dependency. A flat AAR carries no POM, so declare its runtime dependencies
yourself.

```kotlin title="settings.gradle.kts"
dependencyResolutionManagement {
    repositories {
        google()
        mavenCentral()
        flatDir { dirs("aar") }
    }
}
```

```kotlin title="app/build.gradle.kts"
android {
    defaultConfig { minSdk = 28 }
    buildFeatures { compose = true }
}

dependencies {
    implementation(":trinet-sdk-0.5.3@aar")
    implementation("androidx.core:core-ktx:1.13.1")
    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-android:1.9.0")

    // Only if you use the SDK's Compose UI widgets:
    implementation(platform("androidx.compose:compose-bom:2024.10.00"))
    implementation("androidx.compose.ui:ui")
    implementation("androidx.compose.material3:material3")
}
```

## Manifest

Three things are needed for any app that talks to a Trinet camera:

1. the **USB host** feature;
2. the **CAMERA** permission — Android silently denies USB access to video devices without it, so
   request it at runtime too;
3. a **`USB_DEVICE_ATTACHED`** filter (recommended) — your activity then opens automatically when a
   camera is plugged in, and Android pre-grants USB access to it.

```xml title="AndroidManifest.xml"
<uses-feature android:name="android.hardware.usb.host" android:required="true" />
<uses-permission android:name="android.permission.CAMERA" />

<activity android:name=".MainActivity" android:exported="true" android:launchMode="singleTask">
    <intent-filter>
        <action android:name="android.intent.action.MAIN" />
        <category android:name="android.intent.category.LAUNCHER" />
    </intent-filter>
    <intent-filter>
        <action android:name="android.hardware.usb.action.USB_DEVICE_ATTACHED" />
    </intent-filter>
    <meta-data android:name="android.hardware.usb.action.USB_DEVICE_ATTACHED"
               android:resource="@xml/device_filter" />
</activity>
```

```xml title="res/xml/device_filter.xml (decimal IDs)"
<resources>
    <usb-device vendor-id="8711" product-id="22" />
    <usb-device vendor-id="8711" product-id="24" />
    <usb-device vendor-id="8711" product-id="26" />
</resources>
```

The same IDs are available in code as `DeviceInfo.TRINET_VID` and `DeviceInfo.TRINET_PIDS`. The USB
product ID does **not** tell you which camera model is attached — see
[stereo cameras](streaming.md#stereo-cameras).

## Open a camera

```kotlin
// All attached Trinet cameras
val attached = DeviceDiscovery.connectedDevices(context)

// Ask for USB permission (suspends until the user answers; true if already granted)
val granted = DeviceDiscovery.requestPermission(context, attached.first())

// Or all in one: discover, ask, open — off the main thread
val device: TrinetDevice? = withContext(Dispatchers.IO) {
    DeviceDiscovery.openFirstAvailable(context)
}
```

If the user denies permission or another app holds the camera, **unplugging and reconnecting** is the
reliable reset — prompt the user to do that.

Next: [Stream and preview](streaming.md). Full details, including lifecycle and reconnecting after the
camera re-enumerates: [getting-started guide on GitHub](https://github.com/Panoculon-Labs/Trinet-SDK/blob/main/docs/getting-started.md).
