import sys

from worker import servidor_base

if __name__ == "__main__":
    puerto = int(sys.argv[1])
    servidor_base(puerto)
