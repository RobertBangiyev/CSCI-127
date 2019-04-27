//Robert Bangiyev
//November 26, 2018
//This program asks user for number and does seasons
#include <iostream>
using namespace std;

int main()
{
    int num;
    cout << "Enter a number: ";
    cin >> num;
    if(num<3 or num>11)
        cout << "Happy Winter";
    else if(num>3 and num<7)
        cout << "Happy Spring";
    else if(num>=7 and num<9)
        cout << "Happy Summer";
    else
        cout << "Happy Fall";
    return 0;
}
