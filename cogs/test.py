import discohook.discohook as discohook


class Test(discohook.Cog):
    @discohook.Cog.command(name="test", description="YoOOOOOOOOOOO TEST!")
    async def test(self, magic: discohook.Interaction):
        await magic.command.response("Test!")


def setup(client: discohook.Client):
    client.add_cog(Test())
