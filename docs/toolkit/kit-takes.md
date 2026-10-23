---
title: View a kit take in sync
description: After recording with a Wrist Kit, match each take across the cameras' memory cards by its grp number, tell the cameras apart by device tag, and render them side by side on the shared clock.
---

# View a kit take in sync

You've recorded with a [Wrist Kit](../products/wrist-kit.md) — for example a
[Stereo or Stereo GS head camera and two Mono wrist cameras](../products/stereo-wrist-kit.md). Each
camera wrote to its **own** memory card. This page shows how to tell which files belong to the same
take, which camera each file came from, and how to play them side by side on the kit's shared clock.

!!! tip "Try it on sample data first"
    The two *Stereo GS — with wrists* recordings on [Sample data](../data/sample-data.md) are real kit
    takes laid out exactly as below, one folder per camera.

## 1. Copy each card into its own folder

Copy the whole `Trinet` folder from each card into a folder named after **where that camera was
worn**:

```text
my-session/
├── head/      ← from the head camera's card
├── left/      ← from the left-wrist camera's card
└── right/     ← from the right-wrist camera's card
```

Keep the cards apart: the cameras don't share file names, but separate folders make it obvious which
camera a file came from and keep the commands below short. Copy every file — the `.vts` timestamps
are what put a camera on the shared clock.

## 2. Read the file names

Every take recorded as a kit starts with `grp` and a number:

| Camera | Files for one take |
|---|---|
| Mono (wrist) | `grp143024_23890f5f_1.mp4`, `.imu`, `.vts`, `.json` |
| Stereo / Stereo GS (head) | `grp143024_cae8dabe_take0001_L.mp4`, `_R.mp4`, `_L.vts`, `_R.vts`, `.imu` |

| Part | Example | Means |
|---|---|---|
| `grp<number>` | `grp143024` | **The take.** Every camera that recorded this take uses the same number — this is how you match files across cards. A new number is used for every take. |
| Device tag | `23890f5f` | **The camera.** The first 8 characters of its [device ID](../support/glossary.md); it never changes, so it tells you which physical camera wrote the file. |
| `_1`, `_2`, … | `_1` | Part number on a Mono camera — a take continues in a new part after a [cooling pause](../power-and-care/thermal.md) |
| `take0001`, `_L` / `_R` | | The stereo camera's own take counter, and the left / right eye (as seen by the wearer) |

!!! warning "The grp number is the take, not the kit"
    Despite the `grp` prefix, the number changes with **every take**. The kit itself has its own,
    fixed number — `group` in the Mono cameras' `.json` sidecar (below) — which is the same on every
    take the kit records. Use it to sort cards when you run more than one kit.

### Which camera is which

The device tag tells you which camera wrote a file, not where it was worn. Two easy ways to know:

- **Write it down at setup.** Note each camera's tag and position (head, left, right) — the tag of
  any file it records will match. The same camera keeps the same tag forever.
- **Look at the video.** The head camera is the one with `_L` / `_R` files. For the wrists, open one
  short clip from each card — the visible hand tells you left from right.

### The `.json` sidecar (Mono cameras)

Each Mono camera in a kit writes a small `.json` next to each take:

```json
{
  "session": 143024,
  "group": 39759,
  "role": "slave",
  "device_tag": "23890f5f",
  "synced": true,
  "sync_quality_us": 6,
  …
}
```

| Field | Use it to |
|---|---|
| `session` | The take — equals the `grp` number in the file name |
| `group` | The kit — identical on every camera and every take of one kit |
| `role` | `master` is the kit's clock reference; the others are `slave` |
| `synced` | `true` if this camera was locked to the kit's clock for this take |

