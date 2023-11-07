# sort

sort orders data, separated by newlines, in a predictable way.

- default sorting order depends on locale, but essentially alphabetical with
  digits 0-9 ascending
	- can also be used with pipes
- operate on a list of movies with several fields (rank, title, year), for
  example
	- naive `sort` invocation on ranking number: what's wrong with this?
		- hint: show `seq 20 | sort`
		- add `-n`
	- sort by title
		- `-V` (version sort): mix of letters and numbers (GNU extension)
	- sort by year
		- use `-t` and `-k` to select the year field
- `-r` reverse sort
- watch out for `-f`: it's like `-i` in other programs

# shuf

shuf orders data, separated by newlines, in a randomized way.

- randomized book list: `shuf books.txt`
- random book: `shuf -n 1 books.txt`
- `-e`: `shuf -e "this" "that" "the other" -n 1`

# uniq

uniq removes duplicates from data, separated by newlines.

- uniq actually relies on sorted data, so you'll often use this in conjunction
  with a `sort` command
	- `sort -u` is convenient if you don't need special uniq options
- `-c` to prefix each line with how many times it occurs
- `-d` to only print lines that occurred more than once
	- `-c` and `-d` may be combined
