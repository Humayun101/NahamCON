import zlib

with open("5B-0", "rb") as compressed_file:
    compressed_data = compressed_file.read()

decompressed_data = zlib.decompress(compressed_data)

with open("5B-0-decompressed", "wb") as output_file:
    output_file.write(decompressed_data)

print("Decompression complete. Output saved to 5B-0-decompressed")
