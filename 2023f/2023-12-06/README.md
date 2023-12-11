- SuperTuxKart
  - Resembles another "kart" racing game with a certain Itallian plumber
  - `nix-shell -p superTuxKart`
  - `sudo pacman -S supertuxkart`
  - `sudo apt install -y supertuxkart`
  - Try changing the settings. See https://supertuxkart.net/FAQ

- Sauerbraten
  - First-person shooter (wasd, scroll to switch weapons, click to shoot)
  - `nix-shell -p sauerbraten`
  - `sudo pacman -S sauerbraten`
  - `sudo apt install -y sauerbraten` or `sauerbraten-server`
  - To connect, type `/connect $ip` replacing `$ip` with the IP of the server. Note the "command line overlay" is a transparent window whose prompt is at the very bottom of the screen; it can be easy to miss!
  - The server has a relatively small player limit. Put a file with `maxclients 15` in `server-init.cfg` in the current working directory. Perhaps typing `/maxclients 15` will work too; not sure. http://sauerbraten.org/docs/config.html
  - The server admin should press ESC and "Claim Master". They will be need to:
    - Start a new game by pressing ESC and casting a vote
    - Toggle newly joined players from spectating to playing.

- Teeworlds
  - Multiplayer CTF platformer
  - https://teeworlds.com/
  - `nix-shell -p teeworlds`
  - `sudo pacman -S teeworlds`
  - `sudo apt install -y teeworlds`

- Other games
  - https://wiki.archlinux.org/title/List_of_games
  - Doom
  - Quake (ioquake3)
  - Not really multiplayer, but very fun and traditional CLI-based UNIX nerd game https://en.wikipedia.org/wiki/NetHack
