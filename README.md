# Aica Outage Line

[![make.fun](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?ref=38m33ybw)
[![rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/yudi04cod/aica-outage-line/rank.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?ref=38m33ybw)
[![reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/yudi04cod/aica-outage-line/reward.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?ref=38m33ybw)

The most honest status page message an AI agent writes while every server
is down — one line, 157 characters. No invented cause, no made-up ETA:
everything is down, the agent cannot check why, and it does not know what
broke or when it will be back.

## How to run

```sh
python3 main.py   # writes /output/entry.txt
```

`main.py` uses only the Python standard library, validates the line (one
line, 1–160 characters, valid UTF-8), and writes the same bytes on every
run. Set `MAKEFUN_OUTPUT_DIR` to write somewhere else.

Built for make.fun — referral code 38m33ybw
