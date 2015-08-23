#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_tools/license/LICENSE
#
##############################################################################
# Description
##############################################################################

"""
.. module:: pairings
   :platform: Unix
   :synopsis: Support classes for pairing interactions


This module provides classes and utilities for dealing with pairing style
interactions.
----

"""
##############################################################################
# Imports
##############################################################################

import rocon_console.console as console

##############################################################################
# Class
##############################################################################


class Pairing(object):
    """
    Represents a pairing, i.e. a launchable rapp configuration on the rocon
    app manager.
    """
    def __init__(self, msg):
        self.__dict__ = msg.__dict__
        self.msg = msg
        if not self.icon:
            # todo load default from rapp
            pass
        if not self.description:
            # todo load default from rapp
            pass

    def __str__(self):
        '''
          Format the interaction into a human-readable string.
        '''
        s = ''
        s += console.green + "%s" % self.name + console.reset + '\n'
        s += console.cyan + "  Rapp" + console.reset + "             : " + console.yellow + "%s" % str(self.rapp) + console.reset + '\n'  # noqa
        s += console.cyan + "  Icon" + console.reset + "             : " + console.yellow + "%s" % str(self.icon.resource_name) + console.reset + '\n'  # noqa
        s += console.cyan + "  Description" + console.reset + "      : " + console.yellow + "%s" % self.description + console.reset + '\n'  # noqa
        already_prefixed = False
        for remapping in self.remappings:
            if not already_prefixed:
                s += console.cyan + "    Remappings" + console.reset + " : " + console.yellow + "%s->%s" % (remapping.remap_from, remapping.remap_to) + console.reset + '\n'  # noqa
                already_prefixed = True
            else:
                s += "               : " + console.yellow + "%s->%s" % (remapping.remap_from, remapping.remap_to) + console.reset + '\n'  # noqa
        already_prefixed = False
        for pair in self.parameters:
            if not already_prefixed:
                s += console.cyan + "    Parameters" + console.reset + " : " + console.yellow + "%s-%s" % (pair.key, pair.value) + console.reset + '\n'  # noqa
                already_prefixed = True
            else:
                s += "               : " + console.yellow + "%s-%s" % (pair.key, pair.value) + console.reset + '\n'  # noqa
        return s


class RuntimePairingSignature(object):
    """
    Signature identifying a runtime pairing interaction.

    :ivar interaction: the interaction
    :vartype interaction: rocon_interactions.interactions.Interaction
    :ivar remocon_name: name of the remocon that initiated the pairing interaction
    :vartype remocon_name: str
    """
    def __init__(self, interaction, remocon_name):
        self.interaction = interaction
        self.remocon_name = remocon_name

    def __str__(self):
        s = ""
        s += console.green + "%s" % self.interaction.display_name + console.reset + "-"
        s += console.cyan + "%s" % self.interaction.pairing.rapp + console.reset + "-"
        s += console.yellow + "%s" % self.remocon_name + console.reset
        return s
