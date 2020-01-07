import logging
import gi

from gaphor.abc import ActionProvider, Service
from gaphor.core import action, gettext

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

log = logging.getLogger(__name__)


class HelloWorldPlugin(Service, ActionProvider):

    menu_xml = """
      <ui>
        <menubar name="mainwindow">
          <menu action="help">
            <menuitem action="helloworld" />
          </menu>
        </menubar>
      </ui>
    """

    def __init__(self, main_window, export_menu):
        export_menu.add_actions(self)

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
