#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 13:12:34 2021

@author: ciaranmcdonnell
"""

"""
Let's program a game of blackjack:
    - Use functions for the actions (methods in classes would be better but 
                                     let's practice functions)
    - Limit to one deck of cards, dictionary.
    - Loop through game.
    
"""

import random as rand
import numpy as np
from replit import clear
import time


deck = {'Suits': ['Clubs','Hearts','Diamonds','Spades'],
        'Cards': ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
        }
values = {'Ace':np.array([1,11]),'2':np.array([2]),'3':np.array([3]),'4':np.array([4]),
          '5':np.array([5]),'6':np.array([6]),'7':np.array([7]),
          '8':np.array([8]),'9':np.array([9]),'10':np.array([10]),'Jack':np.array([10]),
          'Queen':np.array([10]),'King':np.array([10])}


def generate_deck():
    """generate a new full deck"""
    
    full_deck ={}
    full_card_list = [] # Can't get the random choice from dictionaries to work...
    for i in deck['Suits']:
        for j in deck['Cards']:
            # print(j +' of ' + i + ': ' + str(values[j]))
            full_deck[j +' of ' + i]= values[j]
            full_card_list.append([j +' of ' + i])
    return full_deck, full_card_list

def draw_card(list_deck):
    "Draws one card from current deck"
    
    draw = rand.choice(list_deck)
    
    list_deck.remove(draw)
    

    return draw, list_deck



def deal_cards(players, list_deck):
    """Deal initial hands"""
    player_hands = {}
    
    for i in players:
        draw, list_deck = draw_card(list_deck)

        draw2, list_deck = draw_card(list_deck)
        
        
        if len(full_deck[draw[0]]) == 2 and len(full_deck[draw2[0]]) == 2:
            player_hands[i] = {'Cards':[draw, draw2],'Value': np.array([2,13])}
        player_hands[i] = {'Cards':[draw, draw2],'Value': np.array([full_deck[draw[0]]+ full_deck[draw2[0]]])}
        
    draw_house, list_deck = draw_card(list_deck)
    draw_house1, list_deck = draw_card(list_deck)
    house_hand = {'Cards':[draw_house, draw_house1],'Value': np.array([full_deck[draw_house[0]]+full_deck[draw_house1[0]]])}
    return player_hands, house_hand, list_deck    
        
        
print('============ Welome to Blackjack ============')  
        
# Collecting all player names  
players = []        
num_players = int(input('How many players are there?: '))
for j in range(num_players):
    players.append( input('Player ' + str(j+1) + ': ')  )
    
   
    
# Generates the initial player and house hands saved in two dictionaries player_hands
# and house_hang - Keys are 'Cards' and 'Value'    
full_deck, full_card_list = generate_deck()    
player_hands, house_hand, current_card_list = deal_cards(players, full_card_list)
end_players = {}

   
for k in players:
   # clear() 
    print('House cards: ____ | ' + house_hand['Cards'][1][0] + '\n')
    print(k + "'s hand: " + player_hands[k]['Cards'][0][0] +' | ' 
          + player_hands[k]['Cards'][1][0] + ': ' + str(player_hands[k]["Value"][0]))
    

    player_done = False
    
    while player_done == False:
        print_hand = ''
        
        go = input('Would you like to hit(1) or stick(0) ?: ' )
        
        if go != '1' and go != '0':
             print('Please enter valid choice')
            # break
        
            
        elif go == '0':
            
            end_players[k] = max([ l for l in player_hands[k]["Value"][0] if l <= 21])
            break
        
        elif go == '1':
            draw, current_card_list = draw_card(current_card_list)
            player_hands[k]['Cards'].append(draw)
            player_hands[k]['Value'] = player_hands[k]['Value'] + full_deck[draw[0]]
            
            for n in player_hands[k]['Cards']:
                print_hand += n[0] + ' | '
            
            print(k + "'s hand: " + print_hand  + ': ' + str(player_hands[k]["Value"][0]) +'\n')
            if (player_hands[k]['Value'][0]>21).all():
                print(k + ' has gone bust!')
                time.sleep(3)
                break           
        
            
        
        clear()
        print('House cards: ____ and ' + house_hand['Cards'][1][0] + '\n')
        print(k + "'s hand: " + print_hand  + ': ' + str(player_hands[k]["Value"][0]) +'\n')
        
        
# Now the turn of the house
house_turn_done = False
first_end_players = dict(end_players)
while house_turn_done == False:
    end_players_aux = dict(end_players)
    print_h_hand = ''
    house_max = max([ h for h in house_hand["Value"][0] if h <= 21])
    
    # Remove players beaten by house
    for pl in end_players_aux:
        if house_max >= end_players[pl]:
            del end_players[pl]
           
    # Check if anyone still beating the house.       
    if len(end_players) == 0: 
        for nn in house_hand['Cards']:
                print_h_hand += nn[0] + ' | '
        print('House beats everyone: ' + print_h_hand +': ' + str(house_max))
        house_turn_done = True
    
    elif len(end_players)/num_players < 0.25 and house_max > 15:
        high_winners = ''
        for w in end_players:
            high_winners += w + '. '
            
        print(f'House sticks. Winners are: {high_winners}')    
        house_turn_done = True
        
    else:
        draw, current_card_list = draw_card(current_card_list)
        house_hand['Cards'].append(draw)
        house_hand['Value'] = house_hand['Value'] + full_deck[draw[0]]
        
    # Check if the house has gone bust    
    if (house_hand['Value'][0]>21).all():
        winner_names = ''
        
        for winners in first_end_players:
            winner_names += winners + '. '
            
        print(f'House is bust! Winners are: \n  {winner_names}')
        house_turn_done = True
        
    
        
        
        
        
        
            