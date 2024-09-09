#include<stdio.h>
#include<stdlib.h>
#include<netdb.h>
#include<arpa/inet.h>

int main (int argc, char *argv[])
{
	int i;
	struct hostent* host;
	if(argc!=2)
	{
		printf("Usage: ./gethostip nameofhost\n");
		exit(1);
	}	
	host=gethostbyname(argv[1]);
	if(host==NULL)
	{
		printf("Error: No Such Host Found\n");
		exit(1);
	}
	printf("Host name: %s\n", host->h_name);
	printf("Host IP Address: %s\n", inet_ntoa(*((struct in_addr*) host->h_addr)));
	struct in_addr ** addr_list;
	printf("Other addresses:\n");
	addr_list= (struct in_addr **)host->h_addr_list;
	for(i=0;addr_list[i]!=NULL;i++)
		printf("%s\n",inet_ntoa(*addr_list[i]));
	printf("Other host names or aliases :\n");
	char **names;
	names= (char **)host->h_aliases;
	for(i=0;names[i]!=NULL;i++)
		printf("%s\n",names[i]);
	return 0;
}

