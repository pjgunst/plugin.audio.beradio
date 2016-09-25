from resources.lib import beradio

class BeRadioStation:

    def __init__(self, myitem):
        self.name = myitem.get('name')
        self.streamurl = myitem.get('streamurl')
        self.language = myitem.get('language')
        self.icon = myitem.get('icon256')

    def getIconPath(self):
        return str(beradio.plugin_path+'/resources/media/'+self.icon)

    def getStreamUrl(self,setting):
        mystream = self.streamurl.get(beradio.streams[setting])
        if not mystream:
            mystream = self.streamurl.get(beradio.streams[0])
        return mystream

