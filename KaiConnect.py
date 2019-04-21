import requests


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
