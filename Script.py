class script(object):
    START_TXT = """𝗛𝗲𝗹𝗹𝗼 {}, 𝗠𝘆𝗡𝗮𝗺𝗲 𝗶𝘀 Rᴀꜱʜᴍɪᴋᴀ Mᴀɴᴅᴀɴɴᴀ 
 
𝗜 𝗮𝗺 𝗮𝗻 𝗔𝘂𝘁𝗼𝗙𝗶𝗹𝘁𝗲𝗿 𝗕𝗼𝘁 𝗠𝗮𝗱𝗲 𝗳𝗼𝗿 𝗧𝗲𝗮𝗺 @KR_PICTURE ™🎥 
 
𝗝𝗼𝗶𝗻 𝗠𝘆 𝗚𝗿𝗼𝘂𝗽 & 𝗨𝗽𝗱𝗮𝘁𝗲𝘀 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 𝗳𝗼𝗿 𝗠𝗼𝗿𝗲 𝗗𝗲𝘁𝗮𝗶𝗹𝘀."""
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂.
"""
    ABOUT_TXT = """<b>
○ 𝗠𝘆 𝗡𝗮𝗺𝗲 : 𝙲𝚒𝚗𝚎𝚖𝚊 𝚕𝚘𝚔𝚑𝚊𝚖
○ 𝗖𝗿𝗲𝗮𝘁𝗼𝗿 : <a href=https://t.me/Nikhil5757h>Dictator</a>
○ 𝗟𝗶𝗯𝗿𝗮𝗿𝘆 : Pyrogram
○ 𝗟𝗮𝗻𝗴𝘂𝗮𝗴𝗲 : Python 3.10
○ 𝗗𝗮𝘁𝗮𝗕𝗮𝘀𝗲 : Mongo 𝙳𝙱
○ 𝗠𝘆 𝗦𝗲𝗿𝘃𝗲𝗿 : Koyeb
○ 𝗕𝘂𝗶𝗹𝗱 𝗩𝗲𝗿𝘀𝗶𝗼𝗻 : V1.0 [ 𝙱𝙴𝚃𝙰 ]</b>"""
    SOURCE_TXT = """<b>NOTE:</b>
- RASHMIKA ʙᴏᴛ™ is a private project. 
- Source - <ahref=https://t.me/KR_PICTURE>Click Here😂</a>

<b>DEVS:</b>
- <a href=https://t.me/Nikhil5757h>Dictator</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>
- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message
<b>NOTE:</b>
1. This Bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Eva Maria Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. This Botsupports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/KR_PICTURE)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    FORCESUBSCRIBE_TXT = """Help: <b>𝗙𝗼𝗿𝗰𝗲𝗦𝘂𝗯 𝗠𝗼𝗱</b>

<b>𝗡𝗼𝘁𝗲:
    𝗧𝗵𝗶𝘀 𝗺𝗼𝗱𝘂𝗹𝗲 𝗼𝗻𝗹𝘆 𝘄𝗼𝗿𝗸𝘀 𝗳𝗼𝗿 𝗺𝘆 𝗔𝗱𝗺𝗶𝗻𝘀</b>

<b>𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀 𝗮𝗻𝗱 𝗨𝘀𝗮𝗴𝗲:</b>

• /fsub - Enable ForceSub / Request Sub Settings
• /add_fsub - Add ForceSub / Request Sub Channel
• /get_fsub - Get saved ForceSub Channel Detail
• /ttreq - Get total request counts on current FSub Channel
• /clreq - Clear Requests on current FSub Channel"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> """
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    RESULT_TXT="""Eᴅᴀᴀ Mᴏɴᴇʜ I Fᴏᴜɴᴅ Iɴ Mʏ Dʙ Fᴏʀ Yᴏᴜʀ Qᴜᴇʀʏ {}"""

    CUSTOM_FILE_CAPTION = """<b>{file_name}

𝗝𝗼𝗶𝗻 𝗢𝘂𝗿 𝗖𝗵𝗮𝗻𝗻𝗲𝗹𝘀 ⚡️
𝐌𝐚𝐢𝐧 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 👇
https://t.me/sandalwood_kannada_moviesz

𝐑𝐞𝐪𝐮𝐞𝐬𝐭 𝐌𝐨𝐯𝐢𝐞𝐬 👇
https://t.me/Sandalwood_Kannada_Group</b>"""

    
    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ
