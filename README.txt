Simple game-like app for children.
Displays image associated with pressed key.

Currently only Czech language bindings in preparation,
in future also english mappings are planned.


Requires python (developed with 2.7, probably already installed),
and python's pygame and magickwand and wand:
$ apt-get(etc) install libmagickwand-dev # see wand-py.org
$ pip install pygame
$ pip install Wand

First fetch images to be used:
$ ./download_img.py

If fetching/conversion of any image will fail you have to 
find other suitable and replace the url in img/source.json
or download/convert and place it manualy in img/{img_id}.png.

Launch using:
$ ./main.py

Then press any key (like '1', '2', ... or 'a') and you should see the image.

** Use Ctrl+Alt+Q to quit the app! **
(Thats kind of lock against child breaking out to your system, but actually not so child-proof.)


=====
(c) 2013 - Queria Sa-Tas <public@sa-tas.net>
Until licensing will be cleared here, ask me directly about it.
But it will be under some kind of open (like GPL/Apache/BSD etc) license,
so at least you are free to use and modify this.

