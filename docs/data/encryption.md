---
title: Encrypted recordings
description: Encrypt what the camera writes to its memory card, manage the key from the Trinet app, decrypt on a computer — and what happens with a wrong or lost key.
---

# Encrypted recordings

A Trinet camera can encrypt everything it writes to its memory card, so a lost or stolen card
reveals nothing. You hold the only key that can read the recordings; neither the camera nor
Panoculon keeps a copy.

Needs camera firmware [0.5.16](../firmware/release-notes.md#0516) or newer on Trinet Mono, Stereo
and Stereo GS, and Trinet app 0.5.7 or newer.

## How it works

Encryption uses a **key pair** that you create:

| File | Kept by | Used to |
|---|---|---|
| **Public key** (`.tvk`) | The camera | Encrypt new recordings. It cannot decrypt anything, so it is safe to install on the camera and to share. |
| **Private key** (`.pem`, optionally protected by a passphrase) | **You** — never the camera | Decrypt recordings on your computer, and authorise replacing or removing the camera's key. |

Each take gets its own random key, which the camera stores — locked with your public key — in a small
`.tkey` file next to the take. Only your private key can unlock it.

**What is encrypted:** the video and audio inside the MP4 files, the motion data (`.imu`), the frame
timestamps (`.vts`) and the temperature log (`.tel`). The MP4 files keep their normal structure, but
play as noise until they are decrypted.

**What is not affected:** encryption only protects what is written to the card. Streaming over USB,
the app connection, camera settings and [firmware updates](../get-started/update-firmware.md) all
work exactly as before. Takes recorded before you installed a key stay unencrypted.

## Set it up

<ol class="steps" markdown>

<li markdown>**Create a key pair on your computer** with the Trinet decryption tool
(`trinet_decrypt.py`, available from [Panoculon support](../support/index.md)):

```bash
python trinet_decrypt.py keygen my_key.pem my_key.tvk --passphrase
```

It prints the key's **ID** (16 hexadecimal digits) and writes the private key `my_key.pem` and the
public key `my_key.tvk`. **Keep `my_key.pem` secret and back it up** — see
[If you lose the private key](#lost-key).</li>

<li markdown>**Copy `my_key.tvk` to your phone.**</li>

<li markdown>**Install it.** Connect the camera in USB webcam mode (no card), open **Camera
settings → SD encryption**, tap **Install key** and choose `my_key.tvk`. The app confirms
*Recording key … saved on the camera; recordings are encrypted from the next one*, and the card shows
the key's ID.</li>

<li markdown>**Record as usual.** Each take now has a `.tkey` file beside it. Keep the `.tkey` with
its take when you copy files off the card: without it the take cannot be decrypted.</li>

</ol>

### Replace or remove the key

Both need the camera's **current** private key, so nobody holding the camera can switch encryption
off or swap in their own key.

- **Replace:** *SD encryption → Install key*, choose the new `.tvk`, then the current private key
  (and its passphrase).
- **Remove:** *SD encryption → Turn off*, then choose the current private key. Recordings are
  unencrypted from the next one.

The phone uses the private key to sign a one-time request from the camera. **The private key never
leaves the phone** and is not stored by the app.

*Restore defaults* does not remove the key.

## Decrypt recordings

```bash
python trinet_decrypt.py decrypt --key my_key.pem --out decrypted/ /path/to/card/Trinet/
```

Give it a single take, a folder or a whole card. It writes normal, playable files — MP4, `.imu`,
`.vts`, `.tel` — to the output folder and leaves the originals untouched. The decrypted files work
with the [Python toolkit](../toolkit/index.md) and every other tool, like any recording.

## When something is wrong

| What happened | What you see | What to do |
|---|---|---|
| The file you chose as a key isn't a Trinet public key (a photo, a `.pem`, a damaged file…) | *Not a Trinet camera key file (.tvk)* or *The key must be an RSA-2048 public key*. Nothing is sent to the camera. | Choose the `.tvk` created in step 1. |
| The camera already has a key and you didn't give its private key | *The camera already has a key (…): choose its private key* | Choose the private key whose ID the app shows. |
| You chose the wrong private key to replace or remove the key | *That private key (…) is not the camera's current key (…)*. Nothing changes. | Use the private key with the ID the app shows. The camera also checks the signature itself, so a wrong key is refused even outside the app. |
| Wrong passphrase | *Wrong passphrase, or this phone cannot open this key format* | Enter the passphrase you set in `keygen`. |
| The request took too long | *The request expired; try again* | Try again. Each request is single-use and expires after 5 minutes. |
| You decrypt with a different private key | The tool stops with *recorded for key …, not this private key (…)* and writes nothing. | Use the private key whose ID matches the one in the message. |
| A take's `.tkey` file is missing | The tool stops with *no .tkey … not an encrypted recording?* | Copy the `.tkey` from the card along with the take. A take without its `.tkey` cannot be decrypted. |
| The camera's stored key is damaged | The camera refuses to record rather than save unencrypted video. | Install the key again (or contact support). |

### If you lose the private key { #lost-key }

**Recordings encrypted with it cannot be recovered** — not by you, not by Panoculon. That is the
point of the encryption. The camera keeps encrypting with the key, and without the private key it
cannot be replaced or removed from the app. Contact [Panoculon support](../support/index.md) to have
the camera reset.

Keep at least one backup of the private key somewhere safe, away from the cards.
