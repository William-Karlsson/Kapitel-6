import math

uppmätta_värden = input("Vänligen ange uppmätta värden, separerat med mellanslag: ").split(" ")

uppmätta_värden.sort()

if len(uppmätta_värden) % 2 == 1:
    median = uppmätta_värden[math.floor(len(uppmätta_värden) / 2)]
else:
    median = (int(uppmätta_värden[math.floor((len(uppmätta_värden) / 2))]) + int(uppmätta_värden[math.floor((len(uppmätta_värden) / 2)) - 1])) / 2

print(median)