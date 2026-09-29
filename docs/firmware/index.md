---
title: Update the firmware
description: Update Trinet camera firmware from the Trinet app in about 30 seconds, and check which version your camera runs.
---

# Update the firmware

Camera firmware updates bring new features and reliability fixes — see the
[release notes](release-notes.md). Updates are installed from the [Trinet app](../app/index.md) on
Android.

## Update from the app

<ol class="steps" markdown>
<li markdown>**Prepare the camera.** Turn it off and **remove its memory card**.</li>
<li markdown>**Connect it to the phone.** The light turns <span class="led led-white"></span> white.
Wait until the app shows the camera as connected (allow access if asked).</li>
<li markdown>**Open Update firmware.** The app checks for updates automatically and shows the installed
version, for example *Firmware v0.5.8 · Update available (v0.5.9)*.</li>
<li markdown>**Tap Download & install** and keep the camera plugged in. The camera switches to update mode
— the light turns <span class="led led-magenta"></span> **pink** — and the progress bar runs.</li>
<li markdown>**Wait.** In about 30 seconds the camera restarts by itself on the new firmware.
**Don't unplug or restart it while the light is pink.**</li>
</ol>

!!! success "Safe by design"
    Each camera model has its own update channel, so a camera is never offered firmware for a
    different model, and the camera accepts only genuine Trinet firmware. If an update fails,
    reconnect the camera and try again; if it still won't update, [contact us](../support/index.md).

## Good to know

- **Very old firmware (0.1.5 or earlier):** the update takes about two minutes and then needs you to
  unplug and reconnect the camera.
- **Trinet Stereo on firmware older than 0.5.5:** these cameras need a one-time update from us
  before they can update from the app. [Contact us](../support/index.md).
- **Offline install:** under *Advanced*, the app can install an update file we send you, for sites
  without internet.
- *No updates are published for this camera model yet* means your camera already runs the latest
  firmware available for its model.

## Check your firmware version

- **Update firmware** screen in the app — shows the installed version.
- **[Wireless status](../app/wireless-status.md)** (firmware 0.5.9+) — shows every nearby camera's
  model and firmware, handy for checking a whole kit.
- Recordings made in the app store the firmware version in `meta.json`.

## Keep your cameras current

New features often need both a recent app and recent camera firmware — for example
[Wireless status](../app/wireless-status.md) needs firmware 0.5.9 and app 0.5.3. Update the app
from Google Play and the cameras from the app.
