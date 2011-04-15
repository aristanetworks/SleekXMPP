#!/usr/bin/env python
# Copyright (c) 2011 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

# XXX_AARONB: reindent file
import sys
import time
import Tac
from sleekxmpp.test import *

class TestMUC(SleekTest):
    """
    Test using the XEP-0045 plugin.
    """

    def tearDown(self):
        sys.excepthook = sys.__excepthook__
        self.stream_close()

    def testInvite(self):
       self.stream_start(mode='client',
                         jid='hecate@shakespear.lit',
                         plugins=['xep_0045'])
       happened = []
       def handle_invite(msg):
          happened.append(True)

       self.xmpp.add_event_handler("groupchat_invite", handle_invite)

       invite = """
<message
    from='darkcave@chat.shakespeare.lit'
    to='hecate@shakespeare.lit'>
  <x xmlns='http://jabber.org/protocol/muc#user'>
    <invite from='crone1@shakespeare.lit/desktop'>
      <reason>
        Hey Hecate, this is the place for all good witches!
      </reason>
    </invite>
    <password>cauldronburn</password>
  </x>
</message>
"""

       self.recv( invite )
       self.recv( invite )
       time.sleep(0.1)
       print happened
       self.failUnless(happened == [True, True],
                       "Invite handler was not triggered the correct number of times: %s")


suite = unittest.TestLoader().loadTestsFromTestCase(TestMUC)
