from pypresence import Presence

import time

client_id = "718896866443526175"

RPC = Presence(client_id)

RPC.connect()

milliseconds = int(round(time.time() * 1000))

while True:
    RPC.update(
        details="waiting for ZeroDay",
        start=milliseconds,
        large_image="4k",
        large_text="Slowlydev"
    )
    time.sleep(15)