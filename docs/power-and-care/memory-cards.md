---
title: Memory cards
description: Which microSD cards to use with Trinet, how much each hour of recording needs, and how the camera handles full or removed cards.
---

# Memory cards

## Choosing a card

- **Type:** microSD (SDHC/SDXC), a high-endurance or video-rated card (U3 / V30 or better).
  Endurance cards cope best with hours of continuous writing.
- **Format:** **exFAT**. FAT32 limits single files to 4 GB, which ends long takes early.
- **Size:** 64 GB or more for Trinet Mono; 128 GB or more for Trinet Stereo and Stereo GS. Cards up to
  256 GB are tested.
- Use a genuine card from a known brand. Counterfeit cards report a false size and corrupt
  recordings when they fill up.

## How much you can record

| Camera (default settings) | Per hour | On 64 GB | On 128 GB | On 256 GB |
|---|---|---|---|---|
| Trinet Mono | about 7 GB | about 9 hours | about 18 hours | about 36 hours |
| Trinet Stereo / Stereo GS | about 10 GB | about 6 hours | about 12 hours | about 25 hours |

Choosing H.265 for card recordings (in the [Trinet app](../app/camera-settings.md)) makes files
smaller for the same quality, but not every player or pipeline supports it.

## When the card fills up

Recordings are never overwritten.

- **Trinet Mono:** when the card is nearly full, the take is saved and recording stops. The light
  blinks red rapidly until you replace the card and reconnect power.
- **Trinet Stereo / Stereo GS:** the take is saved and recording stops; the light blinks red for
  about three seconds and returns to green. A stereo camera won't start a new take when less than
  about 256 MB is free.

## Removing the card

- **Stop recording first** and wait for the light to turn green before removing the card.
- If a stereo camera's card is removed while it is ready, the light blinks red slowly; re-insert it
  and the camera checks the card (white) and returns to green.
- If power or the card is lost mid-take, the take is repaired automatically the next time the
  camera starts with that card.

## Formatting

Format new cards as exFAT in your computer before first use. The camera creates its `Trinet` folder
automatically.
