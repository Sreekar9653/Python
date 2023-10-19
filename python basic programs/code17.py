class Color:
    def Display_Color(a):
        if(not a):return
        try:
            if(not(len(a)==1 and a.isalpha())):raise TypeError("An Alphabet should be taken")
            elif(a.lower() in "vibgyor"):print({'v':'violet','i':'indigo','b':'blue','g':'green','y':'yellow','o':'orange','r':'red'}[a.lower()])
            else:raise ValueError("Not a color")
        except TypeError:print("Alphabet should be taken")
        except ValueError:print("Not a color")
        return Color.Display_Color(input("Enter an Alphabet, leave empty if done "))
Color.Display_Color(input("Enter an Alphabet, leave empty if done "))
