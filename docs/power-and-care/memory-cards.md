---
title: Memory cards
description: Recommended microSD cards for Trinet (V30 or higher), how much each hour of recording needs, and how the camera handles full or removed cards.
---

# Memory cards

## Recommended cards

Use a microSD card that carries the **V30** video speed class mark (or higher: V60, V90). V30 means
the card can sustain at least 30 MB/s of writing, far more than a Trinet camera needs — a stereo
camera writes about 20 Mbit/s (2.5 MB/s) — so it keeps up through hours of continuous recording
with margin for slow moments inside the card.

| | Recommended |
|---|---|
| **Speed class** | **V30** or higher (usually also marked **U3**) — see the [SD Association's speed classes ↗](https://www.sdcard.org/developers/sd-standard-overview/speed-class/) |
| **Type** | microSDXC (or microSDHC for 32 GB) from a well-known brand; **high-endurance** cards are the best choice for long, repeated recording sessions |
| **Capacity** | 64 GB or more for Trinet Mono; 128 GB or more for Trinet Stereo and Stereo GS; cards up to 256 GB are tested |
| **Format** | **exFAT** — FAT32 limits single files to 4 GB, which ends long takes early |

**Avoid** cards with only a Class 10 or U1 mark, unbranded or very cheap cards, and cards bought from
unknown sellers — counterfeit cards report a false size and corrupt recordings as they fill up.

!!! warning "No guarantee or liability"
    These are general recommendations to help you choose a card. Panoculon Labs does not test,
    certify, endorse or guarantee any third-party memory card, and accepts no liability for loss or
    corruption of recordings caused by a memory card. Card performance varies between models, batches
    and sellers — test a new card with a short recording before an important session, and keep
    copies of recordings you can't afford to lose.

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
