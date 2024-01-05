# MIDI parser

A parser for MIDI files that I built while learning about the MIDI standard. After reading in MIDI files, it prints out an equivalent JSON representation.

Given [this (public domain) bass sample](https://upload.wikimedia.org/wikipedia/commons/a/a0/Bass_sample.mid), you get the output below:

```
$ python scan.py
{
    "format": "1 (multiple synchronous tracks)",
    "track_count": 2,
    "ticks_per_crotchet": 240,
    "tracks": [
        {
            "length": 28,
            "events": [
                "[0000000000] [Meta] Set time signature to 4/4. Metronome will tick every 1 beat(s). There are 8 demisemiquavers per crotchet",
                "[0000000000] [Meta] Set tempo to 120 bpm",
                "[0000000000] [Meta] This track's SMPTE offset is [64, 0, 0, 0, 0]",
                "[0000000000] END OF TRACK"
            ]
        },
        {
            "length": 135,
            "events": [
                "[0000000000] [Channel  0] Switch to program 33",
                "[0000000000] [Channel  0] Adjust controller 7 to value 127",
                "[0000000000] [Channel  0] Play A3 with velocity 78",
                "[0000000129] [Channel  0] Play A3 with velocity 64",
                "[0000013416] [Channel  0] Play C4 with velocity 81",
                "[0000013536] [Channel  0] Play D4 with velocity 79",
                "[0000013539] [Channel  0] Play C4 with velocity 64",
                "[0000013656] [Channel  0] Play E4 with velocity 68",
                "[0000013665] [Channel  0] Play D4 with velocity 64",
                "[0000013720] [Channel  0] Play E4 with velocity 64",
                "[0000019912] [Channel  0] Play A3 with velocity 82",
                "[0000032296] [Channel  0] Play A3 with velocity 64",
                "[0000032304] [Channel  0] Play G3 with velocity 62",
                "[0000045462] [Channel  0] Play G3 with velocity 64",
                "[0000045472] [Channel  0] Play A3 with velocity 80",
                "[0000046375] [Channel  0] Play A3 with velocity 64",
                "[0000057856] [Channel  0] Play A3 with velocity 88",
                "[0000057933] [Channel  0] Play A3 with velocity 64",
                "[0000061416] [Channel  0] Play C4 with velocity 77",
                "[0000061493] [Channel  0] Play C4 with velocity 64",
                "[0000061536] [Channel  0] Play D4 with velocity 90",
                "[0000061656] [Channel  0] Play E4 with velocity 75",
                "[0000061658] [Channel  0] Play D4 with velocity 64",
                "[0000061753] [Channel  0] Play E4 with velocity 64",
                "[0000063688] [Channel  0] Play A3 with velocity 75",
                "[0000077104] [Channel  0] Play C4 with velocity 77",
                "[0000077109] [Channel  0] Play A3 with velocity 64",
                "[0000089622] [Channel  0] Play C4 with velocity 64",
                "[0000089632] [Channel  0] Play A3 with velocity 78",
                "[0000089722] [Channel  0] Play A3 with velocity 64",
                "[0000090367] END OF TRACK"
            ]
        }
    ]
}
```

I also wrote most of a BNF grammar to help myself keep track of the protocol while writing the parser. Given that even all of the variable length properties are limited in length, I _could_ have written out the whole thing, but that grammar would've been huge, so I've stopped short and will just say that MIDI isn't quite context-free enough for finishing it to be reasonable.