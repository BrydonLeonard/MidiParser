# MIDI parser

A parser for MIDI files that I built while learning about the MIDI standard. After reading in MIDI files, it prints out a description for each chunk of data in the file.

Given [this (public domain) bass sample](https://upload.wikimedia.org/wikipedia/commons/a/a0/Bass_sample.mid), you get the output below:

```
                 4d 54 68 64 00 00 00 06 |> MIDI file standard header
                                   00 01 |> 1 (multiple synchronous tracks)
                                   00 02 |> There are 2 tracks
                                   00 f0 |> There are 240 ticks per crotchet
                             4d 54 72 6b |> Standard track header. Track 1 starting
                             00 00 00 1c |> The track is 28 bytes long
                 00 ff 58 04 04 02 18 08 |>   Delta time =     0. [Meta] Set time signature to 4/4. Metronome will tick every 1 beat(s). There are 8 demisemiquavers per crotchet
                    00 ff 51 03 07 a1 20 |>   Delta time =     0. [Meta] Set tempo to 120 bpm
              00 ff 54 05 40 00 00 00 00 |>   Delta time =     0. [Meta] This track's SMPTE offset is [64, 0, 0, 0, 0]
                             00 ff 2f 00 |>   Delta time =     0. [Meta] END OF TRACK
                             4d 54 72 6b |> Standard track header. Track 2 starting
                             00 00 00 87 |> The track is 135 bytes long
                                00 c0 21 |>   Delta time =     0. [Channel  0] Switch to program 33
                             00 b0 07 7f |>   Delta time =     0. [Channel  0] Adjust controller 7 to value 127
                             00 90 2d 4e |>   Delta time =     0. [Channel  0] Stop A3 with velocity 78
                          81 01 80 2d 40 |>   Delta time =   129. [Channel  0] Start A3 with velocity 64
                          81 67 90 30 51 |>   Delta time =   231. [Channel  0] Stop C4 with velocity 81
                             78 90 32 4f |>   Delta time =   120. [Channel  0] Stop D4 with velocity 79
                             03 80 30 40 |>   Delta time =     3. [Channel  0] Start C4 with velocity 64
                             75 90 34 44 |>   Delta time =   117. [Channel  0] Stop E4 with velocity 68
                             09 80 32 40 |>   Delta time =     9. [Channel  0] Start D4 with velocity 64
                             37 80 34 40 |>   Delta time =    55. [Channel  0] Start E4 with velocity 64
                          81 30 90 2d 52 |>   Delta time =   176. [Channel  0] Stop A3 with velocity 82
                          82 60 80 2d 40 |>   Delta time =   352. [Channel  0] Start A3 with velocity 64
                             08 90 2b 3e |>   Delta time =     8. [Channel  0] Stop G3 with velocity 62
                          81 66 80 2b 40 |>   Delta time =   230. [Channel  0] Start G3 with velocity 64
                             0a 90 2d 50 |>   Delta time =    10. [Channel  0] Stop A3 with velocity 80
                          81 07 80 2d 40 |>   Delta time =   135. [Channel  0] Start A3 with velocity 64
                          82 59 90 2d 58 |>   Delta time =   345. [Channel  0] Stop A3 with velocity 88
                             4d 80 2d 40 |>   Delta time =    77. [Channel  0] Start A3 with velocity 64
                          82 1b 90 30 4d |>   Delta time =   283. [Channel  0] Stop C4 with velocity 77
                             4d 80 30 40 |>   Delta time =    77. [Channel  0] Start C4 with velocity 64
                             2b 90 32 5a |>   Delta time =    43. [Channel  0] Stop D4 with velocity 90
                             78 90 34 4b |>   Delta time =   120. [Channel  0] Stop E4 with velocity 75
                             02 80 32 40 |>   Delta time =     2. [Channel  0] Start D4 with velocity 64
                             5f 80 34 40 |>   Delta time =    95. [Channel  0] Start E4 with velocity 64
                          81 0f 90 2d 4b |>   Delta time =   143. [Channel  0] Stop A3 with velocity 75
                          82 68 90 30 4d |>   Delta time =   360. [Channel  0] Stop C4 with velocity 77
                             05 80 2d 40 |>   Delta time =     5. [Channel  0] Start A3 with velocity 64
                          81 61 80 30 40 |>   Delta time =   225. [Channel  0] Start C4 with velocity 64
                             0a 90 2d 4e |>   Delta time =    10. [Channel  0] Stop A3 with velocity 78
                             5a 80 2d 40 |>   Delta time =    90. [Channel  0] Start A3 with velocity 64
                          83 05 ff 2f 00 |>   Delta time =   389. [Meta] END OF TRACK
```

I also wrote most of a BNF grammar to help myself keep track of the protocol while writing the parser. Given that even all of the variable length properties are limited in length, I _could_ have written out the whole thing, but that grammar would've been huge, so I've stopped short and will just say that MIDI isn't quite context-free enough for finishing it to be reasonable.