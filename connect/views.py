from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.tokens import default_token_generator

from .board import Connect_4 
from .models import Game
import uuid

# Initialising the Board
connect_4 = Connect_4()


def home(request):
  return render(request, "connect/home.html", status=200)


# start the game
def start(request):
  connect_4.reset()

  uid = str(uuid.uuid4())
  game = Game(token = uid)

  game.save()

  return JsonResponse({ 'body' : 'ready', 'token' : uid}, status=200, safe=False)

# Insert in Column
def insert(request):

  col = int(request.GET.get('column'))
  token = request.GET.get('token')
  player = int(request.GET.get('player'))
  
  game = Game.objects.filter(token = token).first()

  if not game:
    return JsonResponse ({'body' : 'Invalid Token'}, status=401)

  if game.winner:
    return JsonResponse ({'body' : f'Winner -> {game.winner}'})

  response = connect_4.insert_in_col(col, player)
  
  game.moves += f"{str((connect_4.player_color.get(player), col))}   " 
  
  if response != 'Invalid':
    player = connect_4.player_color.get(player)
    if connect_4.has_won(response, player):
      game.winner = player
      game.save()
      if player == 'Y':
        return JsonResponse({'body' : 'Yellow Wins'})
      else:
        return JsonResponse({'body' : 'Red Wins'})
    response = 'Valid'
  
  game.save()

  return JsonResponse({'body' : response})

def get_moves(request):
  token = request.GET.get('token')

  game = Game.objects.filter(token = token).first()

  if not game:
    return JsonResponse ({'body' : 'Invalid Token'}, status=401)

  return JsonResponse ({'moves' : f"{game.moves}"})