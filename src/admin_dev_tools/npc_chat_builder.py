# We want to create a json file that contains all the npc chat data
# This is used to create the npc chat data for the game
# We will prompt the admin to enter the npc chat data, then provide all the action codes and the response translations
# options will structure

# in the backend, we will need to map the NPC id with the NPC chat session ids,
# and then map each of the NPC chat session ids with the NPC chat options, which trigger action codes (which might start another chat session or end the chat session or trigger a different event)


import json
import click
import os, sys

chat_data = {}
npc_id = ''

@click.group()
def cli(self):
    """
    Defines the command line interface for the NPC chat builder admin tool
    Reads the chat_session_data.json file and loads the pre-existing data into a list

    Args:
        None
    Returns:
        None
    """
    click.echo('Welcome to the NPC Chat Builder!')
    click.echo('This tool will help you create/modify a JSON file that contains all the NPC chat data for a new NPC')

    # try open JSON file
    with open(os.path.join(sys.path[0], 'chat_session_data.json'), 'r') as f:
        self.chat_data = json.load(f)
        click.echo('JSON file opened successfully!')
    
    id = click.prompt('Please enter the NPC ID for the NPC you want to create the NPC chat data for',
                'Or enter a new NPC ID to create a new session')
    get_npc(id)

@click.command()
@click.argument('input')
def get_npc(self, npc_id: str):
    """
    Asks user to specify an NPC to look up

    Args:
        npc_id: str
            The ID of the NPC object to look up, 0 for a new NPC
    Returns:
        None
    """
    click.echo(f'\nNPC ID: {npc_id}')

    # Create new NPC ID if not exists
    if npc_id not in chat_data:
        click.echo('Creating new NPC chat data for NPC ID: ' + npc_id)
        self.chat_data[self.npc_id] = {}
    # Look up correct NPC ID otherwise
    else:
        click.echo('NPC chat data already exists for NPC ID: ' + npc_id)
        
        # Check for new session or updating old session
        if not click.confirm('Do you want to delete the existing NPC chat sessions?'):
            click.echo('Overwriting existing NPC chat data for NPC ID: ' + npc_id)
            self.chat_data[self.npc_id] = {}
        else:
            click.echo(f'Adding/updating new options to existing NPC chat data for NPC ID: {npc_id}')

