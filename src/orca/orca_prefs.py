# Orca
#
# Copyright 2004-2007 Sun Microsystems Inc.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Library General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Library General Public License for more details.
#
# You should have received a copy of the GNU Library General Public
# License along with this library; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.

"""Common utilities to manage the writing of the user preferences file."""

__id__        = "$Id$"
__version__   = "$Revision$"
__date__      = "$Date$"
__copyright__ = "Copyright (c) 2005-2007 Sun Microsystems Inc."
__license__   = "LGPL"

import os
import commands
import pprint
import settings

from orca_i18n import _  # for gettext support

# The same fields than in orca_gui_prefs.py:
(HANDLER, DESCRIP, MOD_MASK1, MOD_USED1, KEY1, TEXT1, MOD_MASK2, MOD_USED2, KEY2, TEXT2, MODIF, EDITABLE) = range(12)

def _createDir(dirname):
    """Creates the given directory if it doesn't already exist.
    """
    try:
        os.chdir(dirname)
    except:
        os.mkdir(dirname)

def _writePreferencesPreamble(prefs):
    """Writes the preamble to the user-settings.py file."""

    prefs.writelines("# user-settings.py - custom Orca settings\n")
    prefs.writelines("# Generated by orca.  DO NOT EDIT THIS FILE!!!\n")
    prefs.writelines("# If you want permanent customizations that will not\n")
    prefs.writelines("# be overwritten, edit orca-customizations.py.\n")
    prefs.writelines("#\n")
    prefs.writelines("import re\n")
    prefs.writelines("import time\n")
    prefs.writelines("\n")
    prefs.writelines("import orca.debug\n")
    prefs.writelines("import orca.settings\n")
    prefs.writelines("import orca.acss\n")
    prefs.writelines("\n")
    prefs.writelines("# Set the logging level to INFO if you want to log\n")
    prefs.writelines("# Orca's output of speech and braille using the\n")
    prefs.writelines("# Python logging API.  Note that setting the\n")
    prefs.writelines("# orca.debug.debugLevel to orca.debug.LEVEL_INFO\n")
    prefs.writelines("# will output the same information using Orca's\n")
    prefs.writelines("# debug facility.\n")
    prefs.writelines("#\n")
    prefs.writelines("# import logging\n")
    prefs.writelines("# orca.debug.log.setLevel(logging.INFO)\n")
    prefs.writelines("\n")

    prefs.writelines("#orca.debug.debugLevel = orca.debug.LEVEL_OFF\n")
    prefs.writelines("orca.debug.debugLevel = orca.debug.LEVEL_SEVERE\n")
    prefs.writelines("#orca.debug.debugLevel = orca.debug.LEVEL_WARNING\n")
    prefs.writelines("#orca.debug.debugLevel = orca.debug.LEVEL_INFO\n")
    prefs.writelines("#orca.debug.debugLevel = orca.debug.LEVEL_CONFIGURATION\n")
    prefs.writelines("#orca.debug.debugLevel = orca.debug.LEVEL_FINE\n")
    prefs.writelines("#orca.debug.debugLevel = orca.debug.LEVEL_FINER\n")
    prefs.writelines("#orca.debug.debugLevel = orca.debug.LEVEL_FINEST\n")
    prefs.writelines("#orca.debug.debugLevel = orca.debug.LEVEL_ALL\n")
    prefs.writelines("\n")
    prefs.writelines("#orca.debug.eventDebugLevel = orca.debug.LEVEL_OFF\n")
    prefs.writelines("#orca.debug.eventDebugFilter =  None\n")
    prefs.writelines("#orca.debug.eventDebugFilter = re.compile('[\S]*focus|[\S]*activ')\n")
    prefs.writelines("#orca.debug.eventDebugFilter = re.compile('nomatch')\n")
    prefs.writelines("#orca.debug.eventDebugFilter = re.compile('[\S]*:accessible-name')\n")
    prefs.writelines("#orca.debug.eventDebugFilter = re.compile('[\S]*:(?!bounds-changed')\n")

    prefs.writelines("\n")

    prefs.writelines("#orca.debug.debugFile = open(time.strftime('debug-%Y-%m-%d-%H:%M:%S.out'), 'w', 0)\n")
    prefs.writelines("#orca.debug.debugFile = open('debug.out', 'w', 0)\n")
    prefs.writelines("\n")

    prefs.writelines("#orca.settings.useBonoboMain=False\n")
    prefs.writelines("#orca.settings.debugEventQueue=True\n")
    prefs.writelines("#orca.settings.gilSleepTime=0\n")
    prefs.writelines("\n")

    prefs.writelines("if False:\n")
    prefs.writelines("    import sys\n")
    prefs.writelines("    import orca.util\n")
    prefs.writelines("    sys.settrace(orca.util.traceit)\n")
    prefs.writelines("    orca.debug.debugLevel = orca.debug.LEVEL_ALL\n")
    prefs.writelines("\n")

