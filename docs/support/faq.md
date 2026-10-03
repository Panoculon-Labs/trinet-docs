---
title: FAQ
description: Frequently asked questions about Trinet cameras — recording length, resolution and frame rate, sync, calibration, power, software and buying.
---

# Frequently asked questions

## Recording

??? question "Can Trinet record a full working shift (4–8 hours) without a phone?"
    Yes. Record to the memory card with the button. Mono saves each take automatically at 8 hours;
    Stereo takes have no limit. Plan the **card** (about 7 GB/h Mono, about 10 GB/h Stereo —
    [Memory cards](../power-and-care/memory-cards.md)) and **power** (a 10 000 mAh bank runs a Stereo
    camera for roughly 15 hours — [Power](../power-and-care/index.md)).

??? question "Do settings changed in the app apply when recording to the card?"
    Yes — settings are stored on the camera. On Trinet Mono, bitrate, image and audio settings apply to
    card recordings too. On Stereo cameras, card recordings always use 10 Mbps per eye; the recording
    codec (H.264 / H.265) setting applies to card recordings on all cameras with current firmware.

??? question "How do I check framing without a phone?"
    Card recording doesn't show a preview. Check framing once over USB with the
    [Trinet app](../app/record-and-review.md) (the preview), then record standalone. Many teams do a
    short test take and review it before a session.

??? question "Is the data the same when recording to the card and through the app?"
    Yes: the same video, motion data at the same rate, the same frame timestamps and the same
    calibration — in the same file formats.

??? question "Does the camera split long recordings into several files?"
    Normally no — each take is one file set. On Mono a new part is started after a cooling pause, and
    takes are saved at 8 hours.

## Video

??? question "What resolution and frame rate does Trinet record?"
    1920×1080 at 30 fps per camera (per eye on stereo). Other frame rates such as 60 or 120 fps are not
    supported by the product, even where the image sensor itself could run faster.

??? question "Can Trinet Stereo GS record 1920×1200 per eye?"
    No. Stereo GS records 1920×1080 per eye.

??? question "Is a different stereo baseline available?"
    Trinet Stereo and Stereo GS have a fixed 70 mm baseline. For other requirements,
    [contact sales](index.md).

??? question "What is the field of view?"
    All Trinet cameras use ultra-wide fisheye lenses; see each product's specifications for the
    effective field of view: [Mono](../products/mono.md), [Stereo](../products/stereo.md),
    [Stereo GS](../products/stereo-gs.md). Exact values for your unit are in its calibration.

## Timing and sync

??? question "How accurate is the sync?"
    Motion data to video: sub-millisecond, hardware-timestamped. Camera to camera in a Wrist Kit: under
    1 ms. See [Timing and sync](../data/sync.md).

??? question "Can Trinet sync to an external clock, timecode or trigger?"
    Trinet cameras have no external timecode, trigger or network time input. Cameras in a
    [Wrist Kit](../products/wrist-kit.md) sync to each other wirelessly, and card recordings can be
    placed on **UTC** afterwards with the [wireless UTC tool](../toolkit/wireless-utc.md) — the way to
    align Trinet with other cameras and sensors.

??? question "What happens if the wireless sync drops during a kit recording?"
    Every camera keeps recording on its own and re-aligns when the link returns. Nothing is lost.

??? question "Can I see live video wirelessly?"
    No. Wireless status shows each camera's recording state, card and take over Bluetooth, but not
    video. Live preview needs a USB connection.

## Motion data and calibration

??? question "What motion data do I get?"
    3-axis accelerometer (±8 g) and gyroscope (±2000 °/s) at 400 Hz on current cameras, plus a 3-axis
    magnetometer at about 100 Hz — with the sample rate recorded in every file.

??? question "Do you publish IMU noise figures?"
    Each [reference calibration](../calibration/reference-calibrations.md) includes conservative IMU
    noise parameters (noise density and random walk) suitable for VIO. For more detailed
    characterisation, [contact us](index.md).

??? question "Is my camera calibrated?"
    See [Calibration](../calibration/index.md): stereo units carry their own factory calibration; mono
    units use the reference calibration for their version, with per-unit calibration available as a
    service.

## Power

??? question "Can I swap power banks mid-shift?"
    The camera has no internal battery, so disconnecting power ends the current take (it is repaired
    automatically when the camera next starts). Stop recording (wait for green) before swapping, or use
    a bank large enough for the whole session.

??? question "Why does my power bank switch off?"
    The camera draws very little power, and many banks mistake that for a charged phone. See
    [Tested power banks](../power-and-care/power-banks.md).

## Software

??? question "Is there an SDK?"
    Yes — for [Android and iOS](../sdk/index.md), plus the [Python toolkit](../toolkit/index.md). Both
    are open source (MIT).

??? question "Does Trinet work with ROS 2, MCAP, Foxglove or LeRobot?"
    Recordings export to [MCAP](../toolkit/mcap.md) for Foxglove and ROS 2. The open file formats and
    Python reader make conversion to other dataset formats straightforward.

??? question "Is there an iPhone app?"
    iPhones connect to Trinet Mono through apps built with the [iOS SDK](../sdk/ios.md), which includes
    a demo app you can build. The ready-made Trinet app is for Android.

## Buying and warranty

??? question "How do I buy Trinet, or get a quote?"
    See [panoculonlabs.com/trinet](https://www.panoculonlabs.com/trinet) or email
    [innovate@panoculonlabs.com](mailto:innovate@panoculonlabs.com?subject=Inquiry%20regarding%20Trinet).

??? question "What does the warranty cover?"
    See [Warranty](warranty.md).
