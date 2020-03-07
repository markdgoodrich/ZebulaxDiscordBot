import random


#if hit, 10% chance
#if d20, 25% chance

#Roll d12
#if 4-7, roll d20
#if 10, roll d10
#if 11, roll 3d10
#if 12, roll d6
#   if 1, roll 1d4
#

def limb_loss():
    chosen_limb = random.randint(1,5)
    limbs = {
            1: "Head",
            2: "Left Leg",
            3: "Right Leg",
            4: "Left Arm",
            5: "Right Arm"
            }
    ailment = {
            1: "is Blind",
            2: "has half it's speed",
            3: "has half it's speed",
            4: "loses a multiattack",
            5: "loses a multiattack"
            }
    return("AutoGnome's %s has fallen off!  AutoGnome %s!") %(limbs[chosen_limb], ailment[chosen_limb])

def autoGnome_malfunction():
    malfunction = random.randint(1,12)
    #malfunction = 6
    
    if malfunction == 1 or malfunction == 2:
        return("AutoGnome has gone rogue! They're attacking the closest creature!")
    elif malfunction == 3:
        return("AutoGnome has hurt themselves in their confusion! They're attacking themselves for %d rounds!" %int(random.randint(1,4)))
    elif malfunction == 4 or malfunction == 5:
        return(limb_loss())
    elif malfunction == 6 or malfunction == 7:
        reattach = 'AutoGnome spends its turn reattaching one of its limbs.'
        return("%s %s") %(limb_loss(), reattach )
    elif malfunction == 8 or malfunction == 9:
        return("AutoGnome is trying to take a core sample from its victim!  All multiattacks now deal 1d12 until next malfunction.")
    elif malfunction == 10:
        return("AutoGnome has shut down for %d minutes!" %random.randint(1,10))
    elif malfunction == 11:
        threed10 = 0
        for i in range(1,4):
            threed10 += random.randint(1,10)    #roll 3 d10
        return("AutoGnome self destructs!  BOOM! That's %d damage.  Everyone in a 20' radius make a Dex save for half." %threed10)
    elif malfunction == 12:
        d6 = random.randint(1,6)
        if d6 == 1:
            return("Autognome will self destruct for 3d10 damage in %d rounds!  Quick! Someone through water on them!" %random.randint(1,4))
        elif d6 == 2:
            return("Autognome will now give their report.")
        elif d6 == 3:
            return("Autognome asks to record report, and remains stationary until the PC stops talking.")
        elif d6 == 4:
            return("Autognome begins talking backwards.")
        elif d6 == 5:
            return("Autognome recognizes the nearest PC as a baby.")
        elif d6 == 6:
            return("Autognome recognizes the nearest PC as a gnome, and will follow them around.")


#print(autoGnome_malfunction())
