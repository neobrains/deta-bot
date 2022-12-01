import deta
import discohook

db = deta.Deta().base("tags")

modal = discohook.Modal(title="Modal")
modal.add_field(
    label="Tag name",
    field_id="name",
    max_length=25,
    required=True,
)
modal.add_field(
    label="Tag content",
    field_id="content",
    max_length=3,
    required=True,
    default_text="**Tags** support _markdown_! Read more about `discord markdown` here: https://support.discord.com/hc/en-us/articles/210298617-Markdown-Text-101-Chat-Formatting-Bold-Italic-Underline-",
)


@modal.on_submit
async def modal_submit(magic: discohook.Interaction, name: str, content: str):
    await magic.command.response(f"Tag name: {name} \n Tag content: {content}")


class Tags(discohook.Cog):
    @discohook.Cog.command(name="tag", description="Tag system")
    async def tag(self, magic: discohook.Interaction):
        pass

    @tag.subcommand(name="create", description="Create tag")
    async def tag_create(self, magic: discohook.Interaction):
        await magic.send_modal(modal)


def setup(client: discohook.Client):
    client.add_cog(Tags())
