#
# BigBrotherBot(B3) (www.bigbrotherbot.net)
# Copyright (C) 2005 Michael "ThorN" Thornton
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
#
# CHANGELOG
#
#   2014/06/21 - 1.30 - Courgette
#   * fix spam command not considering the loud command prefix (ie: &spam instead of !spam)
#   2014/05/16 - 1.29 - Courgette
#   * Add an optional parameter to the !spam command to allow to send a message to a given player in private
#   2014/05/03 - 1.28.1 - Fenix
#   * Tell player why he is not allowed to use a certain command (issue #183)
#   2014/05/02 - 1.28 - Fenix
#   * Make use of the new getCmd function from functions module
#   * Minor syntax fixes
#   2014/04/21 - 1.27 - 82ndab-Bravo17
#   * Change default messages to new format
#   2014/03/20 - 1.26 - Fenix
#   * make use of self._admins_level in acquireCmdLock() method instead of constant value
#   * refactored plugin syntax: get close to PEP8
#   * let the plugin use the new event dispatcher
#   2014/02/26 - 1.25.2 - Fenix
#   * changed findClientPrompt to return None instead of False when it finds multiple matches
#   * correctly initialize superadmins list: fix code unpredictability
#   2014/01/11 - 1.25.1 - Courgette
#   * fix maskLevel is set with group id while it should be group level
#   2014/01/07 - 1.25 - Courgette
#   * removed the 'peeing in the gene pool' reason for tempbans with durations between 5 and 10 min
#   2013/11/16 - 1.24 - Fenix
#   * added command !pluginfo (display plugin information)
#   2013/09/06 - 1.23.1 - Fenix
#   * make conf pm_global accept yes/no
#   2013/03/02 - 1.23 - Courgette
#   * command !admins message when no admin is online can be customised in the config file -> no_admins
#   2013/02/17 - 1.22 - Courgette
#   * warn_command_abusers default value is no False
#   * suggest command spelling correction in aa many situations as we can
#   * refactor code for detecting fakeCommands and unprivileged access to commands
#   * recognize commands in all chat types (all, team, squad, private)
#   2013/02/16 - 1.21.1 - Courgette
#   * add default messages
#   2013/02/10 - 1.21 - Ozon
#   * add announce_registration option to config to (de)activate public announcement of player using the !register
#     command
#   * !register command feedback message is now configurable in config. See regme_confirmation
#   2013/02/10 - 1.20 - Ozon
#   * add spell corrector for commands
#   2012/10/27 - 1.19 - Courgette
#   * change: !map command will give at most 5 suggestions
#   2012/10/03 - 1.18 - Courgette
#   * add command !lastbans
#   2012/09/29 - 1.17 - Courgette
#   * add command !regulars
#   2012/08/11 - 1.16 - Courgette
#   * config file can refer to group levels by their group keyword
#   2012/07/31 - 1.15.1 - Courgette
#   * fix command !maps when map rotation list is empty
#   2012/07/28 - 1.15 - Courgette
#   * add command !unreg (danger89's idea)
#   2012/07/14 - 1.14.1 - Courgette
#   * log more detail when failing to register a command
#   2012/07/07 - 1.14 - Courgette
#   * better error log messages when registering a command with incorrect level or group keyword
#   2012/07/05 - 1.13 - Courgette
#   * provides default values for warn_reason keywords 'default' and 'generic' if missing from config file
#   * refactors the loading and parsing of warn_reasons from the config file to provide meaningful messages when
#   * errors are detected
#   2012/07/02 - 1.12.2 - Courgette
#   * fix bug un cmd_mask when no player name was given
#   2012/06/17 - 1.12.1 - Courgette
#   * syntax
#   2012/04/15 - 1.12 - Courgette
#   * removes magic command shortcut that would transform the command '!1 blah' into '!say blah'
#   2011/11/15 - 1.11.4 - Courgette
#   * fix bug where command &rules was acting like !rules
#   2011/11/15 - 1.11.3 - Courgette
#   * fix bug xlr8or/big-brother-bot#54 - Plugin Admin: parseUserCommand issue
#   2011/11/15 - 1.11.2 - Courgette
#   * cmd_pause now uses console pause() and unpause() methods instead of sleep()
#   2011/11/05 - 1.11.1 - Courgette
#   * do not tell "There was an error processing your command" to the player if catch a SystemExit
#   2011/05/31 - 1.11.0 - Courgette
#   * refactoring
#   2011/04/30 - 1.10.3 - Courgette
#   * !help response won't include !register if already registered
#   2011/02/26 - 1.10.2 - Courgette
#   * fix doc for !spam command
#   2010/12/12 - 1.10.1 - Courgette
#   * registering a command can use group keywords instead of groups levels
#   2010/11/25 - 1.9.1 - Courgette
#   * calling a command of a disabled plugin now sends a message back to the user
#   2010/11/21 - 1.9 - Courgette
#   * cmd_map now suggests map names if provided by parser
#   2010/10/28 - 1.8.2 - Courgette
#   * make sure to disable the !iamgod command when used while there is already 
#     a superadmin in db.
#   2010/08/25 - 1.8.1 - Courgette
#   * do not fail if warn_command_abusers is missing in config
#   2010/08/24 - 1.8 - kikker916 & Courgette
#   * add warn_command_abusers setting what defines if player should get warned 
#     for trying to use non existing or privileged commands
#   * add documentation into the xml config file
#   * fix a few things with the config file
#   2010/08/14 - 1.7.1 - Courgette
#   * fix _parseUserCmdRE regexp for cases where the player's name start with a digit
#   2010/04/10 - 1.7 - Bakes
#   * new '&' command prefix can be used to say messages in the middle of the screen.
#     has the same settings as '@', this may change in the future.
#   2010/03/22 - 1.6.1 - Courgette
#   * resolve conflict regarding maprotate/rotateMap
#   2010/03/21 - 1.6 - Courgette
#    * make this plugin game independant by delegating the work to the parser for 
#      commands !map and !maprotate
#   2010/03/21 - 1.5 - Courgette
#    * removed commands : greeting, about, groups, cmdlevel, newgroup, delgroup, editgroup
#   3/21/2010 - 1.4.7 - Bakes
#    * moved the !ci command to the pingwatch plugin
#    * moved part of cmd_maprotate to the parser.
#   3/7/2010 - 1.4.6 - Courgette
#    * fix crash on bot startup when loading a plugin which does not requires any config
#      file but still registers commands
#   1/27/2010 - 1.4.5 - Courgette
#    * the iamgod check warns if the command is explicitly enabled by config file but
#      superadmins are found in database
#   1/27/2010 - 1.4.4 - xlr8or
#    * added some verbose info to startup()
#   9/1/2009 - 1.4.3 - xlr8or
#    * check database connection before checking groups
#   8/24/2009 - 1.4.2 - courgette
#    * warning messages are also sent by pm to the admin that give them
#   8/22/2009 - 1.4.1 - courgette
#    * warning messages are shown only to the warned player. This is to prevent the bot from spaming the console.
#   8/19/2009 - 1.4.0 - courgette
#    * penalizeClient() will try to delegate unknown penalty types to inflictCustomPenalty() of the current parser.
#      Requires parser.py v1.10+
#   7/22/2009 - 1.3.5 - xlr8or
#    Generate better documented error when groupstable is empty
#   10/05/2008 - 1.3.4b0 - mindriot
#      * Removed hard code of 1 day for long_tempban_level - now controlled with new setting 'long_tempban_max_duration'
#   8/29/2005 - 1.2.2 - ThorN
#    Moved pbss command to punkbuster plugin
#   8/13/2005 - 1.2.1 - ThorN
#    Added penalizeClient()
#    Moved greeting to welcome plugin
#   7/23/2005 - 1.1.0 - ThorN
#    Made it so registerCommand() will check a plugins config "commands" section for command level overrides
#    Added ci command
#    Added data field to warnClient(), warnKick(), and checkWarnKick()
#

__version__ = '1.30'
__author__ = 'ThorN, xlr8or, Courgette, Ozon, Fenix'

import re
import imp
import time
import threading
import sys
import traceback
import thread
import random
import copy
import b3.plugin

from b3 import functions
from b3.clients import Client, Group
from b3.functions import minutesStr
from b3.functions import getCmd
from ConfigParser import NoOptionError


