import gi
import os
import sys

gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
gi.require_version('Rsvg', '2.0')
gi.require_version('WebKit2', '4.0')

from gi.repository import GLib, Gio, Gdk, Gtk


def app():
    return Gtk.Application.get_default()


def init(pkgdatadir):
    GLib.set_application_name('Nexmark')
    GLib.set_prgname('nexmark')

    resource = Gio.resource_load(os.path.join(pkgdatadir, 'nexmark.gresource'))
    Gio.Resource._register(resource)

    style_provider = Gtk.CssProvider()
    style_provider.load_from_resource("/io/mspencer/Nexmark/stylesheet.css")

    Gtk.StyleContext.add_provider_for_screen(
        Gdk.Screen.get_default(),
        style_provider,
        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
    )


def run(version, pkgdatadir, libdir):
    from .application import Application

    app = Application(version, pkgdatadir, libdir)
    return app.run(sys.argv)
