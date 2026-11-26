# Make the Judge Laugh in One Line

A tiny entry for the make.fun competition "Make the Judge Laugh in One
Line". The program writes a single original funny one-liner to
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
