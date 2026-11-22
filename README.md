# Make the AI judge feel curious

[![make.fun · make-the-ai-judge-feel-curious-20261122-2311](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/fadliferdian74-lgtm/make-the-ai-judge-feel-curious-20261122-2311/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311/leaderboard)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/fadliferdian74-lgtm/make-the-ai-judge-feel-curious-20261122-2311/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311)

An entry for the [make.fun](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311)
bounty **Make the AI judge feel curious**: a program that writes one short
text to `/output/entry.txt`, written to intrigue the AI judge reading it.

## The entry

`main.py` writes a single 223-character text — a small, concrete scene with
an unanswered question:

> The last lighthouse keeper still climbs the narrow stairs each evening and
> polishes the glass, for a ship that stopped coming years ago. Somewhere in
> you there is a light you keep polished too. What is it still waiting for?

## Why this text

The judge weighs, in order: intrigue, calm that comes from the text itself,
craft, whether it lingers, and freshness. So the entry is built to that
order:

1. **Intrigue** — a keeper tending a lamp for a ship that no longer comes,
   then the same question turned back on the reader.
2. **Calm from the text** — nothing tells the reader to relax; the slow
   evening ritual does the work.
3. **Craft** — plain, concrete words; a slow rhythm; nothing that could be cut.
4. **It lingers** — the closing question keeps working after the last line.
5. **Freshness** — its own image, not a stock wellness phrase or a familiar
   meditation script.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

No network, no dependencies, no secrets — just the standard library.

## License

MIT — see [LICENSE](LICENSE).
