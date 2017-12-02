import os

from gi.repository import GLib, Gtk

USER_DATA_DIR = os.path.join(GLib.get_user_data_dir(), 'nexmark')
USER_CACHE_DIR = os.path.join(GLib.get_user_cache_dir(), 'nexmark')


def icon(name, size=Gtk.IconSize.SMALL_TOOLBAR):
    return Gtk.Image.new_from_icon_name(name, size)


def present_window(window: Gtk.Window):
    if window.is_active():
        return

    timestamp = Gtk.get_current_event_time()
    if timestamp == 0:
        from gi.repository import GdkX11
        timestamp = GdkX11.x11_get_server_time(window.get_window())

    window.present_with_time(timestamp)


def property_to_str(display, prop):
    from Xlib import Xatom

    if prop.format == 8:
        if prop.property_type == Xatom.STRING:
            return prop.value.decode('ISO-8859-1')
        elif prop.property_type == display.get_atom('UTF8_STRING'):
            return prop.value.decode('UTF-8')
        else:
            import binascii
            return binascii.hexlify(prop.value).decode('ascii')
    elif prop.format == 32 and prop.property_type == Xatom.ATOM:
        return [display.get_atom_name(v) for v in prop.value]

    else:
        return prop.value
