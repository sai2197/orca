#!/usr/bin/python

"""Test of line navigation on a page with a simple form."""

from macaroon.playback import *
import utils

sequence = MacroSequence()

sequence.append(KeyComboAction("<Control>Home"))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "1. line Down",
    ["BRAILLE LINE:  'Magic disappearing text trick:  $l'",
     "     VISIBLE:  'Magic disappearing text trick:  ', cursor=1",
     "SPEECH OUTPUT: 'Magic disappearing text trick: '",
     "SPEECH OUTPUT: 'entry'",
     "SPEECH OUTPUT: 'tab to me and I disappear'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "2. line Down",
    ["BRAILLE LINE:  'Tell me a secret:  $l'",
     "     VISIBLE:  'Tell me a secret:  $l', cursor=1",
     "SPEECH OUTPUT: 'Tell me a secret: '",
     "SPEECH OUTPUT: 'password text'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "3. line Down",
    ["BRAILLE LINE:  'Tell me a little more about yourself:      $l'",
     "     VISIBLE:  'Tell me a little more about your', cursor=1",
     "SPEECH OUTPUT: 'Tell me a little more about yourself:",
     "'",
     "SPEECH OUTPUT: 'entry'",
     "SPEECH OUTPUT: '     '"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "4. line Down",
    ["KNOWN ISSUE: Something is causing us to keep presenting the field",
     "BRAILLE LINE:  'Tell me a little more about yourself: I am a monkey with a long tail.  I like  $l'",
     "     VISIBLE:  'I am a monkey with a long tail. ', cursor=1",
     "SPEECH OUTPUT: 'Tell me a little more about yourself:",
     "'",
     "SPEECH OUTPUT: 'entry'",
     "SPEECH OUTPUT: 'I am a monkey with a long tail.  I like '"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "5. line Down",
    ["BRAILLE LINE:  'Tell me a little more about yourself: to swing from trees and eat bananas.   $l'",
     "     VISIBLE:  'to swing from trees and eat bana', cursor=1",
     "SPEECH OUTPUT: 'Tell me a little more about yourself:",
     "'",
     "SPEECH OUTPUT: 'Tell me a little more about yourself:'",
     "SPEECH OUTPUT: 'entry'",
     "SPEECH OUTPUT: 'to swing from trees and eat bananas.  '"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "6. line Down",
    ["BRAILLE LINE:  'Tell me a little more about yourself: I've recently taken up typing and plan  $l'",
     "     VISIBLE:  'I've recently taken up typing an', cursor=1",
     "SPEECH OUTPUT: 'Tell me a little more about yourself:",
     "'",
     "SPEECH OUTPUT: 'Tell me a little more about yourself:'",
     "SPEECH OUTPUT: 'entry'",
     "SPEECH OUTPUT: 'I've recently taken up typing and plan '"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "7. line Down",
    ["BRAILLE LINE:  'Tell me a little more about yourself: to write my memoirs. $l'",
     "     VISIBLE:  'to write my memoirs. $l', cursor=1",
     "SPEECH OUTPUT: 'Tell me a little more about yourself:",
     "'",
     "SPEECH OUTPUT: 'Tell me a little more about yourself:'",
     "SPEECH OUTPUT: 'entry'",
     "SPEECH OUTPUT: 'to write my memoirs.'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "8. line Down",
    ["BRAILLE LINE:  'Tell me a little more about yourself:      $l'",
     "     VISIBLE:  '      $l', cursor=1",
     "SPEECH OUTPUT: 'Tell me a little more about yourself:",
     "'",
     "SPEECH OUTPUT: 'Tell me a little more about yourself:'",
     "SPEECH OUTPUT: 'entry'",
     "SPEECH OUTPUT: '     '"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "9. line Down",
    ["BRAILLE LINE:  'Check one or more: < > Red check box < > Blue check box < > Green check box'",
     "     VISIBLE:  'Check one or more: < > Red check', cursor=1",
     "SPEECH OUTPUT: 'Check one or more: '",
     "SPEECH OUTPUT: 'Red'",
     "SPEECH OUTPUT: 'check box'",
     "SPEECH OUTPUT: 'not checked'",
     "SPEECH OUTPUT: 'Blue'",
     "SPEECH OUTPUT: 'check box'",
     "SPEECH OUTPUT: 'not checked'",
     "SPEECH OUTPUT: 'Green'",
     "SPEECH OUTPUT: 'check box'",
     "SPEECH OUTPUT: 'not checked'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "10. line Down",
    ["BRAILLE LINE:  'Make a selection: Water combo box'",
     "     VISIBLE:  'Make a selection: Water combo bo', cursor=1",
     "SPEECH OUTPUT: 'Make a selection: '",
     "SPEECH OUTPUT: 'Water'",
     "SPEECH OUTPUT: 'combo box'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "11. line Down",
    ["KNOWN ISSUE: It seems that we're repeating this widget.",
     "BRAILLE LINE:  'Which sports do you like?Hockey list box'",
     "     VISIBLE:  'Which sports do you like?Hockey ', cursor=1",
     "SPEECH OUTPUT: 'Which sports do you like?",
     "'",
     "SPEECH OUTPUT: 'Which sports do you like?'",
     "SPEECH OUTPUT: 'Hockey'",
     "SPEECH OUTPUT: 'multi-select'",
     "SPEECH OUTPUT: 'List with 4 items'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "12. line Down",
    ["BRAILLE LINE:  'Hockey list box'",
     "     VISIBLE:  'Hockey list box', cursor=1",
     "SPEECH OUTPUT: 'Which sports do you like?'",
     "SPEECH OUTPUT: 'Hockey'",
     "SPEECH OUTPUT: 'multi-select'",
     "SPEECH OUTPUT: 'List with 4 items'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "13. line Down",
    ["BRAILLE LINE:  'Dashing picture of Willie Walker image'",
     "     VISIBLE:  'Dashing picture of Willie Walker', cursor=1",
     "SPEECH OUTPUT: 'Dashing picture of Willie Walker'",
     "SPEECH OUTPUT: 'image'",
     "SPEECH OUTPUT: '",
     "'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "14. line Down",
    ["BRAILLE LINE:  'Ain't he handsome (please say yes)? & y radio button Yes & y radio button No'",
     "     VISIBLE:  'Ain't he handsome (please say ye', cursor=1",
     "SPEECH OUTPUT: 'Ain't he handsome (please say yes)? '",
     "SPEECH OUTPUT: 'not selected'",
     "SPEECH OUTPUT: 'radio button'",
     "SPEECH OUTPUT: 'Yes '",
     "SPEECH OUTPUT: 'not selected'",
     "SPEECH OUTPUT: 'radio button'",
     "SPEECH OUTPUT: 'No '"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Up"))
sequence.append(utils.AssertPresentationAction(
    "15. line Up",
    ["BRAILLE LINE:  'Dashing picture of Willie Walker image'",
     "     VISIBLE:  'Dashing picture of Willie Walker', cursor=1",
     "SPEECH OUTPUT: 'Dashing picture of Willie Walker'",
     "SPEECH OUTPUT: 'image'",
     "SPEECH OUTPUT: '",
     "'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Up"))
sequence.append(utils.AssertPresentationAction(
    "16. line Up",
    ["BRAILLE LINE:  'Hockey list box'",
     "     VISIBLE:  'Hockey list box', cursor=1",
     "SPEECH OUTPUT: 'Which sports do you like?'",
     "SPEECH OUTPUT: 'Hockey'",
     "SPEECH OUTPUT: 'multi-select'",
     "SPEECH OUTPUT: 'List with 4 items'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Up"))
sequence.append(utils.AssertPresentationAction(
    "17. line Up",
    ["BRAILLE LINE:  'Which sports do you like?Hockey list box'",
     "     VISIBLE:  'Which sports do you like?Hockey ', cursor=1",
     "SPEECH OUTPUT: 'Which sports do you like?",
     "'",
     "SPEECH OUTPUT: 'Which sports do you like?'",
     "SPEECH OUTPUT: 'Hockey'",
     "SPEECH OUTPUT: 'multi-select'",
     "SPEECH OUTPUT: 'List with 4 items'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Up"))
sequence.append(utils.AssertPresentationAction(
    "18. line Up",
    ["BRAILLE LINE:  'Make a selection: Water combo box'",
     "     VISIBLE:  'Make a selection: Water combo bo', cursor=1",
     "SPEECH OUTPUT: 'Make a selection: '",
     "SPEECH OUTPUT: 'Water'",
     "SPEECH OUTPUT: 'combo box'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Up"))
sequence.append(utils.AssertPresentationAction(
    "19. line Up",
    ["BRAILLE LINE:  'Check one or more: < > Red check box < > Blue check box < > Green check box'",
     "     VISIBLE:  'Check one or more: < > Red check', cursor=1",
     "SPEECH OUTPUT: 'Check one or more: '",
     "SPEECH OUTPUT: 'Red'",
     "SPEECH OUTPUT: 'check box'",
     "SPEECH OUTPUT: 'not checked'",
     "SPEECH OUTPUT: 'Blue'",
     "SPEECH OUTPUT: 'check box'",
     "SPEECH OUTPUT: 'not checked'",
     "SPEECH OUTPUT: 'Green'",
     "SPEECH OUTPUT: 'check box'",
     "SPEECH OUTPUT: 'not checked'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Up"))
sequence.append(utils.AssertPresentationAction(
    "20. line Up",
    ["KNOWN ISSUE: Why aren't we speaking this? Ditto for the next few items.",
     "BRAILLE LINE:  '      $l'",
     "     VISIBLE:  '      $l', cursor=1"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Up"))
sequence.append(utils.AssertPresentationAction(
    "21. line Up",
    ["BRAILLE LINE:  'to write my memoirs. $l'",
     "     VISIBLE:  'to write my memoirs. $l', cursor=1"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Up"))
sequence.append(utils.AssertPresentationAction(
    "22. line Up",
    ["BRAILLE LINE:  'I've recently taken up typing and plan  $l'",
     "     VISIBLE:  'I've recently taken up typing an', cursor=1"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Up"))
sequence.append(utils.AssertPresentationAction(
    "23. line Up",
    ["BRAILLE LINE:  'to swing from trees and eat bananas.   $l'",
     "     VISIBLE:  'to swing from trees and eat bana', cursor=1"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Up"))
sequence.append(utils.AssertPresentationAction(
    "24. line Up",
    ["BRAILLE LINE:  'I am a monkey with a long tail.  I like  $l'",
     "     VISIBLE:  'I am a monkey with a long tail. ', cursor=1"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Up"))
sequence.append(utils.AssertPresentationAction(
    "25. line Up",
    ["BRAILLE LINE:  'Tell me a little more about yourself:      $l'",
     "     VISIBLE:  'Tell me a little more about your', cursor=1",
     "SPEECH OUTPUT: 'Tell me a little more about yourself:",
     "'",
     "SPEECH OUTPUT: 'Tell me a little more about yourself:'",
     "SPEECH OUTPUT: 'entry'",
     "SPEECH OUTPUT: '     '"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Up"))
sequence.append(utils.AssertPresentationAction(
    "26. line Up",
    ["BRAILLE LINE:  'Tell me a secret:  $l'",
     "     VISIBLE:  'Tell me a secret:  $l', cursor=1",
     "SPEECH OUTPUT: 'Tell me a secret: '",
     "SPEECH OUTPUT: 'password text'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Up"))
sequence.append(utils.AssertPresentationAction(
    "27. line Up",
    ["BRAILLE LINE:  'Magic disappearing text trick: tab to me and I disappear $l'",
     "     VISIBLE:  'Magic disappearing text trick: t', cursor=1",
     "SPEECH OUTPUT: 'Magic disappearing text trick: '",
     "SPEECH OUTPUT: 'entry'",
     "SPEECH OUTPUT: 'tab to me and I disappear'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Up"))
sequence.append(utils.AssertPresentationAction(
    "28. line Up",
    ["BRAILLE LINE:  'Type something here:  $l'",
     "     VISIBLE:  'Type something here:  $l', cursor=1",
     "SPEECH OUTPUT: 'Type something here: '",
     "SPEECH OUTPUT: 'entry'"]))

sequence.append(utils.AssertionSummaryAction())
sequence.start()
