import java.util.*;

class SingleThreadedCpu {
	public int[] getOrder(int[][] tasks) {
		int n = tasks.length;
		int[] ans = new int[n];

		int[][] tasksWithId = new int[n][3];
		for(int i=0; i<n; i++) {
			tasksWithId[i][0] = i; // task index
			tasksWithId[i][1] = tasks[i][0]; // enqueue time
			tasksWithId[i][2] = tasks[i][1]; // process time
		}

		// Sort the array because we time increments in the direction of enqueue time
		Arrays.sort(tasksWithId, (a,b) -> a[1] - b[1]);

		// Priority Queue to hold tasks with prirority given to tasks with minimum processing time
		PriorityQueue<int[]> pq = new PriorityQueue<int[]>((a,b) -> a[2] == b[2] ? a[0] - b[0] : a[2] - b[2]);

		int ansId = 0;
		int taskId = 0;
		int time = 0;

		while(ansId < n) {
			
			// for all the other tasks which have enqueue time lesser than current process time, add to pq
			while(taskId < n && tasksWithId[taskId][1] <= time) {
			 	pq.offer(tasksWithId[taskId]);
				taskId++;
			}

			// when CPU is idle or its the first task, PQ will be empty, we just increament the time with the enqueue time of current taskID
			if(pq.isEmpty()){
				time = tasksWithId[taskId][1];
				continue;
			}

			int[] bestFit = pq.poll();
			int processTime = bestFit[2];
			int index = bestFit[0];

			time += processTime;
			ans[ansId++] = index;
		}

		return ans;
	}
	

	public static void main(String[] args) {
		SingleThreadedCpu stc = new SingleThreadedCpu();
		int[][] tasks = { {1,2}, {2,4}, {3,2}, {4,1} };
		System.out.println("The event goes as follows --> " + Arrays.toString(stc.getOrder(tasks)));
	}
}