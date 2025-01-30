# Start and EXit

    sex(){ ("$@" <>/dev/null >&0 2>&0 &) ; exit ;}
    
    sex evince example.pdf
    
function to start a command in the background and close terminal (e.g. open a PDF while in the shell)
    
# rootname

    function rootname(){ echo "${1%.*}"; }
    
    $ rootname foo/bar/baz.png
    foo/bar/baz

like basename but not

# Google Doc Image Copy

    curl $(wl-paste -n -t text/html | xmllint --html -xpath "string(//img/@src)" -) -o - | wl-copy -t image/png

Extracts and curls the web URL embedded in your clipboard when you copy an image from Google Docs, so your clipboard now has the actual image and not random unpasteable content

# Open files (web browser, LibreOffice, ...)

```
xdg-open https://google.com/
xdg-open document.docx
```

# Git Repo Size

    git gc --quiet && git count-objects -vH | grep size-pack

Prints the size of a git repo (in optimized form) so you can calculate how much space the deltas actually take up. Useful if you have a lot of deletions.

# Play Webcam in Console

    # fancy true color mode
    mpv --vo=tct --profile=low-latency --untimed /dev/video0
    # shitty caca mode
    mpv --vo=caca --profile=low-latency --untimed /dev/video0

# Use Capslock as i3wm/sway modkey

    setxkbmap -layout us -option caps:super,compose:lwin,compose:ralt,keypad:pointerkeys
    
    # in i3/sway config:
    set $mod mod4
  
 - sets capslock as i3 modkey
 - enables windows as xcompose key

