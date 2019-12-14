scrape:
	. `pwd`/.env/bin/activate; python3 scrape.py
	cd ../data; jq . datasets-raw.json > datasets.json
	rm -f ../data/datasets-raw.json


install:
	virtualenv .env --python=/usr/bin/python3 --no-site-packages
	. `pwd`/.env/bin/activate; pip install -r requirements.txt
	@echo "--------------------------------------------------------------------------------------------"
	@echo ""
	@echo "Tudo instalado!"
	@echo "Agora, copia o secrets.py.sample para secrets.py:"
	@echo "    cp secrets.py.sample secrets.py"
	@echo ""
	@echo "E edita o ficheiro com a tua chave da API do Dados.gov.pt."
	@echo "Depois, é só correr:"
	@echo "    make scrape"
	@echo ""

deploy:
	git add ../data/datasets.json
	git commit -m "Atualização automática"
	git push origin master
