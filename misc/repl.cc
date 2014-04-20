#include <string>
#include <iostream>
#include <stdexcept>

void repl(std::string &A, size_t len) {
  int right = A.length() - 1;
  int left = len - 1;
  while (left >= 0) {
    if (A[left] == ' ') {
      if (right < 2) {
        throw std::invalid_argument("invalid input");
      }
      A[right] = '0'; A[right - 1] = '2'; A[right - 2] = '%';
      right -= 3;
    } else {
      A[right] = A[left];
      right--;
    }
    left--;
  }
}

int main() {
  std::string A = "Mr John Smith    ";
  repl(A, 13);
  std::cout << A << std::endl;
}
