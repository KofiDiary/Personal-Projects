#include <iostream>
#include <cmath>
using namespace std;

int calcMean()
{
    int data[50];
    int counter = 0;
    int dataPoints;
    int sum = 0;
    int regulator;
    float mean;

    cout << "\nIf you no longer have values to enter, enter -1 to break from loop" << endl;

    while (true){
        cout << "\nPlease, enter a value: ";
        cin >> dataPoints;

        if(dataPoints != -1){
        data[counter] = dataPoints;
        counter += 1;
        }

        else{
            break;
        }
    }

    for(regulator = 0; regulator < counter; regulator++){
        sum = sum + data[regulator];
    }

    float Sum = sum;
    float Counter = counter;

    mean = Sum / Counter;
    cout << "\nMean = "<< mean << endl;

    return 0;
}

int calcMedian()
{
    int data[50];
    int dataPoints;
    int counter = 0;
    int regulator;
    float median;
    int backCounter;
    int frontCounter;

    cout << "\nIf you no longer have values to enter, enter -1 to break from loop" << endl;

    while(true){
        cout << "\nPlease, enter a value: ";
        cin >> dataPoints;

        if(dataPoints != -1){
        data[counter] = dataPoints;
        counter += 1;
        }

        else{
            break;
        }
    }

    if(counter % 2 == 0){
        counter = counter / 2;
        backCounter = (counter);
        frontCounter = counter - 1;
        median = data[frontCounter] + data[backCounter];
        median = median / 2;
        cout << "\nMedian = " << median << endl;
    }
    else{
        counter += 1;
        counter /= 2;
        counter -= 1;
        median = data[counter];
        cout << "\nMedian = " << median << endl;
    }
    return 0;
}

int calcStanDev()
{
    int data[50];
    int counter = 0;
    int dataPoints;
    int sum = 0;
    float Add = 0;
    int regulator;
    float mean;
    float standard_Dev;

    cout << "\nIf you no longer have values to enter, enter -1 to break from loop" << endl;

    while (true){
        cout << "\nPlease, enter a value: ";
        cin >> dataPoints;

        if(dataPoints != -1){
        data[counter] = dataPoints;
        counter += 1;
        }

        else{
            break;
        }
    }

    for(regulator = 0; regulator < counter; regulator++){
        sum = sum + data[regulator];
    }

    float Sum = sum;
    float Counter = counter;

    mean = Sum / Counter;

    for(regulator = 0; regulator < counter; regulator++){
        Add += pow((data[regulator] - mean), 2);
    }

    Add = Add / counter;
    Add = pow(Add, 0.5);
    standard_Dev = Add;

    cout << "\nStandard Deviation = " << standard_Dev << endl;

    return 0;
}

int calcAll_Three()
{
    int data[50];
    int counter = 0;
    int dataPoints;
    int sum = 0;
    float Add = 0;
    int regulator;
    float mean;
    float standard_Dev;
    float median;
    int backCounter;
    int frontCounter;

    cout << "\nIf you no longer have values to enter, enter -1 to break from loop" << endl;

    while (true){
        cout << "\nPlease, enter a value: ";
        cin >> dataPoints;

        if(dataPoints != -1){
        data[counter] = dataPoints;
        counter += 1;
        }

        else{
            break;
        }
    }

    int Regulator = counter;

    for(regulator = 0; regulator < counter; regulator++){
        sum = sum + data[regulator];
    }

    float Sum = sum;
    float Counter = counter;

    mean = Sum / Counter;
    cout << "\nMean = "<< mean << endl;

    if(counter % 2 == 0){
        counter = counter / 2;
        backCounter = (counter);
        frontCounter = counter - 1;
        median = data[frontCounter] + data[backCounter];
        median = median / 2;
        cout << "\nMedian = " << median << endl;
    }
    else{
        counter += 1;
        counter /= 2;
        counter -= 1;
        median = data[counter];
        cout << "\nMedian = " << median << endl;
    }

    for(regulator = 0; regulator < Regulator; regulator++){
        Add += pow((data[regulator] - mean), 2);
    }

    Add = Add / Regulator;
    Add = pow(Add, 0.5);
    standard_Dev = Add;

    cout << "\nStandard Deviation = " << standard_Dev << endl;

    return 0;
}

void Decisions()
{
    int options;
    cout << "Please select an option to perform operations." << endl;
    cout << "\nOptions \n1. Calculate Mean \n2. Calculate Median \n3. Calculate Standard Deviation \n4. Calculate All Three \n" << endl;
    cin >> options;
    switch(options)
    {
        case 1:
            {
                calcMean();
                break;
            }
        case 2:
            {
                calcMedian();
                break;
            }
        case 3:
            {
                calcStanDev();
                break;
            }
        case 4:
            {
                calcAll_Three();
                break;
            }
        default:
            {
                cout << "\nInvalid input" << endl;
            }
    }
}

int main()
{
    Decisions();

    return 0;
}
