This is Windows only.

This should work with a few different emulators,
but I recommend just using BGB.
https://bgb.bircd.org/#downloads

BGB hotkeys:
F2 - quicksave
F3 - save slot selector
F4 - quickload

USAGE
Get your game running in your emulator first.
If you have python installed, you should be able
to just double click timer.py to get started.

Time is measured in hundredths of a second instead
of frames, because its easier and frame counting
is actually a little weird on gameboy. It will
often turn off its display entirely (such as
during room transitions), which frees it from its
~60hz clock speed temporarily.
