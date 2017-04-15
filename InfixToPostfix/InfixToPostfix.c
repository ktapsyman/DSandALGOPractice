#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#ifndef SAFE_FREE
#define SAFE_FREE(x) if(x)\
					 {\
						 free(x);\
						 x = NULL;\
					 }
#endif
#ifndef MAX_STACK_SIZE
#define MAX_STACK_SIZE 100
#endif
#ifndef FALSE
#define FALSE 0
#endif
#define TRUE !FALSE

void Push( char *CharStack, char NewElement )
{
	if( !CharStack )
	{
		printf("Stack pointer is null!\n");
		return;
	}
	unsigned int CurrentSize = strlen(CharStack);
	if( CurrentSize == MAX_STACK_SIZE )
	{
		printf("Stack is full!\n");
		return;
	}
	CharStack[CurrentSize] = NewElement;
}

char Peek( char *CharStack )
{
	if( !CharStack )
	{
		printf("Stack pointer is null!\n");
		return '\0';
	}
	unsigned int CurrentSize = strlen(CharStack);
	if( !CurrentSize )
	{
		return '\0';
	}
	return CharStack[CurrentSize-1];
}

char Pop( char *CharStack )
{
	if( !CharStack )
	{
		printf("Stack pointer is null!\n");
		return '\0';
	}
	unsigned int CurrentSize = strlen(CharStack);
	char RetChar = Peek( CharStack );
	if( '\0' == RetChar )return RetChar;
	CharStack[CurrentSize-1] = '\0';
	return RetChar;
}

int IsNewElementHigherPriority( char Original, char NewElement)
{
	if( Original == '+' || Original == '-' )
	{
		return ( NewElement == '*' || NewElement == '/' ) ? TRUE : FALSE;
	}
	else if( Original == '*' || Original == '/' )
	{
		return FALSE;
	}
	return TRUE;
}

int main( int argc, char **argv )
{
	if( argc < 2 )
	{
		printf("No input string\n");
		return -1;
	}
	char *CharStack = (char *)calloc( MAX_STACK_SIZE, sizeof(char) );
	if( !CharStack )
	{
		printf("OOM!\n");
		return -1;
	}
	//unsigned int ArgumentLen = strlen( argv[1] )+1;
	while( *argv[1] )
	{
		static int CurrentNum = 0;
		switch(*argv[1] )
		{
			case '0':
			case '1':
			case '2':
			case '3':
			case '4':
			case '5':
			case '6':
			case '7':
			case '8':
			case '9':
				CurrentNum = CurrentNum*10 + (unsigned int)(*argv[1])-48;
				if( *(argv[1]+1) == '\0' )
				{
					printf("%d ", CurrentNum);
				}
				break;
			case '+':
			case '-':
			case '*':
			case '/':
				printf("%d ", CurrentNum);
				CurrentNum = 0;
				if( '\0' != Peek(CharStack) )
				{
					while( FALSE == IsNewElementHigherPriority( Peek(CharStack), *argv[1] ) )
					{
						printf("%c ", Pop(CharStack));
					}
				}
				Push( CharStack, *argv[1] );
				break;
			default:
				break;
		}
		//--ArgumentLen;
		//if( !ArgumentLen )break;
		++argv[1];
	}
	char RestOperator = '\0';
	while( '\0' != (RestOperator = Pop(CharStack)) )
	{
		printf("%c ", RestOperator);
	}
	printf("\n");
	SAFE_FREE( CharStack );
#ifdef SAFE_FREE
#undef SAFE_FREE
#endif
	return 0;
}
