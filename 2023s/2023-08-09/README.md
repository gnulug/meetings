
Options for waiting for files to be ready:

- Busy-poll: try reading each file (possibly each in their own thread).
    - Downside: CPU intensive, inefficient, not scalable
- select syscall: here's a list of FDs, tell me which ones are ready
    - Downside: Stateless, so O(n) un/register in user-space
- poll syscall: like select, but can easily reuse inputs across subsequent interations
    - Downside: Stateless, so O(n) un/register in kernel-space
- epoll syscall (Linux): like poll, but stateful, so far less work in subsequent iterations
    - Downside: like epoll, but not just files. Avoids thundering heard problem
- kqueue syscall (BSD)
    - Downside: Not Linux ;P

Reading:

- https://daemonforums.org/showthread.php?t=2124
- https://long-zhou.github.io/2012/12/21/epoll-vs-kqueue.html
- https://idea.popcount.org/2017-01-06-select-is-fundamentally-broken/
- https://idea.popcount.org/2016-11-01-a-brief-history-of-select2/
- https://idea.popcount.org/2017-02-20-epoll-is-fundamentally-broken-12/
- https://idea.popcount.org/2017-03-20-epoll-is-fundamentally-broken-22/
- https://ariadne.space/2021/06/06/actually-bsd-kqueue-is-a-mountain-of-technical-debt/


```python
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
```
