---
title: Firmware release notes
description: What's new in every Trinet camera firmware release, from 0.2.0 to the latest.
---

# Firmware release notes

Newest first. Products: **Mono** = Trinet Mono, **Stereo** = Trinet Stereo, **Stereo GS** = Trinet
Stereo GS. To update, see [Update the firmware](index.md).

## 0.5.9 — 28 September 2026 { #059 }
<span class="trinet-badge">Mono</span> <span class="trinet-badge">Stereo</span> <span class="trinet-badge">Stereo GS</span>

- **Wireless status.** Cameras recording to their card now broadcast their status — recording or
  idle, card, take, kit — over Bluetooth to the [Trinet app](../app/wireless-status.md). No
  connection needed.
- Each camera announces its **model and firmware version**, so you can see at a glance which cameras
  need an update.
- Card recordings can be placed on **UTC time** with the Trinet-tools
  [wireless UTC tool](../toolkit/wireless-utc.md).
- **Trinet Mono** receives all the recording-reliability improvements from 0.5.5–0.5.8, and the
  choice of H.264 or H.265 for card recordings.
- **Stereo GS:** the first frames of each take are now timestamped correctly.

## 0.5.8 (Stereo GS) — 21 September 2026 { #058-gs }
<span class="trinet-badge">Stereo GS</span>

- Every take after power-on now records, not only the first.
- Fixed occasional black or white blocks in recordings from a warm camera.
- Better image quality: much less grain, crisper edges without halos, no colour tint at the frame
  edges, and no softening after motion.
- A Stereo GS camera in a kit no longer freezes mid-take, and a camera recording on its own no
  longer uses the kit's timing.

## 0.5.8 — 18 September 2026 { #058 }
<span class="trinet-badge">Stereo</span> <span class="trinet-badge">Stereo GS</span>

- **Interrupted recordings are repaired automatically** after a power loss, losing at most the last
  second.
- A slow memory card can no longer corrupt video frames or the card's file system.
- Starts up in seconds even with a full card.
- Audio no longer skips or repeats in some players.
- A kit that briefly lost sync now re-syncs for later takes.

## 0.5.7 — 14 September 2026 { #057 }
<span class="trinet-badge">Stereo</span>

- Stereo card recordings are **H.264** again by default — widely compatible, fast to decode, one
  keyframe per second.
- New: choose **H.264 or H.265** for card recordings from the app; the choice applies to the next
  take, no restart. (Mono gains this in 0.5.9.)

## 0.5.6 — 11 September 2026 { #056 }
<span class="trinet-badge">Stereo</span>

- Long stereo takes (25 minutes and more) now finish saving on the camera.
- Recovery after a power loss can no longer make a take look longer than it was, and recovered takes
  keep the camera's identity.
- Runs slightly cooler, with less motion smear.
- The light stays white — *don't power off* — while recovery runs.

## 0.5.5 — 8 September 2026 { #055 }
<span class="trinet-badge">Stereo</span>

- Stereo recordings no longer stop after about ten minutes as the camera warms up.
- The overheating limit can be tuned per camera for different mounts.
- **Stereo cameras can now be updated from the app.** (Earlier stereo firmware needs a one-time
  update from us — [contact us](../support/index.md).)
- The light shows the correct colour in update mode.

## 0.5.4 — 29 August 2026 { #054 }
<span class="trinet-badge">Mono</span> <span class="trinet-badge">Stereo</span>

- A long button press no longer switches the camera's mode by accident; modes are set by the memory
  card and the app.
- On Trinet Stereo, an inserted memory card now decides the mode, as on Mono.
- Trinet Stereo gets the improved image look from 0.5.3.

## 0.5.3 — 23 August 2026 { #053 }
<span class="trinet-badge">Mono</span>

- Natural colours in daylight and correct exposure in direct sun.
- Faster white-balance and exposure settling.
- Saved camera settings no longer override image-tuning improvements in updates.
- Default mains frequency is 60 Hz, changeable in the app.

## 0.5.2 — 21 August 2026 { #052 }
<span class="trinet-badge">Mono</span>

- Recordings carry the camera's identity and calibration inside the video file.
- One set of bitrate and image settings now applies to streaming and card recording alike.
- Better accuracy for long multi-camera sync takes.
- Card recordings expose correctly in sunlight and use your saved microphone settings.
- New *Restore defaults* setting.

## 0.5.1 — 21 August 2026 { #051 }
<span class="trinet-badge">Mono</span>

- Audio stays in sync with video over long recordings.

## 0.5.0 — 6 August 2026 { #050 }
<span class="trinet-badge">Mono</span>

- Detects flickering mains lighting and adjusts exposure to avoid banding.

## 0.4.0 – 0.4.2 — 6 August 2026 { #040 }
<span class="trinet-badge">Mono</span>

- Exposure recovers from indoor to outdoor within about a fifth of a second, including sunlit scenes.

## 0.3.2 – 0.3.8 — 5–6 August 2026 { #032 }
<span class="trinet-badge">Mono</span>

- Automatic anti-flicker exposure: flicker-free indoors without overexposing outdoors.
- Smooth transitions between indoor and outdoor exposure.

## 0.3.1 — 3 August 2026 { #031 }
<span class="trinet-badge">Mono</span>

- Fixes corrupted or very slow live video on some Android phones with a more robust USB transfer
  mode.

## 0.3.0 — 2 August 2026 { #030 }
<span class="trinet-badge">Mono</span>

- Ships the tuned image profile in the firmware.

## 0.2.2 — 14 July 2026 { #022 }
<span class="trinet-badge">Mono</span>

- No more microphone crackle on card recordings.
- Louder card recordings with automatic gain (can be turned off).
- Motion data stays aligned with video to under 1 ms across a whole recording.

## 0.2.1 — 23 June 2026 { #021 }
<span class="trinet-badge">Mono</span>

- An inserted memory card now always decides the mode: a card without a mode file records.
- The app can switch the camera into card-recording mode.

## 0.2.0 — 20 June 2026 { #020 }
<span class="trinet-badge">Mono</span>

- Overheating protection while streaming: the app pauses recording until the camera cools, then
  resumes.
- Camera image tuning and calibration can be updated from the app.
