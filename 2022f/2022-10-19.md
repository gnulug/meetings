# General stuff

- What to name?

  - Decided: GLUG

- Future sessions?

  - Live coding
  - Linux From Scratch
  - Boot
  - History of opensource
  - Writing apps/kernel hacking for Linux in C
  - Do Linux interview questions

- Co-president

# Moving files over a newtork

## Lightweight methods

- Magic Wormhole
- Termbin
  - No client needed
- wgetpaste
  - Publicly shareable
- Netcat
  - Realtime

## Mid-sized methods

- scp/sftp
  - Recursively transfer directories
- rsync
  - Incremental transfer
  - Compression
- GCP, like Termbin
  - No client needed on read-side
  - Binary files
- IPFS like GCP
  - ```shell
    $ ipfs init
    $ hash=$(ipfs add -q test)
    $ curl https://ipfs.io/ipfs/$hash
    ```

  - No backend needed

## Heavy-duty methods

- Sneakernet
  - Validation
  - Robotics??
  - https://what-if.xkcd.com/31/
- Globus
