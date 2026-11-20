
def charger_memoire():
    solde = 0
    deptot = 0
    try:
        with open("memoire.txt", "r", encoding="utf-8") as fichier:
            for ligne in fichier:
                ligne = ligne.strip()

                if ligne.startswith("SOLDE:"):
                    solde = float(ligne.split(":")[1])

                elif ligne.startswith("TOTAL_DEPENSES:"):
                    deptot = float(ligne.split(":")[1])

    except FileNotFoundError:
        pass

    return solde, deptot


def sauvegarder_memoire(solde, deptot):
    with open("memoire.txt", "a", encoding="utf-8") as fichier:
        fichier.write("SOLDE:" + str(solde) + "\n")
        fichier.write("TOTAL_DEPENSES:" + str(deptot) + "\n")


def enregistrer_operation(type_operation, montant, date, raison):
    with open("memoire.txt", "a", encoding="utf-8") as fichier:
        fichier.write(
            type_operation + ":" + str(montant)
            + "|" + date + "|" + raison + "\n"
        )


def afficher_historique():
    try:
        with open("memoire.txt", "r", encoding="utf-8") as fichier:
            print("\n========== HISTORIQUE ==========")

            for ligne in fichier:
                if ligne.startswith("ENTREE:") or ligne.startswith("DEPENSE:"):
                    print(ligne.strip())

            print("================================")

    except FileNotFoundError:
        print("Aucun historique disponible.")


def gestionnaire():

    solde, deptot = charger_memoire()

    print("~" * 65)
    print("BIENVENUE SUR LE GESTIONNAIRE DE BUDGET")
    print("~" * 65)

    print("Solde récupéré :", solde, "euros")

    while True:
        try:
            print("\n========== MENU ==========")
            print("0 - Ajouter une dépense")
            print("1 - Ajouter une rentrée d'argent")
            print("2 - Afficher le solde")
            print("3 - Afficher l'historique")
            print("4 - Afficher le total des dépenses")
            print("5 - Éteindre le gestionnaire")

            choix = int(input("Votre choix : "))

            if choix == 1:

                ajout = float(input("Combien d'euros voulez-vous ajouter ? "))

                if ajout <= 0:
                    print("Le montant doit être positif.")
                    continue

                date = input("Date (JJ/MM/AAAA) : ")
                raison = input("Origine de l'argent : ")

                solde += ajout

                enregistrer_operation("ENTREE", ajout, date, raison)
                sauvegarder_memoire(solde, deptot)

                print("Rentrée enregistrée !")
                print("Nouveau solde :", solde, "euros")

            elif choix == 0:

                dep = float(input("Combien avez-vous dépensé ? "))

                if dep <= 0:
                    print("Le montant doit être positif.")
                    continue

                if dep > solde:
                    print("Solde insuffisant !")
                    continue

                date = input("Date (JJ/MM/AAAA) : ")
                raison = input("Dans quoi avez-vous dépensé ? ")

                solde -= dep
                deptot += dep

                enregistrer_operation("DEPENSE", dep, date, raison)
                sauvegarder_memoire(solde, deptot)

                print("Dépense enregistrée !")
                print("Nouveau solde :", solde, "euros")

            elif choix == 2:

                print("Votre solde est de", solde, "euros.")

            elif choix == 3:

                afficher_historique()

            elif choix == 4:

                print("Total des dépenses :", deptot, "euros.")

            elif choix == 5:

                sauvegarder_memoire(solde, deptot)
                print("Fin de la session !")
                print("Vos données ont été sauvegardées.")
                break

            else:
                print("Veuillez sélectionner une valeur entre 0 et 5.")

        except ValueError:
            print("Erreur : veuillez entrer un nombre valide !")


gestionnaire()
