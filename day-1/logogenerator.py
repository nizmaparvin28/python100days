#Day 1 LOGO NAME GENERATOR


print("-- WELCOME TO LOGO NAME GENERATOR --")
# Collect inputs
business_type = input("What type of business is this logo for? (e.g., tech, fashion, food):")
vibe = input("What vibe should the logo convey? (e.g., fun, professional, modern): ")
keyword = input("Enter a main keyword or theme for the logo (e.g., eco, urban, smart): ")
color = input("Enter a color that represents your brand (e.g., blue, green): ")
tagline = input("Enter a short slogan or tagline (optional): ")


# Generate a few example logo names using simple concatenation
logo_name1 = color + " " + keyword  + " " + business_type
logo_name2 = vibe  + " " + keyword
logo_name3 = color+ " " + business_type  + " " + vibe


# Display the generated logo names
print("\nHere are some logo name suggestions:")
print("1. " + logo_name1)
print("2. " + logo_name2)
print("3. " + logo_name3)


