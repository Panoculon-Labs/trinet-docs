---
title: Memory cards
description: Recommended microSD cards for Trinet (V30 or higher), how much each hour of recording needs, and how the camera handles full or removed cards.
---

# Memory cards

## Recommended cards

Use a microSD card that carries the **V30** video speed class mark (or higher: V60, V90). V30 means
the card can sustain at least 30 MB/s of writing, far more than a Trinet camera needs — a stereo
camera writes about 20 Mbit/s (2.5 MB/s) — so it keeps up through hours of continuous recording
with headroom for slow moments inside the card.

| | Recommended |
|---|---|
| **Speed class** | **V30** or higher (usually also marked **U3**) — see the [SD Association's speed classes ↗](https://www.sdcard.org/developers/sd-standard-overview/speed-class/) |
| **Type** | microSDXC (or microSDHC for 32 GB) from a well-known brand; **high-endurance** cards are the best choice for long, repeated recording sessions |
| **Capacity** | 64 GB or more for Trinet Mono; 128 GB or more for Trinet Stereo and Stereo GS; cards up to 256 GB are tested |
| **Format** | **exFAT** — FAT32 limits single files to 4 GB, which ends long takes early |

**Avoid** cards with only a Class 10 or U1 mark, unbranded or very cheap cards, and cards bought from
unknown sellers — counterfeit cards report a false size and corrupt recordings as they fill up.

!!! question "A 10 MB/s card is four times what the camera needs. Why isn't it enough?"
    Because recording doesn't fail on the **average** rate — it fails on the **longest pause**. A
    Class 10, U1 or V10 mark means the card managed at least 10 MB/s *sequentially, in good
    condition, with free space to write into*. It promises nothing about how long the card may stop
    to reorganise itself inside.

    That matters because the card is never told which space you freed. Deleting files updates your
    computer's index, not the card's, so after a few cycles of filling and emptying it behaves as
    though it were permanently full and has to shuffle data around before each new write. A card
    with lots of spare speed does that in the gaps between writes and you never notice. A card with
    barely any margin does it *instead of* writing, and stops for seconds at a time.

    One we measured — a cheap card nominally good for four times what a stereo camera needs — had
    settled at **2.8 MB/s average with pauses of up to 36 seconds** after repeated use. The camera
    can ride out a short pause; 36 seconds costs you every frame in it. V30 or better is the
    recommendation because the margin is what keeps the pauses short, not because 30 MB/s is needed.

!!! warning "No guarantee or liability"
    These are general recommendations to help you choose a card. Panoculon Labs does not test,
    certify, endorse or guarantee any third-party memory card, and accepts no liability for loss or
    corruption of recordings caused by a memory card. Card performance varies between models, batches
    and sellers — test a new card with a short recording before an important session, and keep
    copies of recordings you can't afford to lose.

## If a recording has gaps

A card that is too slow, worn out or counterfeit shows itself in a very particular way: **the video
has gaps while the motion data is complete**. The camera keeps sampling motion at full rate — that
is a tiny trickle of data the slowest card can absorb — but video needs about 2.5 MB/s without
pause, and when the card stops accepting writes for a few seconds the frames with nowhere to go are
lost. You may also see a lower bitrate than you chose, and audio running on past the end of the
video.

If you see this:

1. **Try a different card** — ideally a **V30** or better one, in the same camera, same settings.
   This is the quickest way to tell a card problem from a camera problem.
2. **Reformat the card** rather than deleting files. Deleting marks the space free for your computer,
   but the card itself is not told, so it keeps working as though it were still full and gets slower
   the more times you fill and empty it. A full format (the
   [SD Memory Card Formatter ↗](https://www.sdcard.org/downloads/formatter/) is made for this) gives
   the card its free space back and often restores its speed.
3. **Retire the card** if the gaps come back after a reformat.

!!! warning "A card can pass a read test and still ruin a recording"
    Copying files off a card quickly tells you nothing about whether it can *write* fast enough. A
    card we measured read at 41 MB/s and wrote at 2.8 MB/s on average — but it paused for up to
    **36 seconds** at a time, which is what actually costs you frames. If you want to check a card,
    write several gigabytes to it and watch for pauses, rather than timing a copy *from* it.

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
