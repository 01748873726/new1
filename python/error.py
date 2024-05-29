try:
    roll=int(input("enter your roll:"))
    if roll <1:
        raise ValueError
    print("Your roll is=",roll)
except ValueError as e:
    print("invalid roll")
    print(e)
print("Successfully completed")

