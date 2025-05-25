import socket
import time

HOST = 'challenge.nahamcon.com'
PORT = 31746
OUTPUT_FILE = '/home/humayun404/Downloads/NahamCON/book.txt'
PROMPT = "Press enter to continue"

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.settimeout(10)

    buffer = ""
    last_update = time.time()

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        try:
            while True:
                data = s.recv(4096)
                if not data:
                    print("Connection closed by server.")
                    break

                text = data.decode('utf-8', errors='ignore')
                buffer += text
                f.write(text)
                f.flush()

                # Check if the prompt is in the text, send Enter only then
                if PROMPT.lower() in text.lower():
                    s.sendall(b'\n')
                    time.sleep(0.5)

                # Status update every 30 seconds
                if time.time() - last_update > 30:
                    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Still receiving data...")
                    last_update = time.time()

        except socket.timeout:
            print("Connection timed out.")
        except KeyboardInterrupt:
            print("\nUser interrupted.")
        finally:
            s.close()

if __name__ == "__main__":
    main()
