import json
from resources.lib import beradio
from resources.lib.beradiosettings import BeRadioSettings
from resources.lib.beradiostation import BeRadioStation

# compiles the listitems to be passed to Kodi
def process_stations(data,settings):
    myitems = []
    for i,myitem in sorted(data.iteritems()):
        myRadioStation = BeRadioStation(myitem)
        # language filter
        language = myRadioStation.language
        index_language = settings.getLanguage()
        if index_language > 0 and myRadioStation.language != beradio.languages[index_language] :
            continue
        # end language filter
        beradio.plugin.log.info(myRadioStation.getStreamUrl(settings.getStream()))
        myitems.append({
            'label': myRadioStation.name,
            'path': myRadioStation.getStreamUrl(settings.getStream()),
            'icon': myRadioStation.getIconPath(),
            'is_playable': True
        })
    return myitems


# default route
@beradio.plugin.route('/')
def index():
    myRadioSettings = BeRadioSettings()
    with open(beradio.plugin_path+'/resources/stations.json') as data_file:    
        data = json.load(data_file)
    items = process_stations(data, myRadioSettings)
    return items

# main
if __name__ == '__main__':
    beradio.plugin.run()
