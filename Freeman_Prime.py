import os
import time
import sys

def scroll_number():
    number_str = "8091*24^705188+1"
    try:
        # Get terminal width
        cols = os.get_terminal_size().columns
    except:
        cols = 80  # Default if terminal size can't be determined

    # Create scrolling buffer with padding
    padded = number_str + ' ' * cols
    len_total = len(padded)
    offset = 0

    try:
        while True:
            # Calculate current display window
            start = offset % len_total
            end = start + cols
            
            if end <= len_total:
                display = padded[start:end]
            else:
                # Handle wrap-around
                display = padded[start:] + padded[:end - len_total]
            
            # Print with carriage return and flush
            sys.stdout.write('\r' + display)
            sys.stdout.flush()
            
            offset += 1
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        sys.stdout.write('\n')  # New line on exit
        sys.stdout.flush()

if __name__ == "__main__":
    scroll_number()
