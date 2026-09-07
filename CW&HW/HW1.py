rice_pr_kg = 45
sugar_pr_kg = 40
oil_pr_kg = 130

rice_qty = 3
sugar_qty = 2.5
oil_qty = 1.8

rice_ttl = rice_pr_kg * rice_qty
sugar_ttl = sugar_pr_kg * sugar_qty
oil_ttl = oil_pr_kg * oil_qty
print('total price,rice =',rice_ttl)
print('total price,sugar =',sugar_ttl)
print('total price,oil =',oil_ttl)

final_bill = rice_ttl+sugar_ttl+oil_ttl
print('final bill =',final_bill)

print('as integer = ',int(final_bill))
print('as string = ',str(final_bill))

import random
print('with delivery charge = ',random.randrange(5,10)+final_bill)