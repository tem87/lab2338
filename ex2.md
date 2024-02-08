1.	Interpolation search uses interpolation algorithms to predict the target element's prosiible position, 
	enabling a midpoint to be established where it is most likely to occur. 
	While having uniformly distributed data is beneficial, interpolation search works well with non-uniform 
	data distributions. This technique requires less comparisons than binary search, making it a useful algorithm 
	for search operations across varied data distributions.

2.	Interpolation search assumes that the data is uniformly distributed. If the data is not uniformly distributed, 
	then the performance of the interpolation search will be affected as it works by estimating the position of the 
	target element. If the data is not uniformly distributed, then there will be inaccuracy in the estimation of the 
	target position which can lead to wrong results or more comparisons before reaching the desired result.

3.	The line that should be change so the data can follow a different distribution. It determines the position of the desired element in the array:
	pos = low + int(((float(high - low) / (arr[high] - arr[low])) * (x - arr[low])))

4.	When the data is not sorted or the dataset is small, linear search will be faster.

5.	The linear search will outperform both binary and interpolation when you are dealing with small data sets. 
	It’s simpler to implement, more efficient, faster and cheaper rather than sorting the data.
6.	Yes, using the quick sorting algorithm the performance of interpolation and binary search can be improved. 
	The quick sorting algorithm works by pivot selection and partitioning data into two halves.
	The average case complexity for quick sort is O(n log (n)) making it the fastest sorting algorithm. 
	By quickly sorting the data before we perform binary or interpolation search it reduces the search time because it provides 
	data in an organized way which enhances the efficiency of search by reducing the number of comparisons to find the target element.
