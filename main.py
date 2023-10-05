def boxPrint(symbol, width, height):
    if len(symbol) != 1:
      ➊ raise Exception('Symbol must be a single character string.')
    if width <= 2:
      ➋ raise Exception('Width must be greater than 2.')
    if height <= 2:
      ➌ raise Exception('Height must be greater than 2.')

    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        boxPrint(sym, w, h)
  ➍ except Exception as err:
      ➎ print('An exception happened: ' + str(err))