num_of_product, num_of_popular = map(int, input().split())
votes = list(map(int, input().split()))

populars = [i for i in votes if i >= sum(votes) / (4 * num_of_popular)]
if len(populars) >= num_of_popular:
    print('Yes')
else:
    print('No')