import random
import time
import shutil

# MICR Unicode characters for digits 0-9
MICR_DIGITS = {
    '0': '\u2440',
    '1': '\u2441',
    '2': '\u2442',
    '3': '\u2443',
    '4': '\u2444',
    '5': '\u2445',
    '6': '\u2446',
    '7': '\u2447',
    '8': '\u2448',
    '9': '\u2449'
}

def generate_micr_number():
    """Generate a random 9-digit number in MICR encoding"""
    digits = [str(random.randint(0, 9)) for _ in range(9)]
    return ''.join([MICR_DIGITS[d] for d in digits])

def main():
    # ANSI escape codes
    retro_green = "\033[32;40m"
    reset_style = "\033[0m"
    hide_cursor = "\033[?25l"
    show_cursor = "\033[?25h"
    alt_screen = "\033[?1049h"
    main_screen = "\033[?1049l"

    try:
        print(alt_screen + hide_cursor, end="")
        cols, rows = shutil.get_terminal_size()
        
        while True:
            # Generate new numbers
            micr1 = generate_micr_number()
            micr2 = generate_micr_number()

            # Calculate centered positions
            vert_pad = (rows - 4) // 2
            horz_pad1 = (cols - len(micr1)) // 2
            horz_pad2 = (cols - len(micr2)) // 2

            # Build screen buffer
            screen = []
            screen.append(retro_green + "╔" + "═" * (cols - 2) + "╗")
            screen.extend(["║" + " " * (cols - 2) + "║" for _ in range(vert_pad)])
            screen.append(f"║{' ' * horz_pad1}{micr1}{' ' * (cols - 2 - horz_pad1 - len(micr1))}║")
            screen.append(f"║{' ' * horz_pad2}{micr2}{' ' * (cols - 2 - horz_pad2 - len(micr2))}║")
            screen.extend(["║" + " " * (cols - 2) + "║" for _ in range(vert_pad)])
            screen.append("╚" + "═" * (cols - 2) + "╝" + reset_style)

            # Clear and redraw
            print("\033[H")  # Move cursor to home position
            print("\n".join(screen), end="", flush=True)
            time.sleep(3)

    except KeyboardInterrupt:
        print(main_screen + show_cursor, end="")
    finally:
        print(main_screen + show_cursor, end="")

if __name__ == "__main__":
    main()
