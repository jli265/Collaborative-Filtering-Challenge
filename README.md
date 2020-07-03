# Collaborative-Filtering-Challenge
This is a difficult python coding problem in the context of recommender system and collaborative filtering (AI & Machine Learning)
Collaborative Filtering
A Recommender System is capable of predicting the preferences of an active user for a set of items. For example, an online store can suggest a product to the shopper based on a history of purchases or page views.
One of the traditional approaches to construct such a system is to use Collaborative Filtering. It does not require any information about the items themselves and makes recommendations based on the past behavior of many users.
Usually, collaborative filtering can be reduced to two steps:
1.	Look for users with similar interests as the active user
2.	Use ratings from the other users identified above to make a prediction for the active user

Your task is to implement the first step using the number of inversions in the lists of user ratings as a numerical similarity measure.
An Inversion is a pair of elements (Si,Sj) of the sequence, such that i < j and Si > Sj. For example, sorted array (1,2,3,4,5) has zero inversions. Array (5,1,2,3,4) has four inversions (5,1), (5,2), (5,3), (5,4). Array (1,3,5,2,4) has three inversions (3,2), (5,2), (5,4). The maximum possible number of inversions in the array with n elements is n(n-1)/2.
Suppose we asked several people to rank three music genres. Now, we can form lists with ratings for each person from the most favorite genre to the least favorite. See the input description below for an example.
If a person in this set has identical preferences and ranks items exactly the same way as the active user, the number of inversions in the array would be zero. In general, the more inversions the array has, the more varied preferences are. In our example, Alice has 1 inversion compared to Bob. Meanwhile, John has 3 inversions compared to Bob.
So, Alice has more preferences in common with Bob and she is more suitable as the basis of a prediction.
input：
Each line contains a user name and an ordered list of their preferences separated by a colon. Items in the list are comma-separated. The first line of the input has an active user (the user whom a prediction is for). For example:
Bob:Rock,Blues,Jazz
Alice:Rock,Jazz,Blues
John:Jazz,Blues,Rock
output：
Print the list of users to be considered for making a recommendation. The list must be sorted by the number of inversions in ascending order. If two users have the same count of inversions sort them alphabetically. For example:
Alice,John




Here I provide some test cases and correct outputs with my algorithms:
testSolution = Solution()
case0 = '''
Bob:Rock,Blues,Jazz
Alice:Rock,Jazz,Blues
John:Jazz,Blues,Rock
'''
test0 = testSolution.collaborativeFiltering(case0)
print(test0)# Alice,John
case1='''
rabbit:carrot,cabbage,fish,meat turtle:cabbage,carrot,fish,meat 
cat:fish,meat,carrot,cabbage dog:meat,fish,cabbage,carrot
'''
test1=testSolution.collaborativeFiltering(case1) 
print(test1)#turtle,cat,dog
case2='''
Smith:helicopter,car,motorcycle,bicycle,bus 
Johnson:bus,helicopter,motorcycle,car,bicycle 
Williams:bicycle,helicopter,car,motorcycle,bus 
Jones:helicopter,bicycle,motorcycle,car,bus 
Brown:bus,motorcycle,helicopter,bicycle,car 
Davis:motorcycle,bus,car,bicycle,helicopter 
Miller:bicycle,helicopter,car,bus,motorcycle 
Wilson:helicopter,car,bicycle,bus,motorcycle
'''
test2=testSolution.collaborativeFiltering(case2) 
print(test2)#Wilson,Jones,Williams,Miller,Johnson,Brown,Davis
case3='''
James:Avengers,Captain Marvel,Dumbo,Shazam,Hellboy,Joker,Spider-Man,Aladdin,Toy Story,Dark 
Phoenix Olivia:Aladdin,Captain Marvel,Hellboy,Avengers,Toy Story,Spider-Man,Dark Phoenix,Joker,Dumbo,Shazam 
Sophia:Toy Story,Dark Phoenix,Aladdin,Joker,Captain Marvel,Hellboy,Dumbo,Shazam,Avengers,Spider-Man 
Jacob:Dumbo,Avengers,Spider-Man,Dark 
Phoenix,Hellboy,Joker,Aladdin,Captain Marvel,Shazam,Toy Story 
Oliver:Dumbo,Spider-Man,Aladdin,Toy Story,Avengers,Hellboy,Dark Phoenix,Shazam,Joker,Captain Marvel Johannes:Captain Marvel,Joker,Toy Story,Avengers,Aladdin,Hellboy,Shazam,Dark Phoenix,Spider-Man,Dumbo
'''
test3=testSolution.collaborativeFiltering(case3)
print(test3)#Jacob,Johannes,Olivia,Oliver,Sophia
