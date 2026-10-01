---
title: Wireless status
description: Follow Trinet cameras and kits recording to their own memory cards, over Bluetooth, with the Trinet app — no connection needed.
---

# Wireless status

When cameras record to their own memory cards — on people's heads and wrists, with no phone
attached — **Wireless status** lets you see what every camera is doing. The phone only **listens**
to the cameras' Bluetooth broadcasts; it never connects to or controls them, and any number of
phones can follow any number of cameras.

!!! info "Requirements"
    Camera firmware **0.5.9 or newer** (cameras on older firmware don't broadcast — update them
    first) and a phone with Bluetooth LE. The app asks for the Bluetooth scan permission, which is
    never used for location.

## See it in action

Several cameras recording to their cards while the app follows them over Bluetooth (about 3 minutes).

<figure class="drive-video-figure">
  <iframe class="drive-video" src="https://drive.google.com/file/d/19mdQXlmRkHEGx4rpHxbxoyKXCQmTLcBf/preview" title="Trinet Wireless status demo" allow="autoplay; fullscreen" loading="lazy"></iframe>
  <figcaption>Wireless status with several cameras. <a href="https://drive.google.com/file/d/19mdQXlmRkHEGx4rpHxbxoyKXCQmTLcBf/view" target="_blank" rel="noopener">Open in Google Drive ↗</a></figcaption>
</figure>

## What you see

- **Overview** — every kit and camera in range, grouped by kit and sorted by distance (Near,
  Medium, Far, Out of range), with filters and search.
- For each camera: **recording** or idle, **finalizing** a take, **memory card present**, the
  current **take number** and number of recordings on the card, its **model** and **firmware
  version**, and when its last take **started and stopped in UTC**.
- **Kit** and **camera** detail screens, and a **history** of starts and stops.

Distance is a signal-strength hint, not a measurement.

## Alerts

Turn on alerts to be notified when:

- a camera **stops unexpectedly**;
- a camera's **memory card goes missing**;
- a camera is **idle while the rest of its kit is recording**.

## Background logging

Keep logging with the screen off during long sessions — the app keeps a history of every start and
stop.

## Export and UTC

**Export** saves the history (compressed JSON Lines, plus an optional CSV of takes). The
[wireless UTC tool](../toolkit/wireless-utc.md) combines this export with the card recordings to
put every take — and optionally every frame — on UTC time.

## Turning the broadcast off

The broadcast is on by default. Turn it off per camera in
[Camera settings → Wireless](camera-settings.md#wireless).
