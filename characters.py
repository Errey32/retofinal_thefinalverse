from msilib.schema import SelfReg
from time import sleep
from os import system


delay = 1
lang = input("----Wich class are you going to choose for your new game?----\n\t\t\t[Human]\n\t\t\t[Demon]\n\t\t\t[Angel]\n-------------------------------------------------------------\n")
match lang:
    case "Human":

        print("You just woke up from a hundred years sleep, is a dark place you are trapped somewhere so you push and get out from a coffin. ")
        sleep(delay)
        print("You are in the middle of a snowy forest it is to cold for you soyou start lookin around and you see a cabin and you peek in and see some Hunters.")
        sleep(delay)
        lang2 = input("What are you going to do?\n\t\t\t[1.- You go fight the Hunters]\n\t\t\t[2.- You go searchin for another place to shellter]")
        if lang2 == "1":
                #Pelea
                system("cls")
                print("You have defeated the hunters, you stay inside the shellter a few hours to sleep")
                sleep(delay)
                
        elif lang2 == "2":
            print("You found another cabain so you stay a few hours to sleep")

        print("YOU WOKE UP, something loud woke you, you start lookin around in the middle of the night to see what was it")
        sleep(delay)
        print("You find some big guy comming for you, he is covered in flames, you need to fight him.")
        #pelea
        print("You destroyed that guy so you run to see his things and you find the godslayer sword")
        sleep(delay)
        print("With this sword you can defeat the elden ghost that is in the deep of the forest")
        sleep(delay)
        print("YoU start your way into the forest and manage to find a angel")
        print("These angels aren't what they seem to be")
        sleep(delay)
        print("He starts attackin you but you manage to dodge his attacks")
        #pelea
        system("cls")
        
    case "Demon":
           print(Demon)

    case "Angel":
           print(Angel)