# pylint: disable-msg=E1103
class AdminPlugin(b3.plugin.Plugin):

    _commands = {}

    _tkPlugin = None
    _parseUserCmdRE = re.compile(r"^(?P<cid>'[^']{2,}'|[0-9]+|[^\s]{2,}|@[0-9]+)(\s+(?P<parms>.*))?$")
    _long_tempban_max_duration = 1440  # 60m/h x 24h = 1440m = 1d
    _warn_command_abusers = None
    _announce_registration = True

    cmdPrefix = '!'
    cmdPrefixLoud = '@'
    cmdPrefixBig = '&'
    cmdPrefixPrivate = None

    PENALTY_KICK = 'kick'
    PENALTY_TEMPBAN = 'tempban'
    PENALTY_WARNING = 'warning'
    PENALTY_BAN = 'ban'

    warn_delay = 15
    warn_instant_kick_num = 5
    warn_alert_kick_num = 3
    warn_reasons = {}  # dict<warning keyword, tuple(warning duration in minute, warning reason)>

    _noreason_level = 80
    _long_tempban_level = 80
    _hidecmd_level = 80
    _admins_level = 20

    _default_messages = {
        "invalid_parameters": "^7Invalid parameters",
        "error_no_reason": "^1ERROR: ^7You must supply a reason",
        "action_denied_masked": "^7$name ^7is a masked higher level player, action cancelled",
        "baninfo": "^7$name ^7has $num_bans active bans",
        "baninfo_no_bans": "^7$name ^7has no active bans",
        "group_unknown": "^7Group $group_name does not exist",
        "group_beyond_reach": "^7Group $group_name is beyond your reach",
        "cleared_warnings": "$admin ^7has cleared $player ^ of all tk-points and warnings",
        "cleared_warnings_for_all": "$admin ^7has cleared $player ^7of all tk-points and warnings",
        "warn_too_fast": "^7Only one warning per $num_second seconds can be issued",
        "ban_denied": "^7Hey %s^7, you're no Elvis, can't ban %s",
        "help_available": "^7Available commands: %s",
        "temp_ban_self": "^7%s ^7Can't ban yourself newb",
        "groups_in": "^7%s^7 is in groups %s",
        "say": "^7%s^7: %s",
        "player_id": "^7%s [^2%s^7]",
        "seen": "^7%s ^7was last seen on %s",
        "help_no_command": "^7Command not found %s",
        "lookup_found": "^7[^2@%s^7] %s^7 [^3%s^7]",
        "kick_self": "^7%s ^7Can't kick yourself newb!",
        "groups_welcome": "^7You are now a %s",
        "warn_denied": "%s^7, %s^7 owns you, can't warn",
        "groups_already_in": "^7%s^7 is already in group %s",
        "temp_ban_denied": "^7Hey %s^7, you're no ^1Red ^7Elvis, can't temp ban %s",
        "players_matched": "^7Players matching %s %s",
        "ban_self": "^7%s ^7Can't ban yourself newb!",
        "regme_confirmation": "^7Thanks for your registration. You are now a member of the group %s",
        "regme_annouce": "^7%s ^7put in group %s",
        "kick_denied": "^7%s^7 gets 1 point, %s^7 gets none, %s^7 wins, can't kick",
        "no_players": "^7No players found matching %s",
        "spanked_reason": "%s ^7was ^1SPANKED^7 by %s ^7for %s",
        "groups_added": "^7%s ^7added to group %s",
        "groups_put": "^7%s ^7put in group %s",
        "groups_none": "^7%s^7 is not in any groups",
        "help_command": "^2%s%s ^7%s",
        "warn_self": "^7%s ^7Can't warn yourself newb!",
        "regme_regged": "^7You are now a %s",
        "help_none": "^7You have no available commands",
        "spanked": "%s ^7was ^1SPANKED^7 by %s",
        "admins": "^7Admins online: %s",
        "no_admins": "^7There are no admins online",
        "regulars": "^7Regular players online: %s",
        "no_regulars": "^7There are no regular players online",
        "time": "At the sound of the beep it will be ^3%s^7...(beeeep)",
        "unknown_command": "^7Unrecognized command %s",
        "leveltest": "^7%s ^7[^3@%s^7] is a ^3%s ^7[^2%s^7] since %s",
        "leveltest_nogroups": "^7%s ^7[^3@%s^7] is not in any groups",
        "aliases": "^7%s^7 aliases: %s",
        "aliases_more_suffix": "^7[^2and more^7]",
        "no_aliases": "^7%s^7 has no aliases",
        "cmd_plugin_disabled": "^7cannot execute command. Plugin disabled"
    }

    ####################################################################################################################
    ##                                                                                                                ##
    ##   STARTUP                                                                                                      ##
    ##                                                                                                                ##
    ####################################################################################################################

    def onLoadConfig(self):
        """\
        Load plugin configuration
        """
        self.load_config_warn_reasons()
        self.load_config_messages()
        self.load_config_warn()

        try:
            self._noreason_level = self.console.getGroupLevel(self.config.get('settings', 'noreason_level'))
        except (NoOptionError, KeyError), err:
            self.warning("Using default value %s for 'noreason_level'. %s" % (self._noreason_level, err))

        try:
            self._long_tempban_level = self.console.getGroupLevel(self.config.get('settings', 'long_tempban_level'))
        except (NoOptionError, KeyError), err:
            self.warning("Using default value %s for 'long_tempban_level'. %s" % (self._long_tempban_level, err))

        try:
            self._hidecmd_level = self.console.getGroupLevel(self.config.get('settings', 'hidecmd_level'))
        except (NoOptionError, KeyError), err:
            self.warning("Using default value %s for 'hidecmd_level'. %s" % (self._hidecmd_level, err))

        try:
            self._admins_level = self.console.getGroupLevel(self.config.get('settings', 'admins_level'))
        except (NoOptionError, KeyError), err:
            self.warning("Using default value %s for 'admins_level'. %s" % (self._admins_level, err))

        try:
            self._announce_registration = self.config.getboolean('settings', 'announce_registration')
        except NoOptionError:
            self.warning(r'conf settings\announce_registration not found, using default : %s' %
                         'yes' if self._announce_registration else 'no')
        except ValueError, err:
            self.error(r'invalid value for conf setting\announce_registration, using default : %s. %s' %
                       ('yes' if self._announce_registration else 'no', err))
        except Exception, err:
            self.error(r'unexpected error while reading value for conf setting\announce_registration, using default : '
                       r'%s. %s' % ('yes' if self._announce_registration else 'no', err), exc_info=err)

    def load_config_messages(self):
        """\
        Load section 'messages' from config and put the messages in local cache.
        Optionally apply validation rules
        """
        self._messages = dict()

        # regme_confirmation
        self._messages['regme_confirmation'] = "^7Thanks for your registration. You are now a member of the group %s"
        try:
            msg = self.config.getTextTemplate('messages', 'regme_confirmation')
            if not '%s' in msg:
                raise ValueError("message regme_confirmation must have a placeholder '%%s' for the group name")
            self._messages['regme_confirmation'] = msg
        except NoOptionError:
            self.warning("missing message 'regme_confirmation' from config file. "
                         "Using default %r" % self._messages['regme_confirmation'])
        except ValueError, err:
            self.error("message 'regme_confirmation' from config file is invalid: %s. "
                       "Using default" % err)

    def load_config_warn(self):
        """\
        Load section 'warn' from config.
        """
        try:
            raw_data = self.config.getint('warn', 'warn_delay')
            if raw_data < 0:
                raise ValueError("can't be less than 0")
            self.warn_delay = raw_data
        except NoOptionError:
            self.warning("missing 'warn_delay' in section 'warn' from config file. "
                         "Using default %r" % self.warn_delay)
        except ValueError, err:
            self.error("setting 'warn_delay' in section 'warn' from config file is invalid: %s. "
                       "Using default" % err)

        try:
            raw_data = self.config.getint('warn', 'instant_kick_num')
            if raw_data < 0:
                raise ValueError("can't be less than 0")
            self.warn_instant_kick_num = raw_data
        except NoOptionError:
            self.warning("missing 'instant_kick_num' in section 'warn' from config file. "
                         "Using default %r" % self.warn_instant_kick_num)
        except ValueError, err:
            self.error("setting 'instant_kick_num' in section 'warn' from config file is invalid: %s. "
                       "Using default" % err)

        try:
            raw_data = self.config.getint('warn', 'alert_kick_num')
            if raw_data < 0:
                raise ValueError("can't be less than 0")
            self.warn_alert_kick_num = raw_data
        except NoOptionError:
            self.warning("missing 'alert_kick_num' in section 'warn' from config file. "
                         "Using default %r" % self.warn_alert_kick_num)
        except ValueError, err:
            self.error("setting 'alert_kick_num' in section 'warn' from config file is invalid: %s. "
                       "Using default" % err)

    def load_config_warn_reasons(self):
        """\
        Load section 'warn_reasons' from config
        """
        re_valid_warn_reason_value_from_config = re.compile(r"""
                ^
                (?:
                    \s*
                    \d+[smhdw]?         # a duration with one of the optional allowed time suffixes
                    ,\s*                # followed by a comma

                    (?:                 # followed by either
                        (?=/spam\#)/spam\#[^/\s]+   # '/spam#' followed by a keyword
                    |                               # or
                        (?!/spam\#)[^\s].*          # not '/spam#' and anything
                    )
                |

                   /                    # anything that starts with '/'
                   (?!spam\#)           # but is not followed by 'spam#'
                   [^/\s]+              # followed by at least a non blank and non '/' character
                )
                $
                """, re.VERBOSE)

        def load_warn_reason(key, reason_from_config):
            if re.match(re_valid_warn_reason_value_from_config, reason_from_config) is None:
                self.warning("""warn_reason '%s': invalid value "%s". Expected format is : "<duration>, <reason or
                                /spam# followed by a reference to a spamage keyword>" or '/' followed by a reference to
                                another warn_reason""" % (key, reason_from_config))
                return

            if reason_from_config[:1] == '/':
                try:
                    r = self.config.getTextTemplate('warn_reasons', reason_from_config[1:])
                except NoOptionError:
                    self.warning("warn_reason '%s' refers to '/%s' but warn_reason '%s' cannot be found" % (
                        key, reason_from_config[1:], reason_from_config[1:]))
                    return
                except Exception, err:
                    self.error("warn_reason '%s' refers to '/%s' but '%s' could not be read : %s" % (
                        key, reason_from_config[1:], reason_from_config[1:], err), err)
                    return

                if r[:1] == '/':
                    self.warning("warn_reason '%s': Possible recursion %s, %s" % (key, r, reason_from_config[1:]))
                    return
            else:
                r = reason_from_config

            expire, r = r.split(',', 1)
            r = r.strip()

            if r[:6] == '/spam#':
                spam_reason = self.getSpam(r[6:])
                if spam_reason is None:
                    self.warning("warn_reason '%s' refers to '/spam#%s' but spamage '%s' cannot be found" % (
                        key, r[6:], r[6:]))
                    return
                else:
                    r = spam_reason

            return functions.time2minutes(expire.strip()), r

        def load_mandatory_warn_reason(key, default_duration, default_reason):
            if self.config.has_option('warn_reasons', key):
                self.warn_reasons[key] = load_warn_reason(key, self.config.getTextTemplate('warn_reasons', key))
            if not key in self.warn_reasons or self.warn_reasons[key] is None:
                self.warning("No valid option '%s' in section 'warn_reasons'. Falling back on default value" % key)
                self.warn_reasons[key] = functions.time2minutes(default_duration), default_reason
            self.info("warn reason '%s' : %s" % (key, self.warn_reasons[key]))

        self.info("------ loading warn_reasons from config file ------")
        self.warn_reasons = {}
        load_mandatory_warn_reason('default', "1h", "^7behave yourself")
        load_mandatory_warn_reason('generic', "1h", "^7")
        if self.config.has_section('warn_reasons'):
            for key, value in self.config.items('warn_reasons'):
                rv = load_warn_reason(key, value)
                if rv is not None:
                    self.warn_reasons[key] = rv
        for key, (duration, reason) in self.warn_reasons.items():
            self.info("""{0:<10s} {1:<10s}\t"{2}" """.format(key, functions.minutesStr(duration), reason))
        self.info("-------------- warn_reasons loaded ----------------")

    def onStartup(self):
        """\
        Plugin startup
        """
        self.registerEvent(self.console.getEventID('EVT_CLIENT_SAY'), self.OnSay)
        self.registerEvent(self.console.getEventID('EVT_CLIENT_TEAM_SAY'), self.OnSay)
        self.registerEvent(self.console.getEventID('EVT_CLIENT_SQUAD_SAY'), self.OnSay)
        self.registerEvent(self.console.getEventID('EVT_CLIENT_PRIVATE_SAY'), self.OnPrivateSay)
        self.createEvent('EVT_ADMIN_COMMAND', 'Admin Command')

        try:
            cmdPrefix = self.config.get('settings', 'command_prefix')
            if cmdPrefix:
                self.cmdPrefix = cmdPrefix
        except NoOptionError:
            self.warning('could not get command_prefix, using default')

        try:
            cmdPrefixLoud = self.config.get('settings', 'command_prefix_loud')
            if cmdPrefixLoud:
                self.cmdPrefixLoud = cmdPrefixLoud
        except NoOptionError:
            self.warning('could not get command_prefix_loud, using default')

        try:
            cmdPrefixBig = self.config.get('settings', 'command_prefix_big')
            if cmdPrefixBig:
                self.cmdPrefixBig = cmdPrefixBig
        except NoOptionError:
            self.warning('could not get command_prefix_big, using default')

        try:
            cmdPrefixPrivate = self.config.get('settings', 'command_prefix_private')
            if cmdPrefixPrivate:
                self.cmdPrefixPrivate = cmdPrefixPrivate
        except NoOptionError:
            self.warning('could not get command_prefix_private, using default')

        try:
            self._warn_command_abusers = self.config.getboolean('warn', 'warn_command_abusers')
        except NoOptionError:
            self.warning('conf warn\warn_command_abusers not found, using default : no')
            self._warn_command_abusers = False
        except ValueError:
            self.warning('invalid value for conf warn\warn_command_abusers, using default : no')
            self._warn_command_abusers = False

        if 'commands' in self.config.sections():
            for cmd in self.config.options('commands'):
                level = self.config.get('commands', cmd)
                sp = cmd.split('-')
                alias = None
                if len(sp) == 2:
                    cmd, alias = sp

                func = getCmd(self, cmd)
                if func:
                    self.registerCommand(self, cmd, level, func, alias)

        if not self.console.storage.db:
            self.error('There is no database connection! '
                       'Cannot store or retrieve any information. '
                       'Fix the database connection first!')
        else:

            superadmins = []

            try:
                superadmins = self.console.clients.lookupSuperAdmins()
                self.debug('%s superadmins found in database' % len(superadmins))
            except Exception, msg:
                # no proper groups available, cannot continue
                self.critical('Seems your groupstable in the database is empty. '
                              'Please recreate your database using the proper sql syntax. '
                              'Use b3/docs/b3.sql - (%s)' % msg)

            if 'iamgod' in self._commands.keys() and \
                self._commands['iamgod'].level is not None and \
                    self._commands['iamgod'].level[0] >= 0:
                ## here the config file for the admin plugin explicitly enables the iamgod command
                if len(superadmins) == 0:
                    self.verbose('!iamgod command enabled by config file. Be sure to disable it after typing !iamgod.')
                else:
                    self.warning('!iamgod command enabled by config file but %s superadmin are already registered. ' +
                                 'Make sure to disable the iamgod command in the admin plugin', len(superadmins))
            elif len(superadmins) == 0:
                self.verbose('No SuperAdmins found, enabling !iamgod')
                # There are no superadmins, enable the !iamgod command
                self.registerCommand(self, 'iamgod', 0, getCmd(self, 'iamgod'))
            else:
                self.verbose('SuperAdmin(s) found, no need for !iamgod')

    def registerCommand(self, plugin, command, level, handler, alias=None, secretLevel=None):
        """\
        Register a command
        """
        if not handler:
            self.error('Command "%s" registration failed, no handler' % command)
            return False

        if plugin.config and plugin != self and plugin.config.has_option('commands', command):
            # override default level with level in config
            level = plugin.config.get('commands', command)

        clean_level = self.getGroupLevel(level)
        if clean_level is False:
            groups = self.console.storage.getGroups()
            self.error("Cannot register command '%s'. Bad level/group : '%s'. "
                       "Expecting a level (%s) or group keyword (%s)" % (command, level,
                                                                         ', '.join([str(x.level) for x in groups]),
                                                                         ', '.join([x.keyword for x in groups])))
            return

        if secretLevel is None:
            secretLevel = self._hidecmd_level

        try:
            self._commands[command] = Command(plugin, command, clean_level, handler,
                                              handler.__doc__, alias, secretLevel)

            if self._commands[command].alias:
                self._commands[self._commands[command].alias] = self._commands[command]

            self._commands[command].prefix = self.cmdPrefix
            self._commands[command].prefixLoud = self.cmdPrefixLoud
            self._commands[command].prefixPrivate = self.cmdPrefixPrivate

            self.debug('Command "%s (%s)" registered with %s for level %s' % (command, alias,
                                                                              self._commands[command].func.__name__,
                                                                              self._commands[command].level))
            return True
        except Exception, msg:
            self.error('Command "%s" registration failed. %s' % (command, msg))
            self.exception(msg)
            return False

    ####################################################################################################################
    ##                                                                                                                ##
    ##   EVENTS                                                                                                       ##
    ##                                                                                                                ##
    ####################################################################################################################

    def OnPrivateSay(self, event):
        """\
        Handle private say events
        """
        if event.target and event.client.id == event.target.id:
            self.OnSay(event, True)

    def OnSay(self, event, private=False):
        """\
        Handle say events
        """
        self.debug('OnSay handle %s:"%s"', event.type, event.data)

        if len(event.data) >= 3 and event.data[:1] == '#':
            if self.console.debug:
                if event.data[1:] == 'clients':
                    self.debug('Clients:')
                    for k, c in self.console.clients.items():
                        self.debug('client %s (#%i id: %s cid: %s level: %s group: %s) obj: %s',
                                   c.name, id(c), c.id, c.cid, c.maxLevel, c.groupBits, c)
                elif event.data[1:] == 'groups':
                    self.debug('Groups for %s:', event.client.name)
                    for g in event.client.groups:
                        self.debug('group (id: %s, name: %s, level: %s)', g.id, g.name, g.level)

                elif event.data[1:5] == 'vars':
                    try:
                        data = event.data[7:].strip()
                        if data:
                            sclient = self.findClientPrompt(data, event.client)
                            if not sclient:
                                return
                        else:
                            sclient = event.client
                    except Exception:
                        sclient = event.client

                    self.debug('Vars for %s:', sclient.name)

                    try:
                        for k, v in sclient._pluginData.items():
                            self.debug('\tplugin %s:', k)
                            for kk, vv in v.items():
                                self.debug('\t\t%s = %s', kk, str(vv.value))
                    except Exception, e:
                        self.debug('Error getting vars: %s', e)
                    self.debug('End of vars')

                elif event.data[1:7] == 'tkinfo':
                    try:
                        data = event.data[9:].strip()
                        if data:
                            sclient = self.findClientPrompt(data, event.client)
                            if not sclient:
                                return
                        else:
                            sclient = event.client
                    except Exception:
                        sclient = event.client

                    self.debug('Tkinfo for %s:', sclient.name)

                    try:
                        for k, v in sclient._pluginData.items():

                            for kk, vv in v.items():
                                if kk == 'tkinfo':
                                    self.debug('\tplugin %s:', k)
                                    tkinfo = vv.value
                                    self.debug('\t\tcid = %s', tkinfo.cid)
                                    self.debug('\t\tattackers = %s', str(tkinfo.attackers))
                                    self.debug('\t\tattacked = %s', str(tkinfo.attacked))
                                    self.debug('\t\tpoints = %s', tkinfo.points)
                                    self.debug('\t\t_grudged = %s', str(tkinfo._grudged))
                                    self.debug('\t\tlastAttacker = %s', tkinfo.lastAttacker)
                    except Exception, e:
                        self.debug('Error getting Tkinfo: %s', e)
                    self.debug('End of Tkinfo')

        elif len(event.data) >= 2 and event.data[:1] in (self.cmdPrefix, self.cmdPrefixLoud,
                                                         self.cmdPrefixBig, self.cmdPrefixPrivate):

            # catch the confirm command for identification of the B3 devs
            if event.data[1:] == 'confirm':
                self.debug('checking confirmation...')
                self.console.say(functions.confirm(event.client))
                return
            else:
                self.debug('Handle command %s' % event.data)

            if event.data[1:2] in (self.cmdPrefix, self.cmdPrefixLoud, self.cmdPrefixBig, self.cmdPrefixPrivate):
                # self.is the alias for say
                cmd = 'say'
                data = event.data[2:]
            else:
                cmd = event.data[1:].split(' ', 1)

                if len(cmd) == 2:
                    cmd, data = cmd
                else:
                    cmd = cmd[0]
                    data = ''

            try:
                command = self._commands[cmd.lower()]
            except KeyError:
                spell_check = self.get_cmdSoundingLike(cmd, event.client)
                _msg = self.getMessage('unknown_command', cmd)
                if spell_check:
                    _msg += '. Did you mean %s%s ?' % (event.data[:1], spell_check)
                event.client.message(_msg)
                if event.client.maxLevel < self._admins_level and self._warn_command_abusers and event.client.authed:
                    event.client.var(self, 'fakeCommand', 0).value += 1
                    if event.client.var(self, 'fakeCommand').toInt() >= 3:
                        event.client.setvar(self, 'fakeCommand', 0)
                        self.warnClient(event.client, 'fakecmd', None, False)
                return

            cmd = cmd.lower()

            if not command.plugin.isEnabled():
                try:
                    event.client.message(self.getMessage('cmd_plugin_disabled'))
                except NoOptionError:
                    event.client.message("plugin disabled: cannot execute command %s" % cmd)
                return

            elif not event.client.authed and command.level > 0:
                event.client.message('^7Please try your command after you have been authenticated')
                self.console.clients.authorizeClients()
                return
            elif private:
                # self.is a silent command
                if event.client.maxLevel < command.secretLevel:
                    event.client.message('^7You do not have sufficient access to do silent commands')
                    return False

            if command.canUse(event.client):

                try:
                    if event.data[:1] == self.cmdPrefixLoud and event.client.maxLevel >= 9:
                        results = command.executeLoud(data, event.client)
                    elif event.data[:1] == self.cmdPrefixBig and event.client.maxLevel >= 9:
                        results = command.executeBig(data, event.client)
                    elif event.data[:1] == self.cmdPrefixPrivate and event.client.maxLevel >= 9:
                        results = command.executePrivate(data, event.client)
                    else:
                        results = command.execute(data, event.client)
                except (KeyboardInterrupt, SystemExit):
                    pass
                except:
                    event.client.message('^7There was an error processing your command')
                    raise
                else:
                    self.console.queueEvent(self.console.getEvent('EVT_ADMIN_COMMAND',
                                                                  (command, data, results), event.client))
            else:

                if self._warn_command_abusers and event.client.maxLevel < self._admins_level:
                    event.client.var(self, 'noCommand', 0).value += 1
                    if event.client.var(self, 'noCommand').toInt() >= 3:
                        event.client.setvar(self, 'noCommand', 0)
                        self.warnClient(event.client, 'nocmd', None, False)
                        return

                if command.level is None:
                    event.client.message('^7%s%s command is disabled' % (self.cmdPrefix, cmd))
                else:
                    self.info("%s does not have sufficient rights to use %s%s. "
                              "Required level: %s" % (event.client.name, self.cmdPrefix, cmd, command.level[0]))
                    try:
                        # show the preconfigured message
                        group = self.console.getGroup(command.level[0])
                        event.client.message(self.getMessage('cmd_not_enough_access', {'group_name': group.name,
                                                                                       'prefix': self.cmdPrefix,
                                                                                       'command': cmd}))
                    except Exception, e:
                        # fallback to default one if we errors shows up (mostly invalid command level/group specified
                        # in the configuration file thus we fail in retrieving the group from the storage)
                        self.warning("could not format 'cmd_not_enough_access' message (using default): %s" % e)
                        event.client.message('^7You do not have sufficient access to use %s%s' % (self.cmdPrefix, cmd))

    ####################################################################################################################
    ##                                                                                                                ##
    ##   UTILITIES                                                                                                    ##
    ##                                                                                                                ##
    ####################################################################################################################

    def aquireCmdLock(self, cmd, client, delay, all=True):
        if client.maxLevel >= self._admins_level:
            return True
        elif cmd.time + delay <= self.console.time():
            return True
        else:
            return False

    def get_cmdSoundingLike(self, c_word, client):
        c_list = []
        for c, cmd in self._commands.iteritems():
            if cmd.canUse(client):
                if cmd.command not in c_list:
                    c_list.append(cmd.command)
        result = functions.corrent_spell(c_word, ' '.join(c_list))
        return result

    def getAdmins(self):
        """\
        Return a list of online admins
        """
        return self.console.clients.getClientsByLevel(self._admins_level)

    def getRegulars(self):
        """\
        Return a list of online regular players
        """
        return self.console.clients.getClientsByLevel(min=2, max=2)

    def findClientPrompt(self, client_id, client=None):
        """\
        Find a client matching the given input
        """
        matches = self.console.clients.getByMagic(client_id)
        if matches:
            if len(matches) > 1:
                names = []
                for _p in matches:
                    if _p.name == _p.cid:
                        names.append('^7%s' % _p.name)
                    else:
                        names.append('^7%s [^2%s^7]' % (_p.name, _p.cid))

                if client:
                    client.message(self.getMessage('players_matched', client_id, ', '.join(names)))
                return None
            else:
                return matches[0]
        else:
            if client:
                client.message(self.getMessage('no_players', client_id))
            return None

    def parseUserCmd(self, cmd, req=False):
        """\
        Return a tuple of two elements extracted from cmd :
         - a player identifier
         - optional parameters
        req: set to True if parameters is required.
        Return None if could cmd is not in the expected format
        """
        m = re.match(self._parseUserCmdRE, cmd)

        if m:
            cid = m.group('cid')
            parms = m.group('parms')

            if req and not (parms and len(parms)):
                return None

            if cid[:1] == "'" and cid[-1:] == "'":
                cid = cid[1:-1]

            return cid, parms
        else:
            return None

    def getGroupLevel(self, level):
        """\
        Return a group level from group keyword or group level
        understand level ranges (ie: 20-40 or mod-admin)
        """
        level = str(level)
        if level.lower() == 'none':
            return 'none'
        elif level.count('-') == 1:
            (levelmin, levelmax) = level.split('-', 1)
            try:
                levelmin = int(levelmin)
            except ValueError:
                try:
                    levelmin = self.console.getGroupLevel(levelmin)
                except KeyError:
                    self.error('unknown group %s' % levelmin)
                    return False
            try:
                levelmax = int(levelmax)
            except ValueError:
                try:
                    levelmax = self.console.getGroupLevel(levelmax)
                except KeyError:
                    self.error('unknown group %s' % levelmax)
                    return False
            level = '%s-%s' % (levelmin, levelmax)
        else:
            try:
                level = int(level)
            except ValueError:
                try:
                    level = self.console.getGroupLevel(level)
                except KeyError:
                    self.error('unknown group %s' % level)
                    return False
        return level

    def getReason(self, kword):
        """\
        Return a reason according to the given keyword
        """
        if not kword:
            return ''

        r = self.getWarning(kword)
        if r:
            return r[1]
        else:
            return kword

    def getSpam(self, kword):
        """\
        Return a spam message according to the given keyword
        """
        if not kword:
            return ''

        try:
            s = self.config.getTextTemplate('spamages', kword)

            if s[:1] == '/':
                s = self.config.getTextTemplate('spamages', s[1:])
                if s[:1] == '/':
                    self.error('getSpam: Possible spam recursion %s, %s', kword, s)
                    return None

            return s
        except NoOptionError:
            return None
        except Exception, msg:
            self.error('getSpam: Could not get spam "%s": %s\n%s', kword, msg, traceback.extract_tb(sys.exc_info()[2]))
            return None

    def getWarning(self, kword):
        """\
        Return a warning message according to the given keyword
        """
        if not kword:
            kword = 'default'
        return self.warn_reasons.get(kword)

    def assert_commandData(self, data, client, cmd, *formatArgs):
        data = cmd.parseData(data, *formatArgs)
        if not data[0]:
            client.message(data[1])
            return False
        else:
            return data[0]

    def clearAll(self, sclient, client=None):
        """\
        Clear a client of all warnings
        """
        for w in sclient.warnings:
            admin = None
            try:
                admin = self.console.storage.getClient(Client(id=w.adminId))
                # client object needs console to get groups
                admin.console = self.console
            except Exception:
                # warning given by the bot (censor, tk, etc) have adminId = 0 which match no client in storage
                pass

            if admin is None or admin.maxLevel <= client.maxLevel:
                w.inactive = 1
                self.console.storage.setClientPenalty(w)

        self._tkPlugin = self.console.getPlugin('tk')
        if self._tkPlugin:
            self._tkPlugin.forgiveAll(sclient.cid)

        sclient.save()

    def doList(self, client, cmd):
        """\
        List online players
        """
        names = []
        for c in self.console.clients.getClientsByLevel():
            names.append(self.getMessage('player_id', c.name, c.cid))

        cmd.sayLoudOrPM(client, ', '.join(names))
        return True

    def sayMany(self, msg, times=5, delay=1):
        """\
        Print a message to all the players
        """
        for c in range(1, times + 1):
            self.console.say('^%i%s' % (c, msg))
            time.sleep(delay)

    def penalizeClient(self, type, client, reason, keyword=None, duration=0, admin=None, data=''):
        """\
        Inflict a penalty to the given client
        """
        if reason is None:
            reason = self.getReason(keyword)

        duration = functions.time2minutes(duration)

        if type == self.PENALTY_KICK:
            client.kick(reason, keyword, admin, False, data)
        elif type == self.PENALTY_TEMPBAN:
            client.tempban(reason, keyword, duration, admin, False, data)
        elif type == self.PENALTY_BAN:
            client.ban(reason, keyword, admin, False, data)
        elif type == self.PENALTY_WARNING:
            self.warnClient(client, keyword, admin, True, data, duration)
        else:
            if self.console.inflictCustomPenalty(type, client=client, reason=reason,
                                                 duration=duration, admin=admin, data=data) is not True:
                self.error('penalizeClient(): type %s not found', type)

    def warnClient(self, sclient, keyword, admin=None, timer=True, data='', newDuration=None):
        """\
        Warn a client
        """
        try:
            duration, warning = self.getWarning(keyword)
        except Exception:
            duration, warning = self.getWarning('generic')
            warning = '%s %s' % (warning, keyword)

        if newDuration:
            duration = newDuration

        warnrecord = sclient.warn(duration, warning, keyword, admin, data)
        warning = sclient.exactName + '^7, ' + warning

        if timer:
            sclient.setvar(self, 'warnTime', self.console.time())

        warnings = sclient.numWarnings

        try:
            pmglobal = self.config.getboolean('warn', 'pm_global')
        except (NoOptionError, ValueError):
            pmglobal = False

        if pmglobal:
            msg = self.config.getTextTemplate('warn', 'message', warnings=warnings, reason=warning)
            sclient.message(msg)
            if admin:
                admin.message(msg)
        else:
            self.console.say(self.config.getTextTemplate('warn', 'message', warnings=warnings, reason=warning))
        if warnings >= self.warn_instant_kick_num:
            self.warnKick(sclient, admin)
        elif warnings >= self.warn_alert_kick_num:
            duration = functions.minutesStr(self.warnKickDuration(sclient))

            warn = sclient.lastWarning
            if warn:
                self.console.say(self.config.getTextTemplate('warn', 'alert', name=sclient.exactName, warnings=warnings,
                                                             duration=duration, reason=warn.reason))
            else:
                self.console.say(self.config.getTextTemplate('warn', 'alert', name=sclient.exactName, warnings=warnings,
                                                             duration=duration, reason='Too many warnings'))

            sclient.setvar(self, 'checkWarn', True)
            t = threading.Timer(25, self.checkWarnKick, (sclient, admin, data))
            t.start()

        return warnrecord

    def checkWarnKick(self, sclient, client=None, data=''):
        """\
        Check if a client needs to be kicked for too many warnings
        """
        if not sclient.var(self, 'checkWarn').value:
            return

        sclient.setvar(self, 'checkWarn', False)

        kick_num = self.config.getint('warn', 'alert_kick_num')
        warnings = sclient.numWarnings
        if warnings >= kick_num:
            self.warnKick(sclient, client, data)

    def warnKickDuration(self, sclient):
        """\
        Retrieve the duration for a tempban penalty
        due too many warnings
        """
        if sclient.numWarnings > self.config.getint('warn', 'tempban_num'):
            duration = self.config.getDuration('warn', 'tempban_duration')
        else:
            duration = 0
            for w in sclient.warnings:
                duration += w.duration * 60
            duration = (duration / self.config.getint('warn', 'duration_divider')) / 60

            maxDuration = self.config.getDuration('warn', 'max_duration')
            if duration > maxDuration:
                duration = maxDuration

        return duration

    def warnKick(self, sclient, client=None, data=''):
        """\
        Tempban a client for too many warnings
        """
        msg = sclient.numWarnings
        keyword = ''
        warn = sclient.lastWarning
        if warn:
            msg = warn.reason
            keyword = warn.keyword

        duration = self.warnKickDuration(sclient)

        if duration > 0:
            sclient.tempban(self.config.getTextTemplate('warn', 'reason', reason=msg), keyword,
                            duration, client, False, data)

    def _sendRules(self, sclient, big=False):
        """\
        Send rules to the given client
        """
        rules = []

        for i in range(1, 20):
            try:
                rule = self.config.getTextTemplate('spamages', 'rule%s' % i)
                rules.append(rule)
            except NoOptionError:
                break
            except Exception, err:
                self.error(err)
        try:
            if sclient:
                for rule in rules:
                    sclient.message(rule)
                    time.sleep(1)
            else:
                for rule in rules:
                    if big:
                        self.console.saybig(rule)
                    else:
                        self.console.say(rule)
                    time.sleep(1)
        except Exception, err:
            self.error(err)

    ####################################################################################################################
    ##                                                                                                                ##
    ##   COMMANDS                                                                                                     ##
    ##                                                                                                                ##
    ####################################################################################################################

    def cmd_die(self, data, client, cmd=None):
        """\
        - shutdown b3
        """
        cmd.sayLoudOrPM(client, '^7Shutting down ^3%s' % data)
        self.console.die()

    def cmd_restart(self, data, client, cmd=None):
        """\
        - restart b3
        """
        cmd.sayLoudOrPM(client, '^7Shutting down for restart...')
        self.console.restart()

    def cmd_reconfig(self, data, client, cmd=None):
        """\
        - re-load all configs
        """
        self.console.reloadConfigs()
        cmd.sayLoudOrPM(client, '^7Re-loaded configs')

    def cmd_mask(self, data, client, cmd=None):
        """\
        <group> [<name>] - hide level
        """
        m = self.parseUserCmd(data)
        if not m:
            client.message(self.getMessage('invalid_parameters'))
            return False
        elif m[1] is None:
            groupname = m[0]
            sclient = client
        else:
            groupname = m[0]
            sclient = self.findClientPrompt(m[1], client)
            if not sclient:
                return False

        try:
            group = Group(keyword=groupname)
            group = self.console.storage.getGroup(group)
        except Exception:
            client.message(self.getMessage('group_unknown', {'group_name': groupname}))
            return False

        sclient.maskLevel = group.level
        sclient.save()

        if sclient != client:
            client.message('^7Masked %s as %s' % (sclient.name, group.name))

        sclient.message('^7Masked as %s' % group.name)

    def cmd_unmask(self, data, client, cmd=None):
        """\
        [<name>] - un-hide level
        """
        m = self.parseUserCmd(data)
        if not m:
            sclient = client
        else:
            sclient = self.findClientPrompt(m[0], client)

        if sclient:
            sclient.maskLevel = 0
            sclient.save()

            if sclient != client:
                client.message('^7Un-Masked %s' % sclient.name)

            sclient.message('^7Un-Masked')

    def cmd_clear(self, data, client, cmd=None):
        """\
        [<player>] - clear all tk points and warnings
        """
        if data:
            sclient = self.findClientPrompt(data, client)

            if sclient:
                self.clearAll(sclient, client)
                self.console.say(self.getMessage('cleared_warnings', {'admin': client.exactName,
                                                                      'player': sclient.exactName}))
        else:
            for cid, c in self.console.clients.items():
                self.clearAll(c, client)
            self.console.say(self.getMessage('cleared_warnings_for_all', {'admin': client.exactName}))

    def cmd_map(self, data, client, cmd=None):
        """\
        <map> - switch current map
        """
        if not data:
            client.message('^7You must supply a map to change to.')
            return
        suggestions = self.console.changeMap(data)
        if type(suggestions) == list:
            client.message('do you mean : %s ?' % ', '.join(suggestions[:5]))

    def cmd_maprotate(self, data, client, cmd=None):
        """\
        - switch to the next map in rotation
        """
        self.console.rotateMap()

    def cmd_b3(self, data, client, cmd=None):
        """\
        - say b3's version info
        """
        if len(data) > 0 and client.maxLevel >= self._admins_level:
            data = data.lower().strip()
            if data == 'poke':
                self.console.say('^7Do not poke b3 %s^7!' % client.exactName)
            elif data == 'expose':
                self.console.say('^7Do expose b3 to sunlight %s^7!' % client.exactName)
            elif data == 'stare':
                self.console.say('^7Do not stare at b3 %s^7!' % client.exactName)
            elif data == 'stab':
                self.console.say('^7b3 is invincible, %s^7 could not penetrate he hide of b3.' % client.exactName)
            elif data == 'bite':
                self.console.say('^7b3 breaks %s^7\'s teeth with its metalic frame.' % client.exactName)
            elif data == 'fuck':
                self.console.say('^7b3 doesn\'t need your hand me out %s^7.' % client.exactName)
            elif data == 'slap':
                self.console.say('^7%s^7 is not Rick James.' % client.exactName)
            elif data == 'fight':
                self.console.say('^7%s^7 is knocked out by b3.' % client.exactName)
            elif data == 'feed':
                self.console.say('^7b3 enjoys your nourishment %s^7.' % client.exactName)
            elif data == 'throw':
                self.console.say('^7b3 can fly %s^7, and you throw like a sissy.' % client.exactName)
            elif data == 'furniture':
                self.console.say('^7b3 does make a lovely lamp %s^7.' % client.exactName)
            elif data == 'indeed':
                self.console.say('^7You WOULD say that %s^7.' % client.exactName)
            elif data == 'flog':
                self.console.say('^7You are so kinky %s^7.' % client.exactName)
            elif data == 'sexor':
                self.console.say('^7Mmmmm %s^7.' % client.exactName)
            elif data == 'hate':
                self.console.say('^7Don\'t hate the player, %s^7, hate the game.' % client.exactName)
            elif data == 'smoke':
                self.console.say('^7b3 has been known to cause lung cancer when smoked %s^7.' % client.exactName)
            elif data == 'maul':
                self.console.say('^7b3 casts a spell of invisibility, you can\'t find  %s^7.' % client.exactName)
            elif data == 'procreate':
                self.console.say('^7b3 2.0 will soon be on the way %s^7.' % client.exactName)
            elif data == 'shoot':
                self.console.say('^7Your hit detection is off %s^7, b3 is unharmed.' % client.exactName)
            elif data == 'kick':
                client.kick('^7as requested', '', None)
            elif data == 'triangulate':
                self.console.say('^7b3 is at %s.' % self.console._publicIp)
        else:
            cmd.sayLoudOrPM(client, '%s ^7- uptime: [^2%s^7]' % (
                b3.version, functions.minutesStr(self.console.upTime() / 60.0)))

    def cmd_enable(self, data, client, cmd=None):
        """\
        <plugin> - enable a disabled plugin
        """
        data = data.strip().lower()

        if not data:
            client.message('^7You must supply a plugin name to enable.')
            return
        elif data == 'admin':
            client.message('^7You cannot disable/enable the admin plugin.')
            return

        plugin = self.console.getPlugin(data)
        if plugin:
            if plugin.isEnabled():
                client.message('^7Plugin %s is already enabled.' % data)
            else:
                plugin.enable()
                self.console.say('^7%s is now ^2ON' % plugin.__class__.__name__)
        else:
            client.message('^7No plugin named %s loaded.' % data)

    def cmd_disable(self, data, client, cmd=None):
        """\
        <plugin> - disable a plugin
        """
        data = data.strip().lower()

        if not data:
            client.message('^7You must supply a plugin name to disable.')
            return
        elif data == 'admin':
            client.message('^7You cannot disable/enable the admin plugin.')
            return

        plugin = self.console.getPlugin(data)
        if plugin:
            if not plugin.isEnabled():
                client.message('^7Plugin %s is already disabled.' % data)
            else:
                plugin.disable()
                self.console.say('^7%s is now ^1OFF' % plugin.__class__.__name__)
        else:
            client.message('^7No plugin named %s loaded.' % data)

    def cmd_register(self, data, client, cmd=None):
        """\
        - register yourself as a basic user
        """
        try:
            group = Group(keyword='user')
            group = self.console.storage.getGroup(group)
        except Exception:
            return False

        if client.inGroup(group):
            client.message(self.getMessage('groups_already_in', client.exactName, group.name))
        elif client.maxLevel >= group.level:
            client.message('^7You are already in a higher level group')
        else:
            client.setGroup(group)
            client.save()

            client.message(self.getMessage('regme_confirmation', group.name))
            if self._announce_registration:
                self.console.say(self.getMessage('regme_annouce', client.exactName, group.name))
            return True

    def cmd_help(self, data, client, cmd=None):
        """\
        [<command|level>] - get info on how to use a command, you can use *<command> for partial matches
        """
        commands = []
        if re.match(r'^[0-9]+$', data):
            mlevel = int(data)
            for cmd in self._commands.values():
                if cmd.level is not None and cmd.level[0] == mlevel and cmd.canUse(client):
                    if cmd.command not in commands:
                        commands.append(cmd.command)
        elif data[:1] == '*':
            search = data[1:]
            for cmd in self._commands.values():
                if cmd.command.find(search) != -1 and cmd.canUse(client) and cmd.command not in commands:
                    if cmd.command not in commands:
                        commands.append(cmd.command)
        elif data:
            try:
                cmd = self._commands[data]
                if cmd.canUse(client):
                    cmd.sayLoudOrPM(client, self.getMessage('help_command', self.cmdPrefix, cmd.command, cmd.help))
            except KeyError:
                client.message(self.getMessage('help_no_command', data))
            return
        else:
            for c, cmd in self._commands.iteritems():
                if cmd.canUse(client):
                    if cmd.command not in commands:
                        commands.append(cmd.command)

        if not len(commands):
            cmd.sayLoudOrPM(client, self.getMessage('help_none'))
        else:
            # remove the !register command if already registered
            if 'register' in commands and int(client.maxLevel) > 0:
                commands.remove('register')
            commands.sort()
            cmd.sayLoudOrPM(client, self.getMessage('help_available', ', '.join(commands)))

    def cmd_list(self, data, client, cmd=None):
        """\
        - list all connected players
        """
        thread.start_new_thread(self.doList, (client, cmd))

    def cmd_regulars(self, data, client, cmd=None):
        """\
        - lists all the online regular players
        """
        clist = self.getRegulars()

        if len(clist) > 0:
            nlist = []
            for c in clist:
                nlist.append(c.exactName)
            cmd.sayLoudOrPM(client, self.getMessage('regulars', ', '.join([c.exactName for c in clist])))
        else:
            cmd.sayLoudOrPM(client, self.getMessage('no_regulars'))

    def cmd_admins(self, data, client, cmd=None):
        """\
        - lists all the online admins
        """
        self.debug('trying to get admins')
        clist = self.getAdmins()

        if len(clist) > 0:
            nlist = []
            for c in clist:
                if c.maskGroup:
                    nlist.append('%s^7 [^3%s^7]' % (c.exactName, c.maskGroup.level))
                else:
                    nlist.append('%s^7 [^3%s^7]' % (c.exactName, c.maxLevel))

            cmd.sayLoudOrPM(client, self.getMessage('admins', ', '.join(nlist)))
        else:
            msg = self.getMessage('no_admins')
            if msg:
                cmd.sayLoudOrPM(client, self.getMessage('no_admins'))

    def cmd_rebuild(self, data, client, cmd=None):
        """\
        - sync up connected players
        """
        self.console.clients.sync()
        client.message('Synchronizing client info')

    def cmd_regtest(self, cid, client, cmd=None):
        """\
        - display your current user status
        """
        if client and client.maskGroup:
            cmd.sayLoudOrPM(client, self.getMessage('leveltest', client.exactName, client.id, client.maskGroup.name,
                                                    client.maskGroup.level, self.console.formatTime(client.timeAdd)))
        elif client and client.maxGroup:
            cmd.sayLoudOrPM(client, self.getMessage('leveltest', client.exactName, client.id, client.maxGroup.name,
                                                    client.maxLevel, self.console.formatTime(client.timeAdd)))
        else:
            cmd.sayLoudOrPM(client, self.getMessage('leveltest', client.exactName, client.id, 'no groups', 0,
                                                    self.console.formatTime(client.timeAdd)))

        return True

    def cmd_admintest(self, cid, client, cmd=None):
        """\
        - display your current user status
        """
        return self.cmd_regtest(cid, client, cmd)

    def cmd_leveltest(self, data, client, cmd=None):
        """\
        [<name>] - display a user's status
        """
        m = self.parseUserCmd(data)
        if m:
            sclient = self.findClientPrompt(m[0], client)
        else:
            sclient = client
        if sclient:
            if m and sclient.maskGroup:
                cmd.sayLoudOrPM(client,
                                self.getMessage('leveltest', sclient.exactName, sclient.id, sclient.maskGroup.name,
                                                sclient.maskGroup.level, self.console.formatTime(sclient.timeAdd)))
            elif not sclient.maxGroup:
                cmd.sayLoudOrPM(client, self.getMessage('leveltest_nogroups', sclient.exactName, sclient.id))
            else:
                cmd.sayLoudOrPM(client,
                                self.getMessage('leveltest', sclient.exactName, sclient.id, sclient.maxGroup.name,
                                                sclient.maxLevel, self.console.formatTime(sclient.timeAdd)))
        return True

    def cmd_makereg(self, data, client, cmd=None):
        """\
        <name> - make a name a regular
        """
        m = self.parseUserCmd(data)
        if not m:
            client.message(self.getMessage('invalid_parameters'))
            return False

        cid = m[0]

        try:
            group = Group(keyword='reg')
            group = self.console.storage.getGroup(group)
        except Exception:
            client.message('^7Group reg does not exist')
            return False

        sclient = self.findClientPrompt(cid, client)
        if sclient:
            if sclient.inGroup(group):
                client.message(self.getMessage('groups_already_in', sclient.exactName, group.name))
            elif sclient.maxLevel >= group.level:
                client.message('^7%s ^7is already in a higher level group' % sclient.exactName)
            else:
                sclient.setGroup(group)
                sclient.save()
                cmd.sayLoudOrPM(client, self.getMessage('groups_put', sclient.exactName, group.name))
                return True

    def cmd_unreg(self, data, client, cmd=None):
        """\
        <name> - remove a player from the 'regular' group
        """
        m = self.parseUserCmd(data)
        if not m:
            client.message(self.getMessage('invalid_parameters'))
            return False

        cid = m[0]

        try:
            group_reg = self.console.storage.getGroup(Group(keyword='reg'))
        except Exception, err:
            self.debug(err)
            client.message("^7Group 'regular' does not exist")
            return

        try:
            group_user = self.console.storage.getGroup(Group(keyword='user'))
        except Exception, err:
            self.debug(err)
            client.message("^7Group 'user' does not exist")
            return

        sclient = self.findClientPrompt(cid, client)
        if sclient:
            if sclient.inGroup(group_reg):
                sclient.remGroup(group_reg)
                sclient.setGroup(group_user)
                sclient.save()
                cmd.sayLoudOrPM(client, '^7%s^7 removed from group %s' % (sclient.exactName, group_reg.name))
            else:
                client.message('^7%s^7 is not in group %s' % (sclient.exactName, group_reg.name))

    def cmd_putgroup(self, data, client, cmd=None):
        """\
        <client> <group> - add a client to a grou
        """
        m = re.match('^(.{2,}) ([a-z][a-z0-9]+)$', data, re.I)
        if not m:
            client.message(self.getMessage('invalid_parameters'))
            return False

        cid, keyword = m.groups()

        try:
            group = Group(keyword=keyword)
            group = self.console.storage.getGroup(group)
        except Exception:
            client.message(self.getMessage('group_unknown', {'group_name': keyword}))
            return False

        if group.level >= client.maxLevel and client.maxLevel < 100:
            client.message(self.getMessage('group_beyond_reach', {'group_name': group.name}))
            return False

        sclient = self.findClientPrompt(cid, client)
        if sclient:
            if sclient.inGroup(group):
                client.message(self.getMessage('groups_already_in', sclient.exactName, group.name))
            else:
                sclient.setGroup(group)
                sclient.save()

                cmd.sayLoudOrPM(client, self.getMessage('groups_put', sclient.exactName, group.name))
                return True

    def cmd_say(self, data, client, cmd=None):
        """\
        - say a message to all players
        """
        self.console.say(self.getMessage('say', client.exactName, data))
        return True

    def cmd_ungroup(self, cid, client, cmd=None):
        """\
        <client> <group> - remove a client from a group
        """
        m = re.match('^([^ ]{2,}) ([a-z]+)$', cid)
        if not m:
            client.message(self.getMessage('invalid_parameters'))
            return False

        cid, keyword = m.groups()

        try:
            group = Group(keyword=keyword)
            group = self.console.storage.getGroup(group)
        except KeyError:
            client.message(self.getMessage('group_unknown', {'group_name': keyword}))
            return False

        sclient = self.findClientPrompt(cid, client)
        if sclient:
            if sclient.inGroup(group):
                sclient.remGroup(group)
                sclient.save()

                cmd.sayLoudOrPM(client, '^7%s^7 removed from group %s' % (sclient.exactName, group.name))
                return True
            else:
                client.message('^7%s^7 is not in group %s' % (sclient.exactName, group.name))

    def cmd_iamgod(self, data, client, cmd=None):
        """\
        - register yourself as the super admin
        """
        superadmins = self.console.clients.lookupSuperAdmins()
        if len(superadmins) > 0:
            # There are already superadmins, disable this command
            self.warning('%s superadmin(s) found in db. Disabling command' % len(superadmins))
            if 'iamgod' in self._commands.keys():
                self._commands.pop('iamgod')
            return

        try:
            group = Group(keyword='superadmin')
            group = self.console.storage.getGroup(group)
        except Exception, e:
            self.error('^7Could not get superadmin group: %s', e)
            return False

        try:
            command = self._commands['iamgod']
        except KeyError:
            self.error('iamgod command not found')
            return False
        else:
            command.level = 'none'

            if group in client.groups:
                client.message('^7You are already a %s' % group.exactName)
                return True

            client.setGroup(group)
            client.save()

            client.message('^7You are now a %s' % group.name)
            self.bot('created %s %s - %s', group.name, client.name, client.guid)

            return True

    def cmd_time(self, data, client=None, cmd=None):
        """\
        [<timezone/offset>] - display the servers current time
        """
        cmd.sayLoudOrPM(client, self.getMessage('time', self.console.formatTime(time.time(), data)))
        return True

    def cmd_seen(self, data, client=None, cmd=None):
        """\
        <name> - when was a player last seen?
        """
        m = self.parseUserCmd(data)
        if not m:
            client.message(self.getMessage('invalid_parameters'))
            return False

        data = m[0]
        clients = self.console.clients.lookupByName(data)

        if len(clients) == 0:
            client.message(self.getMessage('no_players', data))
        else:
            for c in clients:
                cmd.sayLoudOrPM(client, self.getMessage('seen', c.exactName, self.console.formatTime(c.timeEdit)))

        return True

    def cmd_lookup(self, data, client=None, cmd=None):
        """\
        <name> - lookup a player in the database
        """
        if not self.console.storage.status():
            cmd.sayLoudOrPM(client, '^7Cannot lookup, database appears to be ^1DOWN')
            return

        m = re.match('^(.+)$', data)
        if not m:
            client.message(self.getMessage('invalid_parameters'))
            return False

        clients = self.console.clients.lookupByName(data)

        if len(clients) == 0:
            client.message(self.getMessage('no_players', data))
        else:
            for c in clients:
                cmd.sayLoudOrPM(client, self.getMessage('lookup_found', c.id, c.exactName,
                                                        self.console.formatTime(c.timeEdit)))

        return True

    def cmd_status(self, data, client=None, cmd=None):
        """\
        - report status of bot
        """
        if self.console.storage.status():
            cmd.sayLoudOrPM(client, '^7Database appears to be ^2UP')
        else:
            cmd.sayLoudOrPM(client, '^7Database appears to be ^1DOWN')

    def cmd_scream(self, data, client=None, cmd=None):
        """\
        <message> - yell a message to all player
        """
        thread.start_new_thread(self.sayMany, (data, 5, 1))

    def cmd_find(self, data, client=None, cmd=None):
        """\
        <name> - test to find a connected player
        """
        m = self.parseUserCmd(data)
        if not m:
            client.message(self.getMessage('invalid_parameters'))
            return False

        cid = m[0]
        sclient = self.findClientPrompt(cid, client)

        if sclient:
            cmd.sayLoudOrPM(client, '^7Found player matching %s [^2%s^7] %s' % (cid, sclient.cid, sclient.exactName))

    def cmd_clientinfo(self, data, client=None, cmd=None):
        """\
        <name> <field> - get info about a client
        """
        m = self.parseUserCmd(data, True)
        if not m:
            client.message(self.getMessage('invalid_parameters'))
            return False

        cid, field = m

        sclient = self.findClientPrompt(cid, client)
        if sclient:
            try:
                cmd.sayLoudOrPM(client, '%s^7: %s^7 is %s' % (sclient.exactName, field, getattr(sclient, field)))
            except AttributeError:
                client.message('^7Unrecognized field %s' % field)

    def cmd_kick(self, data, client=None, cmd=None):
        """\
        <name> [<reason>] - kick a player
        """
        m = self.parseUserCmd(data)
        if not m:
            msg = self.getMessage('invalid_parameters')
            client.message(msg)
            return False

        cid, keyword = m
        reason = self.getReason(keyword)

        if not reason and client.maxLevel < self._noreason_level:
            client.message(self.getMessage('error_no_reason'))
            return False

        sclient = self.findClientPrompt(cid, client)
        if sclient:
            if sclient.cid == client.cid:
                self.console.say(self.getMessage('kick_self', client.exactName))
                return True
            elif sclient.maxLevel >= client.maxLevel:
                if sclient.maskGroup:
                    client.message(self.getMessage('action_denied_masked', {'name': sclient.exactName}))
                else:
                    self.console.say(
                        self.getMessage('kick_denied', sclient.exactName, client.exactName, sclient.exactName))
                return True
            else:
                sclient.kick(reason, keyword, client)
                return True
        elif re.match('^[0-9]+$', cid):
            # failsafe, do a manual client id ban
            self.console.kick(cid, reason, client)

    def cmd_kickall(self, data, client=None, cmd=None):
        """\
        <pattern> [<reason>] - kick all players matching <pattern>
        """
        m = self.parseUserCmd(data)
        if not m:
            client.message(self.getMessage('invalid_parameters'))
            return False

        cid, keyword = m
        reason = self.getReason(keyword)

        if not reason and client.maxLevel < self._noreason_level:
            client.message(self.getMessage('error_no_reason'))
            return False

        matches = self.console.clients.getByMagic(cid)
        for sclient in matches:
            if sclient.cid == client.cid:
                continue
            elif sclient.maxLevel >= client.maxLevel:
                continue
            else:
                sclient.kick(reason, keyword, client)

    def cmd_spank(self, data, client=None, cmd=None):
        """\
        <name> [<reason>] - spank a player, naughty boy!
        """
        m = self.parseUserCmd(data)
        if not m:
            client.message(self.getMessage('invalid_parameters'))
            return False

        cid, keyword = m
        reason = self.getReason(keyword)

        if not reason and client.maxLevel < self._noreason_level:
            client.message(self.getMessage('error_no_reason'))
            return False

        sclient = self.findClientPrompt(cid, client)
        if sclient:
            if sclient.cid == client.cid:
                self.console.say(self.getMessage('kick_self', client.exactName))
                return True
            elif sclient.maxLevel >= client.maxLevel:
                if sclient.maskGroup:
                    client.message(self.getMessage('action_denied_masked', {'name': sclient.exactName}))
                else:
                    self.console.say(
                        self.getMessage('kick_denied', sclient.exactName, client.exactName, sclient.exactName))
                return True
            else:
                if reason:
                    self.console.say(self.getMessage('spanked_reason', sclient.exactName, client.exactName, reason))
                else:
                    self.console.say(self.getMessage('spanked', sclient.exactName, client.exactName))
                sclient.kick(reason, keyword, client, silent=True)
                return True
        elif re.match('^[0-9]+$', cid):
            # failsafe, do a manual client id ban
            self.console.kick(cid, reason, client)

    def cmd_spankall(self, data, client=None, cmd=None):
        """\
        <pattern> [<reason>] - kick all players matching <pattern>
        """
        m = self.parseUserCmd(data)
        if not m:
            client.message(self.getMessage('invalid_parameters'))
            return False

        cid, keyword = m
        reason = self.getReason(keyword)

        if not reason and client.maxLevel < self._noreason_level:
            client.message(self.getMessage('error_no_reason'))
            return False

        matches = self.console.clients.getByMagic(cid)
        for sclient in matches:
            if sclient.cid == client.cid:
                continue
            elif sclient.maxLevel >= client.maxLevel:
                continue
            else:
                if reason:
                    self.console.say(self.getMessage('spanked_reason', sclient.exactName, client.exactName, reason))
                else:
                    self.console.say(self.getMessage('spanked', sclient.exactName, client.exactName))
                sclient.kick(reason, keyword, client, silent=True)

    def cmd_permban(self, data, client=None, cmd=None):
        """\
        <name> [<reason>] - ban a player permanently
        """
        m = self.parseUserCmd(data)
        if not m:
            client.message(self.getMessage('invalid_parameters'))
            return False

        cid, keyword = m
        reason = self.getReason(keyword)

        if not reason and client.maxLevel < self._noreason_level:
            client.message(self.getMessage('error_no_reason'))
            return False

        sclient = self.findClientPrompt(cid, client)
        if sclient:
            if sclient.cid == client.cid:
                self.console.say(self.getMessage('ban_self', client.exactName))
                return True
            elif sclient.maxLevel >= client.maxLevel:
                if sclient.maskGroup:
                    client.message(self.getMessage('action_denied_masked', {'name': sclient.exactName}))
                else:
                    self.console.say(self.getMessage('ban_denied', client.exactName, sclient.exactName))
                return True
            else:
                sclient.groupBits = 0
                sclient.save()
                sclient.ban(reason, keyword, client)
                return True

        elif re.match('^[0-9]+$', cid):
            # failsafe, do a manual client id ban
            self.console.ban(cid, reason, client)

    def cmd_ban(self, data, client=None, cmd=None):
        """\
        <name> [<reason>] - ban a player
        """
        m = self.parseUserCmd(data)
        if not m:
            client.message(self.getMessage('invalid_parameters'))
            return False

        cid, keyword = m
        reason = self.getReason(keyword)

        if not reason and client.maxLevel < self._noreason_level:
            client.message(self.getMessage('error_no_reason'))
            return False

        sclient = self.findClientPrompt(cid, client)
        if sclient:
            if sclient.cid == client.cid:
                self.console.say(self.getMessage('ban_self', client.exactName))
                return True
            elif sclient.maxLevel >= client.maxLevel:
                if sclient.maskGroup:
                    client.message(self.getMessage('action_denied_masked', {'name': sclient.exactName}))
                else:
                    self.console.say(self.getMessage('ban_denied', client.exactName, sclient.exactName))
                return True
            else:
                sclient.groupBits = 0
                sclient.save()
                duration = self.config.getDuration('settings', 'ban_duration')
                sclient.tempban(reason, keyword, duration, client)
                return True

        elif re.match('^[0-9]+$', cid):
            # failsafe, do a manual client id ban
            duration = self.config.getDuration('settings', 'ban_duration')
            self.console.tempban(cid, reason, duration, client)

    def cmd_banall(self, data, client=None, cmd=None):
        """\
        <pattern> [<reason>] - ban all players matching <pattern>
        """
        m = self.parseUserCmd(data)
        if not m:
            client.message(self.getMessage('invalid_parameters'))
            return False

        cid, keyword = m
        reason = self.getReason(keyword)

        if not reason and client.maxLevel < self._noreason_level:
            client.message(self.getMessage('error_no_reason'))
            return False

        duration = self.config.getDuration('settings', 'ban_duration')
        matches = self.console.clients.getByMagic(cid)
        for sclient in matches:
            if sclient.cid == client.cid:
                continue
            elif sclient.maxLevel >= client.maxLevel:
                continue
            else:
                sclient.tempban(reason, keyword, duration, client)

    def cmd_lastbans(self, data, client=None, cmd=None):
        """\
        list the 5 last bans
        """
        def format_ban(penalty):
            c = self.console.storage.getClient(Client(_id=penalty.clientId))
            txt = "^2@%s^7 %s^7" % (penalty.clientId, c.exactName)
            if penalty.type == 'Ban':
                txt += ' (Perm)'
            elif penalty.type == 'TempBan':
                txt += ' (%s remaining)' % minutesStr((penalty.timeExpire - self.console.time()) / 60.0)
            else:
                raise AssertionError("unexpected penalty type : %r" % penalty.type)
            if penalty.reason:
                txt += ' %s' % penalty.reason
            return txt

        bans = self.console.storage.getLastPenalties(types=('Ban', 'TempBan'), num=5)
        if len(bans):
            for line in map(format_ban, bans):
                cmd.sayLoudOrPM(client, line)
        else:
            cmd.sayLoudOrPM(client, '^7There are no active bans')

    def cmd_baninfo(self, data, client=None, cmd=None):
        """\
        <name> - display how many bans a user has
        """
        m = self.parseUserCmd(data)
        if not m:
            client.message(self.getMessage('invalid_parameters'))
            return False

        sclient = self.findClientPrompt(m[0], client)
        if sclient:
            bans = sclient.numBans
            if bans:
                cmd.sayLoudOrPM(client, self.getMessage('baninfo', {'name': sclient.exactName, 'num_bans': bans}))
            else:
                cmd.sayLoudOrPM(client, self.getMessage('baninfo_no_bans', {'name': sclient.exactName}))

    def cmd_runas(self, data, client=None, cmd=None):
        """\
        <name> <command> - run a command as a different user
        """
        m = self.parseUserCmd(data)
        if not m or m[1] == '':
            client.message(self.getMessage('invalid_parameters'))
            return False

        sclient = self.findClientPrompt(m[0], client)
        if sclient:
            self.OnSay(self.console.getEvent('EVT_CLIENT_SAY', m[1], sclient))

    def cmd_unban(self, data, client=None, cmd=None):
        """\
        <name> - un-ban a player
        """
        m = self.parseUserCmd(data)
        if not m:
            client.message(self.getMessage('invalid_parameters'))
            return False

        cid, reason = m
        reason = self.getReason(reason)

        sclient = self.findClientPrompt(cid, client)
        if sclient:
            for w in sclient.bans:
                if w.adminId:
                    try:
                        admin = self.console.storage.getClient(Client(id=w.adminId))
                        if admin.maxLevel > client.maxLevel:
                            client.message('^7You can not clear a ban from ' % admin.exactName)
                            return
                    except Exception:
                        pass

            sclient.unban(reason, client)

    def cmd_aliases(self, data, client=None, cmd=None):
        """\
        <name> - list a players aliases
        """
        m = self.parseUserCmd(data)
        if not m:
            client.message(self.getMessage('invalid_parameters'))
            return False

        cid = m[0]

        sclient = self.findClientPrompt(cid, client)
        if sclient:
            if sclient.maskGroup:
                cmd.sayLoudOrPM(client, self.getMessage('no_aliases', sclient.exactName))
            else:
                myaliases = []
                for a in sclient.aliases:
                    myaliases.append('%s^7' % a.alias)
                    if len(myaliases) > 10:
                        myaliases.append(self.getMessage('aliases_more_suffix'))
                        break

                if len(myaliases):
                    cmd.sayLoudOrPM(client, self.getMessage('aliases', sclient.exactName, ', '.join(myaliases)))
                else:
                    cmd.sayLoudOrPM(client, self.getMessage('no_aliases', sclient.exactName))

    def cmd_warns(self, data, client=None, cmd=None):
        """\
        - list warnings
        """
        client.message('^7Warnings: %s' % ', '.join(
            sorted([x for x in self.warn_reasons.keys() if x not in ('default', 'generic')])))

    def cmd_notice(self, data, client=None, cmd=None):
        """\
        <name> <notice> - add a good/bad behavior note for the player
        """
        m = self.parseUserCmd(data)
        if not m or m[0] == '' or m[1] == '':
            client.message(self.getMessage('invalid_parameters'))
            return False

        cid, notice = m
        sclient = self.findClientPrompt(cid, client)
        if sclient:
            if sclient.maxLevel >= client.maxLevel:
                client.message('^7Can not add notice to higher level admin %s' % sclient.exactName)
            else:
                sclient.notice(notice, None, client)
                client.message('^7Notice %s added to %s' % (notice, sclient.exactName))

    def cmd_warn(self, data, client=None, cmd=None):
        """\
        <name> [<warning>] - warn user
        """
        m = self.parseUserCmd(data)
        if not m:
            client.message(self.getMessage('invalid_parameters'))
            return

        cid, keyword = m
        sclient = self.findClientPrompt(cid, client)
        if sclient:
            if sclient.id == client.id:
                client.message(self.getMessage('warn_self', client.exactName))
            elif sclient.maxLevel >= client.maxLevel:
                client.message(self.getMessage('warn_denied', client.exactName, sclient.exactName))
            else:
                if sclient.var(self, 'warnTime').toInt() > self.console.time() - self.warn_delay:
                    client.message(self.getMessage('warn_too_fast', {'num_second': self.warn_delay}))
                    return

                self.warnClient(sclient, keyword, client)

    def cmd_warntest(self, data, client=None, cmd=None):
        """\
        <warning> - test a warning
        """
        try:
            duration, warning = self.getWarning(data)
        except Exception:
            duration, warning = self.getWarning('generic')
            warning = '%s %s' % (warning, data)

        warning = warning % {'name': client.exactName}
        client.message('^2TEST: %s' % self.config.getTextTemplate('warn', 'message', warnings=1, reason=warning))
        return True

    def cmd_warnremove(self, data, client=None, cmd=None):
        """\
        <name> - remove a users last warning
        """
        m = self.parseUserCmd(data)
        if not m:
            client.message(self.getMessage('invalid_parameters'))
            return False

        sclient = self.findClientPrompt(m[0], client)
        if sclient:
            w = sclient.lastWarning
            if not sclient.numWarnings or not w:
                client.message('^7No warnings found for %s' % sclient.exactName)
                return

            if w.adminId:
                try:
                    admin = self.console.storage.getClient(Client(id=w.adminId))
                    if admin.maxLevel > client.maxLevel:
                        client.message('^7You can not clear a warning from %s' % admin.exactName)
                    return
                except Exception:
                    pass

            w.inactive = 1
            self.console.storage.setClientPenalty(w)

            cmd.sayLoudOrPM(client, '%s ^7last warning cleared: ^3%s' % (sclient.exactName, w.reason))

    def cmd_warnclear(self, data, client=None, cmd=None):
        """\
        <name> - clear all of a users warnings
        """
        m = self.parseUserCmd(data)
        if not m:
            client.message(self.getMessage('invalid_parameters'))
            return False

        sclient = self.findClientPrompt(m[0], client)
        if sclient:
            if not sclient.numWarnings:
                client.message('^7No warnings found for %s' % sclient.exactName)
                return

            cleared = 0
            failed = 0
            for w in sclient.warnings:
                if w.adminId:
                    try:
                        admin = self.console.storage.getClient(Client(id=w.adminId))
                        if admin.maxLevel > client.maxLevel:
                            failed += 1
                        break
                    except Exception:
                        pass

                cleared += 1
                w.inactive = 1
                self.console.storage.setClientPenalty(w)

            if failed and cleared:
                cmd.sayLoudOrPM(client, '^7Cleared ^3%s ^7warnings and left ^3%s ^7warnings for %s' % (
                                        failed, cleared, sclient.exactName))
            elif failed:
                client.message('^7Could not clear ^3%s ^7warnings for %s' % (failed, sclient.exactName))
            else:
                self.console.say('^7All warnings cleared for %s' % sclient.exactName)

    def cmd_warninfo(self, data, client=None, cmd=None):
        """\
        <name> - display how many warning points a user has
        """
        m = self.parseUserCmd(data)
        if not m:
            client.message(self.getMessage('invalid_parameters'))
            return False

        sclient = self.findClientPrompt(m[0], client)
        if sclient:
            warns = sclient.numWarnings

            if warns:
                msg = ''
                warn = sclient.firstWarning
                if warn:
                    expire = functions.minutesStr((warn.timeExpire - (self.console.time())) / 60)
                    msg = ', expires in ^2%s' % expire

                warn = sclient.lastWarning
                if warn:
                    msg += '^7: ^3%s' % warn.reason

                message = '^7%s ^7has ^1%s ^7active warnings%s' % (sclient.exactName, warns, msg)
            else:
                message = '^7%s ^7has no active warnings' % sclient.exactName

            cmd.sayLoudOrPM(client, message)

    def cmd_maps(self, data, client=None, cmd=None):
        """\
        - list the server's map rotation
        """
        if not self.aquireCmdLock(cmd, client, 60, True):
            client.message('^7Do not spam commands')
            return

        maps = self.console.getMaps()
        if maps is None:
            client.message('^7Error: could not get map list')
        elif len(maps):
            cmd.sayLoudOrPM(client, '^7Map Rotation: ^2%s' % '^7, ^2'.join(maps))
        else:
            cmd.sayLoudOrPM(client, '^7Map Rotation list is empty')

    def cmd_nextmap(self, data, client=None, cmd=None):
        """\
        - list the next map in rotation
        """
        if not self.aquireCmdLock(cmd, client, 60, True):
            client.message('^7Do not spam commands')
            return

        mapname = self.console.getNextMap()
        if mapname:
            cmd.sayLoudOrPM(client, '^7Next Map: ^2%s' % mapname)
        else:
            client.message('^7Error: could not get map list')

    def cmd_pause(self, data, client=None, cmd=None):
        """\
        <duration> - pause the bot from parsing
        """
        m = re.match('^([0-9]+[a-z]*)$', data)
        if not m:
            client.message(self.getMessage('invalid_parameters'))
            return False

        duration = functions.time2minutes(data)
        self.console.say('^7Sleeping for %s' % functions.minutesStr(duration))
        unpause_task = threading.Timer(duration * 60, self.console.unpause)
        unpause_task.daemon = True # won't block the bot in case of shutdown
        self.console.pause()
        unpause_task.start()

    def cmd_spam(self, data, client=None, cmd=None):
        """\
        [player] <message> - spam a predefined message to all players or a given player
        """
        m = re.match('^((?P<player>\w+)\s+)?(?P<keyword>\w{2,})$', data)
        if not m:
            client.message(self.getMessage('invalid_parameters'))
            return
        keyword = m.group("keyword")
        msg = self.getSpam(keyword)
        if not msg:
            client.message('^7Could not find spam message %s' % keyword)
            return
        player_name = m.group("player")
        if not player_name:
            if cmd and cmd.big:
                self.console.saybig(msg)
            else:
                self.console.say(msg)
            return
        sclient = self.findClientPrompt(player_name, client)
        if sclient:
            sclient.message(msg)


    def cmd_rules(self, data, client=None, cmd=None):
        """\
        - say the rules
        """
        if not self.aquireCmdLock(cmd, client, 60, True):
            client.message('^7Do not spam commands')
            return

        m = self.parseUserCmd(data)
        if m:
            if client.maxLevel >= self._admins_level:
                sclient = self.findClientPrompt(m[0], client)
                if not sclient:
                    return

                if sclient.maxLevel >= client.maxLevel:
                    client.message('%s ^7already knows the rules' % sclient.exactName)
                    return
                else:
                    client.message('^7Sir, Yes Sir!, spamming rules to %s' % sclient.exactName)
            else:
                client.message('^7Stop trying to spam other players')
                return
        elif cmd.loud or cmd.big:
            thread.start_new_thread(self._sendRules, (), {'sclient': None, 'big': cmd.big})
            return
        else:
            sclient = client

        thread.start_new_thread(self._sendRules, (), {'sclient': sclient})

    def cmd_spams(self, data, client=None, cmd=None):
        """\
        - list spam messages
        """
        ws = sorted(self.config.options('spamages'))
        if len(ws):
            client.message('^7Spamages: %s' % ', '.join(ws))
        else:
            client.message('^7no spamage message defined')

    def cmd_tempban(self, data, client=None, cmd=None):
        """\
        <name> <duration> [<reason>] - temporarily ban a player
        """
        m = self.parseUserCmd(data)

        if not m or not m[1]:
            client.message(self.getMessage('invalid_parameters'))
            return False

        cid = m[0]
        m = re.match('^([0-9]+[dwhsm]*)(?:\s(.+))?$', m[1], re.I)
        if not m:
            client.message(self.getMessage('invalid_parameters'))
            return False

        duration, keyword = m.groups()
        duration = functions.time2minutes(duration)

        #    10/05/2008 - 1.3.4b0 - mindriot
        #      * Removed hard code of 1 day for long_tempban_level - now controlled with new
        #        setting 'long_tempban_max_duration'
        try:
            long_tempban_max_duration = self.config.getDuration('settings', 'long_tempban_max_duration')
        except NoOptionError:
            long_tempban_max_duration = self._long_tempban_max_duration
            self.debug('Using default value (%s) for long_tempban_max_duration', self._long_tempban_max_duration)

        if client.maxLevel < self._long_tempban_level and duration > long_tempban_max_duration:
            # temp ban for maximum specified in settings
            duration = long_tempban_max_duration

        reason = self.getReason(keyword)

        if not reason and client.maxLevel < self._noreason_level:
            client.message(self.getMessage('error_no_reason'))
            return False
        elif not duration:
            client.message('^7You must supply a duration to ban for')
            return False

        sclient = self.findClientPrompt(cid, client)
        if sclient:
            if sclient.cid == client.cid:
                self.console.say(self.getMessage('temp_ban_self', client.exactName))
                return True
            elif sclient.maxLevel >= client.maxLevel:
                if sclient.maskGroup:
                    client.message(self.getMessage('action_denied_masked', {'name': sclient.exactName}))
                else:
                    self.console.say(self.getMessage('temp_ban_denied', client.exactName, sclient.exactName))
                return True
            else:
                sclient.tempban(reason, keyword, duration, client)
                return True
        elif re.match('^[0-9]+$', cid):
            # failsafe, do a manual client id ban
            self.console.tempban(cid, reason, duration, client)

    def cmd_poke(self, data, client=None, cmd=None):
        """\
        <player> - Notify a player that he needs to move
        """
        m = self.parseUserCmd(data)
        if not m:
            client.message(self.getMessage('invalid_parameters'))
            return False

        if m[0] == 'b3':
            self.warnClient(client, 'Do not poke b3!', None, False, '', 1)
        else:
            sclient = self.findClientPrompt(m[0], client)
            if sclient:
                message = random.choice(('Wake up', '*poke*', 'Attention', 'Get up', 'Go', 'Move out'))
                self.console.say('^7%s %s^7!' % (message, sclient.exactName))

    def cmd_pluginfo(self, data, client=None, cmd=None):
        """\
        <plugin> - display information on the specified plugin
        """
        if not data:
            client.message(self.getMessage('invalid_parameters'))
            return

        # lowercase the input string
        data = data.strip().lower()
        if data == 'admin':
            a = __author__
            v = __version__
        else:

            try:
                # check if it's a standard plugin
                package = 'b3.plugins.%s' % data
                module = __import__(package)
                components = package.split('.')
                for comp in components[1:]:
                    module = getattr(module, comp)
            except ImportError:
                fp = None
                try:
                    # check if it's an external plugin
                    fp, path, desc = imp.find_module(data, [self.console.config.getpath('plugins', 'external_dir')])
                    module = imp.load_module(data, fp, path, desc)
                except (ImportError, NoOptionError):
                    fp = None
                    module = None
                finally:
                    if fp:
                        fp.close()

            if not module:
                client.message('^7No plugin named ^1%s ^7loaded' % data)
                return

            a = getattr(module, '__author__', 'Unknown Author')
            v = getattr(module, '__version__', 'Unknown Version')

        # cleanup a bit the author
        # some people put also website and/or email address in it
        r1 = re.compile(r'(?:http[s]?://|www.)[^\s]*')  # web
        r2 = re.compile(r'[a-zA-Z0-9._%-+]+@[a-zA-Z0-9._%-]+.[a-zA-Z]{2,6}')  # email

        if re.search(r1, a):
            a = re.sub(r1, '', a)
            a = re.sub(re.compile(r'-|\|'), '', a)

        if re.search(r2, a):
            a = re.sub(r2, '', a)
            a = re.sub(re.compile(r'-|\|'), '', a)

        a = a.strip()
        n = '%sPlugin' % data.title()
        cmd.sayLoudOrPM(client, '%s v ^3%s ^7by ^3%s' % (n, v, a))


