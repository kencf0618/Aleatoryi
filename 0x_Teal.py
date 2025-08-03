
import curses
import random
import time

def main(stdscr):
    # Initialize colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    
    # Initialize curses settings
    curses.curs_set(0)  # Hide cursor
    stdscr.nodelay(1)   # Non-blocking input
    
    hex_digits = "0123456789ABCDEF"
    stored_screen = None
    stored_height, stored_width = 0, 0
    
    # Display 16 screens
    for screen in range(16):
        # Clear the screen
        stdscr.clear()

        # Get current screen dimensions
        height, width = stdscr.getmaxyx()

        # Generate entire screen content
        screen_content = []
        for row in range(height):
            hex_row = ''.join(random.choice(hex_digits) for _ in range(width))
            screen_content.append(hex_row)

        # Draw entire screen with special handling for last row
        for row in range(height):
            try:
                if row < height - 1:
                    stdscr.addstr(row, 0, screen_content[row])
                else:
                    if width > 0:
                        if width > 1:
                            stdscr.addstr(row, 0, screen_content[row][:-1])
                        stdscr.addch(row, width - 1, screen_content[row][-1])
            except curses.error:
                pass

        stdscr.refresh()
        
        # Store the last screen (16th)
        if screen == 15:
            stored_screen = screen_content
            stored_height, stored_width = height, width
        
        # Wait 1.5 seconds per screen with quit check
        start_time = time.time()
        while time.time() - start_time < 1.5:
            if stdscr.getch() in (ord('q'), ord('Q')):  # Fixed missing parenthesis
                return
            time.sleep(0.1)

    # Main loop for highlighting characters
    while True:
        # Wait 1.5 seconds (with key check)
        start_time = time.time()
        while time.time() - start_time < 1.5:
            if stdscr.getch() in (ord('q'), ord('Q')):
                return
            time.sleep(0.1)

        # Select random position
        row = random.randint(0, stored_height - 1)
        col = random.randint(0, stored_width - 1)

        # Get character at position
        char = stored_screen[row][col]

        # Highlight in red
        try:
            stdscr.addch(row, col, char, curses.color_pair(2))
            stdscr.refresh()
        except curses.error:
            pass

        # Wait 1.5 seconds (with key check)
        start_time = time.time()
        while time.time() - start_time < 1.5:
            if stdscr.getch() in (ord('q'), ord('Q')):
                return
            time.sleep(0.1)

        # Revert to green
        try:
            stdscr.addch(row, col, char, curses.color_pair(1))
            stdscr.refresh()
        except curses.error:
            pass

if __name__ == "__main__":
    curses.wrapper(main)
