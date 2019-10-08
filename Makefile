.PHONY: build

build:
	docker build -t micro-infrastructure/main-lofar .

run: build
	docker run -dt --rm -P micro-infrastructure/main-lofar

push: build
	docker push micro-infrastructure/main-lofar

