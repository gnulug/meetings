import select
import subprocess
import os

# Don't forget to `chmod a+r` these inputs.
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
# Without having to worry that it will block when we get to th eend
for fd in file_descriptors:
    os.set_blocking(fd, False)

while True:
    # select(read_set, write_set, exceptional_set) -> read_fds_ready, write_fds_ready, exceptional_fds_ready
    # We don't care about the write_fds or the exceptional_fds
    ready = select.select(file_descriptors, [], [])[0]

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
