```
                               _ _       _       _      _                    
  __ _ _ __      _ __ __ _  __| (_) ___ | |_ ___| | ___| |_ _   _ _ __   ___ 
 / _` | '__|____| '__/ _` |/ _` | |/ _ \| __/ _ \ |/ _ \ __| | | | '_ \ / _ \
| (_| | | |_____| | | (_| | (_| | | (_) | ||  __/ |  __/ |_| |_| | |_) |  __/
 \__, |_|       |_|  \__,_|\__,_|_|\___/ \__\___|_|\___|\__|\__, | .__/ \___|
 |___/                                                      |___/|_|         
```

A GNU Radio module for demodulating radioteletype (AKA RTTY), and also PSK31.

## Installation

Note: These instructions are written for Linux OS. Similar commands work for Mac and Windows.

1. Open a terminal window.
2. Change to the home directory.
```
cd ~/  
```
3. Clone the repository:
```
git clone https://github.com/dl1ksv/gr-radioteletype.git
```
4. ```cd ~/gr-radioteletype```
5. ```mkdir build```
6. ```cd build```
7. ```cmake -DCMAKE_INSTALL_PREFIX="/usr/local" -DCMAKE_BUILD_TYPE=Release ../```
8. ```make```
9. ```sudo make install```
10. ```sudo ldconfig```

## Summary of Contents

* ```radioteletype.demodulators.rtty_demod_db```

  A hierarchical omnibus block. RF in, ASCII out.

* ```radioteletype.demodulators.async_word_extractor```

  Extract words from an asynchronous serial protocol. That is, something with start and stop bits.

* ```radioteletype.demodulators.baudot_decode_bb```

  Decode Baudot code to ASCII.

* ```radioteletype.demodulators.varicode_decode_bb```

  Decode Varicode to ASCII.

* ```radioteletype.demodulators.tone_detector_cf```

  The detector used for individual FSK tones.

* ```radioteletype.demodulators.psk31_demodulator_cbc```

  Modulated PSK31 in, bits out. Send output to ```varicode_decode_bb``` for ASCII output.

* ```radioteletype.filters.raised_cos```

  Generate FIR taps for a raised cosine filter.

* ```radioteletype.filters.extended_raised_cos```

  Generate FIR taps made of a sequence of raised cosine filters which approaches a boxcar function while maintaining zero ISI. See ```examples/recursive_filter.grc```

* ```radioteletype.modulators.am_fsk_mod_bc```

  Generate FSK by switching the envelopes of two free-running oscillators.

* ```radioteletype.modulators.fm_fsk_mod_bc```

  Generate FSK by FM, optionally with some filtering of the modulating signal.

* ```radioteletype.modulators.baudot_encode_bb```

  Convert ASCII to Baudot code.

* ```radioteletype.modulators.varicode_encode_bb```

  Convert ASCII to Varicode.

* ```radioteletype.modulators.psk31_modulator_bc```

  Bits in, modulated PSK31 out.

## Notes

If running the examples, be sure to run from the ```gr-radioteletype/examples``` directory. Some of them open WAV files for input with relative paths, expecting them to be in the current directory. You'll need to either start GRC from the examples directory, or generate (but not run) the blocks with GRC, and then run the generated program from a terminal.

