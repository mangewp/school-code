def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    return dollars_per_gallon / miles_per_gallon * miles_driven


def input_compute_and_print():
    miles_per_gallon = float(input())
    dollars_per_gallon = float(input())

    miles = [10, 50, 400]
    for i in miles:
        print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, i):.2f}')





if __name__ == '__main__':
    input_compute_and_print()