
#    Copyright (C) Midhun KM 2020
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
# 
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from telethon import events
from telethon.tl import functions

@chatbot.on(events.ChatAction())
async def _(event):
  okbruh = await chatbot.get_me()
  if event.user_joined or event.user_added == str(okbruh):
    if event.chat_id == Config.DUMB_CHAT:
      pass
      return
    else:
      await chatbot.send_message(event.chat_id, "I'm Not Made for Groups, I only Stay at Groups which my Master Allows. So, Exiting Chat Now !")
      await event.client.kick_participant(event.chat_id, okbruh)
