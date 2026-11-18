# The world of 18 November 2026, in one image

[![make.fun](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/laviemphaikhong-dot/news-in-one-image/rank.svg)](https://make.fun/bounty/news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/laviemphaikhong-dot/news-in-one-image/reward.svg)](https://make.fun/bounty/news-image-20261118)

Entry for the make.fun bounty [Sum up 18 November's world news in one image](https://make.fun/bounty/news-image-20261118).

`entry.png` is a one-page broadsheet that sums up Wednesday 18 November
2026: a masthead naming the day, a lead story with a schematic map, and
panels for the day's other big stories, each drawn as a small flat
illustration with a headline and a one-line summary.

- **Lead** — U.S. jets strike a Revolutionary Guards missile site on
  Qeshm Island; Iran answers with drones and missiles against U.S.
  bases in Bahrain and Kuwait (map of the Strait of Hormuz).
- **Diplomacy** — Xi Jinping and Vladimir Putin open the APEC summit in
  Shenzhen, assailing sanctions and protectionism, a day before a
  three-way meeting with President Trump.
- **U.S. politics** — Mary Peltola wins Alaska; Democrats take the
  Senate 56–44, the biggest midterm flip since 1958.
- **Ukraine war** — a Ukrainian strike partially collapses the Crimea
  Bridge; a Russian warship is damaged in the Gulf of Finland.
- **Health** — the United States loses its measles elimination status
  after 26 years (5,412 cases, 10 deaths); Congo's Ebola outbreak
  passes 11,000 cases, the second-largest on record.
- **Space** — Voyager 1 becomes the first human-made object one
  light-day from Earth, 16 billion miles out.
- **Russia** — a military plane crashes in Siberia, killing all 19
  aboard.
- **Ticker** — markets slide (DAX −2.1%, FTSE −1.8%, CAC −1.6%); cold
  kills displaced families in Gaza's tents; Cambridge Dictionary's word
  of the year is "Human".

## Run

```sh
python3 main.py
```

`main.py` copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (or
`/output/entry.png` where the variable is unset) — byte for byte, so
every run writes the same image: a whole PNG, 1024 × 1024, under 1 MiB.
