//Robert Bangiyev
//November 26, 2018
//This program asks user for number and does triangles
#include <iostream>
using namespace std;

int main()
{
    int num;
    int i;
    int j;
    cout << "Enter a number: ";
    cin >> num;
    for(i=1;i<=num;i++)
    {
        for(j=i;j>0;j--)
        {
            cout << "*";
            if(j==1)
                cout << "\n";
        }
    }
    return 0;
}