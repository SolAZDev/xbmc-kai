#! /usr/bin/python2.7
# XBMC-Kai by SolAZDev
from KaiConnect import KaiConnect

import xbmc
import xbmcgui
import xbmcaddon

aPrevMenu = 10
aSelectItem = 7

__addon__ = xbmcaddon.Addon()
__cwd__ = __addon__.getAddonInfo('path').decode("utf-8")


class XMLMenu(xbmcgui.WindowXMLDialog):

    def __init__(self, file, basedir, fall1, fall2):
        pass

    def onInit(self):
        # Put your List Populating code/ and GUI startup stuff here
        pass

    def onAction(self, action):
        kai = KaiConnect()
        if action == aPrevMenu:
            self.close()
        if action == aSelectItem:
            d = xbmcgui.Dialog()
            d.ok('It works?', 'Kai\'s link is... ' +
                 kai.GetFromKai('getstatus'))
        pass

    def onClick(self, controlID):
        """
            Notice: onClick not onControl
            Notice: it gives the ID of the control not the control object
        """
        pass

    def onFocus(self, controlID):
        pass


class MainMenu(xbmcgui.Window):
    def __init__(self):
        kai = KaiConnect()
        res = kai.GetFromKai('getstatus')
        self.strHead = xbmcgui.ControlLabel(
            250, 80, 200, 50, '', 'font14', '0xFF00FF00')
        self.addControl(self.strHead)
        self.strHead.setLabel('XMBC-Kai Plugin')

        self.strStatus = xbmcgui.ControlLabel(
            250, 250, 400, 400, '', 'font14', '0xFF00FF00')
        self.addControl(self.strStatus)
        self.strStatus.setLabel(res)

    def onAction(self, action):
        kai = KaiConnect()
        if action == aPrevMenu:
            self.close()
        if action == aSelectItem:
            d = xbmcgui.Dialog()
            d.ok('It works?', 'Kai\'s link is... ' +
                 kai.GetFromKai('getstatus'))


# if __name__ == '__main__':
#     kai = KaiConnect()
#     kai.main()

# diag = xbmcgui.Dialog()
# kai = KaiConnect()
# res = kai.GetFromKai('getstatus')
# diag.ok('result', res)


# xkWindow = MainMenu()
# xkWindow.doModal()

xkWindow = XMLMenu('window.xml', __cwd__, 'default', '720p')
xkWindow.doModal()

del xkWindow
