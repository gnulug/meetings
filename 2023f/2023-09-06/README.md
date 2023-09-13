# Shkype

- [Repository](https://github.com/Evidlo/shkype/)


# Ricing shell demo

1. Choose shell: Bash, Zsh, Fish, Xonsh, others
   - Bash: standard, exists everywhere
   - Fish: good out-of-the-box configuration
   - Zsh: most customizable
   - Xonsh: mixes Python with Bash
   - List of all shells: https://wiki.archlinux.org/title/Command-line_shell
   - List of "improved" shell languages: https://github.com/oilshell/oil/wiki/Alternative-Shells
   - History of shells: https://developer.ibm.com/tutorials/l-linux-shells/
   - Comparison of syntax of "classic" shells: https://hyperpolyglot.org/unix-shells
1. PS1
   - https://www.gnu.org/software/bash/manual/html_node/Bash-Startup-Files.html
   - https://wiki.archlinux.org/title/Bash/Prompt_customization
   - https://tldp.org/HOWTO/Bash-Prompt-HOWTO/c141.html
   - `export PS1=blah` to set PS1. Use backslash to delay evaluation of dollar-signs.
   - Try putting directory basename and username: `export PS1="\$(whoami)@\$(hostname) \$(dirname \$PWD) \\\$"`
   - `emacs ~/.bashrc` to edit
   - `source ~/.bashrc` to run
   - ANSI escape codes
     - https://notes.burke.libbey.me/ansi-escape-codes/
   - Try putting color in your prompt
   - Prebuilt:
     - Powerbash: https://github.com/napalm255/powerbash
     - Liquidprompt (Bash + Zsh): https://liquidprompt.readthedocs.io/en/stable/index.html
     - Powerlevel10k (Zsh): https://github.com/romkatv/powerlevel10k
     - Spaceship (Zsh): https://spaceship-prompt.sh/
 	- Starship (anything): https://starship.rs/
   - Try showing Spack env (if any is active) in liquidprompt
     - `function spack_ps1() { if [ -n "${SPACK_ENV}" ]; then echo "($(basename ${SPACK_ENV})) "; fi }; export LP_PS1_PREFIX="\$(spack_ps1)"`
1. Direnv
   - https://direnv.net/docs/installation.html
   - `echo 'spack env activate myenv' >> .envrc && direnv allow`
1. Aliases and git aliases
   - https://snyk.io/blog/10-git-aliases-for-faster-and-productive-git-workflow/
   - `alias l='ls -ahlt'`
1. Shell features
   - GNU readline
     - ctrl+r
   - Job management
     - /j
   - pushd/popd
   - https://github.com/junegunn/fzf/wiki
   - https://github.com/charmbracelet/gum
   - Stay away from Zsh plugin managers
1. Tmux