All fields: [Recording-meta sidecar](../data/metadata.md#recording-meta-sidecar-json).

!!! note "Stereo head cameras don't write a `.json`"
    A Stereo or Stereo GS camera carries the same sync information inside its `.vts` files instead.
    Identify its takes by the `grp` number in the file name.

### List the takes

To see which takes every camera has, list the `grp` numbers in each folder:

```bash
# macOS / Linux
for d in head left right; do echo "$d:"; ls my-session/$d | grep -o '^grp[0-9]*' | sort -u; done
```

```powershell
# Windows PowerShell
foreach ($d in "head","left","right") { "${d}:"; Get-ChildItem my-session\$d -Filter "grp*" |
  ForEach-Object { ($_.Name -split "_")[0] } | Sort-Object -Unique }
```

A take that appears in all three folders was recorded by all three cameras. Files without `grp`
(`recording…` or `take…` on their own) were recorded while the camera was not in a kit, and can't be
put on the shared clock.

## 3. Render the take side by side

With the [Python toolkit](index.md) installed, run from the `Trinet-tools` folder and give
`sync_view.py` one file per camera for the same `grp` number (replace `my-session` with the path to
your copy). For the head camera, give the **left-eye** file:

```bash
python scripts/sync_view.py \
    my-session/left/grp143024_23890f5f_1.mp4 \
    my-session/head/grp143024_cae8dabe_take0001_L.mp4 \
    my-session/right/grp143024_990dd5dd_1.mp4 \
    --audio 1 -o grp143024_sync.mp4
```

Panels appear in the order you list the files — here left wrist, head, right wrist — and
`--audio 1` uses the head camera's sound. Every frame is placed on the kit's shared clock, so the
same instant lines up across panels, and the header shows the live camera-to-camera offset.
Add `--imu` for motion plots under each panel, `--rotate180 0,2` if the wrist cameras were worn
upside down, or `--show` to preview in a window instead of writing a file. All options:
[Visualize and check sync](visualize.md#several-cameras-on-one-timeline).

To render **every** take recorded by all three cameras:

```bash
for g in $(ls my-session/head | grep -o '^grp[0-9]*' | sort -u); do
  L=$(ls my-session/left/${g}_*.mp4 2>/dev/null | head -1)
  H=$(ls my-session/head/${g}_*_L.mp4 2>/dev/null | head -1)
  R=$(ls my-session/right/${g}_*.mp4 2>/dev/null | head -1)
  [ -n "$L" ] && [ -n "$H" ] && [ -n "$R" ] && \
    python scripts/sync_view.py "$L" "$H" "$R" --audio 1 -o "${g}_sync.mp4"
done
```

A Mono take split into parts by a cooling pause (`_1`, `_2`, …) is rendered one part at a time:
pass the matching part number from each wrist.

!!! info "Why not `--auto`?"
    `sync_view.py --auto DIR` groups takes by the `.json` sidecars in **one** folder. A stereo head
    camera writes no `.json`, so `--auto` would leave the head out. For a kit with a stereo head, list
    the files as above.

## Check the sync

`sync_view.py` prints a line per camera before it renders:

- **synced, self-reported ~N µs** — the camera was locked to the kit's clock; typical values are
  tens of microseconds.
- **NOT synced** — that camera wasn't locked for this take (for example its radio beacon was off or
  out of range), so it can't be placed precisely on the shared clock.
- *Recordings do not overlap on the shared clock* — the files are from different takes; check that
  the `grp` numbers match.

The first one to two seconds of a take can be less tightly aligned while cameras lock on. Accuracy
and method: [Timing and sync](../data/sync.md) and the [validation report](../data/sync-validation.md).

## Sharing a kit take

- **To show it** — share the rendered `grp…_sync.mp4`; it plays in any video player.
- **To work with it** — share the three folders (`head/`, `left/`, `right/`) with **all** files for
  the take, not just the `.mp4`s. The `.vts` files are what put each camera on the shared clock, and
  the `.imu` files hold the motion data. Anyone with the toolkit can then render or
  [export to MCAP](mcap.md) themselves.

## Related

[Files on the card](../get-started/files-on-the-card.md) ·
[Put recordings on UTC](wireless-utc.md) · [Export to MCAP / ROS 2](mcap.md) ·
[Stereo and 3D](stereo-and-3d.md)
