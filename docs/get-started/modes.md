---
title: Recording modes
description: How a Trinet camera chooses between recording to its memory card, USB webcam mode and iPhone mode — and how to switch.
---

# Recording modes

A Trinet camera starts in one of three modes:

| Mode | What it does | Light when ready |
|---|---|---|
| **Card recording** | Records video, motion data and audio to the memory card with the button | <span class="led led-green"></span> Green |
| **USB webcam** | Streams live over USB to the [Trinet app](../app/index.md) on Android, or to a computer | <span class="led led-white"></span> White |
| **iPhone** (Trinet Mono) | Streams live over USB to an iPhone app built with the [iOS SDK](../sdk/ios.md) | <span class="led led-cyan"></span> Cyan |

## How the camera chooses

The camera decides at power-on:

1. **A memory card is inserted** → **card recording**, unless the card contains a mode file (below).
2. **No memory card** → the mode last chosen in the Trinet app's **Boot mode** setting, which the
   camera remembers across power cycles. Out of the box, that is **USB webcam**.

### The mode file

To force a mode with a card inserted, create a text file on the card at
`Trinet/trinet_mode.conf` containing one line:

=== "USB webcam"

    ```ini
    mode=uvc
    ```

=== "iPhone (Trinet Mono)"

    ```ini
    mode=ncm
    ```

=== "Card recording"

    ```ini
    mode=imu
    ```

Insert the card and power on; the light confirms the mode.

!!! note "Stereo and iPhone"
    Trinet Stereo and Stereo GS stream in USB webcam mode only. On a stereo camera, `mode=ncm`
    starts USB webcam mode.

## Switching modes

- **To record to a card:** insert a card (without a mode file) and power on. Inserting a card is also
  the simplest way to get back to card recording from any mode.
- **To stream over USB:** power on without a card, or put a mode file on the card.
- **From the app:** *Camera settings → Advanced → Boot mode* sets the mode used when no card is
  inserted. The camera restarts to apply it.

The button never changes the mode.
