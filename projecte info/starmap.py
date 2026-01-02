"""
starmap.py
"""
import functions
import json

def main():
    starmap = {} 
    
    while True:
        print("\nMenú")
        print("")
        print("1. Afegir constel·lació")
        print("2. Afegir estrelles a constel·lació")
        print("3. Afegir adjacència entre estrelles de constel·lació")
        print("4. Eliminar adjacència entre estrelles de constel·lació")
        print("5. Eliminar estrella de constel·lació")
        print("6. Llistar constel·lació (i estadístiques)")
        print("7. Llistar constel·lacions")
        print("8. Dibuixar constel·lació (Turtle)")
        print("9. Guardar constel·lació en JSON")
        print("10. Carregar constel·lació des de JSON")
        print("11. Modificar posició d'una estrella")
        print("12. Eliminar constel·lació")
        print("13. Sortir de l'aplicació")
        print("14. Calcular distància entre dues estrelles")
        print("15. Trobar l'estrella més propera")

        opcio = input("\nTria la teva opció: ")

        if opcio == '1':
            nom = input("Dona nom de la nova constel·lació: ")
            functions.addConstellation(starmap, nom)
            print("Nova constel·lació creada amb èxit.")
        
        elif opcio == '2':
            const = input("Dona nom de la constel·lació: ")
            if const in starmap:
                nomsestrelles = input("Dona noms de les estrelles separats per comes: ")
                divisiones = nomsestrelles.split(',')
                llista_estrelles = []
                for nomsestrelles in divisiones:
                    llista_estrelles.append(nomsestrelles)
                
                functions.addStars(starmap, const, llista_estrelles)
                print("Estrelles afegides correctament.")
            else:
                print("La constel·lació no existeix.")

        elif opcio == '3':
            const = input("Dona nom de la constel·lació: ")
            if const in starmap:
                starA = input("Dona nom de l'estrella origen: ")
                starB = input("Dona nom de l'estrella destí: ")
                functions.addAdjacencies(starmap, const, starA, [starB])
                print("Adjacència creada entre", starA, "i", starB)
            else:
                print("La constel·lació no existeix.")

        elif opcio == '4':
            const = input("Dona nom de la constel·lació: ")
            if const in starmap:
                starA = input("Dona nom de l'estrella origen: ")
                starB = input("Dona nom de l'estrella destí: ")
                
                estrelles = starmap[const]['stars']
                if starA in estrelles and starB in estrelles:
                    functions.deleteAdjacencyWithBackup(starmap, const, starA, starB, "backup.json")
                    print("Adjacència entre", starA, "i", starB, "eliminada.")
                else:
                    print("Alguna de les estrelles no existeix.")
            else:
                print("La constel·lació no existeix.")

        elif opcio == '5':
            const = input("Dona nom de la constel·lació: ")
            if const in starmap:
                star = input("Dona nom de l'estrella a eliminar: ")
                
                if star in starmap[const]['stars']:
                    functions.deleteStarWithBackup(starmap, const, star, "backup.json")
                    print("Estrella", star, "eliminada correctament.")
                else:
                    print("Aquesta estrella no existeix a la constel·lació.")
            else:
                print("La constel·lació no existeix.")
            
        elif opcio == '6':
            const = input("Dona nom de la constel·lació: ")
            if const in starmap:
                print("Dades:")
                functions.listAllStars(starmap, const)
                
                total = functions.countStars(starmap, const)
                print("Total d'estrelles:", total)
                
                aillades = functions.listIsolatedStars(starmap, const)
                print("Estrelles aïllades:", aillades)
            else:
                print("La constel·lació no existeix.")
            
        elif opcio == '7':
            print("Constel·lacions disponibles:")
            functions.listAllConstellations(starmap)

        elif opcio == '8':
            const = input("Dona nom de la constel·lació: ")
            if const in starmap:
                print("Dibuixant", const)
                functions.drawConstellation(starmap, const)
                print("Dibuix finalitzat.")
            else:
                print("La constel·lació no existeix.")

        elif opcio == '9':
            fitxer = input("Introdueix nom del fitxer per guardar: ")
            functions.saveStarmapJSON(starmap, fitxer)
            print("Mapa guardat a", fitxer)

        elif opcio == '10':
            fitxer = input("Introdueix nom del fitxer a carregar: ")
            nou_mapa = functions.loadStarmapJSON(fitxer)
            if nou_mapa:
                starmap.update(nou_mapa)
                print("Mapa carregat i afegit a la memòria.")
            else:
                print("Error carregant el mapa o fitxer buit.")
            
        elif opcio == '11':
            const = input("Dona nom de la constel·lació: ")
            if const in starmap:
                star = input("Dona nom de l'estrella a moure: ")
                coords = input("Noves coordenades x,y: ")
                llista_xy = coords.split(',')
                x = float(llista_xy[0])
                y = float(llista_xy[1])
                
                functions.assignCoordinates(starmap, const, star, x, y)
                print("Posició de la estrella ", star, "actualitzada.")
            else:
                print("La constel·lació no existeix.")
            
        elif opcio == '12':
            const = input("Dona nom de la constel·lació a eliminar: ")
            if const in starmap:
                functions.deleteConstellationWithBackup(starmap, const, "backup.json")
                print("Constel·lació", const, "eliminada.")
            else:
                print("La constel·lació no existeix.")

        elif opcio == '13':
            print("Tancant Programa")
            break
            
        elif opcio == '14':
            const = input("Dona nom de la constel·lació: ")
            if const in starmap:
                s1 = input("Estrella 1: ")
                s2 = input("Estrella 2: ")
                dist = functions.distanceBetween(starmap, const, s1, s2)
                print("La distància és:", dist)
            else:
                print("La constel·lació no existeix.")

        elif opcio == '15':
            const = input("Dona nom de la constel·lació: ")
            if const in starmap:
                s1 = input("Estrella central: ")
                propera = functions.nearestStar(starmap, const, s1)
                print("Estrella més propera:", propera)
            else:
                print("La constel·lació no existeix.")

        else:
            print("Opció no vàlida.")
main()
