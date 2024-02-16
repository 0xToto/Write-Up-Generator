import os
import datetime
from colorama import Fore

def generate_writeup_template(ctf_name, challenge_name, category, difficulty, author, description, solution, flag, avis):
    template = f"""# Writeup CTF - {ctf_name}

## Challenge: {challenge_name}

- **Category:** {category}
- **Difficulty:** {difficulty}
- **Author:** {author}
- **Date:** {datetime.datetime.now().strftime("%Y-%m-%d")}

## Description
{description}

## Solution
{solution}

## Flag
The flag is: {flag}

## Avis / Suggestions
{avis}
"""
    return template

ctf_name = input("Nom du CTF >>> ")
challenge = input("Nom du Challenge >>> ")
categorie = input("Catégorie du challenge >>> ")
difficulte = input("Difficulté >>> ")
auteur = input("Auteur du CTF >>> ")
description = input("Description du CTF >>> ")
solution = input("Solutions >>> ")
flag = input("Flag >>> ")
avis = input("Avis sur le CTF >>> ")

writeup = generate_writeup_template(ctf_name, challenge, categorie, difficulte, auteur, description, solution, flag, avis)

writeup_folder = "Write-Up"
if not os.path.exists(writeup_folder):
    os.makedirs(writeup_folder)

writeup_filename = f"{writeup_folder}/{ctf_name.replace(' ', '_')}_Writeup.md"

with open(writeup_filename, 'w') as file:
    file.write(writeup)

print(Fore.GREEN + "Writeup créé avec succès :",writeup_filename)
