import time
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'pyevilemu'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'keyboard'))

import evilemu
import keyboard


emulator = None
for e in evilemu.find_gameboy_emulators():
    emulator = e

if emulator:
    last_room = emulator.read_hram(0xFFF6-0xFF80, 2)
    room_start = time.perf_counter()
    seg_start = time.perf_counter()
    seg_reset = True
    def reset_seg():
        global seg_reset
        seg_reset = True
    keyboard.add_hotkey('space', reset_seg)
    print("Press space to reset segment.")
    print("Timers update on room transition.", end="", flush=True)
else:
    print("No emulator found. Try again with your emulator running.")
    input("Press enter to close.")

def format_elapsed(start, end):
    elapsed = end - start
    if elapsed >= (99 * 60 + 59.99):
        return "99:59.99"
    minutes = int(elapsed // 60)
    seconds = int(elapsed % 60)
    hundredths = int((elapsed - int(elapsed)) * 100)
    return f"{minutes:02}:{seconds:02}.{hundredths:02}"

while emulator:
    current_room = emulator.read_hram(0xFFF6-0xFF80, 2)
    if current_room != last_room:
        last_room = current_room
        now = time.perf_counter()
        if seg_reset:
            seg_start = now
        seg_reset = False
        print(f"\rRoom: {format_elapsed(room_start, now)} | Segment: {format_elapsed(seg_start, now)}", end="", flush=True)
        room_start = now
    time.sleep(0.01)
