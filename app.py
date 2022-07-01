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
    if enemy_class == 'Knight':
        enemy = Knight_enemy()
    elif enemy_class == 'Magician':
        enemy = Magician_enemy()
    elif enemy_class == 'Archer':
        enemy = Archer_enemy()

    try:
        player.health = player.max_health
        enemy.health = enemy.max_health
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

        player_attack_target = form.player_attack_target.data
        player_dices = player.roll_the_dice()
        enemy_dices = enemy.roll_the_dice()
        
        enemy_attack_target = random.choice(list(player.parts.keys()))

        def make_a_hit(winner, looser, attacked_part):
            was_hit = False
            hit = 0
            if randrange(1,10) in range(1, int(looser.parts[player_attack_target]['chance']*10)):
                was_hit = True
            if was_hit:
                hit = winner.strength * abs((sum(player_dices) - sum(enemy_dices))) * looser.parts[attacked_part]['criticality']
                looser.health -= hit
                if looser.health < 0:
                    looser.health = 0

            return (was_hit, hit)

        if sum(player_dices) > sum(enemy_dices):
            (was_hit, hit) = make_a_hit(player, enemy, player_attack_target)
        elif sum(player_dices) < sum(enemy_dices):
            (was_hit, hit) = make_a_hit(enemy, player, enemy_attack_target)
        else:
            (was_hit, hit) = (True, 0)
    
        return jsonify(
            player_dices=player_dices, 
            enemy_dices=enemy_dices,
            enemy_attack_target=enemy_attack_target,
            player_attack_target=player_attack_target,
            was_hit=was_hit,
            hit=hit, 
            player_hp=player.health, 
            enemy_hp=enemy.health,
            player_max_hp=player.max_health, 
            enemy_max_hp=enemy.max_health
        )

    return render_template(
        'fight.html', 
        form=form, 
        enemy=enemy,
        player=player)


if __name__ == '__main__':
    app.run(debug=True)