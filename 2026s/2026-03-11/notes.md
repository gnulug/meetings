https://pradyunsg.me/blog/2023/01/21/thoughts-on-python-packaging/
https://www.courtbouillon.org/blog/00016-the-toolbox/
competing standards xkcd
https://blog.ganssle.io/articles/2021/10/setup-py-deprecated.html
https://discuss.python.org/t/how-can-build-backends-avoid-breaking-users-when-they-make-backwards-incompatible-changes/85847/9
https://www.reddit.com/r/rust/comments/lfysy9/pythons_cryptography_package_introduced_build/
https://pypackaging-native.github.io/key-issues/native-dependencies/cpp_deps/

Email I got

       - > The main challenge with this is that there are two package types commonly distributed on PyPI today: wheels and sdists. While wheels do contain static dependency data, sdists are "built" on installation and can run any arbitrary commands, including (but not limited to) dynamically determining dependency relationships. As a result, when installing an sdist its dependencies cannot be assumed in advance by the installer, and have to be determined during installation.
         >
         > No need to point out the obvious, that this historical tech debt leads to a fairly terrible situation, but the sdist (source distribution) package format long pre-dates wheels and there are still a nontrivial number of popular libs which are only distributed as sdists. Also, because non-pure-python wheels are platform-specific, if there is no wheel which suits your platform then retrieving and building the project's sdist is the standard fallback path for installers.
         >
         > I agree "it's stupid that PyPI can't" know package dependencies in all cases and provide that information to installers, but fixing it necessarily means a substantial backwards-incompatible change upending the entire Python package ecosystem. If it could have been solved easily, don't you think it would have been (decades ago)?
         >
         > ---https://lwn.net/Articles/920832/
- https://discuss.python.org/t/a-proposal-for-sdist-build-complexity-signaling-providing-user-agency/57474
     - When you need shell to build
       - https://pypackaging-native.github.io/other_issues/
       - https://pypackaging-native.github.io/key-issues/native-dependencies/cpp_deps/
       - https://pypackaging-native.github.io/key-issues/abi/
     - GPU problems
       - https://pypackaging-native.github.io/key-issues/gpus/
     - Whole Shebang package managers: Conda, Pixi, Nix, Spack
       - Cross-platform focus (Conda's lockfile depends on glibc and kernel, I think)
     - System package managers
   - https://nielscautaerts.xyz/python-dependency-management-is-a-dumpster-fire.html
   - Environments vs system-wide (rootful)
     - https://stackoverflow.com/questions/75608323/how-do-i-solve-error-externally-managed-environment-every-time-i-use-pip-3
     - https://askubuntu.com/questions/802544/is-sudo-pip-install-still-a-broken-practice
     - https://stackoverflow.com/questions/68673221/why-do-i-still-get-a-warning-about-running-pip-as-the-root-user-inside-a-doc
     - https://askubuntu.com/questions/378349/when-using-sudo-to-run-pip-pip-command-not-found-but-its-installed
   - Import name vs package name
     - https://packaging.python.org/en/latest/discussions/distribution-package-vs-import-package/
   - Lib vs app; specfile vs lockfile ('~' operator)
   - https://zahlman.github.io/posts/python-packaging-1/
   - https://chriswarrick.com/blog/2023/01/15/how-to-improve-python-packaging/#tooling-proliferation-and-the-python-package-authority
4. Other examples
   - Julia
   - Perl/CPAN
   - R/CRAN
   - Node/NPM/Yarn
   - Zplug/oh-my-zsh
   - Go
   - NuGet
   - Haskell?
   - https://chriswarrick.com/blog/2023/01/15/how-to-improve-python-packaging/#tooling-proliferation-and-the-python-package-authority
   - Considerations:
     - Popularity
     - Native code
     - NPM has commercial support; PyPA did not in the early days
     - Uniform testing infra
     - Language churn rate, packaging improvements/churn
     - Package management did not work the way it does now (build-from-source, global, not known to be NP-C)
     - NPM/Cargo needs shell to build
       - https://medium.com/@v_pragma/12-strange-things-that-can-happen-after-installing-an-npm-package-45de7fbf39f0
     - Monolingual dependencies
       - >      Python has a way, way, WAY harder context here than rust (where dependencies are mostly mono-lingual and can be built with the same build system, which conveniently also comes with a uniform compiler everywhere), since it exists as a glue language to just about everything. So without a comprehensive and cross-platform answer how to deal with non-python artefacts (building, distribution) that live in python projects - anything from C/C++/Fortran/Rust/Java/NodeJS/CUDA… - a cargo-like experience is very far away. 
    - https://lwn.net/Articles/920832/
    - > (CPAN) Yes, you need an appropriate compiler installed if you install a module that wraps another language like C.
      >
      > Yes, you do need to install non-Perl dependencies such as C libraries yourself.
      >
      > And there is no good solution for keeping multiple versions of the same Perl module around at the same time. The only mitigating factor is that Perl modules rarely break backward compatibility and it's quite rare for code to require exactly version X.Y of a module. Usually its "X.Y or newer." This is, of course, not enforced or enforceable. It's just the common practice.
      >
      > If you do need multiple versions of a module, you need to store them in different directories and adjust your @INC path as appropriate.
      > ---https://lwn.net/Articles/920832/
    - > Perl has exactly the same problems mentioned here about Python: multiple different packaging tools and styles, multiple tools to install Perl modules, disagreement over how to handle additional module installs required for a specific application, and no good way to handle conflicting versions of modules. It also has some problems that Python doesn't have, such as lack of a good dependency resolver that understands how to downgrade one module to meet the overall version constraints of a project.
      >
      > You hear less about these problems in Perl mostly because the pace of development in Perl modules is so much slower that distribution packaging does a great job for core Perl modules and additional module installs are usually more ancillary things without complex dependency trees. I think it's much more common in Perl development to use whatever Perl and module set came with your distribution as a starting point and only add on a few things around the edges.
      > ---https://lwn.net/Articles/920832/


https://lwn.net/Articles/924104/
https://lwn.net/Articles/1020576/
