"""
This module contains the CLI for the NPC Chat Builder.

Usage:
    python3 dialogue_cli.py
"""
import json
import sys
import os

def read_chat_data() -> dict:
    """
    Reads the chat data from the chat data file.

    Args:
        None
    Returns:    
        The chat data from the chat data file.
    Raises:
        None
    """
    with open('chat_data.json', 'r') as chat_data_file:
        chat_data = json.load(chat_data_file)
    return chat_data

def find_npc_id(chat_data: dict) -> int:
    """
    Finds the npc_id specified by the user from the chat data.
    
    Args:
        chat_data: The chat data from the chat data file.
    Returns:
        The npc_id specified by the user.
    Raises:
        None
    """
    print('Please enter the NPC ID for the NPC you want to create the NPC chat data for')
    npc_id = input('\nNPC ID: ')
    if npc_id not in chat_data:
        print('Creating new NPC chat data for NPC ID: ' + npc_id)
        chat_data[npc_id] = {}
    else:
        print('NPC chat data already exists for NPC ID: ' + npc_id)
        print('Do you want to delete the existing NPC chat sessions, or update the data?')
        print('1. Yes - delete existing chat sessions (overwrite existing sessions)')
        print('2. No - add new options to existing NPC chat data')
        overwrite_choice = input('Choice: ')
        if overwrite_choice == '1':
            print('Overwriting existing NPC chat data for NPC ID: ' + npc_id)
            chat_data[npc_id] = {}
        else:
            print('Adding/updating new options to existing NPC chat data for NPC ID: ' + npc_id)

def print_npc_chat_data(chat_data: dict) -> None:
    """
    Prints the NPC chat data to the console.
    
    Args:
        chat_data: The chat data from the chat data file.
    Returns:
        None
    Raises:
        None
    """
    print('\nNPC Chat Data:')
    for npc_id in chat_data:
        print('NPC ID: ', npc_id)
        for chat_session in chat_data[npc_id]:
            print('Chat Session: ', chat_session)

def update_npc_chat_data(chat_data: dict, npc_id: int) -> None:
    """
    Updates the NPC chat data.
    
    Args:
        chat_data: The chat data from the chat data file.
    Returns:
        None
    Raises:
        None
    """
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

# FIXME: add types for the arguments
def add_option(
    chat_data: dict, 
    npc_id: int, 
    chat_session_id: int,
    option_id: int, 
    order_id: int, 
    action_code, 
    action_code_condition, 
    translation_code: int=None, 
    translation_text: str=None):
    """
    Adds options to the NPC chat data.

    Some examples for options:
    action codes
        EXIT_CHAT
        TRIGGER_EVENT
        START_NEW_SESSION
    action code conditions
        with enemies
            fight
        with party members, will start a dialogue tree
            start_confidant_dialogue
            end_confidant_dialogue
        with quest givers
            start_quest
            progress_quest
            end_quest
    
    Args:
        option_id: the ID of the option
        order_id: the order of the option
        action_code: the trigger event for the option
        action_code_condition: the condition in which the event will be triggered
        translation_code: the translation code of the option
        translation_text: the translated text of the option
    Returns:
        None
    Raises:
        None
    """
    chat_data[npc_id][chat_session_id]['options'].append({
        'id': option_id, # unique id for the option
        'order': order_id, # this is the order in which the options are displayed to the player
        'translation_code': translation_code, # this is the translation code for the option text
        'action_code': action_code, # e.g. EXIT_CHAT or TRIGGER_EVENT or START_NEW_CHAT_SESSION
        'action_code_condition': action_code_condition, # e.g. None or 'fight' or 'start_quest' or 'progress_quest' or 'end_quest'
        #'action_code_parameter_type': action_code_parameter_type # e.g. None or quest_id (int), or npc_id (int)
    })
    # also add the translation text in our translation_data.eng.json file
    with open(os.path.join(sys.path[0], 'translation_data.eng.json'), 'r') as f:
        translation_data = json.load(f)
    translation_data[translation_code] = translation_text
    with open(os.path.join(sys.path[0], 'translation_data.eng.json'), 'w') as f:
        json.dump(translation_data, f, indent=4)

def print_option(option: dict) -> None:
    """
    Prints the option to the console.
    
    Args:
        option: The option to print.
    Returns:
        None
    Raises:
        None
    """
    print('Option ID: ', option['id'])
    print('Order: ', option['order'])
    print('Translation Code: ', option['translation_code'])
    print('Action Code: ', option['action_code'])
    print('Action Code Condition: ', option['action_code_condition'])
    print('Action Code Parameter Type: ', option['action_code_parameter_type'])

def print_all_options(chat_data: dict, npc_id: int, chat_session_id: int) -> None:
    """
    Prints all options for the NPC chat data.
    
    Args:
        chat_data: The chat data from the chat data file.
    Returns:
        None
    Raises:
        None
    """
    print('\nExisting options for NPC chat session')
    for option in chat_data[npc_id][chat_session_id]['options']:
        print(
            option['id'], ':', 
            option['order'], 
            option['translation_code'], 
            option['action_code'], 
            option['action_code_parameter'], 
            option['action_code_parameter_type'])
        
def saveFile(chat_data: dict, file_path: str) -> None:
    with open(os.path.join(sys.path[0], 'chat_session_data.json'), 'w') as f:
        json.dump(chat_data, f)

"""
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

                
        
'''
new NPC
-> checks for chat data
-> loads all the chat sessions for the npc, translates if necessary
NPC->startChatSession(3)
NPC->rampUpHealth()
NPC->rampUpMana()
NPC->fightTheBoss(50)
NPC->startQuest(1) 
'''
"""

# FIXME: call functions involved in creating a new NPC
def create_npc(chat_data: dict, npc_id: int):
    """
    Creates a new NPC

    Args:
        chat_data: the chat data for the NPC
        npc_id: the ID of the NPC
    Returns:
        the NPC
    Raises:
        KeyError: if the NPC ID is already in use
    """
    npc_id = len(chat_data) + 1
    chat_data[npc_id] = {}
    return npc_id

# FIXME: call functions involved in creating a new chat session
def manage_npc(chat_data: dict, npc_id: int):
    """
    Manages an NPC

    Args:
        chat_data: the chat data for the NPC
        npc_id: the ID of the NPC
    Returns:
        the NPC
    Raises:
        KeyError: if the NPC ID is not in use
    """
    print('What do you want to do?')
    print('1. Add a new option')
    print('2. Update an existing option')
    print('3. Delete an existing option')
    print('.')
    print('0. Finish')
    selection = input('Choice: ')

def cli() -> int:
    """
    Create an interface for creating and managing NPCs.

    Args:
        None
    Returns:
        int: 0 if successful, 1 if not
    Raises:
        None
    """
    print('Welcome to the NPC Chat Builder!')
    print('This tool will help you create a json file that contains all the npc chat data for a new NPC')
    print('What do you want to do?')
    print('1. Create a new NPC')
    print('2. Manage an existing NPC')
    print('3. Exit')
    selection = input('Choice: ')
    if selection == '1':
        #create_npc()
        pass
    elif selection == '2':
        #manage_npc()
        pass
    elif selection == '3':
        print('Goodbye!')
        return
    else:
        print('Invalid selection')
        cli()
