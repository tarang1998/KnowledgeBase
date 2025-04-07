# Example deck with suits
deck_with_suits = ['5 of Clubs', '5 of Diamonds','King of Hearts', 'Ace of Spades', 'Jack of Diamonds']

card_order = ['Ace', '1', '2', '3', '4', '5', '6', '7', '8', 'Jack', 'Queen', 'King']
value_to_rank = {val: idx for idx, val in enumerate(card_order)}

suits_order = ['Diamonds', 'Clubs', 'Hearts', 'Spades'] 
suit_to_rank = {suit: idx for idx, suit in enumerate(suits_order)}

# Using Python inbuild function
sorted_deck = sorted(deck_with_suits, key=lambda x: (value_to_rank[x.split(' of ')[0]], 
                                                    suit_to_rank[x.split(' of ')[1]]))

print("Sorted deck with suits:", sorted_deck)

def merge(left,right):

    result = []

    i = 0
    j = 0

    while i<len(left) and j<len(right):

        left_val, left_suit = left[i].split(' of ')
        right_val, right_suit = right[j].split(' of ')

        # Compare by value first, then suit
        left_rank = (value_to_rank[left_val], suit_to_rank[left_suit])
        right_rank = (value_to_rank[right_val], suit_to_rank[right_suit])

        
        if left_rank <= right_rank:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    
    result.extend(left[i:])
    result.extend(right[j:])

    return result



# Using custom sorting function
def merge_sort(deck):

    if len(deck)<=1:
        return deck
    
    mid = len(deck)//2
    left = deck[:mid]
    right = deck[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left,right)



print("Sorted deck with suits using custom sort :", merge_sort(deck_with_suits))




