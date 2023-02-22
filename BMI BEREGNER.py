#kort information om BMI
print("Hej! Jeg vil gerne fortælle dig om Body Mass Index (BMI).")
print("BMI er et mål for din kropsvægt i forhold til din højde.")
print("Det bruges som et groft værktøj til at vurdere, om du er undervægtig, normalvægtig, overvægtig eller svært overvægtig.")
print("Lad os beregne dit BMI og se, hvad resultatet siger om din vægtstatus.")

# Spørger om navn for at personalisere oplevelsen
navn = input('Hvad hedder du?: ')
print('Hej', navn + ', lad os beregne dit BMI.')

# Spørger om vægt og højde for at beregne BMI
while True:
    try:
        højde_i_cm = float(input('Hvor høj er du (i cm)?: '))
        vægt_i_kg = float(input('Hvor meget vejer du (i kg)?: '))
        bmi = vægt_i_kg / ((højde_i_cm / 100) ** 2)
        print("Dit BMI er: ", bmi)
        break
        # Tjekker hvis inputten er gyldig
    except ValueError:
        print("Du indtastede ikke en gyldig værdi. Prøv igen.")

# Udfra BMI-værdi, fortæller programmet om vægtstatus
if bmi <= 18.5:
    print("Du er undervægtig")
elif bmi >= 18.5 and bmi < 25:
    print("Du er normalvægtig")
elif bmi >= 25 and bmi < 30:
    print("Du er overvægtig")
else:
    print("Du er svært overvægtig")

# Giver råd om sundhed baseret på BMI-værdi
if bmi >= 25:
    print("Du bør overveje at besøge følgende hjemmeside for mere information om sundhed: https://www.sundhed.dk/borger/patienthaandbogen/sundhedsoplysning/overvaegt/overvaegt-hvad-er-det/")
if bmi < 25:
    print("Du er inden for det normale BMI-interval. Det er godt at tage vare på din sundhed! Fortsæt med det!")
if bmi <= 18.5:
    print("Du bør overveje at besøge følgende hjemmeside for mere information om sundhed: https://www.sundhed.dk/borger/patienthaandbogen/sundhedsoplysning/undervaegt/")

# kort information om hvad han/hun kan spise
print("Spis en sund og varieret kost, der inkluderer en blanding af frugt, grøntsager, fuldkorn, magre proteiner og sunde fedtstoffer.")

print("Håber du har en god dag, og fortsætter med at udvikle dig selv")
