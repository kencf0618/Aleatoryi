import time

def perverted_conversion(seed_hex):
    """Generates a sequence by recursively misinterpreting decimal numbers as hex"""
    current_value = seed_hex
    iteration = 0
    
    try:
        print(f"Starting cryptographic sequence with seed: 0x{seed_hex}")
        print("Press Ctrl+C to capture any value in the sequence\n")
        
        while True:
            # Convert hex to decimal
            decimal_value = int(current_value, 16)
            
            # Generate new "random" value
            current_value = str(decimal_value)
            
            # Print cryptographic sequence information
            print(f"Iteration {iteration}: 0x{current_value} → {decimal_value} "
                  f"(Digits: {len(current_value)}, Entropy: {len(current_value)*4} bits)")
            
            iteration += 1
            time.sleep(1.5)

    except KeyboardInterrupt:
        # Capture the last generated value as a potential cryptographic nonce
        print(f"\n\nCaptured at iteration {iteration}: {decimal_value}")
        print(f"Total entropy generated: {len(str(decimal_value))*4} bits")
        return decimal_value

# Initialize with cryptographic seed
SEED = "867"  # 0x867 = 2151 decimal
perverted_conversion(SEED)
