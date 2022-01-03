#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int bitwiseComplement(int n)
{
  int x = 1;
  while (x < n)
    x = 2 * x + 1;
  return n ^ x;
}