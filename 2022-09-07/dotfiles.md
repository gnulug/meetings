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
  - Dotfiles for: editor, shell (aliases, env vars, UI), Git, terminal, terminal multiplexer
  - Symlinks or copy?
    - Hard to install on a new machine
  - Manual, DIY own script, or use a dotfile manager?
