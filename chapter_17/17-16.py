"""
17.16 The Masseuse: A popular masseuse receives a sequence of back-to-back appointment requests
and is debating which ones to accept. She needs a 15-minute break between appointments and
therefore she cannot accept any adjacent requests. Given a sequence of back-to-back appointment
requests (all multiples of 15 minutes, none overlap, and none can be moved), find the optimal
(highest total booked minutes) set the masseuse can honor. Return the number of minutes.
EXAMPLE
Input: {30, 15, 60, 75, 45, 15, 15, 45}
Output:180 minutes ({30, 60, 45, 45}).
Hints: #495, #504, #576, #526, #542, #554, #562, #568, #578, #587, #607
"""

def masseuse(apps):
	return best_booking(apps,0,[0]*	len(apps))

def best_booking(apps, i, possible_bookings):
	if i >= len(apps):
		return 0
	if possible_bookings[i] == 0:
		accept = apps[i] + best_booking(apps, i+2, possible_bookings)
		skip = best_booking(apps, i+1, possible_bookings)
		possible_bookings[i] = max(accept, skip)
		return possible_bookings[i]
	else:
		return possible_bookings[i]

apps = [30,15,60,75,45,15,15,45]
print(masseuse(apps))
