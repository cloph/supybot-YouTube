###
# coding: utf-8
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
###

from supybot.test import *


class YouTubeTestCase(ChannelPluginTestCase):
    plugins = ('YouTube',)

    sampleVidID = 'zFAS7jPwPKk'
    sampleVidAuthor = 'Sick Dom'
    sampleVidTitle = '[NA] World 1st Vale Guardian - Scrapper Tank Gameplay'
    expectedResponse = 'YouTube - {} by: {}'.format(
        ircutils.bold(sampleVidTitle), ircutils.bold(sampleVidAuthor))

    if network:
        def testWatchSlash(self):
            self.assertSnarfResponse(
                'bla https://www.youtube.com/watch/{} bla'.format(
                    self.sampleVidID), self.expectedResponse)

        def testWatchQuery(self):
            # ok to forget space between URL and link
            self.assertSnarfResponse(
                'lahttps://www.youtube.com/watch?v={} bla'.format(
                    self.sampleVidID), self.expectedResponse)
            self.assertSnarfResponse(
                'ba www.youtube.com/watch?playlist=whatever&v={} bla'.format(
                    self.sampleVidID), self.expectedResponse)

        def testShort(self):
            self.assertSnarfNoResponse('bla on youtu.be something')
            self.assertSnarfResponse(
                'bla bla https://youtu.be/{} bla bla'.format(
                    self.sampleVidID), self.expectedResponse)

        def testCommand(self):
            self.assertResponse('youtube zFAS7jPwPKk', '{} by: {}'.format(
                ircutils.bold(self.sampleVidTitle),
                ircutils.bold(self.sampleVidAuthor)))

    def testInvalidCommands(self):
        self.assertSnarfNoResponse('bla on youtu.be something')
        self.assertSnarfNoResponse('bla on youtube.com/watch')
        self.assertHelp('youtube')
        self.assertHelp('youtube bla 1')
# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