#commandstxt = file('commands.txt', 'w')
class Command:
    command = ''
    help = ''
    level = 0
    secretLevel = 0
    func = None
    alias = ''
    plugin = None
    time = 0
    prefix = '!'
    prefixLoud = '@'
    prefixBig = '&'

    PLAYER_DATA = re.compile(r'^([\w\d\s-]+|@\d+|\d+)$', re.I)
    _reType = type(re.compile('.*'))

    def __init__(self, plugin, cmd, level, func, help=None, alias=None, secretLevel=100):
        """\
        Build a new command object
        """
        self.command = cmd.strip()
        self.func = func
        self.plugin = plugin
        self.loud = False
        self.big = False
        self.private = False

        if help:
            self.help = help.strip()
        if alias:
            self.alias = alias.strip()

        level = str(level)
        if level.lower() == 'none':
            self.level = None
        elif level.count('-') == 1:
            level = level.split('-', 1)
            self.level = (int(level[0]), int(level[1]))
        else:
            self.level = (int(level), 100)

        if secretLevel is None:
            self.secretLevel = 100

            # global commandstxt
            # commandstxt.write('%s (%s) %s, levels %s - %s\n' % (self.command, self.alias,
            #                                                     self.help, self.level[0], self.level[1]))
            # commandstxt.flush()

    def canUse(self, client):
        """\
        Check whether a client can use such command
        """
        if self.level is None:
            return False
        else:
            return self.level[0] <= int(client.maxLevel) <= self.level[1]

    def execute(self, data, client):
        """\
        Execute a command
        """
        self.func(data, client, copy.copy(self))
        self.time = self.plugin.console.time()

    def executeLoud(self, data, client):
        """\
        Execute a command a redirect the output to console say
        """
        cmd = copy.copy(self)
        cmd.loud = True
        self.func(data, client, cmd)
        self.time = self.plugin.console.time()

    def executeBig(self, data, client):
        """\
        Execute a command and redirect the output to console saybig
        """
        cmd = copy.copy(self)
        cmd.big = True
        self.func(data, client, cmd)
        self.time = self.plugin.console.time()

    def executePrivate(self, data, client):
        """\
        Execute a command and redirect the output to console saytell
        """
        cmd = copy.copy(self)
        cmd.private = True
        self.func(data, client, cmd)
        self.time = self.plugin.console.time()

    def sayLoudOrPM(self, client, message):
        """\
        Display a message with visibility regulated by the command prefix
        """
        if self.loud:
            self.plugin.console.say(message)
        elif self.big:
            self.plugin.console.saybig(message)
        else:
            client.message(message)

    def parseData(self, data, *args):
        """\
        Parse command data
        """
        _p = self.splitData(data)

        if not len(args):
            return _p

        params = {}

        i = 0
        for i in range(0, min(len(args), len(_p))):
            params[args[i][0]] = _p[i]

        if len(_p) > i:
            params[args[i][0]] = ' '.join(_p[i:])

        badfield = None
        valid = True
        for a in args:
            if not a[0] in params.keys() or len(params[a[0]]) == 0:
                if len(a) == 3:
                    # set the default
                    params[a[0]] = a[2]
                else:
                    badfield = a[0]
                    valid = False
                    break

            if len(a) > 1:
                if type(a[1]) == self._reType:
                    # see if it matches regexp
                    valid = re.match(a[1], params[a[0]])

                    if not valid:
                        badfield = a[0]
                else:
                    # see if it can be converted to type
                    try:
                        params[a[0]] = a[1](params[a[0]])
                    except ValueError:
                        badfield = a[0]
                        valid = False

        if valid:
            return params, None
        else:
            h = ['^1Input Error! ^7Example: ']
            if self.loud:
                h.append('%s%s' % (self.prefixLoud, self.command))
            else:
                h.append('%s%s' % (self.prefix, self.command))

            for a in args:
                if len(a) == 3:
                    #optional
                    parm = '[%s]' % a[0]
                else:
                    parm = '<%s>' % a[0]

                if a[0] == badfield:
                    parm = '^1%s^7' % parm

                h.append(parm)

            return None, ' '.join(h)

    def splitData(self, data):
        """\
        Split command parameters
        """
        params = []
        buf = ''
        in_quote = False
        in_dquote = False
        for c in str(data).strip():
            if c == "'":
                if in_dquote:
                    buf += c
                elif in_quote:
                    params.append(buf)
                    buf = ''
                    in_quote = False
                elif len(buf):
                    buf += c
                else:
                    in_quote = True
                    buf = ''
            elif c == '"':
                if in_dquote:
                    params.append(buf)
                    buf = ''
                    in_dquote = False
                elif in_quote:
                    buf += c
                elif len(buf):
                    buf += c
                else:
                    in_dquote = True
                    buf = ''
            elif c.isspace():
                if len(buf):
                    if in_dquote or in_quote:
                        if not buf[-1].isspace():
                            buf += c
                    else:
                        params.append(buf)
                        buf = ''
            else:
                buf += c

        if len(buf):
            params.append(buf)

        return params

    def __repr__(self):
        return "Command<" + self.command + ">"