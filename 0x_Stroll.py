import curses
import random
import time

def main(stdscr):
    # Initialize curses settings
    curses.curs_set(0)  # Hide cursor
    stdscr.nodelay(1)   # Non-blocking input
    stdscr.clear()
    
    hex_digits = "0123456789ABCDEF"
    
    while True:
        # Get current screen dimensions
        height, width = stdscr.getmaxyx()
        
        # Generate screen content
        for row in range(height):
            # Create a string of random hex digits for the entire row
            hex_row = ''.join(random.choice(hex_digits) for _ in range(width))
            try:
                # Add the row if it's not the last line (curses exception prevention)
                if row < height - 1:
                    stdscr.addstr(row, 0, hex_row)
            except curses.error:
                pass  # Ignore edge-case write errors
        
        stdscr.refresh()
        
        # Check for quit key (q or Q)
        if stdscr.getch() in (ord('q'), ord('Q')):
            break
        
        time.sleep(0.05)  # Small delay to reduce CPU usage

if __name__ == "__main__":
    curses.wrapper(main)
