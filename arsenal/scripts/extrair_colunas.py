"""Extrai texto de cadernos IGEDUC em duas colunas, na ordem de leitura (esquerda, depois direita)."""
import sys, pdfplumber

def extrair(path):
    paginas = []
    with pdfplumber.open(path) as pdf:
        for i, pg in enumerate(pdf.pages):
            full = pg.extract_text() or ""
            if "GABARITO DEFINITIVO" in full:
                paginas.append(("GAB", full))
                continue
            w, h = pg.width, pg.height
            meio = w / 2
            esq = pg.crop((0, 0, meio, h)).extract_text() or ""
            dir_ = pg.crop((meio, 0, w, h)).extract_text() or ""
            paginas.append(("CAD", esq + "\n" + dir_))
    return paginas

if __name__ == "__main__":
    for tipo, t in extrair(sys.argv[1]):
        print(f"\n===== {tipo} =====\n{t}")
