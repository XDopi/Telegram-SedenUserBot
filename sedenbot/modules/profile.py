from os import remove
from time import sleep

from sedenbot import HELP, TEMP_SETTINGS
from sedenecem.core import (
    download_media_wc,
    edit,
    extract_args,
    get_download_dir,
    get_translation,
    sedenify,
    send_log,
)

# ====================== CONSTANT ===============================
ALWAYS_ONLINE = 'offline'
# ===============================================================

@sedenify(pattern='^.online', compat=False)
def online(client, message):
    args = extract_args(message)
    offline = ALWAYS_ONLINE in TEMP_SETTINGS
    if args == 'disable':
        if offline:
            del TEMP_SETTINGS[ALWAYS_ONLINE]
            edit(message, f'`{get_translation("alwaysOnlineOff")}`')
            return
        else:
            edit(message, f'`{get_translation("alwaysOnlineOff2")}`')
            return
    elif offline:
        edit(message, f'`{get_translation("alwaysOnline2")}`')
        return

    TEMP_SETTINGS[ALWAYS_ONLINE] = True

    edit(message, f'`{get_translation("alwaysOnline")}`')

    while ALWAYS_ONLINE in TEMP_SETTINGS:
        try:
            client.send(UpdateStatus(offline=False))
            sleep(5)
        except BaseException:
            return


HELP.update({'profile': get_translation('profileInfo')})
