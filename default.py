#! /usr/bin/python2.7
# XBMC-Kai by SolAZDev
#import xbmc
import requests
import xbmc
import xbmcgui

aPrevMenu = 10
aSelectItem = 7


class XBMCKai(xbmcgui.Window):
    def onAction(self, action):
        if action == aPrevMenu:
            self.close()
        if action == aSelectItem:
            res = KaiConnect.GetFromKai('getStatus')
            self.strAction = xbmcgui.ControlLabel(
                300, 200, 200, 500, res, 'font14', '0xFF00FF00')
            self.addControl(self.strAction)


class KaiConnect:
    """Connection to Kai Engine via IP and Port."""
    kaiIP = '10.0.52.103'
    kaiPort = '34522'
    kaiPortFoward = 30000  # Doubt I'll need this

    kaiIP.__doc__ = "Kai Engine's IP Address"
    kaiPort.__doc__ = "Kai Engine's WebUI Port. Max of 5 digits"
    kaiPortFoward.__doc__ = "Unused So far. Kai Engine's Portfoward port."

    def CheckForKai(self):
        url = 'http://'+self.kaiIP+':'+self.kaiPort+'/api/v1/isalive'
        print('Trying to get '+url)
        r = requests.get(url)
        r.status_code
        if r.status_code != 200:
            print("Wrong address, try again, Error Code: "+r.status_code)
        else:
            print(r.text)

    def GetFromKai(self, getCall):
        url = 'http://'+self.kaiIP+':'+self.kaiPort+'/api/v1/'+getCall
        print('Trying to get '+url)
        r = requests.get(url)
        print(r.status_code)
        if r.status_code != 200:
            print("Wrong address, try again, Error Code: "+r.status_code)
        else:
            return r.text
            # print(r.text)

    def main(self):
        self.CheckForKai()
        print(self.GetFromKai('getstatus'))
        print(self.GetFromKai('getvector'))


# if __name__ == '__main__':
#     kai = KaiConnect()
#     kai.main()

diag = xbmcgui.Dialog()
diag.ok(KaiConnect.GetFromKai('getstatus'))


# xkWindow = XBMCKai()
# xkWindow.doModal()
# del xkWindow
