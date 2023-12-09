# Time and Space complexity O(n)

baseURL = 'https://codefirstgirls.com/'
currentPath = []

pages = {
    '': {
        'courses': {
            'cfgdegree': {}
        },
        'opportunities': {
            'ambassadors': {}
        }
    }
}

nextPage = ''
while True:
    if nextPage == 'back':
        currentPath = currentPath[:-1]
    else:
        currentPath.append(nextPage)

    print(f"You are currently on the URL {baseURL + '/'.join(currentPath)}")
    print(f"Where are you clicking?")

    options = pages
    for i in currentPath:
        options = options[i]
    options = [i[0].upper() + i[1:] for i in options.keys()] + (['Back'] if currentPath != [''] else [])
    options = ', '.join (options)

    print(f"Options: {options}")

    nextPage = input().lower()

    if nextPage != 'exit':
        continue
    break