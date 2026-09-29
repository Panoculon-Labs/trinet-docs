---
title: Put recordings on UTC
description: Give every Trinet card recording — and every frame — a UTC time using the Trinet app's wireless status log.
---

# Put recordings on UTC

Trinet cameras don't have a real-time clock: their timestamps count from power-on. To line card
recordings up with other sensors, logs or cameras, the **wireless UTC tool** gives every take —
and optionally every frame — a UTC time, with an uncertainty and a confidence.

## How it works

While cameras record to their cards, they broadcast their status over Bluetooth, and the
[Trinet app's Wireless status](../app/wireless-status.md) logs every start and stop with the phone's
UTC time. The tool matches that log to the takes on the cards and fits each camera's clock to UTC.
It also corrects for an inaccurate phone clock. In a field check, three cameras agreed within
0.32 ms.

## Steps

<ol class="steps" markdown>
<li markdown>Update cameras to firmware **0.5.9 or newer** and the app to **0.5.3 or newer**.</li>
<li markdown>Keep **Wireless status** running on a phone near the cameras for the whole session
(background logging lets you turn the screen off).</li>
<li markdown>After the session, **export** the history from the app (a `.jsonl.gz` file).</li>
<li markdown>Run the tool with the export and the cards (or copies of them):

```bash
python scripts/wireless_utc.py phone_export.jsonl.gz --recordings /media/CARD1 /media/CARD2
```
</li>
</ol>

## Useful options

| Option | Does |
|---|---|
| `--per-frame` | A UTC time for every frame, not just first and last |
| `--write-sidecars` | Write the UTC results next to each recording |
| `--csv`, `--json`, `-o DIR` | Output formats and folder |
| `--unit ID` | Only one camera |
| `--inspect` | Show what the log contains (cameras, models, firmware) without matching |
| `--min-confidence`, `--strict` | Reject weak matches |

The method, accuracy and output columns are described in the toolkit's
[wireless UTC guide](https://github.com/Panoculon-Labs/Trinet-tools/blob/main/docs/wireless_utc.md).
