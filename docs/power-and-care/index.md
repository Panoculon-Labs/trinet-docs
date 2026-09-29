---
title: Power and runtime
description: How to power a Trinet camera, how much power it uses, and how long it records on a power bank.
---

# Power and runtime

Trinet cameras have no internal battery. They run from any USB-C source that supplies **5 V at
1 A or more** — a USB power bank for wearable use, or a phone, computer or charger.

## How much power the camera uses

| | Typical current at 5 V |
|---|---|
| Standby (ready, not recording) | about 50 mA |
| Trinet Mono, recording | about 170 mA |
| Trinet Stereo / Stereo GS, recording or streaming | about 350 mA |

This low draw is why some power banks switch off — see [below](#power-banks-that-switch-off).

## How long it records

Estimated continuous recording time on a fully charged power bank:

| Power bank | Trinet Mono | Trinet Stereo / Stereo GS |
|---|---|---|
| 5 000 mAh | about 15 hours | about 7 hours |
| 10 000 mAh | about 30 hours | about 15 hours |
| 20 000 mAh | about 60 hours | about 30 hours |

These are estimates. Real runtime depends on the power bank's efficiency, its age and
temperature, and settings such as bitrate. To estimate for your bank:

!!! example "Runtime estimate"
    runtime (hours) ≈ capacity (mAh) × 3.7 V × 0.85 ÷ (camera current (mA) × 5 V)

    For a 10 000 mAh bank and a Stereo camera: 10 000 × 3.7 × 0.85 ÷ (350 × 5) ≈ 18 hours at best;
    plan for about 15.

For multi-hour sessions, use a full-capacity bank, keep it charged before each session, and avoid
charging the bank while recording for long periods.

## Power banks that switch off

Many power banks decide a device is "fully charged" when it draws only a little current, and switch
off after a few seconds or minutes — cutting power mid-recording. Fast-charging and MagSafe-style
wireless banks are especially prone to this.

- Use a bank that is [known to work](power-banks.md), or test yours for a full session before relying
  on it.
- Some banks work on their USB-A port but not their USB-C port (a USB-A to USB-C cable or adapter
  helps).
- **Don't press the power bank's button during a recording** — on many banks that restarts the
  auto-off timer or switches the output off.

## If power is lost

If power is interrupted mid-take, the recording is not lost. The next time the camera starts with
that card it repairs the take automatically (light shows white), losing at most the last second.