Also check out [kragen/xcompose](https://github.com/kragen/xcompose), crowdsourced .XCompose with useful Unicode symbols/accents

# Send email with UIUC email relay

    echo "msgbody" | s-nail -S smtp=outbound-relays.techservices.illinois.edu -s "msgsubject" -r noreply@illinois.edu "destination@illinois.edu"

# Get env as JSON

`env` is good and all, but it doesn't work well if the value of an environment variable contains an newline and equals sign.

Instead, consider

```
python -c 'import os, json; print(json.dumps(dict(**os.environ)))' > env.json
```

I aliased this to `printenv_json`.

You can "restore" an env recorded as JSON (e.g., from `printenv_json`).

```
python -c 'import sys, json, pathlib, os
env = json.loads(pathlib.Path(sys.argv[1]).read_text())
os.execvpe(sys.argv[2], sys.argv[2:], env)' env.json [cmd-goes-here]
```

Lastly, I have [this script](https://github.com/charmoniumQ/dotfiles.nix/blob/main/lib/scripts/env_bisector) around that "bisects" your environment, searching for the right env vars configuration until some command works, but it's a bit more than one line.

# Perl one-liners

## pae
```sh
#!/bin/sh
exec perl -aE "$@"
```

Splits each line into `@F`. E.g., sum the last field in a file:

```sh
pae 'END{say $tot} $tot += $F[-1]' <file>
```

## ppae
```shell
#!/bin/sh
exec perl -paE "$@"
```

Same as above, but print each line:

```
ppae _ <file>                    # noop
ppae s,/foo,/foo/bar,g <file>    # replace
```

## ppie
```sh
#!/bin/sh
exec perl -pi -E "$@"
```

Same as above, but make changes in place (will overwrite the file!)

Use file globbing for mass search-replace.


# Not strictly one-liners, but cool commands?

## Git log pretty
```
[alias]
lg1 = log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(auto)%d%C(reset)' --all
lg2 = log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold cyan)%aD%C(reset) %C(bold green)(%ar)%C(reset)%C(auto)%d%C(reset)%n''          %C(white)%s%C(reset) %C(dim white)- %an%C(reset)'
lg = lg1
```

```
git lg
```

## Git with Meld

```
git difftool -t meld --dir-diff
```

## Get my IP
```
curl https://httpbin.org/ip
```

## Copy file contents to clipboard

```
cat file | wl-copy
cat file | xclip -sel
```

## Copy file itself to clipboard

Useful to paste into a GUI

```shell
wl-copy -t text/uri-list "file://$(realpath $1)"
```

```shell
echo "file://$(realpath $1)" | xclip -sel clip -t text/uri-list
```

## Do stuff remotely

Most people use SSH interactively. You can also use SSH in automations

```
ssh $host cat ~/.bashrc | wl-copy
```

You can also crate alises that automagically apply the right SSH flags. Consider:

```
ssh -J user1@jumphost -p 4444 user2@hostname
```

```
$ cat ~/.ssh/ssh_config
Host hostname
    JumpHost user1@jumphost
    Port 4444
    User user2
    HostName hostname

$ ssh hostname
```

## Pastebin from cmdline

```
$ echo just testing! | nc termbin.com 9999
https://termbin.com/test
$ curl https://termbin.com/test
just testing!
```

## Share file securely

```
$ wormhole send README.md
wormhole send README.md
Sending 7924 byte file named 'README.md'
On the other computer, please run: wormhole receive
Wormhole code is: 7-crossover-clockwork

$ # on another host, far, far away...
$ wormhole recieve 7-crossover-clockwork
Receiving file (7924 bytes) into: README.md
ok? (y/n): y
```

## Namecheap/Porkbun DNS

``` bash
#!/bin/bash

# get address
address=$(curl ifconfig.me)

# ----- namecheap -----
subdomain=bar
domain=example.org
password=80cc...
url="https://dynamicdns.park-your-domain.com/update?host=${subdomain}&domain=${domain}&password=${password}&ip=${address}"
echo $url
curl "${url}"

# ----- porkbun -----
subdomain=foo
domain=example.com
id=9...
apikey=pk1_7c8f...
secretapikey=sk1_452...
data='{"apikey":"'${apikey}'","secretapikey":"'${secretapikey}'","name":"'${subdomain}'","type":"A","content":"'${address}'"
}'
url=https://porkbun.com/api/json/v3/dns/editByNameType/${domain}/A/${subdomain}

curl "${url}" --data "${data}"
```

## Copy-dir-and-ssh

Let's say you are hacking on `./foobar`.

Now you realize your machine is too underpowered to run `./foobar`.

You want to copy everything to a remote, run `./foobar` on the remote, copy back the changes.

The second time, you don't even need to do a full copy; differential copy is better.

That's what [r](https://github.com/charmoniumQ/dotfiles.nix/blob/main/lib/scripts/r) does.

```
$ cat .r-mount
remote.host.name.com:path/to/dir/on/remote
--verbose --other-rsync-args-here

$ r ./foobar
# copies with rsync
# runs ./foobar, printing result
# copies changes back with rsync
```

## Don't do cd

`cd` is imperative. Imperative = bad. You need to invoke the shell.

```
cd foo
./bar
```

Instead, consider

```
env --chdir=foo ./bar
```

## Set your CDPATH

## Asci enema

<https://asciinema.org/>

## fortune | cowsay

## Imagemagick convert

```
magick image.jpg -resize 10% image.png
```

## Protect your .bash_history from overwrite

``` bash
# backup history/warn about deleted history
if (( $(wc -l < ~/.bash_history) < 10000 ))
then
    echo "#######################"
    echo ".bash_history was cleared"
    echo ""
    echo "WARNING!"
    echo ""
    echo "#######################"
    # make a backup of the history backup, and never overwrite
    cp -n ~/.bash_history.back ~/.bash_history.archive
else
    cp ~/.bash_history ~/.bash_history.back
fi
```

Bash has a dumb race condition that causes history to be wiped out sometimes.  This makes a backup of the history for each terminal session (based on line length).

## Try new distro
```bash
alis ll='rm -rf / && sudo !!'
```

## Ask AI for help
```
gh copilot suggest "how to print to stdout"
gh copilot explain "foobar"
```

## cheat.sh

```
curl cheat.sh
```

## Scroll text in panel or in terminal
```
zscroll -l 50 -d 0.2 -b " " -U 0.1 --update-check true "xtitle"
```

