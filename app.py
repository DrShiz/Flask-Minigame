from flask import Flask, render_template, request, url_for, redirect, jsonify
from project.forms import FightForm
from project.characters import *
from random import randrange
import random


app = Flask(__name__)
app.secret_key = 'fuy(&^)+ugisuiksdbib&)%^*fffP(*Y_99990JJJJ_989yhh3!@#$%'


@app.route('/', methods=['GET', 'POST'])
def main():
    form = FightForm()
    enemy_class = random.choice(characters)

    if 'enemy' in globals():
        enemy.health = enemy.max_health

    if 'player' in globals():
        player.health = player.max_health
    # if request.method == 'POST':
    #     player = form.player.data
    #     if player == 'Knight':
    #         player = Knight()
    #     elif player == 'Magician':
    #         player = Magician()
    #     elif player == 'Archer':
    #         player = Archer()
    #     return redirect(url_for("fight", enemy=enemy))
    return render_template('index.html', enemy_class=enemy_class, form=form)


@app.route('/fight/enemy:<enemy_class>/', methods=['GET'])
def fight(enemy_class):
    form = FightForm()

    if 'enemy' not in globals():
        global enemy
        if enemy_class == 'knight':
            enemy = Knight_enemy()
        elif enemy_class == 'magician':
            enemy = Magician_enemy()
        elif enemy_class == 'archer':
            enemy = Archer_enemy()

    if 'player' not in globals():
        global player
        player = request.args['player']
        if player == 'Knight':
            player = Knight_player()
        elif player == 'Magician':
            player = Magician_player()
        elif player == 'Archer':
            player = Archer_player()

    return render_template(
        'fight.html', 
        form=form, 
        enemy=enemy,
        player=player)

@app.route('/fight/enemy:<enemy_class>/', methods=['POST'])
def fight_hit(enemy_class):
    form = FightForm()
    player_parts = ['head', 'body', 'hands', 'legs']
    chances = {
        'head': 0.7,
        'body': 0.9,
        'hands': 0.4,
        'legs': 0.6
    }
    hit_strength = {
        'head': 1,
        'body': 0.8,
        'hands': 0.3,
        'legs': 0.5
    }

    if request.method == 'POST':
        attack_target = form.attack_target.data
        player_dices = (randrange(1, 6), randrange(1, 6))
        enemy_dices = (randrange(1, 6), randrange(1, 6))
        was_hit = False
        attacked_by_enemy = ''
        hit = 0
        if sum(player_dices) > sum(enemy_dices):
            if randrange(1,10) in range(1, int(chances[attack_target]*10)):
                was_hit = True
            if was_hit:
                hit = player.strength * (sum(player_dices) - sum(enemy_dices)) * hit_strength[attack_target]
                enemy.health -= hit
                if enemy.health < 0:
                    enemy.health = 0
        else:
            attacked_by_enemy = random.choice(player_parts)
            if randrange(1,10) in range(1, int(chances[attacked_by_enemy]*10)):
                was_hit = True
            if was_hit:
                hit = enemy.strength * (sum(enemy_dices) - sum(player_dices)) * hit_strength[attacked_by_enemy]
                player.health -= hit
                if player.health < 0:
                    player.health = 0
        return jsonify(
            player_dices=player_dices, 
            enemy_dices=enemy_dices,
            attacked_by_enemy=attacked_by_enemy,
            was_hit=was_hit,
            hit=hit, 
            player_hp=player.health, 
            enemy_hp=enemy.health
            # enemy_class=enemy_class
        )

if __name__ == '__main__':
    app.run(debug=True)