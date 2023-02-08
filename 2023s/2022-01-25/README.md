- Attendance: 6

# Demo for ACM Open House

Loose script:

- Our website doesn't work: http://web.samgrayson.me:6000/ip
- Linux is all about tools, and these are the tools we are going to use to fix the problem.
- First we will connect to the server to figure out the problem.
- Optional: I'm using a key file to authenticate, so I don't need a password
  - `mosh demo-0@web.samgrayson.me`
- Optional: I am using Mosh instead of SSH. Unlike SSH, if I shut my laptop or go to a different network, I can pick back up in Mosh.
- Optional: I want to pair-code with someone else. I join their terminal session in Tmux. Now we see the same cursor and output.
  - `tmux attach -t 0`
- Let's try to test our HTTP server in the terminal. What tool should we use?
  - `curl http://web.samgrayson.me:6000/ip`
- It seems to be broken...
- I'm going to ask Tmux to split this screen (ctrl+h, |)
- Let's check the status continuously. What tool should we use?
  - `watch -n 1 curl http://host.samgrayson.me:6000/ip`
- Back to the other terminal (ctrl+h, left)
- We want to know which process is accessing serving HTTP requests, so we can fix it. What tool should we use?
  - `lsof -i :6000`
- Optional: Let's find the command this process is running
  - `lsof -t -i :6000 | xargs ps -o '%a'`
- Let's store the PID and command as a variable
  - `pid=$(lsof -t -i :6000)`
  - `command=$(ps -o '%a' --no-headers $pid)`
- Optional: But we don't know where httpbin's "core.py" is found. Or just say it's probably in ~/httpbin.
  - `fd core\.py`
- We want to know what files it is reading, so we can fix it. What tool should we use?
  - `kill $pid`
  - `strace --trace=openat --output=log $command`
- We need to read this log. What should we use?
  - `emacs log` or `less log`
- Let the watch hit our broken server a few times
- The last error is most likely to be the problem, since it happens
- Now we know that the process is trying to read a file that does not exist. We need to find out where the source code references this file. What tool should we use?
  - `rg config.yaml`
- We've found the erroneous config.yaml open-syscall
- Now we need to edit this file. What tool should we use?
  - emacs, vim, nano, ...
- Comment out the offending code and relaunch
  - ctrl+c
  - `$command`
- Now the other buffer should begin to work!

Setup of server:

- Enable TCP:6000-6010 out for the webserver
- Enable TCP:60000-61000 out for Mosh
- As admin (update $NEW_USER and MY_$SSH_KEY):

```bash
sudo apt update && sudo apt install --assume-yes zsh git-core curl mosh tmux python3 python3-pip lsof ripgrep fd-find neofetch toilet lolcat
export NEW_USER=demo-1
sudo adduser $NEW_USER
export MY_SSH_KEY='ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDWwABCkuyQy2cqP7wppkQbMgfZqCWmQ18FHrh9P18C8 sam@laptop'
sudo --user=$NEW_USER sh <<EOF
mkdir --parents ~/.ssh
echo $MY_SSH_KEY >> ~/.ssh/authorized_keys
#$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
git clone https://github.com/zsh-users/zsh-completions ${ZSH_CUSTOM:-${ZSH:-~/.oh-my-zsh}/custom}/plugins/zsh-completions
pip install --user pipenv
git clone https://github.com/postmanlabs/httpbin.git
git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm
curl https://termbin.com/go8l > ~/.zshrc
curl https://termbin.com/l7ky > ~/.tmux.conf
cd httpbin
curl https://termbin.com/i16tj | git apply
pipenv install
EOF
```
Try logging in as $NEW_USER@web.samgrayson.me

```bash
chsh --shell $(which zsh) $NEW_USER
exec zsh
tmux # ctrl+h, I
```

# Status on server

- Documented at <https://github.com/gnulug/acm-glug-cloud/blob/main/progress.md>

# Ideas for server

- Documented at <https://github.com/gnulug/acm-glug-cloud/blob/main/proposal.md#resource-alocation>

# Merkle tree-based file system

- Documented at <https://github.com/charmoniumQ/merkle-tree-file-system>
