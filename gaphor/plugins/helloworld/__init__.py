
from zope import interface
from gaphor.interfaces import IService, IActionProvider
from gaphor.core import _, inject, action, build_action_group


class HelloWorldPlugin(object):

    interface.implements(IService, IActionProvider)

    gui_manager = inject('gui_manager')

    menu_xml = """
      <ui>
        <menubar name="mainwindow">
          <menu action="help">
            <menuitem action="helloworld" />
          </menu>
        </menubar>
      </ui>
    """

    def __init__(self):
        self.action_group = build_action_group(self)       

    def init(self, app):
        self._app = app
        log.info('Hello world plugin initialized')

    def shutdown(self):
        pass

    @action(name='helloworld', label=_('Hello world'),
            tooltip=_('Every application should have a Hello world plugin!'))
    def helloworld_action(self):
        main_window = self.gui_manager.main_window
        import gtk
        dialog = gtk.MessageDialog(
                parent=main_window.window,
	        type=gtk.MESSAGE_INFO,
	        buttons=gtk.BUTTONS_OK,
	        message_format='Every application should have a Hello world plugin!')
        dialog.run()
        dialog.destroy()


# vim: sw=4:et:ai
