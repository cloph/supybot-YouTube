###
# coding: utf-8
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
###

"""
Fetches title of youtube videos when a youtube link is posted to a channel
"""

import supybot
import supybot.world as world
import config
import plugin
if world.testing:
    # noinspection PyUnresolvedReferences
    import test

# Use this for the version of this plugin.  You may wish to put a CVS keyword
# in here if you're keeping the plugin in CVS or some similar system.
__version__ = "1"

__author__ = supybot.Author('Christian Lohmaier', 'cloph',
                            'lohmaier+github@googlemail.com')

__contributors__ = {}

__url__ = 'https://github.com/cloph/supybot-YouTube'

reload(plugin)  # In case we're being reloaded.

Class = plugin.Class
configure = config.configure
# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
