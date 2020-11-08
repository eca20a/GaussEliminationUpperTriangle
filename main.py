import pprint
from typing import List, Union


Scalar = Union[int, float]
Row = List[Scalar]
Matrix = List[Row]


def gauss_elimination(Ab:Matrix) -> None:
    # pivot loop
    for p in range(0, len(Ab)-1):
        pivot = Ab[p][p]
        one_over_minus_pivot = -1.0 / pivot

        # row loop
        for i in range(p+1, len(Ab)):
            multiplier = Ab[i][p] * one_over_minus_pivot
            
            # column loop
            for j in range(p, len(Ab[p])):
                Ab[i][j] += multiplier * Ab[p][j]


def main():
  # Kreyszig, Numerical Methods in Linear Algebra, Advanced Engineering Mathematics, 5th ed, John Wiley & Sons, 1983.
  matAb = [
    [2,  1,  2,  1,  6],
    [6, -6,  6, 12, 36],
    [4,  3,  3, -3, -1],
    [2,  2, -1,  1, 10],
  ]
  print("before calling GE")
  pprint.pprint(matAb, width=40)

  gauss_elimination(matAb)

  print("after calling GE")
  pprint.pprint(matAb, width=40)

if "__main__" == __name__:
  main()
