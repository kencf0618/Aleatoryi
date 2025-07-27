while True:
    user_input = input("Enter a hexadecimal number (0x...) or 'q' to quit: ").strip()
    
    if user_input.lower() == 'q':
        print("Exiting...")
        break
    
    if not user_input.startswith('0x'):
        print("Error: Input must start with '0x'. Try again.")
        continue
    
    try:
        decimal_value = int(user_input, 16)
        print(f"Decimal equivalent: {decimal_value}\n")
    except ValueError:
        print("Error: Invalid hexadecimal digits. Please try again.\n")
