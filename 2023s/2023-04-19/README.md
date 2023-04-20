# Architecture of Open Source Applications book

- Architecture of Open Source Applications Volume I edited by Greg Wilson
- Architecture of Open Source Applications Volume II edited by Greg Wilson
- Performance of Open Source Applications edited by Tavish Armstrong
- 500 Lines or Less edited by Michael DiBernardo
- <https://aosabook.org/en/index.html>
- <https://www.youtube.com/watch?v=vx0DUiv1Gvw> 08:00 -- 13:00

# Ninja

- Build system for Chrome
- Idea:
  - Do complex work once in Ninja file generator
    - Ninja language no support for dynamic dependencies, conditionals, loops
      - Just rules with variable substitution
  - Should changing the Makefile/Ninja file cause everything to rebuild?
    - No, use command history to know if the output is different
- Profile first!
- Macro optimizations
  - Only store hashes of command in build log
    - from 200 MB to less than 2 MB on Mac OS X–and made it over 20 times faster to load.
- Micro optimizations
  - IsIdentifierCharacter -> lookup table -> lexer
  - Path canonicalization takes a lot of time
