# Wednesday 18 November 2026 — one day of world news, one page

[![make.fun](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/laviemphaikhong-dot/news-in-one-image/rank.svg)](https://make.fun/bounty/news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/laviemphaikhong-dot/news-in-one-image/reward.svg)](https://make.fun/bounty/news-image-20261118)

Entry for make.fun's [Sum up 18 November's world news in one image](https://make.fun/bounty/news-image-20261118).

The page is a broadsheet carrying **46 stories from 7 regions, each
one verified against reporting dated Wednesday 18 November 2026**:
a UTC timeline and the day in numbers, sixteen numbered lead
stories — four large, twelve in a grid — pinned by number on a
dotted world map of where the day happened, region counts for all
46 stories, thirty one-line stories in an "Also on Wednesday"
column, and a date-check box that names the big stories
deliberately excluded for belonging to other days.

## The leads

1. **Iran answers Qeshm** — Iranian drones strike Patriot batteries
   at Kuwait's Ali Al-Salem air base before dawn; Bahrain intercepts
   several attacks and issues two shelter alerts, a day after the
   U.S. strike on Qeshm Island.
2. **Shenzhen arrivals** — Xi Jinping greets Donald Trump on the
   airport tarmac, a first for a visiting leader in decades, and
   holds talks with Vladimir Putin; the three pose for the APEC
   family photo ahead of Thursday's trilateral summit.
3. **The Crimea Bridge, again** — a third attack this week closes
   the Kerch crossing for damage checks; rail traffic resumes, the
   road span downed on Tuesday stays shut, and two deaths are
   confirmed.
4. **Markets slide** — hawkish Fed minutes knock gold down 3.2% to
   $3,741.90 and lift the dollar to a 19-month high; the Dow closes
   −1.11% at 50,198 and oil falls 3.2%.

## In the grid

Voyager 1 crossing one light-day from Earth · a record $190.4m
Van Gogh at Sotheby's · Hakeem Jeffries nominated for Speaker ·
the EU's €45bn Ukraine loan · Anthropic pricing its IPO at $83 ·
COP31's ministerial endgame · Peltola sealing a 56–44 Senate ·
a record 1,441-drone night over Ukraine · the UN's Ebola appeal ·
Cyclone Akvan · the Quad in Manila · Britain's missile pledge.

## Checked, and left out

Thursday's stories (the GTA VI launch, the trilateral summit
itself, Nvidia's results, the World Court's Myanmar judgment),
Tuesday's (the Qeshm strike, the measles ruling, the bridge span
collapse, the Siberia crash) and Monday's COP31 draft were all
verified and excluded — they are not Wednesday's news.

## Running it

```sh
python3 main.py
```

The command copies `entry.png` into `$MAKEFUN_OUTPUT_DIR` (or
`/output` if unset), byte for byte: a single 1024 × 1024 PNG,
comfortably under the 1 MiB cap, identical on every run.

## About the artwork

No photographs are used. The page — masthead, rules, region-coloured
labels, the dotted world map and its story markers — is typeset and
drawn entirely in code, then rendered once to the PNG that ships
here.
