#!/usr/bin/python3
# -*- coding: utf-8 -*-

import adbs
import os
import signal
from datetime import date

try:
    import gi
    gi.require_version('AppIndicator3', '0.1')
    from gi.repository import AppIndicator3 as ai
    from gi.repository import Gtk as gtk
    from gi.repository import GObject as gobject
except ImportError:
    print('Repository version required is not available!!')
    exit(1)

APPINDICATOR_ID = 'nepcal-applet'
indicator = ai.Indicator.new(APPINDICATOR_ID,
                             os.path.abspath('nepaliflag.png'),
                             ai.IndicatorCategory.OTHER)


def get_today():
    today = date.today().strftime('%Y/%m/%d')
    bs_today = adbs.ad_to_bs(today)['ne']
    return '{} {} {}, {}'.format(bs_today['year'], bs_today['str_month'],
                                 bs_today['day'], bs_today['str_day_of_week'])


def set_label():
    indicator.set_label(get_today(), "")
    return True


def menu():
    menu = gtk.Menu()
    item_quit = gtk.MenuItem('Quit')
    item_quit.connect('activate', quit)
    menu.append(item_quit)
    menu.show_all()
    return menu


def quit(src):
    gtk.main_quit()


def main():
    indicator.set_status(ai.IndicatorStatus.ACTIVE)
    indicator.set_label(get_today(), "")
    gobject.timeout_add(5000, set_label)
    indicator.set_menu(menu())
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    gtk.main()

if __name__ == '__main__':
    main()
