import logging
import gi

from gaphor.abc import ActionProvider, Service
from gaphor.core import action
try:
    from gaphor.core import gettext
except ImportError:
    def gettext(s): return s


gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

log = logging.getLogger(__name__)


class HelloWorldPlugin(Service, ActionProvider):

    def __init__(self, main_window, tools_menu):
        self.main_window = main_window
        tools_menu.add_actions(self)

    def shutdown(self):
        pass

    @action(
        name="helloworld",
        label=gettext("Hello world"),
        tooltip=gettext("Every application should have a Hello world plugin!"),
    )
    def helloworld_action(self):
        main_window = self.main_window
        dialog = Gtk.MessageDialog(
            parent=main_window.window,
            type=Gtk.MessageType.INFO,
            buttons=Gtk.ButtonsType.OK,
            message_format="Every application should have a Hello world plugin!",
        )
        dialog.run()
        dialog.destroy()
