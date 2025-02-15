TOKEN = "YOUR_TOKEN_HERE"

bot_prefix = "mch!"
bot_status_type = 0  # unknown = -1, playing = 0, streaming = 1, listening = 2, watching = 3, custom = 4, competing = 5
bot_status_message = "with commands"

bot_owner_id = 263862604915539969  # Tomlacko, can use Application owners if set to None

bot_logs_channel_id = 729090739702595596  # bot-logs
muted_role_id = 721780279643209789

log_onload_event = True

use_jishaku = True

database_dir = "database"
cogs_dir = "cogs"
cogs = {
    "test_commands": True,
    "util_commands": True,
    "embed_creator": True,
    "welcome_messages": False,
    "new_accounts_alerts": True,
    "bottom_message": True,
    "muteme": True,
    "mojira_embeds": True,
    "fun_commands": True,
    "mathstuff": True,
    "debugging": False,
}

permission_levels = {
    720725702516932658: 200,  # Administrator
    774373485015072801: 150,  # Server Mod
    738045010519392317: 140,  # Bot+
    720725754605994087: 100,  # Chat Mod
    889242293310214194: 90,  # Bot
    720778741701410866: 70,  # PPA
    722845569403322369: 50,  # PCA
    756990603945967639: 20,  # Member
    766083300682498088: 10,  # Project Contributor
}
