#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/ioctl.h>
#include <net/if.h>
#include <unistd.h>
#include <arpa/inet.h>

int main() 
{
    char interface[IFNAMSIZ];
    printf("Enter the network interface (e.g., eth0, wlan0): ");
    scanf("%s", interface);   
    int sock;
    struct ifreq ifr;
    unsigned char *mac;
    sock = socket(AF_INET, SOCK_DGRAM, 0);
    if (sock == -1) 
    {
        perror("Socket creation failed");
        exit(EXIT_FAILURE);
    }
    strncpy(ifr.ifr_name, interface, IFNAMSIZ - 1);
    ifr.ifr_name[IFNAMSIZ - 1] = '\0';
    if (ioctl(sock, SIOCGIFHWADDR, &ifr) == -1) 
    {
        perror("ioctl failed");
        close(sock);
        exit(EXIT_FAILURE);
    }
    mac = (unsigned char *)ifr.ifr_hwaddr.sa_data;
    printf("MAC address of %s: %02X:%02X:%02X:%02X:%02X:%02X\n", interface, mac[0], mac[1], mac[2], mac[3], mac[4], mac[5]);
    close(sock);
    return 0;
}
