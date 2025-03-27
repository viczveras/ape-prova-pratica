
def registros(file: str) -> list:
    arq = open(file, 'r')
    lista = arq.read().splitlines()
    arq.close()

    return lista[1:]


def quantidade_registros(registros: list) -> int:
    return len(registros)


def campi(registros: list) -> list:
    lista_campi = []
    for linha in registros:
        campos = linha.split(';')  
        nome_campus = campos[4].strip('"')  
        if nome_campus not in lista_campi:  
            lista_campi.append(nome_campus)
    return lista_campi


def cursos(registros: list, nome_campus: str) -> list:
    lista_cursos = []
    for linha in registros:
        campos = linha.split(';')
        campus = campos[4].strip('"')  
        curso = campos[6].strip('"')   
        if campus == nome_campus and curso not in lista_cursos:  
            lista_cursos.append(curso)
    return lista_cursos


def maior_nota_instituicao(registros: list) -> float:
    maior_nota = 0.0
    for linha in registros:
        campos = linha.split(';')
        nota = float(campos[16].strip('"').replace(',', '.'))  
        if nota > maior_nota:
            maior_nota = nota
    return maior_nota


def maior_nota_campus(registros: list, nome_campus: str) -> float:
    maior_nota = 0.0
    for linha in registros:
        campos = linha.split(';')
        campus = campos[4].strip('"')  
        if campus == nome_campus:
            nota = float(campos[16].strip('"').replace(',', '.'))  
            if nota > maior_nota:
                maior_nota = nota
    return maior_nota


def maior_nota_curso(registros: list, codigo_curso: int) -> float:
    maior_nota = 0.0
    for linha in registros:
        campos = linha.split(';')
        codigo = int(campos[5].strip('"'))  
        if codigo == codigo_curso:
            nota = float(campos[16].strip('"').replace(',', '.'))  
            if nota > maior_nota:
                maior_nota = nota
    return maior_nota


def maior_nota_corte_instituicao(registros: list) -> float:
    maior_nota_corte = 0.0
    for linha in registros:
        campos = linha.split(';')
        nota_corte = float(campos[17].strip('"').replace(',', '.'))  
        if nota_corte > maior_nota_corte:
            maior_nota_corte = nota_corte
    return maior_nota_corte


def maior_nota_corte_campus(registros: list, nome_campus: str) -> float:
    maior_nota_corte = 0.0
    for linha in registros:
        campos = linha.split(';')
        campus = campos[4].strip('"')  
        if campus == nome_campus:
            nota_corte = float(campos[17].strip('"').replace(',', '.'))  
            if nota_corte > maior_nota_corte:
                maior_nota_corte = nota_corte
    return maior_nota_corte

def maior_nota_corte_curso(registros: list, codigo_curso: int) -> float:
    maior_nota_corte = 0.0
    for linha in registros:
        campos = linha.split(';')
        codigo = int(campos[5].strip('"'))  
        if codigo == codigo_curso:
            nota_corte = float(campos[17].strip('"').replace(',', '.'))  
            if nota_corte > maior_nota_corte:
                maior_nota_corte = nota_corte
    return maior_nota_corte


def codigo_curso(registros: list, nome_campus: str, nome_curso: str) -> int:
    for linha in registros:
        campos = linha.split(';')
        campus = campos[4].strip('"')  
        curso = campos[6].strip('"')   
        if campus == nome_campus and curso == nome_curso:
            return int(campos[5].strip('"'))  
    return 0  # 