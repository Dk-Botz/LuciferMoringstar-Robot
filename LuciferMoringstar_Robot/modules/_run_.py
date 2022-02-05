from pyrogram import Client as LuciferMoringstar_Robot, filters as Worker
from LuciferMoringstar_Robot.modules.autofilter import group_filters, pm_autofilter
from config import AUTH_GROUPS, AUTH_USERS



@LuciferMoringstar_Robot.on_message(Worker.text & Worker.group & Worker.incoming & Worker.chat(AUTH_GROUPS) if AUTH_GROUPS else Worker.text & Worker.group & Worker.incoming)
async def groupfilters(client, message):
    await group_filters(client, message)



@LuciferMoringstar_Robot.on_message(Worker.text & Worker.private & Worker.incoming & Worker.user(AUTH_USERS) if AUTH_USERS else Worker.text & Worker.private & Worker.incoming)
async def pm_filters(client, message):
    await pm_autofilter(client, message)


