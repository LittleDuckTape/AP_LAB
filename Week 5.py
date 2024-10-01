import math

class Circle:
    pi = math.pi

    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def getColor(self):
        return self.color
    
    def getCircum(self):
        return 2 * Circle.pi * self.radius
    
# example:
circle = Circle(37, 'Orange')
print('Color:', circle.getColor()) # output should be Orange
print('Circumference:', circle.getCircum()) # output should be around 232.48

#------------------------------

class Player:
    def __init__(self, name, initial_money=100, initial_health=100):
        self.name = name
        self.money = initial_money
        self.health = initial_health
        self.inventory = {}

    # inventory system
    def addItem(self, item, quantity):
        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity
        print(f'{quantity} {item}(s) have been added to your inventory.')

    def removeItem(self, item, quantity):
        if item in self.inventory and self.inventory[item] >= quantity:
            self.inventory[item] -= quantity
            if self.inventory[item] == 0:
                del self.inventory[item]
            print(f'{quantity} {item}(s) have been removed from your inventory.')
        else:
            print(f'Not enough {item}(s) in your inventory to remove.')

    # money system
    def addMoney(self, amount):
        self.money += amount
        print(f'{amount}G added. Current balance: {self.money}G.')
    
    def spendMoney(self, amount):
        if self.money >= amount:
            self.money -= amount
            print(f'{amount}G spent. Current balance: {self.money}G.')
        else:
            print(f'Not enough Gold.')

    # health system
    def takeDamage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            self.checkStatus()
        else:
            print(f'{self.name} has taken {amount} damage. Current HP: {self.health}.')
    
    def checkStatus(self):
        if self.health == 0:
            print(f'{self.name} is dead.')

    def heal(self, amount):
        self.health += amount
        print(f'{self.name} is healed by {amount}HP. Current HP: {self.health}')

# example:
player = Player(name='Himmel')

player.addItem('Potion', 3)
player.addItem('Sword', 1)
player.removeItem('Potion', 1)

player.addMoney(50)
player.spendMoney(70)

player.takeDamage(20)
player.takeDamage(100)
player.heal(65)

#------------------------------

# i couldn't think of anything so i just expanded on your player class, sorry man TT
class Irene:
    def __init__(self, name, health=100, mana=50, attack=85, defense=70, speed=55):
        self.name = name
        self.level = 1
        self.experience = 0
        self.skills = []
        self.inventory = {}
        self.health = health
        self.mana = mana
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.weapon = None
    
    # levels & exp
    def levelUp(self):
        self.level += 1
        self.health = min(self.health + 20, 200)
        self.mana = min(self.mana + 10, 150)
        self.attack = min(self.attack + 15, 150)
        self.defense = min(self.defense + 20, 200)
        self.speed = min(self.speed + 15, 120)
        print(f"{self.name} leveled up to level {self.level}!")
        print(f"HP: {self.health}, MP: {self.mana}, ATK: {self.attack}, DEF: {self.defense}, SPD: {self.speed}.")


    def experienceToNextLevel(self):
        return 100 * self.level

    def gainExperience(self, exp):
        self.experience += exp
        print(f"{self.name} gained {exp} experience points. Total EXP: {self.experience}.")
        while self.experience >= self.experienceToNextLevel():
            self.experience -= self.experienceToNextLevel()
            self.levelUp()

    # inventory & weapon
    def equipWeapon(self, weapon_name):
        if weapon_name in self.inventory and isinstance(self.inventory[weapon_name], dict):
            self.weapon = weapon_name
            weapon_damage = self.inventory[weapon_name]["details"].get("damage", 0)
            print(f"{self.name} equipped {weapon_name} with {weapon_damage} damage.")
        else:
            print(f"{weapon_name} is not a weapon in your inventory.")


    def addItem(self, item, quantity=1, details=None):
        if item in self.inventory:
            self.inventory[item]["quantity"] += quantity
        else:
            self.inventory[item] = {"quantity": quantity, "details": details or {}}
        print(f"{item} added to your inventory.")

    # skills
    def useSkill(self, skill):
        for learned_skill in self.skills:
            if learned_skill["name"] == skill:
                mana_cost = learned_skill["mana_cost"]
                if self.mana >= mana_cost:
                    self.mana -= mana_cost
                    print(f"{self.name} used {skill}. Remaining MP: {self.mana}.")
                else:
                    print(f"Not enough MP to use {skill}.")
                return
        print(f"{skill} is not a learned skill.")

    def learnSkill(self, skill, mana_cost=10):
        if all(s["name"] != skill for s in self.skills):
            self.skills.append({"name": skill, "mana_cost": mana_cost})
            print(f"{self.name} learned {skill} (Cost: {mana_cost} MP)!")
        else:
            print(f"{self.name} already knows {skill}.")
        
    # battle stuff
    def attackEnemy(self, enemy):
        if self.weapon:
            weapon_damage = self.inventory[self.weapon]["details"].get("damage", 0)
            damage = self.attack + weapon_damage - enemy.defense
            damage = max(damage, 0)
            enemy.health -= damage
            print(f"{self.name} attacked {enemy.name} for {damage} damage!")
        else:
            print(f"{self.name} doesn't have a weapon equipped.")
    
    # health & mana recovery
    def heal(self, amount):
        self.health = min(self.health + amount, 100)
        print(f"{self.name} healed by {amount}. Current HP: {self.health}.")

    def checkHealth(self):
        if self.health <= 0:
            print(f"{self.name} has fallen in battle.")
        else:
            print(f"{self.name} has {self.health} HP remaining.")


    def recoverMana(self, amount):
        self.mana = min(self.mana + amount, 50)
        print(f"{self.name} recovered {amount} mana. Current MP: {self.mana}.")

# example:
player = Irene("Reine")

player.gainExperience(150)

player.addItem("Staff", details={"damage": 15})
player.addItem("Potion", quantity=2)
player.equipWeapon("Staff")

player.learnSkill("Fireball", mana_cost=15)
player.useSkill("Fireball")

player.heal(20)
player.recoverMana(10)

enemy = Irene("Goblin", health=80, defense=50)
player.attackEnemy(enemy)

# output current stats
print(f"Irene's Current Status: Level: {player.level}, EXP: {player.experience}, HP: {player.health}, MP: {player.mana}")
print(f"Enemy's Current Status: {enemy.name}'s HP: {enemy.health}")
