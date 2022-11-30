import discohook.discohook as discohook


class Tags(discohook.Cog):
    @discohook.Cog.command(
        name="tag",
        description="Display tag",
        options=[
            discohook.StringOption(
                name="name", description="The tag to retrieve", required=True
            )
        ],
    )
    async def tag(self, magic: discohook.Interaction, name):
        await magic.command.response(name)


def setup(client: discohook.Client):
    client.add_cog(Tags())
