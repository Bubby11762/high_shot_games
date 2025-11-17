print("Welcome! Type something:")
# Simple REPL-ish demo
import sys
for i in range(3):
    s = input()  # will block; better replace with JS prompt for real UX
    print(f"You typed: {s}")