@Nikhil5757h</b>"""
    
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
    SPOLL_NOT_FND="""Eᴅᴀᴀ Mᴏɴᴇʜ🤚🏻
I couldn't find anything related to your request. 😵
Try reading the instruction below 👇🏼
    """
#SPELL CHECK LANGUAGES TO KNOW callback
    ENG_SPELL="""Please Note Below📓
1️⃣Ask in Correct Spelling
2️⃣Don't ask Movies which are not Realased on OTT PLATFORMS
3️⃣Possible  ASK [movie name langauge] like this or [movie year]
    """
    MAL_SPELL="""ദയവായി താഴെ ശ്രദ്ധിക്കുക📓
1️⃣ശരിയായ അക്ഷരവിന്യാസത്തിൽ ചോദിക്കുക
2️⃣OTT പ്ലാറ്റ്‌ഫോമുകളിൽ റിലീസ് ചെയ്യാത്ത സിനിമകൾ ചോദിക്കരുത്
3️⃣ഇത് പോലെ [സിനിമയുടെ പേര് ഭാഷ] അല്ലെങ്കിൽ [സിനിമ വർഷം] ചോദിക്കാം
    """
    HIN_SPELL="""कृपया नीचे ध्यान दें📓
1️⃣सही वर्तनी में पूछें
2️⃣उन फिल्मों के बारे में न पूछें जो ओटीटी प्लेटफॉर्म पर रिलीज नहीं हुई हैं
3️⃣संभव है पूछें [मूवी का नाम भाषा] इस तरह या [मूवी वर्ष]
    """
    TAM_SPELL="""கீழே கவனிக்கவும்📓
1️⃣சரியான எழுத்துப்பிழையில் கேளுங்கள்
2️⃣வெளியாகாத திரைப்படங்களைக் கேட்காதீர்கள்
3️⃣இந்த வடிவத்தில் கேளுங்கள் [திரைப்படத்தின் பெயர், ஆண்டு]
    """

    CHK_MOV_ALRT="""♻️ Eᴅᴀᴀ Mᴏɴᴇʜ ᴄʜᴇᴄᴋɪɴɢ ꜰɪʟᴇ ᴏɴ ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ... ♻️"""
    
    OLD_MES=""" Eᴅᴀᴀ Mᴏɴᴇʜ 𝐘𝐨𝐮 𝐚𝐫𝐞 𝐮𝐬𝐢𝐧𝐠 𝐨𝐧𝐞 𝐨𝐟 𝐦𝐲 𝐨𝐥𝐝 𝐦𝐞𝐬𝐬𝐚𝐠𝐞𝐬🤔, 𝐩𝐥𝐞𝐚𝐬𝐞 𝐬𝐞𝐧𝐝 𝐭𝐡𝐞 𝐫𝐞𝐪𝐮𝐞𝐬𝐭 𝐚𝐠𝐚𝐢𝐧"""
    
    MOV_NT_FND="""<b>Eᴅᴀᴀ Mᴏɴᴇʜ Tʜɪs Mᴏᴠɪᴇ Is Nᴏᴛ Yᴇᴛ Rᴇᴀʟᴇsᴇᴅ Oʀ Aᴅᴅᴇᴅ Tᴏ DB</b>
Report To ADMIN - @Nikhil5757h
"""
    DMCA_TXT = """<b><u>This Telegram bot is designed to operate within the guidelines of the Digital Millennium Copyright Act (DMCA) and respects intellectual property rights. We are committed to responding to any valid DMCA takedown notices promptly.</u></b>

<blockquote>Please send your DMCA takedown notice to @Nikhil5757h</blockquote>
"""
