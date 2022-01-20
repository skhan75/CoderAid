import java.util.*;

/**
 * https://leetcode.com/problems/design-in-memory-file-system/
 */

public class FileSystem {
    class Directory {
        boolean isfile = false;
        HashMap<String, Directory> files = new HashMap<>();
        String content = "";
    }

    Directory root;

    public FileSystem() {
        root = new Directory();
    }

    public List<String> ls(String path) {
        Directory pwd = root;
        List<String> result = new ArrayList<>();
        if(!path.equals("/")) {
            String[] dirs = path.split("/");
            for (int i = 1; i < dirs.length; i++) {
                pwd = pwd.files.get(dirs[i]); // go to the end directory in the path
            }
            if(!pwd.isfile) {
                result.add(dirs[dirs.length - 1]);
                return result;
            }
        }
        List<String> resFiles = new ArrayList<>(pwd.files.keySet());
        Collections.sort(resFiles);
        return resFiles;
    }

    public void mkdir(String path) {
        Directory pwd = root;
        String[] dirs = path.split("/");
        for (int i = 1; i < dirs.length; i++) {
            if(!pwd.files.containsKey(dirs[i])) {
                pwd.files.put(dirs[i], new Directory());
            }
            pwd = pwd.files.get(dirs[i]);
        }
    }

    public void addContentToFile(String filePath, String content) {
        Directory t = root;
        String[] d = filePath.split("/");
        for (int i = 1; i < d.length - 1; i++) {
            t = t.files.get(d[i]);
        }
        if (!t.files.containsKey(d[d.length - 1]))
            t.files.put(d[d.length - 1], new Directory());
        t = t.files.get(d[d.length - 1]);
        t.isfile = true;
        t.content = t.content + content;
    }

    public String readContentFromFile(String filePath) {
        Directory pwd = root;
        String[] d = filePath.split("/");
        for (int i = 1; i < d.length - 1; i++) {
            pwd = pwd.files.get(d[i]);
        }
        return pwd.files.get(d[d.length - 1]).content;
    }

      public static void main(String[] args) {
        FileSystem fs = new FileSystem();

        System.out.println(fs.ls("/")); 
        fs.mkdir("/a/b/c"); 
        System.out.println(fs.ls("/a/b"));
        fs.addContentToFile("/a/b/c/d", "hello");
        System.out.println(fs.ls("/"));
        System.out.println(fs.readContentFromFile("/a/b/c/d"));
    }

}



