import click

@click.command()
def print_npc_data(self, chat_data, npc_id) -> None:
    """
    Prints all NPC chat data in the JSON file opened

    Args:
        chat_data: dict
            A JSON object unloaded containing chat session for NPCs
        npc_id: str
            Specified by the user of which NPC chat session to access
    Returns:
        None
    Raises:
        None
    """
    # list out all the NPC chat sessions for the NPC and the description of the session (developer notes)
    for chat_session_id in chat_data[npc_id]:
        print(chat_session_id, chat_data[chat_session_id]['description'])