def _writePreferencesPostamble(prefs):
    """Writes the postamble to the user-settings.py file."""
    prefs.writelines("\ntry:\n")
    prefs.writelines("    __import__(\"orca-customizations\")\n")
    prefs.writelines("except ImportError:\n")
    prefs.writelines("    pass\n")

def _enableAccessibility():
    """Enables the GNOME accessibility flag.  Users need to log out and
    then back in for this to take effect.

    Returns True if an action was taken (i.e., accessibility was not
    set prior to this call).
    """

    alreadyEnabled = commands.getoutput(\
        "gconftool-2 --get /desktop/gnome/interface/accessibility")
    if alreadyEnabled != "true":
        os.system("gconftool-2 --type bool --set " \
                  + "/desktop/gnome/interface/accessibility true")

    return alreadyEnabled != "true"

def _getDisplayString(display):
    """Returns a string that represents the source or taget magnifier display.

    Arguments:
    - display: the magnifier source or taget display string.

    Returns a string suitable for the preferences file.
    """

    if not display:
        return "''"
    else:
        return "'%s'" % display

def _getSpeechServerFactoryString(factory):
    """Returns a string that represents the speech server factory passed in.

    Arguments:
    - factory: the speech server factory

    Returns a string suitable for the preferences file.
    """

    if not factory:
        return None
    elif isinstance(factory, basestring):
        return "'%s'" % factory
    else:
        return "'%s'" % factory.__name__

def _getSpeechServerString(server):
    """Returns a string that represents the speech server passed in.

    Arguments:
    - server: a speech server

    Returns a string suitable for the preferences file.
    """
    if not server:
        return None
    elif isinstance(server, [].__class__):
        return repr(server)
    else:
        return repr(server.getInfo())

def _getVoicesString(voices):
    """Returns a string that represents the list of voices passed in.

    Arguments:
    - voices: a list of ACSS instances.

    Returns a string suitable for the preferences file.
    """

    voicesStr = "{\n"
    for voice in voices:
        voicesStr += "'%s' : orca.acss.ACSS(" % voice
        voicesStr += pprint.pformat(voices[voice]) + "),\n"
    voicesStr += "}"

    return voicesStr

def _getKeyboardLayoutString(keyboardLayout):
    """Returns a string that represents the keyboard layout passed in."""

    if keyboardLayout == settings.GENERAL_KEYBOARD_LAYOUT_DESKTOP:
        return "orca.settings.GENERAL_KEYBOARD_LAYOUT_DESKTOP"
    else:
        return "orca.settings.GENERAL_KEYBOARD_LAYOUT_LAPTOP"

def _getOrcaModifierKeysString(orcaModifierKeys):
    """Returns a string that represents the Orca modifier keys passed in."""

    if orcaModifierKeys == settings.DESKTOP_MODIFIER_KEYS:
        return "orca.settings.DESKTOP_MODIFIER_KEYS"
    else:
        return "orca.settings.LAPTOP_MODIFIER_KEYS"

def _getVerbosityString(verbosityLevel):
    """Returns a string that represents the verbosity level passed in."""
    if verbosityLevel == settings.VERBOSITY_LEVEL_BRIEF:
        return "orca.settings.VERBOSITY_LEVEL_BRIEF"
    elif verbosityLevel == settings.VERBOSITY_LEVEL_VERBOSE:
        return "orca.settings.VERBOSITY_LEVEL_VERBOSE"
    else:
        return "orca.settings.VERBOSITY_LEVEL_VERBOSE"

def _getBrailleRolenameStyleString(rolenameStyle):
    """Returns a string that represents the rolename style passed in."""
    if rolenameStyle == settings.BRAILLE_ROLENAME_STYLE_SHORT:
        return "orca.settings.BRAILLE_ROLENAME_STYLE_SHORT"
    elif rolenameStyle == settings.BRAILLE_ROLENAME_STYLE_LONG:
        return "orca.settings.BRAILLE_ROLENAME_STYLE_LONG"
    else:
        return "orca.settings.BRAILLE_ROLENAME_STYLE_LONG"

