//Robert Bangiyev
//November 28, 2018
//This program does something
#include <iostream>
using namespace std;

int main()
{
  std::cout.precision(2);
  std::cout.setf(std::ios::fixed);
  double pop=325.7;
  int years;
  double brate=12.4;
  double drate=8.4;
  cout << "Enter number of years: ";
  cin >> years;
  cout << "Year 2017 " << pop << "\n"; 
  for(int i=1;i<years;i++)
  {
      pop=pop+(brate*pop)-(drate*pop);
      cout << "Year " << 2017+i << " " << pop << "\n";
  }
  
  return 0;
}
