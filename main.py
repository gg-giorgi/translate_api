import requests

def translate_text(text, target_lang):
    api_url = 'https://api.mymemory.translated.net/get'

    params = {
        'q': text,
        'langpair': f'en|{target_lang}'
    }

    response = requests.get(api_url, params=params)
    data = response.json()

    if 'responseData' in data and 'translatedText' in data['responseData']:
        translated_text = data['responseData']['translatedText']
        print(f'შედეგი: {translated_text}')
    else:
        print('სამწუხაროდ, თარგმნა ვერ მოხერხდა.')

text = input('შეიყვენათ ტექსტი: ')
target_lang = input('შეიყვანეთ ენა, რომელზეც გსურთ თარგმნა (მაგალითან, "en" ინგლისურისთვის): ')
translate_text(text, target_lang)
'''ქართულიდან სამწუხაროდ არ თარგმნის :D'''