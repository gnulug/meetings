CFLAGS = -Wall -g -Og

%.html: %.md
	pandoc --standalone --to=revealjs --output=$@ $<

%.o: %.c
	gcc -g -c $(CFLAGS) -o $@ $<

%.exe: %.c
	gcc -g $(CFLAGS) -o $@ $<

%.tiny_exe: %.c Makefile
	gcc -ffreestanding -nostdlib -s -Os $(CFLAGS) -o $@ $<

%.tiny_o: %.c Makefile
	gcc -ffreestanding -nostdlib -s -Os -c $(CFLAGS) -o $@ $<

%.s: %.o
	objdump --disassemble $< > $@
