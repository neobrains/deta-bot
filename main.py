import os
import discohook

app = discohook.Client(
    application_id=int(os.getenv("APPLICATION_ID")),
    public_key=os.getenv("PUBLIC_KEY"),
    token=os.getenv("DISCORD_TOKEN"),
    log_channel_id=902228501120290866,
    mode="static",
)
app.load_cogs("cogs.docs", "cogs.rescue")
