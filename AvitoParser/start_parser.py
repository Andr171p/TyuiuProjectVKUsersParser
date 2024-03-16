from AvitoParser.parser import AvitoParser
from AvitoParser.config import AVITO_URL


parser_ads = AvitoParser(url=AVITO_URL, ads_number=10).get_parse()
print(parser_ads)

