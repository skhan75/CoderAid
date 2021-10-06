public ListNode mergeTwoLists(ListNode l1, ListNode l2) {

	// Node that marks the starting of the head of new list
	ListNode prehead = new ListNode();
	ListNode head = prehead;

	while(l1!=null && l2!=null) {
		if(l1.val <= l2.val){
			head.next = l1;
			l1 = l1.next;
		} else {
			head.next = l2;
			l2 = l2.next;
		}
	}

	if(l1==null)
		head.next = l2;
	else
		head.next = l1;

	return prehead.next;

}