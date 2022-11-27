import discohook.discohook as discohook


class Docs(discohook.Cog):
    @discohook.Cog.command(name="docs", description="Search deta.sh docs")
    async def docs(self, magic: discohook.Interaction):
        pass

    @docs.subcommand(
        name="base",
        description="Deta base docs",
        options=[
            discohook.StringOption(
                name="topic",
                description="Base topic",
                required=True,
                choices=[
                    discohook.Choice(name="About", value="about"),
                    discohook.Choice(name="SDK", value="sdk"),
                    discohook.Choice(name="HTTP API", value="http"),
                    discohook.Choice(name="Queries", value="queries"),
                    discohook.Choice(name="Base UI", value="base_ui"),
                    discohook.Choice(name="Expiring Items", value="expiring_items"),
                    discohook.Choice(name="Node.js Tutorial", value="node_tutorial"),
                    discohook.Choice(name="Python Tutorial", value="python_tutorial"),
                ],
            )
        ],
    )
    async def deta_base(self, magic: discohook.Interaction, topic: str):
        return await magic.command.response(content=topic)


def setup(client: discohook.Client):
    client.add_cog(Docs())
