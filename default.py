#! /usr/bin/python2.7
# XBMC-Kai by SolAZDev
# import xbmc
import requests
import xbmc
import xbmcgui

aPrevMenu = 10
aSelectItem = 7


class KaiConnect:
    """Connection to Kai Engine via IP and Port."""
    kaiIP = '10.0.52.103'
    kaiPort = 34522
    kaiPortFoward = 30000  # Doubt I'll need this

    def CheckForKai(self):
        url = 'http://'+self.kaiIP+':'+`self.kaiPort`+'/api/v1/isalive'
        print('Trying to get '+url)
        r = requests.get(url)
        r.status_code
        if r.status_code != 200:
            print("Wrong address, try again, Error Code: "+r.status_code)
        else:
            print(r.text)

    def GetFromKai(self, getCall):
        url = 'http://'+self.kaiIP+':'+`self.kaiPort`+'/api/v1/'+getCall
        print('Trying to get '+url)
        r = requests.get(url)
        print(r.status_code)
        if r.status_code != 200:
            print("Wrong address, try again, Error Code: "+`r.status_code`)
        else:
            return r.text
            # print(r.text)

    def main(self):
        self.CheckForKai()
        print(self.GetFromKai('getstatus'))
        print(self.GetFromKai('getvector'))


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


xkWindow = MainMenu()
xkWindow.doModal()
del xkWindow
