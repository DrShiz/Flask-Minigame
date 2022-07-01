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

    global player
    global enemy

    enemy_class = random.choice(characters)
    if enemy_class == 'knight':
        enemy = Knight_enemy()
    elif enemy_class == 'magician':
        enemy = Magician_enemy()
    elif enemy_class == 'archer':
        enemy = Archer_enemy()
    enemy.health = enemy.max_health

    try:
        player.health = player.max_health
    except:
        pass

    if request.method == 'POST':
        player = form.player.data
        if player == 'Knight':
            player = Knight_player()
        elif player == 'Magician':
            player = Magician_player()
        elif player == 'Archer':
            player = Archer_player()
        return redirect(url_for("fight", enemy_class=enemy_class))
        
    return render_template('index.html', enemy_class=enemy_class, form=form)


@app.route('/fight/enemy:<enemy_class>/', methods=['GET', 'POST'])
def fight(enemy_class):

    form = FightForm()

    if request.method == 'POST':
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

        attack_target = form.attack_target.data
        player_dices = player.roll_the_dice()
        enemy_dices = enemy.roll_the_dice()
        
        attacked_by_enemy = random.choice(player.parts)

        def make_a_hit(winner, looser, attacked_part):
            was_hit = False
            hit = 0
            if randrange(1,10) in range(1, int(chances[attack_target]*10)):
                was_hit = True
            if was_hit:
                hit = winner.strength * abs((sum(player_dices) - sum(enemy_dices))) * hit_strength[attacked_part]
                looser.health -= hit
                if looser.health < 0:
                    looser.health = 0

            return (was_hit, hit)

        if sum(player_dices) > sum(enemy_dices):
            (was_hit, hit) = make_a_hit(player, enemy, attack_target)
        elif sum(player_dices) < sum(enemy_dices):
            (was_hit, hit) = make_a_hit(enemy, player, attacked_by_enemy)
        else:
            (was_hit, hit) = (True, 0)
    
        return jsonify(
            player_dices=player_dices, 
            enemy_dices=enemy_dices,
            attacked_by_enemy=attacked_by_enemy,
            was_hit=was_hit,
            hit=hit, 
            player_hp=player.health, 
            enemy_hp=enemy.health
        )

    return render_template(
        'fight.html', 
        form=form, 
        enemy=enemy,
        player=player)


if __name__ == '__main__':
    app.run(debug=True)