CC = gcc
CFLAGS = -Wall
OUTPUTDIR = ./Output
ProjName = InfixToPostfix
_OBJS = $(ProjName).o
OBJS = $(patsubst %, $(OUTPUTDIR)/%, $(_OBJS))

$(OUTPUTDIR)/%.o:*.c
	$(CC) -c -o $@ $< $(CFLAGS)
$(ProjName):$(OBJS)
	$(CC) -o $@ $^ $(CFLAGS)
clean:
	rm -f $(OUTPUTDIR)/* ./$(ProjName)
