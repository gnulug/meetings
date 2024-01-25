# `nl`
- `nl` numbers lines
- **Note** that `cat -n` or `cat --number` is an easier way to number the lines.
- ```
  $ echo -e 'a\nb\nc'
  a
  b
  c

  $ echo -e 'a\nb\nc' | nl
     1  a
     2  b
     3  c
  ```
- Great, done.
- Edge-case for blank lines
- ```
  $ echo -e 'a\nb\n\nc' | nl
       1  a
       2  b

       3  c

  $ man nl

  $ echo -e 'a\nb\n\nc' | nl --body-numbering=a
       1  a
       2  b
       3  
       4  c

  ```
- Great, done.
- Edge-case for `\:`
- ```
  $ echo -e '\na\n\\:\nb\n\nc' | nl --body-numbering=a
     1  
     2  a

       b
       
       c

  $ man nl

  $ info '(coreutils) nl invocation'

  $ echo -e '\\:\\:\\:\nheader1 (page 1)\nheader2\n\\:\\:\nbody1\nbody2\n\\:\nfooter1\nfooter2\n\\:\\:\\:\nheader1 (page 2)\nheader2\n\\:\\:\nbody1\nbody2\n\\:\nfooter1\nfooter2' > doc

  $ nl doc

       header1 (page 1)
       header2

     1  body1
     2  body2

       footer1
       footer2

       header1 (page 2)
       header2

     1  body1
     2  body2

       footer1
       footer2

  $ open https://www.man7.org/linux/man-pages/man1/nl.1.html

  $ nl --body-numbering=a --section-delimiter= doc
       1  \:\:\:
       2  header1 (page 1)
       3  header2
       4  \:\:
       5  body1
       6  body2
       7  \:
       8  footer1
       9  footer2
      10  \:\:\:
      11  header1 (page 2)
      12  header2
      13  \:\:
      14  body1
      15  body2
      16  \:
      17  footer1
      18  footer2
  ```
- Great, done.
- Edge-case for short-options
- ```
  $ nl -ba -d'' doc
  nl: option requires an argument -- 'd'
  Try 'nl --help' for more information.

  $ printf "'%s'\n" abc 'def' ghi
  'abc'
  'def'
  'ghi'

  $ printf "'%s'\n" abc'def'
  'abcdef'

  $ printf "'%s'\n" -d''
  '-d'

  $ nl -ba -d '' doc
  ```

# `head`

- ```
  $ nl -ba -d '' doc > doc-num

  $ head --lines=4 doc-num
       1  \:\:\:
       2  header1 (page 1)
       3  header2
       4  \:\:

  $ head --lines=-4 doc-num
       1  \:\:\:
       2  header1 (page 1)
       3  header2
       4  \:\:
       5  body1
       6  body2
       7  \:
       8  footer1
       9  footer2
      10  \:\:\:
      11  header1 (page 2)
      12  header2
      13  \:\:
      14  body1

  ```

# `tail`

- ```
  $ tail --lines=4 doc-num
      15  body2
      16  \:
      17  footer1
      18  footer2

  $ tail --lines=+4 doc-num
       4  \:\:
       5  body1
       6  body2
       7  \:
       8  footer1
       9  footer2
      10  \:\:\:
      11  header1 (page 2)
      12  header2
      13  \:\:
      14  body1
      15  body2
      16  \:
      17  footer1
      18  footer2
  ```

# `tail --folow`

- ```
  $ touch test

  $ tail --follow test

  $ # Switch another terminal, while leaving that oen open

  $ cat > test
  start typing, press enter.
  ```
