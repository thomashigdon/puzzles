void swap(char *a, char *b) {
  char tmp = *a;
  *a = *b;
  *b = tmp;
}

int reverse(char *input) {
  int len = 0;
  char *rightpos = input;
  char *leftpos = input;
  if (!input) {
    return -1;
  }
  if (!*input)
    return 0;
  while (*(++rightpos)) len++;
  rightpos--;
  while (leftpos < rightpos) {
    swap(leftpos, rightpos);
    leftpos++;
    rightpos--;
  }
  return 0;
}

#include <stdlib.h>

int main() {
  char *blah = "i love you";
  char *blah2 = malloc(10);
  strcpy(blah2, blah);
  int result = reverse(blah2);
  if (result) {
    printf("error %d occurred\n", result);
  }
  printf("%s", blah2);
}
