
def get_named_temp(districts, temp_list):
    # Adds district name with temperature list
    return dict(zip(districts, temp_list))


def get_average_temp(district_temp):
    # Calculate average district temperature
    # Convert to arrays from dict and average based on array count
    average_temp = dict()
    for district, temperatures in district_temp.items():
        dts = list(temperatures.values())
        average_temp[district] = sum(dts) / len(dts)

    return average_temp


def get_top_ten(district_temp):
    # Filter top ten district based on low temperature
    cool_ten = dict(
        sorted(district_temp.items(), key=lambda item: item[1])[:10]
    )

    return cool_ten
