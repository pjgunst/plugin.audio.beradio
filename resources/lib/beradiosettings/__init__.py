import resources.lib.beradio as beradio

class BeRadioSettings:
        
    def __init__(self):
        self.language = beradio.beradio_addon.getSetting('settings_lang')
        self.stream = beradio.beradio_addon.getSetting('settings_stream')

    def getLanguage(self):
        index_language = beradio.cast_integer(self.language)
        try:
            mylang = beradio.languages[index_language]
        except IndexError:
            plugin.log.debug('language setting: '+self.language+' is not in our list, assuming '+beradio.languages[0])
            index_language = 0
        return index_language

    def getStream(self):
        index_stream = beradio.cast_integer(self.stream)
        try:
            mystream = beradio.streams[index_stream]
        except IndexError:
            plugin.log.info('stream setting: '+self.stream+' is not in our list, assuming '+beradio.streams[0])
            index_stream = 0
        return index_stream