'''
# list out all the NPC chat sessions for the NPC and the description of the session (developer notes)

for chat_session_id in chat_data[npc_id]:
    print(chat_session_id, chat_data[chat_session_id]['description'])

print('\nPlease enter the session id for the session you want to update the NPC chat data for, or enter 0 to create a new session')
chat_session_id = input('Session ID: ')
if chat_session_id == '0':
    print('Creating new NPC chat session')
    chat_session_id = len(chat_data[npc_id]) + 1
    chat_data[npc_id][chat_session_id] = {}
    chat_data[npc_id][chat_session_id]['options'] = []
    chat_data[npc_id][chat_session_id]['features'] = []
    chat_data[npc_id][chat_session_id]['requirements'] = {} # requirements to start a session (e.g. min_player_level, completed_quest_id, has_inventory_item, etc)
else:
    # make sure the session id exists
    if chat_session_id not in chat_data[npc_id]:
        print('Session ID: ' + chat_session_id + ' does not exist for NPC ID: ' + npc_id)
        sys.exit()

print('Updating existing NPC chat session')
chat_data[npc_id][chat_session_id]['description'] = input('Session description: ')

# now we need to add the options for the NPC chat session and specify any unique limiting features (such as CANNOT_EXIT or CANNOT_REPEAT or CANNOT_SKIP or REQUIREMENTS)
"""
action codes
    EXIT_CHAT
    TRIGGER_EVENT
    START_NEW_SESSION
action code parameter
    with enemies
        fight
    with party members, will start a dialogue tree
        start_confidant_dialogue
        end_confidant_dialogue
    with quest givers
        start_quest
        progress_quest
        end_quest
"""
def add_option(option_id, order_id, translation_code, translation_text, action_code, action_code_parameter, action_code_parameter_type):
    chat_data[npc_id][chat_session_id]['options'].append({
        'id': option_id, # unique id for the option
        'order': order_id, # this is the order in which the options are displayed to the player
        'translation_code': translation_code, # this is the translation code for the option text
        'action_code': action_code, # e.g. EXIT_CHAT or TRIGGER_EVENT or START_NEW_CHAT_SESSION
        'action_code_parameter': action_code_parameter, # e.g. None or 'fight' or 'start_quest' or 'progress_quest' or 'end_quest'
        'action_code_parameter_type': action_code_parameter_type # e.g. None or quest_id (int), or npc_id (int)
    })
    # also add the translation text in our translation_data.eng.json file
    with open(os.path.join(sys.path[0], 'translation_data.eng.json'), 'r') as f:
        translation_data = json.load(f)
    translation_data[translation_code] = translation_text
    with open(os.path.join(sys.path[0], 'translation_data.eng.json'), 'w') as f:
        json.dump(translation_data, f, indent=4)


print('\nExisting options for NPC chat session')
for option in chat_data[npc_id][chat_session_id]['options']:
    print(option['id'], ':', option['order'], option['translation_code'], option['action_code'], option['action_code_parameter'], option['action_code_parameter_type'])

# ask if they want to add a new option, update an existing option, or enter 0 to finish
print('What do you want to do?')
print('1. Add a new option')
print('2. Update an existing option')
print('3. Delete an existing option')
print('.')
print('0. Finish')
selection = input('Choice: ')

# finally, we can save the updated chat data to the chat_session_data.json file
# FIXME: write to the same file that it opened at the start
def saveFile():
    with open(os.path.join(sys.path[0], 'chat_session_data.json'), 'w') as f:
        json.dump(chat_data, f)

while selection != '0':
    if selection == '1':
        print('Adding a new option')
        option_id = len(chat_data[npc_id][chat_session_id]['options']) + 1
        order_id = input('Order ID: ')
        translation_code = input(
            'Translation code (translation code to be looked up in the translation dictionary) e.g. GANON_BOSS_FIGHT_1: ')
        translation_text = input('Translation text (text to be displayed to the player): ')
        action_code = input('Action code (e.g. EXIT_CHAT or TRIGGER_EVENT or START_CHAT)  : ')
        action_code_parameter = input('Action code parameter (leave blank for None):')
        action_code_parameter_type = input('Action code parameter type (leave blank for None): ')
        if action_code_parameter == '':
            action_code_parameter = None
        if action_code_parameter_type == '':
            action_code_parameter_type = None
        add_option(option_id, order_id, translation_code, translation_text, action_code, action_code_parameter,
                   action_code_parameter_type)
    elif selection == '2':
        # TODO: make sure the option exists, otherwise ask again
        # TODO: add a proper menu system instead of just doing everything linearly
        print('Updating an existing option')
        option_id = input('Option ID: ')
        order_id = input('Order ID: ')
        translation_code = input(
            'Translation code (translation code to be looked up in the translation dictionary) e.g. GANON_BOSS_FIGHT_1: ')
        translation_text = input('Translation text (text to be displayed to the player): ')
        action_code = input('Action code (e.g. EXIT_CHAT or TRIGGER_EVENT or START_CHAT)  : ')
        action_code_parameter = input('Action code parameter (leave blank for None):')
        action_code_parameter_type = input('Action code parameter type (leave blank for None): ')
        if action_code_parameter == '':
            action_code_parameter = None
        if action_code_parameter_type == '':
            action_code_parameter_type = None
        add_option(option_id, order_id, translation_code, translation_text, action_code, action_code_parameter,
                   action_code_parameter_type)
    elif selection == '3':
        print('Deleting an existing option')
        option_id = input('Option ID: ')
        for option in chat_data[npc_id][chat_session_id]['options']:
            if option['id'] == option_id:
                chat_data[npc_id][chat_session_id]['options'].remove(option)
                break

if selection == '0':
    saveFile()
    print('Done!')

                
        
"""
new NPC
-> checks for chat data
-> loads all the chat sessions for the npc, translates if necessary

NPC->startChatSession(3)
NPC->rampUpHealth()
NPC->rampUpMana()
NPC->fightTheBoss(50)
NPC->startQuest(1) 
"""
'''

cli()
