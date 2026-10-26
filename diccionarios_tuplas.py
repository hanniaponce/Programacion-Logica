#Diccionarios y tuplas

#1.Predicados
Predicados={
    "animal" : "x es un animal",
    "pelo": "x tiene pelo",
    "leche": "x da leche a sus crias",
    "cuatroPatas": " x tiene cuatro patas",
    "amigable": "x es amigable",
    "domestico": "x es domestico",
    "mamifero": "x es mamifero",
    "pezunas": " x tiene pezunas",
    "cuerpoRobusto": "x tiene cuerpo robusto",
    "pasto": "x se alimenta principalmente de pasto",
    "perro": "x es perro",
    "vaca": "x es vaca",
    "plumas": "x tiene plumas",
    "vuela": "x vuela",
    "huevos": "x pone huevos",
    "carne": "x come carne",
    "ave": " x es un ave",
    "carnivoro": "x es carnivoro",
    "ungulado": "x es ungulado",  
}

#2.Hechos
Hechos={
    "Perro":{
        "animal","pelo","leche","cuatroPatas", "amigable", "domestico",
    },
    "Vaca":{
        "animal", "pelo", "leche","cuatroPatas","pezunas", "cuerpoRobusto","pasto",
    },
}

#3.Reglas
Reglas=[
    {"id":1, "si": ("animal", "pelo"),  "entonces": "mamifero"},
    {"id":2, "si": ("animal", "leche"),  "entonces": "mamifero"},
    {"id":3, "si": ("animal", "plumas"),  "entonces": "ave"},
    {"id":4, "si": ("vuela", "huevos"),  "entonces": "ave"},
    {"id":5, "si": ("mamifero", "carne"),  "entonces": "carnivoro"},
    {"id":6, "si": ("mamifero", "pezunas"),  "entonces": "ungulado"},
    {"id":7, "si": ("carnivoro", "colorLeonado", "manchasOscuras"),  "entonces": "guepardo"},
    {"id":8, "si": ("carnivoro", "colorLeonado","RayasNegras"),  "entonces": "tigre"},
    {"id":9, "si": ("ungulado", "cuelloLargo", "ManchasOscuras"),  "entonces": "jirafa"},
    {"id":10, "si": ("ungulado", "RayasNegras"),  "entonces": "cebra"},
    {"id":11, "si": ("ave","nada","blancoNegro"),  "entonces": "pinguino"},
    {"id":12, "si": ("ave", "vuelaMuyBien"),  "entonces": "albatros"},

    #perro
    {"id":13, "si": ("pelo", "cuatroPatas","amigable"),  "entonces": "perro"},
    {"id":14, "si": ("amigable", "domestico","pelo", "cuatroPatas"),  "entonces": "perro"},
    #vaca
    {"id":15, "si": ("pelo", "leche"),  "entonces": "mamifero"},
    {"id":16, "si": ("mamifero", "pezunas","cuerpoRobusto"),  "entonces": "vaca"},
    {"id":17, "si": ("cuatroPatas", "pezunas","pasto"),  "entonces": "vaca"},
]
#4.Ontologia
Ontologia=(
    ("mamifero", "es_un", "animal"),
    ("ave", "es_un", "animal"),
    ("carnivoro", "es_un", "mamifero"),
    ("ungulado", "es_un", "mamifero"),
    ("guepardo", "es_un", "carnivoro"),
    ("tigre", "es_un", "carnivoro"),
    ("jirafa", "es_un", "ungulado"),
    ("cebra", "es_un", "ungulado"),
    ("vaca", "es_un", "ungulado"),
    ("perro", "es_un", "mamifero"),
    ("pinguino", "es_un", "ave"),
    ("albatros", "es_un", "ave"),
)

def inferir(individuo):
    conocimiento = set(Hechos[individuo])
    derivaciones ={}
    cambio = True
    while cambio:
        cambio = False
        for regla in Reglas:
            conclusion = regla["entonces"]
            if conclusion not in conocimiento and all(
                c in conocimiento for c in regla["si"]
            ):
                conocimiento.add(conclusion)
                derivaciones[conclusion] = regla["id"]
                cambio = True 
    return conocimiento, derivaciones

def ancestros(categoria):
    resultado = []
    for sujeto, relacion, objeto in Ontologia:
        if sujeto == categoria and relacion =="es_un":
            resultado.append(objeto)
            resultado.extend(ancestros(objeto))
    return resultado

if __name__ == "__main__":
    for nombre in Hechos:
        conocimiento, derivaciones = inferir(nombre)
        print(f"\n== {nombre} ==")
        print("Hechos:", sorted(Hechos[nombre]))
        for conclusion, regla_id in derivaciones.items():
            cadena =" -> ".join([conclusion] + ancestros(conclusion))
            print(f" Regla {regla_id}: {conclusion}  ({cadena})")
