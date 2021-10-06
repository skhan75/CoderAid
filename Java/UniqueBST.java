public int numTrees(int n) {


	int[] G = new int[n+1];

	// 0 - 1
	// 1 - 1
	// 2 - 2
	// 3 - 5

	G[0] = 1;
	G[1] = 1;

	// G[3] = F(1,3) + F(2,3) + F(3,3)
	//       /     \
	//    G[0]     G[2]
	for(int i=2; i<n; i++){
		for(int j=1; j<=i; j++) // possibility space
			G[i] = G[i] + (G[i-1] * G[i-j]);

	}

	return G[n];

	/** using catalan number formula **/
	long C = 0;
	for(int i=0; i<n; i++)
		C = C * 2 * (2 * i+1) / (i+2);

	return (int)C;

}