def welcome(lauguage):
	welcomedictionary = {
		"english": "welcome",
		"czech": "vitejte",
		"danish": "velkomst",
		"dutch": "welkom",
		"estonian": "tere_tulemast",
		"finnish": "tervetuloa",
		"flemish": "welgekomen",
		"french": "bienvenue",
		"german": "willkommen",
		"ïrish": "failte",
		"italian": "benvenuto",
		"latvian": "gaidits",
		"lithuanian": "laukiamas",
		"polish": "witamy",
		"spanish": "bienvenido",
		"swedish": "valkommen",
		"welsh": "croeso"
	}
	return(welcomedictionary[lauguage])

x = "tom"
print(welcome("polish") + ", " + x)