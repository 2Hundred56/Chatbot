import printio as io

alphabet = list("abcdefghijklmnopqrstuvwxyz0123456789")

def sanitize(msg):
    # Returns the new msg as a string
    # Character limit is for string after sanitization
    msg = msg.lower()
    final = ""
    for char in msg:
        if char in alphabet:
            final+=char
    return final
def process(msg):
    pass
def respond(msg):
    pass
def on_input(msg):
    process(msg)
    io.output(respond(msg))
