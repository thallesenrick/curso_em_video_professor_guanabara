def votacao(a):
    from datetime import date
    anoatual = date.today().year
    idade = anoatual - a
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA!'
    elif 16 <= idade < 18 or idade > 70:
        return f'Com {idade} anos: VOTO FACULTATIVO!'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'


nasc = int(input('Em que ano você nasceu? '))
print(votacao(nasc))