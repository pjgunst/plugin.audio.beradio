# xbmcswift2 to be replaced with kodiswift
# dependency: https://github.com/xbmc/repo-scripts/pull/197
from xbmcswift2 import Plugin
import xbmc
import xbmcaddon

# used globally
beradio_addon = xbmcaddon.Addon()
plugin = Plugin()
plugin_path=xbmc.translatePath(beradio_addon.getAddonInfo('path')).decode('utf-8')
languages = [ 'all', 'nl', 'fr', 'de' ]
streams = [ 'high', 'low' ]

# int() but with 0 as our default, as we're going to use it for list indices
def cast_integer(numstring):
    try:
        return int(numstring)
    except ValueError:
        plugin.log.error(numstring+' can not be cast to an integer')
        return 0
