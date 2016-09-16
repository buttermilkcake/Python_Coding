sandwich_orders = ['pastrami', 'reuben', 'pastrami', 'turkey club', 'pastrami']
finished_orders = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while current_order = sandwich_orders.pop():

if current_order != 'pastrami':
    print("Your " + current_order + " sandwich has been ordered.")
    finished_orders.append(current_order)

    print("\nThe following sandwiches have been ordered:")
    for finished_order in finished_orders:
        print(finished_order)
