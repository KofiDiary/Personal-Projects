# include <iostream>

using namespace std;
int main()
{
	int Age;
	cout <<"Enter your age: ";
	cin >> Age;
	if (Age > 20)
	{
		cout <<"You're too old, you can't ride";
	}
	else
	{
		cout <<"You're young, you can ride";
	}
	return 0;
}