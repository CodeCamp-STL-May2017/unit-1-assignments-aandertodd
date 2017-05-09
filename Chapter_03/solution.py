def calculate_temp(num_clicks):
# TODO calculate the temperature (use the variable name of temp) num clicks will be number of clicks 
# #put answer in the temp variable
    num_clicks = clicks
    temp = (num_clicks % 50) + 40
    
    return temp

if __name__ == '__main__':
    clicks_str = input("By how many clicks has the dial been turned? ")
    clicks = int(clicks_str)
    print(calculate_temp(num_clicks))
