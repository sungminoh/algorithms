#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main(int argc, const char *argv[])
{
  while(--argc > 1 && !fork());
  usleep(argc = atoi(argv[argc]));
  printf("%d\n", argc);
  wait(0);
  return 0;
}

