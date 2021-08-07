MeanGroups {
	int[][] meanGroups(int[][] a) {
    
    Map<Integer, List<Integer>> map = new LinkedHashMap<>();
    
    
    for(int i=0; i<a.length; i++) {
        int sum = 0;
        for(int j=0; j<a[i].length; j++) {
            sum += a[i][j];
        }
        
        int avg = sum/a[i].length;
        
        List<Integer> current = map.getOrDefault(avg, new ArrayList<>());
        current.add(i);
        map.put(avg, current);
    }
    
    int[] result = new int[map.size()];
    int count = 0;
    
    for(Map.Entry<Integer,List<Integer>> entry : map.entrySet()){
        int[] lst = new int[entry.getValue().size()];
        int[] primitive = entry.getValue().stream()
                            .mapToInt(Integer::intValue)
                            .toArray();
        // int i=0;
        // for(int n : entry.getValue()) {
        //     lst[i] = n;
        //     i++;
        // }
        
        // result[count] = lst;
        // count++;
    }
    

    // for(int i = 0;i < ret.length;i++)
    //     ret[i] = list.get(i);
    
    
    
    System.out.println(result);
    return null;
}

}