def _getVerbalizePunctuationStyleString(punctuationStyle):
    """Returns a string that represents the punctuation style passed in."""
    if punctuationStyle == settings.PUNCTUATION_STYLE_NONE:
        return "orca.settings.PUNCTUATION_STYLE_NONE"
    elif punctuationStyle == settings.PUNCTUATION_STYLE_SOME:
        return "orca.settings.PUNCTUATION_STYLE_SOME"
    elif punctuationStyle == settings.PUNCTUATION_STYLE_MOST:
        return "orca.settings.PUNCTUATION_STYLE_MOST"
    elif punctuationStyle == settings.PUNCTUATION_STYLE_ALL:
        return "orca.settings.PUNCTUATION_STYLE_ALL"
    else:
        return "orca.settings.PUNCTUATION_STYLE_ALL"

def _getMagCursorColorString(cursorColor):
    """Returns a string that represents the magnification cursor color
    passed in.

    Arguments:
    - cursorColor: magnification cursor color

    Returns a string suitable for the preferences file.
    """

    cursorColorStr = "'%s'" % cursorColor

    return cursorColorStr

def _getMagSmoothingModeString(smoothingMode):
    """Returns a string that represents the magnification smoothing mode
    passed in.

    Arguments:
    - smoothingMode: magnification smoothing mode.

    Returns a string suitable for the preferences file.
    """

    if smoothingMode == settings.MAG_SMOOTHING_MODE_BILINEAR:
        return "orca.settings.MAG_SMOOTHING_MODE_BILINEAR"
    elif smoothingMode == settings.MAG_SMOOTHING_MODE_NONE:
        return "orca.settings.MAG_SMOOTHING_MODE_NONE"
    else:
        return "orca.settings.MAG_SMOOTHING_MODE_BILINEAR"

def _getMagMouseTrackingModeString(mouseTrackingMode):
    """Returns a string that represents the magnification mouse tracking
    mode passed in.

    Arguments:
    - mouseTrackingMode: magnification mouse tracking mode.

    Returns a string suitable for the preferences file.
    """

    if mouseTrackingMode == settings.MAG_MOUSE_TRACKING_MODE_CENTERED:
        return "orca.settings.MAG_MOUSE_TRACKING_MODE_CENTERED"
    elif mouseTrackingMode == settings.MAG_MOUSE_TRACKING_MODE_NONE:
        return "orca.settings.MAG_MOUSE_TRACKING_MODE_NONE"
    elif mouseTrackingMode == settings.MAG_MOUSE_TRACKING_MODE_PROPORTIONAL:
        return "orca.settings.MAG_MOUSE_TRACKING_MODE_PROPORTIONAL"
    elif mouseTrackingMode == settings.MAG_MOUSE_TRACKING_MODE_PUSH:
        return "orca.settings.MAG_MOUSE_TRACKING_MODE_PUSH"
    else:
        return "orca.settings.MAG_MOUSE_TRACKING_MODE_CENTERED"

def _writeKeyBindingsPreamble(prefs):
    """Writes the preamble to the user-settings.py keyBindings section."""

    prefs.writelines("\n")
    prefs.writelines("# Set up a user key-bindings profile\n")
    prefs.writelines("#\n")
    prefs.writelines('def overrideKeyBindings(script, keyB):\n')

    return

def _writeKeyBinding(prefs, tupl):
    """Writes a single keyBinding to the user-settings.py keyBindings section.

    Arguments:
    - prefs: text string - file to write the key binding to.
    - tupl:    tuple     - a tuple with the values of the
                             keybinding (gtk.TreeStore model columns)
    """

    prefs.writelines("   keyB.removeByHandler(script.inputEventHandlers['"+str(tupl[HANDLER])+"'])\n")

    if (tupl[TEXT1]):
        prefs.writelines("   keyB.add(orca.keybindings.KeyBinding(\n")
        prefs.writelines("      '" + str(tupl[KEY1]) + "',\n")
        if tupl[MOD_MASK1] or tupl[MOD_USED1]:
            prefs.writelines("      " + str(tupl[MOD_MASK1]) + ",\n")
            prefs.writelines("      " + str(tupl[MOD_USED1]) + ",\n")
        else:
            prefs.writelines("      0,\n")
            prefs.writelines("      0,\n")
        prefs.writelines('      script.inputEventHandlers["'+ str(tupl[HANDLER]) +'"]))\n\n')

    if (tupl[TEXT2]):
        prefs.writelines("   keyB.add(orca.keybindings.KeyBinding(\n")
        prefs.writelines("      '" + str(tupl[KEY2]) + "',\n")
        if tupl[MOD_MASK2] or tupl[MOD_USED2]:
            prefs.writelines("      " + str(tupl[MOD_MASK2]) + ",\n")
            prefs.writelines("      " + str(tupl[MOD_USED2]) + ",\n")
        else:
            prefs.writelines("      0,\n")
            prefs.writelines("      0,\n")
        prefs.writelines('      script.inputEventHandlers["'+ str(tupl[HANDLER]) +'"]))\n\n')
    return

