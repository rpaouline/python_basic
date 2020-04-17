rating_list = [9, 7, 7, 7, 5, 5, 2]

new_rating = 0

while not new_rating:
    new_rating = input("Input natural number (int > 0)\n")
    if new_rating.isdigit():
        new_rating = int(new_rating)

        if new_rating < 1:
            new_rating = 0
    else:
        new_rating = 0

if new_rating in rating_list:
    # If new rating in our list, find first place of this number and quantity of this number
    # Their sum is our new index
    new_index = rating_list.index(new_rating) + rating_list.count(new_rating)
    rating_list.insert(new_index, new_rating)
else:
    # Try to find closest smaller rating
    smaller_rating = min(new_rating,max(rating_list))
    while smaller_rating not in rating_list and smaller_rating > 0:
        smaller_rating -= 1

    if smaller_rating == 0:
        rating_list.append(new_rating)
    else:
        rating_list.insert(rating_list.index(smaller_rating),new_rating)

print(rating_list)
