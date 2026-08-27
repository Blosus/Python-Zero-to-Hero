print('*** Argumentos Variables ***')

def superheroe_superpoderes(superheroe, nombre, *args):
    print(f'Superhero: {superheroe} - {nombre} - {args}')
    # Iteramos los superpoderes
    for superpoder in args:
        print(f'SUperpoder: {superpoder}')

# Llamar la funcion
superheroe_superpoderes('Spider-Man', 'Peter Parker', 'Instinto Aracnido', 'Telaraña')
superheroe_superpoderes('Iron Man', 'Tony Stark', ' Armadura', 'Playboy', 'Millonario')

# Es opcional enviar argumentos variables
superheroe_superpoderes('Captain Kelby', 'Gororia-Chan')