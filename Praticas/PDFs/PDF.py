from pathlib import Path

from PyPDF2 import PdfReader

PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdfs_origen'
PASTA_NOVA = PASTA_RAIZ / 'PDFs'

RELATORIO_BACEN = PASTA_ORIGINAIS / '1657231536919.pdf'

PASTA_NOVA.mkdir(exist_ok=True)

reader = PdfReader(RELATORIO_BACEN)

# print(len(reader.pages))
# for page in reader.pages:
#     print(page)
#     print()

page0 = reader.pages[0]
imagem0 = page0.images[0]

# print(page0.extract_text())
# with open(PASTA_NOVA / imagem0.name, 'wb') as fp:
#     fp.write(imagem0.data)