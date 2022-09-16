# Dotfiles by Samuel Grayson

- Mechanisms
  - Central database (Windows Registry, dconf)
    - Corruption would be bad
    - Different options need different permissions
  - System-wide config file (/etc, /usr/local/etc)
    - Needs root
  - User config file (~/.thing or ~/.config/thing)
  - Project-local config file (.envrc, .gitconfig)

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
    - Demo

- Dotfiles for:
  - Editor
  - Shell (aliases, env vars, UI)
  - Terminal
  - Terminal multiplexer
