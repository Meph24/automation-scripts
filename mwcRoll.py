#!/usr/bin/python

from random import randint

def rndRace():
 return ['Altmer','Argonian','Bosmer','Breton','Dunmer','Imperial','Khajiit','Nord','Orc','Redguard'][randint(0,9)]

def rndSign():
 return ['Warrior','Mage','Thief','Serpent','Lady','Steed','Lord','Apprentice','Atronach','Ritual','Lover','Shadow','Tower'][randint(0,12)]

def rndTown():
 return ['Ald Velothi','Ald\'Ruhn','Balmora','Caldera','Dagon Fel','Ebonheart','Gnisis','Hla Oad','Khuul','Maar Gan','Molag Mar','Mournhold','Pelagiad','Sadrith Mora','Seyda Neen','Skaal Village','Suran','Tel Aruhn','Tel Branora','Tel Fyr','Tel Mora','Vivec','Vos'][randint(0,22)]

def rndFacGreatHouse():
 return 'House '+ (['Hlaalu', 'Redoran', 'Telvanni'][randint(0,2)])

def rndFacVampire():
 return (['Aundae', 'Berne', 'Quarra'][randint(0,2)]) + ' Vampire'

def rndFacReligion():
 return ['Tribunal Temple', 'Imperial Cult', 'Deadra Worship/Sixth House'][randint(0,2)]

def rndFaction():
 return [rndFacGreatHouse(), rndFacVampire(), rndFacReligion(), 'Fighters Guild','Mages Guild','Thieves Guild','Blades','Morag Tong', 'Imperial Legion','East Empire Company'][randint(0,9)]

def rndClass():
 return ['Acrobat','Agent','Archer','Assassin','Barbarian','Bard','Battlemage','Crusader','Healer','Knight','Mage','Monk','Nightblade','Pilgrim','Rogue','Scout','Sorcerer','Spellsword','Thief','Warrior','Witchhunter'][randint(0,19)]

print ('Race \t\t: ', rndRace())
print ('Class \t\t: ',rndClass())
print ('Birthsign \t: ', rndSign())
fac2 = 'Mages Guild'
fac1 = 'House Telvanni'
while (fac1, fac2) == ('House Telvanni','Mages Guild') or fac1 == fac2:
 fac1 = rndFaction()
 fac2 = rndFaction()
print('Faction 1 \t: ',fac1)
print('Faction 2 \t: ',fac2)
print ('Hometown \t: ', rndTown())
