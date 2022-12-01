import discohook


class Tags(discohook.Cog):
    @discohook.Cog.command(name="tag", description="Tag system")
    async def tag(self, magic: discohook.Interaction):
        pass

    @tag.subcommand(name="test", description="Test command")
    async def tag_test(self, magic: discohook.Interaction):
        await magic.command.response("Test!")


def setup(client: discohook.Client):
    client.add_cog(Tags())
