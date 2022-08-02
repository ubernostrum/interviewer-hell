#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>


bool is_square(int n) {
  // Negative numbers aren't squares.
  if(n < 0) {
    return false;
  }

  // Zero is a square.
  if(n == 0) {
    return true;
  }

  long total = 0;
  int next = 1;

  while(total < n) {
    total += next;
    if(total == n) {
      return 1;
    }
    next += 2;
  }

  return false;
}


int main(int argc, char *argv[]) {
  int input = atoi(argv[1]);
  if(is_square(input)) {
    printf("%d is a square.\n", input);
  } else {
    printf("%d is not a square.\n", input);
  }
  return 0;
}
