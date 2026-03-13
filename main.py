meme_dict = {

    "CRINGE": "algo ultrapassado, tipo epoca dos dinossáuros.",
    "67": "um número aleatório que virou meme do nada e tá todo mundo falando sobre.",
    "SELOKO NUM COMPENSA": 'algo que compensaria se não fosse por um motivo x.',
    'SABOR': 'algo que é TIPO uma coisa, mas não é essa coisa MESMO. exemplo: chá é SABOR bom, não é bom, é SABOR bom.'
    
}

word = input('fala uma palavra que você não conhece, ou SABOR conhece: ')

if word in meme_dict:
    print(meme_dict[word])
else:
    print('não válido.')
