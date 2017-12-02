import dbus

system_bus = dbus.SystemBus()

battery = system_bus.get_object('org.freedesktop.UPower',
                                '/org/freedesktop/UPower/devices/DisplayDevice')


def get_info():
    return battery.GetAll('org.freedesktop.UPower.Device',
                          dbus_interface='org.freedesktop.DBus.Properties')
