NOTA_MIN = 0.0
NOTA_MAX = 10.0
MEDIA_APROVACAO = 7.0
MEDIA_REPROVACAO = 4.0
def situacao(media):
    if media >= MEDIA_APROVACAO:
        return "aprovado"
    if media >= MEDIA_REPROVACAO:
        return "recuperacao"
    return "reprovado"

def _valida(nota):
    if not (NOTA_MIN <= nota <= NOTA_MAX):
        raise ValueError(f"Nota fora do intervalo: {nota}")

def calcula_media(n1, n2, n3):
    for nota in (n1, n2, n3):
        _valida(nota)
    return (n1 + n2 + 2 * n3) / 4
