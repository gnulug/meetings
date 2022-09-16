# Dotfiles by Samuel Grayson

- Mechanisms
  - Central database (Windows Registry, dconf)
    - Corruption would be bad
    - Different options need different permissions
  - System-wide config file (/etc, /usr/local/etc)
    - Needs root
  - User config file (~/.thing or ~/.config/thing)
    - xdg specification is to use ~/.config/thing, which cleans up your home directory.
    - https://github.com/b3nj5m1n/xdg-ninja
  - Project-local config file (direnv)
    -
	```
# Create a new folder for demo purposes.
$ mkdir ~/my-project
$ cd ~/my-project

# Show that the FOO environment variable is not loaded.
$ echo ${FOO}

# Create a new .envrc. This file is bash code that is going to be loaded by
# direnv.
$ echo export FOO=foo > .envrc
.envrc is not allowed

# The security mechanism didn't allow to load the .envrc. Since we trust it,
# let's allow its execution.
$ direnv allow .
direnv: reloading
direnv: loading .envrc
direnv export: +FOO

# Show that the FOO environment variable is loaded.
$ echo $FOO
foo

# Exit the project
$ cd ..
direnv: unloading

# And now FOO is unset again
$ echo $FOO

	```

- Dotfile management
  - Symlinks
    - Demo
  - GNU Stow?
    - Demo
    -
      ```
        # Install Stow
        sudo apt install -y stow

        # Create the Stow directory
        mkdir -p dotfiles
        cd dotfiles

        # Create an epic Bash config
        mkdir bash
        echo 'export PS1="\e[45m\u@\h :\w$ \e[m"' >> bash/.bash_profile

        # Deploy our config
        stow bash

        # Test it out
        cd ~
    ```
  - Nix for dotfiles
    - https://github.com/charmoniumQ/dotfiles.nix/tree/main/home.nix

- Dotfiles for:
  - Editor
  - Shell (aliases, env vars, UI)
  - Terminal
  - Terminal multiplexer
