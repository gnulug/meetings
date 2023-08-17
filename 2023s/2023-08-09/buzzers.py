#############################################
#
# This script implements a "jeopardy/quizbowl" buzzer system.
#
# Each user plugs in an input device (keyboard, mouse, joystick) to
# one computer.  Modify `devices` to their device name and usename.
# Those users can buzz in by submitting any input (keys, clicking,
# mouse movement).
#
# It is implemented using the select(2) syscall.  This is the same
# mechanism that an HTTP server would use to serve multiple requests
# concurrently.  Conceptually, "file descriptor" can be a physical
# input or a TCP socket, so the select(2) mechanism still applies.
#
#############################################

import select
import subprocess
import os

# Use evtest to find your /dev/input/event* path.
# Don't forget to `chmod a+r` that input.
# BUT `chmod a-r` after that;
# while we are chmod'ed, any process can see ALL events on that input (e.g., keylogging)!!
devices = [
    ("/dev/input/event18", "Sam"),
    ("/dev/input/event23", "Caden"),
    ("/dev/input/event27", "Pomona"),
]

# File path -> file obj
files = [open(device, "rb", buffering=0) for (device, owner) in devices]

# File obj -> file descriptor
file_descriptors = [file.fileno() for file in files]

# Set nonblocking allows us to clear out the file descriptor by repeated .read()
# Without having to worry that it will block when we get to the end
for fd in file_descriptors:
    os.set_blocking(fd, False)

while True:
    # select(read_fds, write_fds, exceptional_fds) -> read_fds_ready, write_fds_ready, exceptional_fds_ready
    # We don't care about the write_fds or the exceptional_fds
    ready, _, _ = select.select(file_descriptors, [], [])

    # At this point, at least one FD is ready to read

    for file_descriptor in ready:
        # file descriptor -> owner
        index = file_descriptors.index(file_descriptor)
        _, owner = devices[index]
        print(owner)

        # Clear out the data so we don't get pinged again about this.
        bufferf = b"not an empty string"
        while bufferf:
            bufferf = files[index].read()
            # When the input is exhausted, read will return an empty string immediately.
