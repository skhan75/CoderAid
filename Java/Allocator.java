import java.util.HashSet;

import java.util.*;

public class Allocator {
    
    private Queue<Integer> freeList;
    private Set<Integer> allocated;
    private final int MAX_ID;

    public Allocator(int maxId) {
        this.MAX_ID = maxId;
        this.freeList = new ArrayDeque<>();
        for(int i=0; i<maxId; i++) {
            freeList.offer(i);
        }
        this.allocated = new HashSet<>();
    }

    public int allocate() {
        if(freeList.isEmpty()) {
            return -1;
        }
        int id = freeList.poll();
        allocated.add(id);
        return id;
    }

    public void release(int id) {
        if(id < 0 || id >= MAX_ID) {
            return;
        }
        this.allocated.remove(id);
        this.freeList.add(id);
    }

    public boolean check(int id) {
        return !allocated.contains(id);
    }

    public static void main(String[] args) {
        Allocator allocator = new Allocator(10);
        int id1 = allocator.allocate();
        int id2 = allocator.allocate();
        int id3 = allocator.allocate();

        System.out.println(id1 + "," + id2 + "," + id3);
        System.out.println(allocator.check(id1));
        System.out.println(allocator.check(id2));
        System.out.println(allocator.check(id3));
        System.out.println(allocator.check(11));
        System.out.println(allocator.check(-1));
  
        allocator.release(2);
        System.out.println(allocator.check(id3));

    }
}
