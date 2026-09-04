# Define variables
SCRIPT = simple-script.sh
OUTPUT = output.txt

# Target default
all: help

# Target to run the Bash script
run-script: $(SCRIPT)
	@echo "Menjalankan script Bash..."
	bash $(SCRIPT)

# Target to build the docker image (bagian tantangan, lihat README)
docker-build:
	@echo "Building docker image..."
	docker build -t docker-app ../03-docker-containerization

# Target to clean the output file
clean:
	@echo "Membersihkan file output..."
	rm -f $(OUTPUT)

# Target to display the help message
help:
	@echo "Use 'make run-script' to run the Bash script."
	@echo "Use 'make docker-build' to build the docker image."
	@echo "Use 'make clean' to clean the output file."
	@echo "Use 'make help' to display this message."

# example:
# make
