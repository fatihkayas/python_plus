   
# Task : Estimating the risk of death from coronavirus.

# Consider the following questions in terms of True/False regarding anyone else.
# Are you a cigarette addict older than 75 years old? Variable → age
# Do you have a severe chronic disease? Variable → chronic
# Is your immune system too weak? Variable → immune
# Set a logical algorithm using boolean logic operators (and/or) and the given variables in order to give us True  # (there is a risk of death) or False (there is not a risk of death) as a result.

age = input("Are you a cigarette addict older than 75 years old?(Please answer as Yes or No): ")
chronic = input("Do you have a severe chronic disease?(Please answer as Yes or No): ")
immune = input("Is your immune system too weak?(Please answer as Yes or No): ")
if age == "Yes" or chronic == "Yes" or immune == "Yes":
  print(bool("There is a risk of death"))
else:
  print(bool())
