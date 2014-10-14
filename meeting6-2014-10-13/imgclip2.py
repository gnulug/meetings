#!/usr/bin/python
# uses python gtk3
import sys
from gi.repository import Gtk, Gdk

def copy_image(f):
    image = Gtk.Image.new_from_file(f)
    clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
    if image.get_storage_type() == Gtk.ImageType.PIXBUF:
        clipboard.set_image(image.get_pixbuf())
        clipboard.store()
    else:
        print("No image has been pasted yet.")

copy_image(sys.argv[1]);