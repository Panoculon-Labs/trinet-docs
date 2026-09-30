---
title: LED indications
description: What every colour and blink pattern of the Trinet status light means — recording, saving, card problems, kit pairing, USB modes, updates and heat.
---

# LED indications

The status light tells you what the camera is doing. Patterns: **solid**, **blink** (steady on/off),
**fast blink** (rapid flicker) and **slow blink** (about two seconds on, two seconds off).


<div class="photo-row"><figure><img class="product-shot" src="../../assets/images/product/led-green-ready.webp" alt="Status light green" loading="lazy"><figcaption>Green — ready</figcaption></figure><figure><img class="product-shot" src="../../assets/images/product/led-blue-recording.webp" alt="Status light blue" loading="lazy"><figcaption>Blue — recording</figcaption></figure><figure><img class="product-shot" src="../../assets/images/product/led-white-usb.webp" alt="Status light white" loading="lazy"><figcaption>White — saving, repairing, or USB camera ready</figcaption></figure></div>

## Recording to a memory card

| Light | Meaning | What to do |
|---|---|---|
| <span class="led led-white"></span> White, solid — at start-up or after inserting a card | Starting up and processing earlier recordings (repairing any interrupted take) | **Don't power off.** Wait for green |
| <span class="led led-green"></span> Green, solid | Ready | Tap the button to record |
| <span class="led led-blue"></span> Blue, solid | Recording | Tap the button to stop |
| <span class="led led-white"></span> White, solid — after stopping | Saving the take | **Don't power off or remove the card.** Wait for green |
| <span class="led led-red led-blink-slow"></span> Red, slow blink | Memory card missing, not detected, or removed | Power off, reseat or replace the card |

!!! note "Recording colour"
    Blue is the standard recording colour. Some units are configured with a different recording
    colour for a specific deployment.

## Problems while recording

| Light | Meaning | What to do |
|---|---|---|
| <span class="led led-red led-blink-fast"></span> Red, fast blink, **stays** (Mono) | Memory card full. The take was saved and recording stopped | Replace the card, then disconnect and reconnect power |
| <span class="led led-red led-blink-fast"></span> Red, fast blink for about 3 s, then green (Stereo) | The take ended: memory card full, or recording could not continue | Free up or replace the card; tap to try again |
| <span class="led led-red"></span> Red, solid for about 2 s, then green (Mono) | Recording could not start | Tap to try again; check the card |
| <span class="led led-red"></span> Red, solid, **stays** | Internal fault | Disconnect and reconnect power. If it persists, [contact support](../support/index.md) |

## Heat

| Light | Meaning | What to do |
|---|---|---|
| <span class="led led-blue"></span> Blue stays on, but no new recording (Mono) | Cooling pause — the take was saved and recording resumes automatically | Nothing. Give the camera some air |
| <span class="led led-red led-blink"></span> Red, blink (half-second) — Stereo in a kit | The kit is pausing while a camera cools; recording resumes automatically | Nothing. Tap to cancel the pause |
| <span class="led led-red"></span> Red, solid for about 2 s, then off (Stereo) | Overheated — both eyes were saved and the camera switched itself off | Let it cool, then reconnect power |

More in [Heat and thermal protection](../power-and-care/thermal.md).

## Wrist Kit pairing

These appear only while the camera is idle (green) and you are pairing.

| Light | Meaning |
|---|---|
| <span class="led led-blue led-blink"></span> Blue, blink | This camera is the kit leader; pairing is open for 30 seconds |
| <span class="led led-green led-blink"></span> Green, blink | Searching for a kit leader to join |
| <span class="led led-green"></span> Green, short flash | Joined a kit — or, on the leader, another camera joined |
| <span class="led led-red led-blink-fast"></span> 5 red blinks | Left the kit (unpaired) |

See [Set up a Wrist Kit](wrist-kit-setup.md).

## USB and update modes

| Light | Meaning |
|---|---|
| <span class="led led-white"></span> White, solid | USB webcam mode — ready for the Trinet app or a computer |
| <span class="led led-cyan"></span> Cyan, solid | iPhone mode — ready for an iPhone (Trinet Mono) |
| <span class="led led-magenta"></span> Magenta (pink), solid | Receiving a firmware update — **keep it connected** |
| <span class="led led-red led-blink"></span> Red, blink (1 s on, 1 s off) | USB or update mode could not start — reconnect the camera |

In USB modes, apps built with the [SDK](../sdk/index.md) can also set the light colour themselves.

## Microphone mute switch

When you move the [microphone mute switch](mute-switch.md) on the bottom of the camera, the light
flashes <span class="led led-red"></span> red for one second when you mute and
<span class="led led-green"></span> green when you unmute, then returns to its previous colour.

!!! tip "Not listed here?"
    If you see a colour or pattern that isn't on this page, disconnect power, wait a few seconds and
    reconnect. If it happens again, note the pattern and [contact us](../support/index.md).
