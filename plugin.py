###
# coding: utf-8
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
###

import re
from supybot.commands import *
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
import htmlentitydefs
import supybot.utils as utils

_titleRE = re.compile(r'<title>([^<]+)</title>', re.I)
_authorRE = re.compile(r'<author_name>([^<]+)</author_name>', re.I)
_entityRE = re.compile(r'&(\w+?);')


def descape_entity(m, entities=htmlentitydefs.entitydefs):
    # callback: translate one entity to its character value
    try:
        return entities[m.group(1)]
    except KeyError:
        return m.group(0)  # use as is


def descape(string):
    return _entityRE.sub(descape_entity, string)


def GetYTinfo(videoID):
    # TODO: switch to using API to be able to get duration
    try:
        text = utils.web.getUrl(
            'http://www.youtube.com/oembed?url='
            'https://www.youtube.com/watch?v={}&format=xml'.format(videoID))
        response = []
        m = _titleRE.search(text)
        response.append('{}'.format(ircutils.bold(m.group(1))))
        m = _authorRE.search(text)
        response.append(' by: {}'.format(ircutils.bold(m.group(1))))

        return descape(''.join(response))
    except utils.web.Error, e:
        e = str(e)
        e += ' - failed to get YT info from videoID {}'.format(videoID)
        return e


class YouTube(callbacks.PluginRegexp):
    """the YouTube plugin snarfs the messages for a URL pointing to a youtube
    video and then responds with the title and uploader name """
    # what subs implement a snarfer
    regexps = ['parseURL']

    # noinspection PyIncorrectDocstring,PyUnusedLocal
    @urlSnarfer
    def parseURL(self, irc, msg, match):
        r"""(?:https?://)?(?:www.youtube.com/watch"""\
          r'(?:/|\?(?:[^?]*&)?v=)|youtu.be/)([-_a-zA-Z0-9]+)'
        videoID = match.group(1)
        videoInfo = GetYTinfo(videoID)
        irc.reply('YouTube - {}'.format(videoInfo))

    # noinspection PyIncorrectDocstring,PyUnusedLocal,PyMethodMayBeStatic
    def youtube(self, irc, msg, args, videoID):
        """<videoID>
        
        Ask the bot to hand out the title and uploader of a youtube video"""
        videoInfo = GetYTinfo(videoID)
        irc.reply('{}'.format(videoInfo))
    youtube = wrap(youtube, ['somethingWithoutSpaces'])

Class = YouTube
# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
