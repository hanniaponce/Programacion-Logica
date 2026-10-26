# Ontologia
## 1. Jerarquía de clases 

```mermaid
graph TD
    animal --> mamifero
    animal --> ave
    mamifero --> carnivoro
    mamifero --> ungulado
    mamifero --> perro
    carnivoro --> guepardo
    carnivoro --> tigre
    ungulado --> jirafa
    ungulado --> cebra
    ungulado --> vaca
    ave --> pinguino
    ave --> albatros
```

## 2. Reglas

```mermaid
graph LR
    pelo --> mamifero
    leche --> mamifero
    plumas --> ave
    vuela --> ave
    huevos --> ave
    mamifero --> carnivoro
    carne --> carnivoro
    mamifero --> ungulado
    pezunas --> ungulado
    carnivoro --> guepardo
    leonado_manchas_oscuras["leonado + manchas oscuras"] --> guepardo
    carnivoro --> tigre
    leonado_rayas["leonado + rayas negras"] --> tigre
    ungulado --> jirafa
    cuello_manchas["cuello largo + manchas oscuras"] --> jirafa
    ungulado --> cebra
    rayas["rayas negras"] --> cebra
    ave --> pinguino
    nada_bn["nada + blanco y negro"] --> pinguino
    ave --> albatros
    vuela_bien["vuela muy bien"] --> albatros
    cuatroPatas --> perro
    amigable --> perro
    domestico --> perro
    pezunas --> vaca
    cuerpoRobusto --> vaca
    pasto --> vaca
```

## 3. Individuos 
```mermaid
graph TD
    Rex((Rex)) -->|pelo, leche| mamifero
    Rex -->|cuatroPatas, amigable, domestico| perro
    Lola((Lola)) -->|pelo, leche| mamifero
    Lola -->|pezunas| ungulado
    Lola -->|pezunas, cuerpoRobusto, pasto| vaca
    perro -->|es_un| mamifero
    vaca -->|es_un| ungulado
    ungulado -->|es_un| mamifero
```

## 4. Tabla de reglas

| # | Si | Entonces |
|---|----|----------|
| 1 | animal tiene pelo | mamífero |
| 2 | animal da leche a sus crías | mamífero |
| 3 | animal tiene plumas | ave |
| 4 | vuela y pone huevos | ave |
| 5 | mamífero come carne | carnívoro |
| 6 | mamífero tiene pezuñas | ungulado |
| 7 | carnívoro leonado con manchas oscuras | guepardo |
| 8 | carnívoro leonado con rayas negras* | tigre |
| 9 | ungulado de cuello largo con manchas oscuras | jirafa |
| 10 | ungulado con rayas negras | cebra |
| 11 | ave que nada y es blanca y negra | pingüino |
| 12 | ave que vuela muy bien | albatros |
| 13–14 | pelo, cuatro patas, amigable (y doméstico) | perro |
| 15 | pelo y da leche | mamífero |
| 16 | mamífero con pezuñas y cuerpo robusto | vaca |
| 17 | cuatro patas, pezuñas y se alimenta de pasto | vaca |
