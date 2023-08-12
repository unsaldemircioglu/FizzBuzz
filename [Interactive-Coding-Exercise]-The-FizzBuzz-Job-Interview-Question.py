'''
Temel olarak, daire şeklinde oturan ve saat yönünde
ilerleyen bir gurup çocuk var ilk çocuk 1 diyor, ikinci
çocuk 2 diyor ancak bir çocuk üçe tam bölünebilen bir sayı
ile karşılaştığında, o sayıyı söylemek yerine "Fizz" diyecektir
ve sayı beşe bölünebildiğinde, sayıyı söylemek yerine "Buzz" demelidirler.
ve eğer sayı hem üçe hem beşe blünebiliyorsa,örn: 15, o zaman
"FizzBuzz" demelidir.
'''

for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        # şu an karşılaştırdığımız sayı hem üçe hem beşe bölünüyorsa,
        # FizzBuzz yazmamız lazım
        print("FizzBuzz")
    elif number % 3 == 0:
        # sadece 3'e bölünüyor ise Fizz
        print("Fizz")
    elif number % 5 == 0:
        # sadece 5'e bölünüyor ise Buzz
        print("Buzz")
    else:
        # Diğer tüm sayıları yakalamak için
        print(number)