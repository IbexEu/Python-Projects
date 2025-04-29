import requests

# Function to get a snapshot of an item from the SkyApi
def get_item_snapshot(item_tag):
    # Replace this with the actual base URL of SkyApi
    url = f"https://sky.coflnet.com/api/bazaar/{item_tag}/snapshot"  # Replace with the actual URL

    # Send a GET request to the SkyApi
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        
        # Extract snapshot information
        buy_price = data.get('buyPrice', 'N/A')
        sell_price = data.get('sellPrice', 'N/A')

        # Return the extracted buy and sell prices
        return buy_price, sell_price
    else:
        # Handle errors if the request failed
        print(f"Error fetching data for {item_tag}. HTTP Status code: {response.status_code}")
        return None

# List of fine gemstones (with "FINE_" prefix)
fine_gemstones = [
    "FINE_AQUAMARINE_GEM", "FINE_CITRINE_GEM", "FINE_JADE_GEM", "FINE_PERIDOT_GEM", 
    "FINE_ONYX_GEM", "FINE_SAPPHIRE_GEM", "FINE_TOPAZ_GEM", "FINE_JASPER_GEM", 
    "FINE_OPAL_GEM", "FINE_AMETHYST_GEM", "FINE_RUBY_GEM", "FINE_AMBER_GEM"
]

# List of flawless gemstones (without "FINE_" prefix)
flawless_gemstones = [
    "FLAWLESS_AQUAMARINE_GEM", "FLAWLESS_CITRINE_GEM", "FLAWLESS_JADE_GEM", "FLAWLESS_PERIDOT_GEM", 
    "FLAWLESS_ONYX_GEM", "FLAWLESS_SAPPHIRE_GEM", "FLAWLESS_TOPAZ_GEM", "FLAWLESS_JASPER_GEM", 
    "FLAWLESS_OPAL_GEM", "FLAWLESS_AMETHYST_GEM", "FLAWLESS_RUBY_GEM", "FLAWLESS_AMBER_GEM"
]

# Create a list to store results for sorting
buy_order_results = []

# Loop through each fine gemstone and fetch its prices
for fine_gem, flawless_gem in zip(fine_gemstones, flawless_gemstones):
    fine_result = get_item_snapshot(fine_gem)
    flawless_result = get_item_snapshot(flawless_gem)

    if fine_result and flawless_result:
        fine_buy_price, fine_sell_price = fine_result
        flawless_buy_price, flawless_sell_price = flawless_result

        fine_price_for_80 = fine_buy_price * 80
        fine_sell_price_for_80 = fine_sell_price * 80

        # Compare buy prices and calculate profits
        fine_vs_flawless_buy = fine_price_for_80 < flawless_sell_price  # Corrected typo here
        fine_vs_flawless_sell = fine_sell_price_for_80 < flawless_sell_price

        if fine_vs_flawless_buy:
            profit = flawless_sell_price - fine_price_for_80
            buy_order_results.append((fine_gem, "buy order", profit))
        elif fine_vs_flawless_sell:
            profit = flawless_sell_price - fine_sell_price_for_80
            buy_order_results.append((fine_gem, "buy order", profit))

# Sort results by profit in descending order
buy_order_results.sort(key=lambda x: x[2], reverse=True)

# Print the sorted results in the required format
for gem, action, profit in buy_order_results:
    print(f"{action} for {gem.split('_')[1]} is {profit} coins profit")
