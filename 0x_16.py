import curses
import random
import time

def main(stdscr):
    # Initialize curses settings
    curses.curs_set(0)  # Hide cursor
    stdscr.nodelay(1)   # Non-blocking input
    
    hex_digits = "0123456789ABCDEF"
    
    for screen in range(16):
        # Clear the screen for fresh drawing
        stdscr.clear()
        
        # Get current screen dimensions
        height, width = stdscr.getmaxyx()
        
        # Generate entire screen content at once
        screen_content = []
        for row in range(height):
            # Create full width string of random hex digits
            hex_row = ''.join(random.choice(hex_digits) for _ in range(width))
            screen_content.append(hex_row)
        
        # Draw entire screen at once
        for row, content in enumerate(screen_content):
            try:
                # For all but the last row, write the full content
                if row < height - 1:
                    stdscr.addstr(row, 0, content)
                # Special handling for the last row to avoid curses exception
                elif width > 0:
                    # Write all but the last character
                    if width > 1:
                        stdscr.addstr(row, 0, content[:-1])
                    # Write the last character separately
                    stdscr.addch(row, width - 1, content[-1])
            except curses.error:
                pass  # Ignore any write errors
        
        # Refresh to display the entire screen simultaneously
        stdscr.refresh()
        
        # Check for quit key (q or Q)
        if stdscr.getch() in (ord('q'), ord('Q')):
            return
        
        # Pause between screens except before the last one
        if screen < 15:
            time.sleep(1.5)
        elif screen == 14:
            time.sleep(0.5)  # Longer pause before final screen
    
    # After 16 screens, keep last screen displayed until interrupted
    stdscr.nodelay(0)  # Switch to blocking input
    stdscr.getch()     # Wait for any key press

if __name__ == "__main__":
    curses.wrapper(main)
