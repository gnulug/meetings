LUG Meeting 5 Mutt Slides
=========

In order to recompile this you need to have a form of LaTeX installed. That's either going to be TexLive for Linux, MikTex for Windows, or MacTex for Mac OS. You will need to have the Beamer package installed. On TexLive systems, you can download that by issuing a `sudo tlmgr install beamer` - or perhaps it is in your distribution's package management system. On the other systems, it should be just as simple. 

The actual presentation is a pdf file called chameleon.pdf - the source that is in chameleon.tex, but most of the actual content you'll want to edit for the actual slides is in content.tex - it should be pretty simple to see how things are laid out.

So all you need to do to edit this, is open up content.tex in a plaintext editor, write whatever you want, then in the same directory as all the files, issue `pdflatex chameleon.tex` and it'll recompile.

The code/information in this presentation is all hereby published under the GNU GPL, the presentation theme is the "Beamer-Torino" courtesy of Marco Barisione - and it is additionally published under the GPL as well. 


Any config files for mutt are in the mutt subfolder
