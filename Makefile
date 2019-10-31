VERSION?=-1
ENV_NAME=env


run:
	streamlit run app/app.py

use_model:
ifeq ($(VERSION),-1)
	@echo "VERSION should be specified"
else
	rm -f app/model_used.txt
	@echo $(VERSION) > app/model_used.txt
endif

train:
ifeq ($(VERSION),-1)
	@echo "VERSION should be specified"
else
	python app/model/training.py $(VERSION)
endif

setup:
	pip install -r requirements.txt

