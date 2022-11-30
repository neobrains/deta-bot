import discohook.discohook as discohook
from extras.func import get_docs


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
                    discohook.Choice(name="Async SDK", value="async_sdk"),
                    discohook.Choice(name="HTTP API", value="HTTP"),
                    discohook.Choice(name="Queries", value="queries"),
                    discohook.Choice(name="Base UI", value="base_ui"),
                    discohook.Choice(name="Expiring Items", value="expiring_items"),
                    discohook.Choice(name="Node.js Tutorial", value="node_tutorial"),
                    discohook.Choice(name="Python Tutorial", value="py_tutorial"),
                ],
            ),
            discohook.StringOption(
                name="query", description="Query base topic", required=True
            ),
        ],
    )
    async def deta_base(self, magic: discohook.Interaction, topic: str, query: str):
        e = discohook.Embed(
            title=f"{topic.capitalize()}",
            url=f"https://docs.deta.sh/docs/base/{topic}/#{query}",
            description=get_docs(section="base", doc_page=topic, doc_query=query),
            color=0xEE4196,
        )
        return await magic.command.response(
            embed=e,
        )


def setup(client: discohook.Client):
    client.add_cog(Docs())
