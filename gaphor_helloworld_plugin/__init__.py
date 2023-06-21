import logging
import gi

from gaphor.abc import ActionProvider, Service
from gaphor.action import action
from gaphor.i18n import gettext

from gi.repository import Adw

log = logging.getLogger(__name__)


class HelloWorldPlugin(Service, ActionProvider):

    def __init__(self, main_window, tools_menu):
        self.main_window = main_window
        tools_menu.add_actions(self)

    def shutdown(self):
        pass

    @action(
        name="helloworld",
        label=gettext("Hello World"),
        tooltip=gettext("Every application should have a Hello world plugin!"),
    )
    def helloworld_action(self):
        window = self.main_window.window

        dialog = Adw.MessageDialog.new(
            window,
            gettext("Hello world"),
        )
        dialog.set_body(
            gettext(
                "Every application should have a Hello world plugin!"
            )
        )
        dialog.add_response("close", gettext("Close"))
        dialog.set_close_response("close")

        dialog.set_visible(True)
