---
title: Record your first take
description: Step-by-step — record video and motion data to a memory card with a Trinet camera, then copy it to your computer.
---

# Record your first take

This records video, motion data and audio to the camera's memory card, with no phone or computer
involved.

<ol class="steps" markdown>

<li markdown>**Insert a memory card.** Use a **V30** microSD card formatted as exFAT
([recommended cards](../power-and-care/memory-cards.md#recommended-cards)). Insert it before powering the camera.
<div class="photo-row"><figure><img class="product-shot" src="../../assets/images/product/insert-sd-card.webp" alt="Inserting a microSD card into the camera" loading="lazy"><figcaption>Slide the card in, contacts first.</figcaption></figure><figure><img class="product-shot" src="../../assets/images/product/sd-card-inserted.webp" alt="microSD card fully inserted" loading="lazy"><figcaption>Fully inserted.</figcaption></figure></div>
</li>

<li markdown>**Remove the lens cap.** Pull it straight off. Don't twist the lens — the focus is set at
the factory.
<div class="photo-row"><figure><img class="product-shot" src="../../assets/images/product/mono-lens-cap-on.webp" alt="Camera with the lens cap on" loading="lazy"><figcaption>Lens cap on.</figcaption></figure><figure><img class="product-shot" src="../../assets/images/product/mono-lens-cap-off.webp" alt="Camera with the lens cap removed" loading="lazy"><figcaption>Lens cap off — ready to record.</figcaption></figure></div>
</li>

<li markdown>**Connect power.** Plug the USB-C cable into the camera and into a power bank or
charger. The light turns <span class="led led-white"></span> **white** straight away while the
camera starts up and processes recordings from earlier sessions (for example repairing a take after
power was pulled mid-recording). This can take a little while. Don't unplug it — it turns green when
done.</li>

<li markdown>**Wait for green.** A solid <span class="led led-green"></span> **green** light means
ready.
<div class="photo-row"><figure><img class="product-shot" src="../../assets/images/product/led-green-ready.webp" alt="Status light solid green" loading="lazy"><figcaption>Green: ready.</figcaption></figure></div>
</li>

<li markdown>**Press the button to record.** Tap the button once. The light turns
<span class="led led-blue"></span> **blue** — you're recording.
<div class="photo-row"><figure><img class="product-shot" src="../../assets/images/product/led-blue-recording.webp" alt="Status light solid blue" loading="lazy"><figcaption>Blue: recording.</figcaption></figure></div>
</li>

<li markdown>**Press again to stop.** The light turns <span class="led led-white"></span> **white**
while the camera finishes saving the take, then <span class="led led-green"></span> **green**.

<div class="admonition danger"><p class="admonition-title">Don't unplug while the light is white</p><p>White means the take is still being written. Wait for green before removing power or the card.</p></div>

</li>

<li markdown>**Copy your recording.** Unplug the camera, take out the card and put it in a card reader.
Your recordings are in the `Trinet` folder — see [Files on the card](files-on-the-card.md).</li>

</ol>

## What next?

- **Look at the data.** The `.imu` and `.vts` files are binary; open them with the
  [Python toolkit](../toolkit/index.md), which can also draw the motion data over the video.
- **Record for hours.** Mono takes are saved automatically after 8 hours; Stereo takes have no
  limit. Check [power](../power-and-care/index.md) and [heat](../power-and-care/thermal.md) for long
  sessions.
- **Multiple cameras?** A [Wrist Kit](wrist-kit-setup.md) starts and stops every camera together.
- **Something unexpected?** See [LED indications](led-indications.md) and
  [Troubleshooting](../support/troubleshooting.md).

!!! tip "If power is lost mid-take"
    Don't worry. The next time the camera starts with that card, it repairs the interrupted take
    automatically (light shows white), losing at most the last second.
