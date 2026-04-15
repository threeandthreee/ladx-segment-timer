import time
import os
import sys
import select
import termios
import tty
from gameboy import Gameboy

class RawInput:
    def __init__(self):
        self.fd = sys.stdin.fileno()
        self.old_settings = None

    def __enter__(self):
        if os.name == 'nt':
            # Windows doesn't need termios, but we might need msvcrt setup if using it later
            return self
        else:
            # Save current settings
            self.old_settings = termios.tcgetattr(self.fd)
            # Set cbreak mode: keys are sent immediately, no line buffering
            tty.setcbreak(self.fd)
            return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.old_settings:
            # Restore original settings
            termios.tcsetattr(self.fd, termios.TCSADRAIN, self.old_settings)

def kbhit():
    """Check if a key is available without blocking."""
    if os.name == 'nt':
        import msvcrt
        return msvcrt.kbhit()
    else:
        # Check if stdin has data ready
        return select.select([sys.stdin], [], [], 0)[0]

def get_non_blocking_key():
    """Read a single key if available."""
    if kbhit():
        if os.name == 'nt':
            import msvcrt
            return msvcrt.getch().decode('utf-8')
        else:
            return sys.stdin.read(1)
    return None

gb = Gameboy()

print("Looking for bgb or retroarch...")
while not gb.findEmulator():
    time.sleep(1)
    
last_room = gb.readRam(0xFFF6, 2)
room_start = time.perf_counter()
seg_start = time.perf_counter()
seg_reset = True

print("Press space to reset segment, q to quit.")
print("Timers update on room transition.", end="", flush=True)

def format_elapsed(start, end):
    elapsed = end - start
    if elapsed >= (99 * 60 + 59.99):
        return "99:59.99"
    minutes = int(elapsed // 60)
    seconds = int(elapsed % 60)
    hundredths = int((elapsed - int(elapsed)) * 100)
    return f"{minutes:02}:{seconds:02}.{hundredths:02}"    

with RawInput():
    try:
        while True:
            key = get_non_blocking_key()
            if key == ' ':
                seg_reset = True

            current_room = gb.readRam(0xFFF6, 2)
            if current_room != last_room:
                last_room = current_room
                now = time.perf_counter()
                if seg_reset:
                    seg_start = now
                seg_reset = False
                print(f"\rRoom: {format_elapsed(room_start, now)} | Segment: {format_elapsed(seg_start, now)}", end="", flush=True)
                room_start = now
            time.sleep(0.01)
    except KeyboardInterrupt:
        print("\nInterrupted!")
    finally:
        # Ensure terminal is restored even if crash occurs
        pass 
