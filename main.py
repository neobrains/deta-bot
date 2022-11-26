import os
import discohook.discohook as discohook

app = discohook.Client(
    application_id=int(os.getenv("APPLICATION_ID")),
    public_key=os.getenv("PUBLIC_KEY"),
    token=os.getenv("DISCORD_TOKEN"),
    express_debug=True,
)

app.load_cog("cogs.test")
