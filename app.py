from flask import Flask, render_template, request, url_for, redirect, jsonify
from project.forms import FightForm
from project.characters import *
from random import randrange
import random
import jsonpickle
import json


app = Flask(__name__)
app.secret_key = 'fuy(&^)+ugisuiksdbib&)%^*fffP(*Y_99990JJJJ_989yhh3!@#$%'


@app.route('/', methods=['GET', 'POST'])
def main():
    form = FightForm()

    global player
    global enemy

    enemy_class = random.choice(characters)
    if enemy_class == 'Knight':
        enemy = Knight()
    elif enemy_class == 'Magician':
        enemy = Magician()
    elif enemy_class == 'Archer':
        enemy = Archer()

    if request.method == 'POST':
        player_class = form.player.data
        if player_class == 'Knight':
            player = Knight()
        elif player_class == 'Magician':
            player = Magician()
        elif player_class == 'Archer':
            player = Archer()

        return redirect(url_for("fight", enemy_class=enemy_class))
        
    return render_template('index.html', enemy_class=enemy_class, form=form)


@app.route('/use_item/', methods=['POST'])
def use_item():
    item_id = request.json['item_id']
    player.inventory['items'][item_id].use(player)
    player.inventory['items'].pop(item_id, None)
    return jsonify(
        player=jsonpickle.encode(player, unpicklable=True),
        )

@app.route('/fight/enemy:<enemy_class>/', methods=['GET', 'POST'])
def fight(enemy_class):

    form = FightForm()

    if request.method == 'POST':
        # print(json.dumps(player))

        player.attack_target = form.player_attack_target.data
        player.roll_the_dice()
        enemy.roll_the_dice()
        
        enemy.attack_target = random.choice(list(player.parts.keys()))

        def make_a_hit(winner, looser, attacked_part):
            was_hit = False
            hit = 0
            if randrange(1,10) in range(1, int(looser.parts[player.attack_target]['chance']*10)):
                was_hit = True
            if was_hit:
                hit = winner.strength * (sum(winner.dices) - sum(looser.dices)) * looser.parts[attacked_part]['criticality']
                if winner.dices[0] == winner.dices[1]:
                    hit *= 2
                looser.health -= hit
                if looser.health < 0:
                    looser.health = 0

            return (was_hit, hit)

        if sum(player.dices) > sum(enemy.dices):
            (was_hit, hit) = make_a_hit(player, enemy, player.attack_target)
        elif sum(player.dices) < sum(enemy.dices):
            (was_hit, hit) = make_a_hit(enemy, player, enemy.attack_target)
        else:
            (was_hit, hit) = (True, 0)
    


        return jsonify(
            was_hit=was_hit,
            hit=hit,
            player = jsonpickle.encode(player, unpicklable=True),
            enemy = jsonpickle.encode(player, unpicklable=True), 
        )

    return render_template(
        'fight.html', 
        form=form, 
        enemy=enemy,
        player=player)


if __name__ == '__main__':
    app.run(debug=True)