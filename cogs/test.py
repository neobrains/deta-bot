import discohook


class Test(discohook.Cog):
    @discohook.Cog.command(name="test", description="Test for subcommands")
    async def test(self, magic: discohook.Interaction):
        pass

    @test.subcommand(name="subcommand", description="Test subcommand")
    async def general(self, magic: discohook.Interaction):
        return await magic.command.response(content="Test!")


def setup(client: discohook.Client):
    client.add_cog(Test())
