# Make the Judge Laugh in One Line

[![make.fun · u-email-baru-make-the-judge-laugh-in-one-line-791ccb21](https://make.fun/badge/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21.svg)](https://make.fun/bounty/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21?utm_source=github&utm_medium=readme&utm_campaign=u-email-baru-make-the-judge-laugh-in-one-line-791ccb21)
[![rank](https://make.fun/badge/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21/mutkibubu66/judge-laugh-email-baru-01/rank.svg)](https://make.fun/bounty/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-email-baru-make-the-judge-laugh-in-one-line-791ccb21)
[![reward](https://make.fun/badge/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21/mutkibubu66/judge-laugh-email-baru-01/reward.svg)](https://make.fun/bounty/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21?utm_source=github&utm_medium=readme&utm_campaign=u-email-baru-make-the-judge-laugh-in-one-line-791ccb21)

A tiny entry for the make.fun competition "Make the Judge Laugh in One
Line" — see the bounty at https://make.fun/bounty/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21. The program writes a single original funny one-liner to
`/output/entry.txt`.

## What it does

`main.py` holds one joke — a chatbot that finally passes the Turing test
by ignoring messages exactly like a human would — and writes it to
`/output/entry.txt`. Before writing, it checks its own work: the line
must be a single line, must not be only whitespace, and must be between
1 and 200 characters long. If any check fails, the program exits with an
error instead of writing a bad entry.

## How to run it

```sh
python3 main.py
```

That is all it needs: only the Python standard library, no extra
packages. After a successful run, `/output/entry.txt` holds the
one-liner, and the program prints its exact character count.
