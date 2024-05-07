def compress_text(text, char_map):
    compressed = [char_map.get(char.lower(), '') for char in text]
    return compressed

def decompress_text(compressed, char_map):
    decompressed = [char_map.get(num, '') for num in compressed]
    return ''.join(decompressed)

# Example character mapping
char_map = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
            'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
            't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, ' ': 27}

while True:
    operation = input("Enter 'c' to compress or 'd' to decompress (or 'q' to quit): ").lower()
    
    if operation == 'q':
        break
    
    if operation not in ['c', 'd']:
        print("Invalid operation. Please enter 'c', 'd', or 'q'.")
        continue
    
    text = input("Enter the text: ")
    
    if operation == 'c':
        compressed_text = compress_text(text, char_map)
        print("Compressed:", compressed_text)
    elif operation == 'd':
        decompressed_text = decompress_text(text.split(), {v: k for k, v in char_map.items()})
        print("Decompressed:", decompressed_text)
