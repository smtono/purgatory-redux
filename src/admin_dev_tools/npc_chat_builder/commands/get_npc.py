import click

@click.command()
@click.argument('input')
def get_npc(self, chat_data, input: str):
    """
    Specify an NPC to look up

    User enters an NPC identifier that is stored in the JSON file associated with this CLI
    If the ID exists, returns that data associated with that ID
    If not, creation of a new chat session associated with that ID will be created

    Args:
        chat_data: dict
            The dict object returned when loading the JSON file
        npc_id: str
            The ID of the NPC object to look up, 0 for a new NPC
    Returns:
        None
    """
    # prompt user for ID
    id = click.prompt('Please enter the NPC ID for the NPC you want to create the NPC chat data for',
                'Or enter a new NPC ID to create a new session')
    click.echo(f'\nNPC ID: {input}')

    # Attempt to create new NPC ID if not exists
    if input not in chat_data:
        inp = click.input('NPC does not exist! Would you like to create a new session? (y/n)')
        done = False
        while not done:
            if inp == 'y':
                done = True
                pass
            elif inp == 'n':
                done = True
                pass
            else:
                click.echo("Invalid input...Please input (y/n)")
    # Look up correct NPC ID otherwise
    else:
        click.echo('NPC chat data already exists for NPC ID: ' + input)
        
        # Check for new session or updating old session
        if not click.confirm('Do you want to delete the existing NPC chat sessions?'):
            click.echo('Overwriting existing NPC chat data for NPC ID: ' + input)
            self.chat_data[self.npc_id] = {}
        else:
            click.echo(f'Adding/updating new options to existing NPC chat data for NPC ID: {input}')