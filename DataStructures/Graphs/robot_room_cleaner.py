class Robot(object):
   def move(self):
       """
       Returns true if the cell in front is open and robot moves into the cell.
       Returns false if the cell in front is blocked and robot stays in the current cell.
       :rtype bool
       """

   def turnLeft(self):
       """
       Robot will stay in the same cell after calling turnLeft/turnRight.
       Each turn will be 90 degrees.
       :rtype void
       """

   def turnRight(self):
       """
       Robot will stay in the same cell after calling turnLeft/turnRight.
       Each turn will be 90 degrees.
       :rtype void
       """

   def clean(self):
       """
       Clean the current cell.
       :rtype void
       """
class Solution(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def backtrack(cell = (0, 0), d = 0):
            visited.add(cell)
            robot.clean()
            # going clockwise : 0: 'up', 1: 'right', 2: 'down', 3: 'left'
            for i in range(4):
                new_d = (d + i) % 4
                new_cell = (cell[0] + directions[new_d][0], \
                            cell[1] + directions[new_d][1])

                if not new_cell in visited and robot.move():
                    backtrack(new_cell, new_d)
                    go_back()
                # turn the robot following chosen direction : clockwise
                robot.turnRight()

        # going clockwise : 0: 'up', 1: 'right', 2: 'down', 3: 'left'
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()
        backtrack()

"""
public class RobotRoomCleaner {

    public static void main(String args[]) {
        int[][] room = {
            {0, 1, 1, 1},
            {1, 1, 1, 1},
            {1, 1, 0, 0},
            {1, 1, 1, 1},
        };
        int[] pos = {1, 1};
        Robot robot = new RobotImpl(room, pos);
        new RobotRoomCleaner().cleanRoom(robot);
    }

    interface Robot {
        boolean move();

        void turnLeft();

        void turnRight();

        void clean();
    }

    public void cleanRoom(Robot robot) {
        dfs(robot, 0, 0, 0, new HashSet<>());
    }

    private void dfs(Robot robot, int i, int j, int dir, Set<String> visited) {
        // cell identifier
        String pos = i + "_" + j;
        if (visited.contains(pos)) return;
        robot.clean();
        visited.add(pos);
        for (int n = 0; n < 4; n++) { // move in all directions
            if (robot.move()) {
                int row = i, col = j;
                switch (dir) {
                    case 0: row = i - 1; break;
                    case 90: col = j + 1; break;
                    case 180: row = i + 1; break;
                    case 270: col = j - 1; break;
                }
                // visit next branch
                dfs(robot, row, col, dir, visited);
                robot.turnLeft();
                robot.turnLeft();
                robot.move();
                robot.turnRight();
                robot.turnRight();
            }
            // rotate 90 degrees to visit that branch
            robot.turnRight();
            dir += 90;
            dir = dir % 360;
        }
    }

    static class RobotImpl implements Robot {

        int[] pos;
        int[][] room;
        int dir = 0; // up: 0, right: 1, down: 2, left: 3

        public RobotImpl(int[][] room, int[] pos) {
            this.room = room;
            this.pos = pos;
        }

        @Override
        public boolean move() {
            int x = 0, y = 0;
            switch (dir) {
                case 0:
                    y = -1;
                    break;
                case 1:
                    x = 1;
                    break;
                case 2:
                    y = 1;
                    break;
                case 3:
                    x = -1;
                    break;
            }
            int newX = pos[0] + x;
            int newY = pos[1] + y;
            boolean outOfbounds = (newX < 0 || newY < 0 || newX > room.length - 1 || newY > room[0].length - 1);
            if (outOfbounds || room[newX][newY] == 0) {
                return false;
            }
            pos = new int[]{newX, newY};
            System.out.println("Robot at: " + pos[0] + " , " + pos[1]);

            return true;
        }

        @Override
        public void turnLeft() {
            dir -= 1;
            if (dir < 0) dir = 3;
        }

        @Override
        public void turnRight() {
            dir += 1;
            if (dir > 3) dir = 0;
        }

        @Override
        public void clean() {
            System.out.println("Cleaning  " + pos[0] + " , " + pos[1]);
        }
    }
}
"""
if __name__ == "__main__":
    s = Solution()
    room = [
      [1,1,1,1,1,0,1,1],
      [1,1,1,1,1,0,1,1],
      [1,0,1,1,1,1,1,1],
      [0,0,0,1,0,0,0,0],
      [1,1,1,1,1,1,1,1]
    ],
    row = 1,
    col = 3
    r = Robot()
    print s.cleanRoom(r)
