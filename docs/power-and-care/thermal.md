---
title: Heat and thermal protection
description: How Trinet cameras protect themselves from overheating — cooling pauses on Mono and kits, protective shutdown on Stereo — and how to avoid it.
---

# Heat and thermal protection

Trinet cameras monitor their internal temperature and protect themselves in hot conditions. What
happens depends on the camera and on whether it is recording alone or in a kit.

## Trinet Mono

When the camera reaches **75 °C** inside during a recording:

1. The current take is **saved**.
2. Recording **pauses** while the camera cools. The light stays <span class="led led-blue"></span>
   **blue**.
3. After cooling — typically 3 to 12 minutes — recording **resumes automatically** as the next part
   of the same session (`recording3_2`, `recording3_3`, …).

A small log of the pause is written to the card. You don't need to do anything.

## Trinet Stereo and Stereo GS (recording alone)

Stereo cameras don't pause — they have more thermal headroom and run to a higher
limit. If a stereo camera reaches **95 °C** inside:

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

## What to expect in normal use

The temperatures above are measured inside the camera, not on its surface, and they are a long way
from where a camera normally sits. Recording continuously to the card for six hours, a stereo
camera at room temperature settles at **about 75–81 °C** — some 15–20 °C below the point at which it
would switch off. It climbs over the first hour or so and then holds steady rather than creeping
upwards.

So a camera that shuts down for heat is telling you something about its surroundings — covered,
in direct sun, or in a hot room — rather than about continuous recording itself.

Every take also records the temperature the camera saw while it ran, so if a session ends
unexpectedly you can check afterwards whether heat was the reason.

## Avoiding heat

- **Let air reach the camera.** Don't cover it with hoods, hats or thick fabric, or press it against
  the body for long periods.
- **Keep it out of direct sun** — on the head between sessions, and in cars or windows.
- The camera is designed primarily for indoor use in well-ventilated environments. In hot
  conditions, plan for cooling pauses.
