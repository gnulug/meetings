
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
(rd_fds_ready, wr_fds_ready, exc_fds_ready) = select.select(rd_fds, wr_fds, exc_fds)
for rd_fd in rd_fds_ready:
    handle(rd_fd) # possibly in another thread :)
```

See `./buzzers.py`
