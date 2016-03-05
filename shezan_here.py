import os

from gi.repository import Nautilus, GObject

class ColumnExtension(GObject.GObject, Nautilus.MenuProvider):
    def __init__(self):
        pass
    def menu_activate_cb(self, menu, file):

    	uri=file.get_uri()
	uri="/"+uri.split("///")[1]
	print uri

	os.system("cd %s && gnome-terminal -e 'jupyter notebook' &"%uri)

    def get_background_items(self, window, file):
        item = Nautilus.MenuItem(name='ExampleMenuProvider::Foo2', 
                                         label='Open Jupyter Here', 
                                         tip='',
                                         icon='')
        item.connect('activate', self.menu_activate_cb, file)
        return item,