def _writeKeyBindingsPostamble(prefs):
    """Writes the postamble to the user-settings.py keyBindings section."""

    prefs.writelines('   return keyB')
    prefs.writelines("\n\n")
    prefs.writelines('orca.settings.overrideKeyBindings = overrideKeyBindings')
    prefs.writelines("\n")
    return

def _writeKeyBindingsMap(prefs, treeModel):
    """Write to configuration file 'prefs' the key bindings passed in the
    model treeModel.
    """

    _writeKeyBindingsPreamble(prefs)

    iter = treeModel.get_iter_first()
    while iter != None:
        iterChild = treeModel.iter_children(iter)
        while iterChild != None:
            values = treeModel.get(iterChild, 0,1,2,3,4,5,6,7,8,9,10,11)
            if values[MODIF]:
                _writeKeyBinding(prefs, values)
            iterChild = treeModel.iter_next(iterChild)
        iter = treeModel.iter_next(iter)

    _writeKeyBindingsPostamble(prefs)

    return

def readPreferences():
    """Returns a dictionary containing the names and values of the
    customizable features of Orca."""

    prefsDict = {}
    for key in settings.userCustomizableSettings:
        if settings.__dict__.has_key(key):
            prefsDict[key] = settings.__dict__[key]

    return prefsDict

def writePreferences(prefsDict, treeModel=None):
    """Creates the directory and files to hold user preferences.  Note
    that callers of this method may want to consider using an ordered
    dictionary so that the keys are output in a deterministic order.

    Arguments:
    - prefsDict: a dictionary where the keys are orca preferences
    names and the values are the values for the preferences.

    Returns True if accessibility was enabled as a result of this
    call."""

    # Set up the user's preferences directory (~/.orca by default).
    #
    orcaDir = settings.userPrefsDir
    _createDir(orcaDir)

    # Set up ~/.orca/orca-scripts as a Python package
    #
    orcaScriptDir = os.path.join(orcaDir, "orca-scripts")
    _createDir(orcaScriptDir)
    initFile = os.path.join(orcaScriptDir, "__init__.py")
    if not os.path.exists(initFile):
        os.close(os.open(initFile, os.O_CREAT, 0700))

    # Set up ~/.orca/app-settings as a Python package.
    #
    orcaSettingsDir = os.path.join(orcaDir, "app-settings")
    _createDir(orcaSettingsDir)
    initFile = os.path.join(orcaSettingsDir, "__init__.py")
    if not os.path.exists(initFile):
        os.close(os.open(initFile, os.O_CREAT, 0700))

    # Write ~/.orca/user-settings.py
    #
    prefs = open(os.path.join(orcaDir, "user-settings.py"), "w")
    _writePreferencesPreamble(prefs)
    for key in settings.userCustomizableSettings:
        if prefsDict.has_key(key):
            if key == "voices":
                value = _getVoicesString(prefsDict[key])
            elif key == "speechServerInfo":
                value = _getSpeechServerString(prefsDict[key])
            elif key == "speechServerFactory":
                value = _getSpeechServerFactoryString(prefsDict[key])
            elif key.endswith("VerbosityLevel"):
                value = _getVerbosityString(prefsDict[key])
            elif key == "brailleRolenameStyle":
                value = _getBrailleRolenameStyleString(prefsDict[key])
            elif key == "verbalizePunctuationStyle":
                value = _getVerbalizePunctuationStyleString(prefsDict[key])
            elif key == "magCursorColor":
                value = _getMagCursorColorString(prefsDict[key])
            elif key == "magSmoothingMode":
                value = _getMagSmoothingModeString(prefsDict[key])
            elif key == "magMouseTrackingMode":
                value = _getMagMouseTrackingModeString(prefsDict[key])
            elif key == "magSourceDisplay" or key == "magTargetDisplay":
                value = _getDisplayString(prefsDict[key])
            elif key == "keyboardLayout":
                value = _getKeyboardLayoutString(prefsDict[key])
            elif key == "orcaModifierKeys":
                value = _getOrcaModifierKeysString(prefsDict[key])
            else:
                value = prefsDict[key]
            prefs.writelines("orca.settings.%s = %s\n" % (key, value))

    if treeModel:
        _writeKeyBindingsMap(prefs, treeModel)

    _writePreferencesPostamble(prefs)
    prefs.close()

    # Return True if this caused accessibility to be enabled
    # as a result of this call.
    #
    return _enableAccessibility()