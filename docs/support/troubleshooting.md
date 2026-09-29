---
title: Troubleshooting
description: Fixes for common Trinet problems — the camera won't record, card errors, power cutting out, the app can't see the camera, kits not starting together, and recordings that won't play.
---

# Troubleshooting

Start with the [status light](../get-started/led-indications.md) — it usually says what's wrong.

## Recording to a card

??? question "The light blinks orange and never turns green"
    The camera can't read the memory card. Power off, remove and reinsert the card, and power on
    again. If it continues (on Mono it turns to a slow red blink after a minute), try another card
    and make sure it is formatted **exFAT** — see [Memory cards](../power-and-care/memory-cards.md).

??? question "The light blinks red slowly"
    The memory card is missing, not detected or was removed. Insert the card (or reseat it) and
    power-cycle the camera.

??? question "The light stays white for a long time after power-on"
    The camera is checking and repairing recordings from an earlier session — for example after power
    was pulled mid-take. This can take a while on a large card. **Don't power off**; it turns green
    when done.

??? question "I pressed the button but it didn't start recording"
    - Wait for **green** — the button is ignored while the light is white.
    - A short **red** light means recording couldn't start: check the card has free space, then try
      again.
    - After a card-full stop on Mono, replace the card and reconnect power before recording again.

??? question "The recording stopped by itself"
    - **Fast red blink:** the card is full — see [Memory cards](../power-and-care/memory-cards.md).
    - **Mono, after 8 hours:** takes are saved automatically at 8 hours; tap to record again.
    - **Mono, light stayed blue with no new file for a few minutes:** a cooling pause; recording
      resumes by itself as the next part.
    - **Stereo, solid red then off:** the camera overheated and switched off — see
      [Heat](../power-and-care/thermal.md).
    - **Power cut out:** see *power* below.

??? question "The camera switches off or restarts during recording"
    Most often the **power bank** switches off at the camera's low power draw, or the **cable** is
    worn. Try a [bank known to work](../power-and-care/power-banks.md) and a good USB-C cable, and
    don't press the power bank's button during a recording. Takes interrupted by power loss are
    repaired automatically the next time the camera starts.

## USB and the Trinet app

??? question "The app doesn't see the camera"
    - Remove the memory card (or use a `mode=uvc` [mode file](../get-started/modes.md)) and reconnect —
      the light should be **white**.
    - Allow access when Android asks; if you declined, unplug and reconnect the camera.
    - Your phone needs USB-C host (OTG) support. Try another cable, and avoid USB hubs.
    - Close other apps that might be using the camera.

??? question "The preview stutters, freezes or disconnects"
    Use a short, good-quality USB-C cable directly into the phone, and keep the app and camera
    firmware up to date. The stream-health readout shows the measured frame rate.

??? question "A setting is greyed out with *Update the camera firmware*"
    That feature needs newer camera firmware — [update the firmware](../firmware/index.md).

??? question "The firmware update doesn't start or fails"
    Remove the memory card, reconnect, wait for the app to show the camera as connected, and try
    again; keep the camera plugged in while the light is pink. Stereo cameras on firmware older than
    0.5.5 need a one-time update from us — [contact us](index.md).

## Wrist Kit

??? question "Only one camera starts recording"
    Check each camera has its radio-beacon adapter attached and is **green**, then
    [pair the kit again](../get-started/wrist-kit-setup.md#pair-cameras-into-a-kit).

??? question "A camera doesn't appear in Wireless status"
    Wireless status needs camera firmware **0.5.9 or newer** and the broadcast switched on (it's on by
    default). Update the camera, and make sure Bluetooth is on for the phone.

## Files and playback

??? question "A recording plays as only one second, or an uploader rejects it"
    Run the toolkit's [repair script](../toolkit/inspect-and-repair.md#recording-shows-only-one-second-repair-it)
    — it fixes the file index without re-encoding.

??? question "I can't open the .imu or .vts files"
    They are binary data files. Use the [Python toolkit](../toolkit/index.md) or the
    [SDK](../sdk/index.md), or see [File formats](../data/file-formats.md).

??? question "H.265 recordings won't play"
    Some players and tools don't support H.265. Switch card recordings back to H.264 in
    [Camera settings](../app/camera-settings.md#video), or use a player such as VLC.

??? question "Motion data seems to lag the video by tens of milliseconds"
    You are probably aligning with the video's playback timestamps or the computer's clock. Use the
    recorded frame timestamps — see [Timing and sync](../data/sync.md).

## Still stuck?

[Contact us](index.md) with your camera model, firmware version and what the light shows.
