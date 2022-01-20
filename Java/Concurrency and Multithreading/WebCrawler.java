import java.util.LinkedList;
import java.util.Queue;

/**
 * Given a getLinks(String initialURL) function, which takes an URL, scan the
 * page and returns a list of URLs found on this page, write a function to find
 * all the URLs that can be accessed by the initialURL.
 * 
 * https://www.webarchitects.io/dropbox-interview-question-multi-threaded-web-crawler/
 */


public class WebCrawler {
    Queue<String> queue = new LinkedList<>();
    Set<String> visited = new HashSet<>();
    
    public Set<String> crawl() {
        queue.addAll(getLinks(initialURL));

        while(!queue.isEmpty()) {
            String url = queue.poll();
            for(String childUrl : getLinks(url)) {
                if(!set.contains(childUrl)) {
                    set.add(childUrl);
                    queue.offer(childUrl);
                }
            }
        }

        return result;
    }

    /** OPTIMIZATION
     * getLinks() function is the most time consuming part, which needs to scan the page * for urls. So we need to make the page scanning multithreaded while still keeping  * the function thread safe 
     */
    public void crawlThreadSafe() {
        int workingThreads = 0;

        OUTER_LOOP: while(true) {
            String nextUrl;
            // First synchronized block gurantees that the thread can only proceed when there are some URLs in the queue.
            synchronized(this){
                while(!queue.isEmpty()) {
                    if(workingThreads == 0 && queue.isEmpty()) {
                        break OUTER_LOOP;
                    }
                    try {
                        wait();
                    } catch(InterruptedException e) {
                        e.printStackTrace();
                    }
                }
                nextUrl = queue.poll();
                workingThreads++;
            }

            // This method is not in any sync block, so we can optimize this using multi threading
            List<String> urls = getLinks(nextUrl);

            // In this block, we are looping through the newly found URLs and checking if they are already scanned.
            synchronized(this) {
                for(String url : urls) {
                    if(!visited.contains(url)) {
                        queue.offer(url);
                        visited.add(newUrl);
                    }
                }
                workingThreads--; // The thread will exit when there are no threads scanning the URLs and queue is empty
                // At the end, we notify all the sleeping threads to wake up and continue after wait
                notifyAll();
            }
        }
    }

    /* 
    * This is a method that calls a downstream service ton retrieve all links
    *  And could take an order magnitude of time to respond
    */
    public String[] getLinks(String url) {
        return new String();
    }
}
