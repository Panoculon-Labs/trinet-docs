---
title: Heat and thermal protection
description: How Trinet cameras protect themselves from overheating — cooling pauses on Mono and kits, protective shutdown on Stereo — and how to avoid it.
---

# Heat and thermal protection

Trinet cameras monitor their internal temperature and protect themselves in hot conditions. What
happens depends on the camera and on whether it is recording alone or in a kit.

## Trinet Mono

When the camera reaches its temperature limit during a recording:

1. The current take is **saved**.
2. Recording **pauses** while the camera cools. The light stays <span class="led led-blue"></span>
   **blue**.
3. After cooling — typically 3 to 12 minutes — recording **resumes automatically** as the next part
   of the same session (`recording3_2`, `recording3_3`, …).

A small log of the pause is written to the card. You don't need to do anything.

## Trinet Stereo and Stereo GS (recording alone)

Stereo cameras don't pause. If a stereo camera reaches its critical temperature:

1. Both eyes of the current take are **saved**.
2. The light shows <span class="led led-red"></span> **solid red** for about two seconds.
3. The camera **switches off** and stays off until you disconnect and reconnect power.

A small record of the shutdown is written to the card.

## In a Wrist Kit

If **any** camera in a kit gets too warm, the **whole kit pauses** together and resumes once every
camera has cooled (or after at most 12 minutes). Stereo cameras show a
<span class="led led-red led-blink"></span> red blink during the pause; tapping a stereo camera's
button cancels the pause.

## With the Trinet app

When streaming over USB, the app shows *Camera cooling down*, pauses the recording on the phone and
resumes automatically when the camera has cooled.

## Avoiding heat

- **Let air reach the camera.** Don't cover it with hoods, hats or thick fabric, or press it against
  the body for long periods.
- **Keep it out of direct sun** — on the head between sessions, and in cars or windows.
- The camera is designed primarily for indoor use in well-ventilated environments. In hot
  conditions, plan for cooling pauses.
