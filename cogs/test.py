import discohook


class Test(discohook.Cog):
    @discohook.Cog.command(name="test", description="some test command")
    async def test(self, magic: discohook.Interaction):
        await magic.command.response("done!")


def setup(client: discohook.Client):
    client.add_cog(Test())
